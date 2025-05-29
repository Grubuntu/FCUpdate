CHECKUPDATEVERSION = "1.0"

import os
import re
import sys
import json
import time
import webbrowser
import requests
from datetime import datetime, timedelta
from pathlib import Path

from PySide import QtGui, QtCore, QtWidgets
import FreeCAD as App
import FreeCADGui as Gui

from functools import partial

# === CONFIGURATION ===

URL_WEEKLY = "https://api.github.com/repos/FreeCAD/FreeCAD-Bundle/releases/tags/weekly-builds"
URL_STABLE = "https://api.github.com/repos/FreeCAD/FreeCAD-Bundle/releases/latest"
CHECK_INTERVAL = timedelta(hours=1)

def get_freecad_config_dir():
    if sys.platform == "win32":
        return os.path.join(os.getenv("APPDATA"), "FreeCAD")
    elif sys.platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Library", "Preferences", "FreeCAD")
    else:
        return os.path.join(os.path.expanduser("~"), ".config", "FreeCAD")

CONFIG_DIR = get_freecad_config_dir()
CONFIG_FILE = os.path.join(CONFIG_DIR, "FCUpdate.cfg")
os.makedirs(CONFIG_DIR, exist_ok=True)

ICON_UP_TO_DATE = QtGui.QApplication.style().standardIcon(QtGui.QStyle.SP_DialogApplyButton)
ICON_UPDATE_AVAILABLE = QtGui.QApplication.style().standardIcon(QtGui.QStyle.SP_BrowserReload)

# === FONCTIONS VERSIONS ===

def get_local_build_number():
    build_str = App.Version()[3]
    match = re.search(r'(\d+)', build_str)
    return int(match.group(1)) if match else None

def get_remote_build_number():
    try:
        with requests.get(URL_WEEKLY, timeout=10) as r:
            r.raise_for_status()
            html = r.text
            match = re.search(r"FreeCAD_weekly-builds-(\d+)-", html)
            return int(match.group(1)) if match else None
    except Exception as e:
        App.Console.PrintError(f"Erreur récupération version en ligne : {e}\n")
        return None

# === CACHE TEMPOREL ===

def read_cache():
    if not os.path.exists(CONFIG_FILE):
        return None, []
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            last_check = datetime.fromisoformat(data.get("last_check", ""))
            results = data.get("results_cache", [])
            return last_check, results
    except Exception:
        return None, []

def write_cache(last_check, results_cache):
    with open(CONFIG_FILE, "w") as f:
        json.dump({
            "last_check": last_check.isoformat() if last_check else "",
            "results_cache": results_cache
        }, f, indent=4)

# === BOUTON INTERFACE ===

def check_for_updates():
    local = get_local_build_number()
    remote = get_remote_build_number()
    tooltip = "FreeCAD est à jour."
    icon = ICON_UP_TO_DATE

    if local and remote:
        if remote > local:
            icon = ICON_UPDATE_AVAILABLE
            tooltip = f"Mise à jour disponible : {remote} > {local}"
        else:
            tooltip = f"FreeCAD à jour : {local}"
    elif not local:
        tooltip = "Version locale inconnue."
    elif not remote:
        tooltip = "Erreur réseau : version distante non récupérée."

    add_button(icon, tooltip)

def add_button(icon, tooltip):
    mw = Gui.getMainWindow()
    action = QtGui.QAction(icon, "Mise à jour FreeCAD", mw)
    action.setToolTip(tooltip)
    action.triggered.connect(launch_freecad_downloader)

    toolbar = mw.findChild(QtWidgets.QToolBar, "FreeCADUpdateToolbar")
    if not toolbar:
        toolbar = mw.addToolBar("FreeCAD Update")
        toolbar.setObjectName("FreeCADUpdateToolbar")

    for act in toolbar.actions():
        if act.text() == "Mise à jour FreeCAD":
            toolbar.removeAction(act)

    toolbar.addAction(action)

# === FENÊTRE PRINCIPALE ===

class FreeCADDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FreeCAD update checker" + CHECKUPDATEVERSION)
        self.setFixedSize(600, 600)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setPalette(QtWidgets.QApplication.palette())

        self.results = []
        self.old_pos = None

        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        self.liste_files = QtWidgets.QTableWidget(0, 2)
        self.liste_files.setHorizontalHeaderLabels(["Nom du fichier", "Action"])
        self.liste_files.verticalHeader().setVisible(False)
        self.liste_files.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.liste_files.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.liste_files.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.liste_files.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.liste_files.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        layout.addWidget(self.liste_files)

        self.status_label = QtWidgets.QLabel("Chargement...")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setMargin(10)
        layout.addWidget(self.status_label)

        button_layout = QtWidgets.QHBoxLayout()
        update_btn = QtWidgets.QPushButton("Actualiser")
        update_btn.clicked.connect(self.force_update)
        close_btn = QtWidgets.QPushButton("Fermer")
        close_btn.clicked.connect(self.close)

        button_layout.addWidget(update_btn)
        button_layout.addWidget(close_btn)
        layout.addLayout(button_layout)

    def load_data(self):
        last_check, cached_results = read_cache()
        now = datetime.now()

        if not last_check or now - last_check > CHECK_INTERVAL:
            self.results = self.fetch_all_files()
            write_cache(now, self.results)
            self.status_label.setText("Vérification des mises à jour effectuée.")
        else:
            self.results = cached_results
            minutes = int((now - last_check).total_seconds() // 60)
            self.status_label.setText(f"Dernière vérification il y a {minutes} minutes.")

        self.update_ui(self.results)

    def force_update(self):
        self.results = self.fetch_all_files()
        write_cache(datetime.now(), self.results)
        self.status_label.setText("Liste actualisée.")
        self.update_ui(self.results)

    def fetch_all_files(self):
        results = []
        def fetch(url, section):
            results.append((section, ""))
            try:
                r = requests.get(url, timeout=10)
                r.raise_for_status()
                for asset in r.json().get("assets", []):
                    name = asset.get("name", "")
                    durl = asset.get("browser_download_url", "")
                    if name.lower().endswith((".appimage", ".7z", ".dmg")):
                        results.append((name, durl))
            except Exception as e:
                App.Console.PrintError(f"Erreur récupération {section} : {e}\n")

        fetch(URL_STABLE, "Canal Stable :")
        fetch(URL_WEEKLY, "Canal Développement :")
        return results

    def update_ui(self, results):
        self.liste_files.setRowCount(0)

        for name, url in results:
            row = self.liste_files.rowCount()
            self.liste_files.insertRow(row)

            item_name = QtWidgets.QTableWidgetItem(name)
            item_name.setFlags(QtCore.Qt.ItemIsEnabled)

            if not url:
                font = item_name.font()
                font.setBold(True)
                item_name.setFont(font)
                item_name.setBackground(QtGui.QColor("#777777"))
                self.liste_files.setSpan(row, 0, 1, 2)
                self.liste_files.setItem(row, 0, item_name)
            else:
                btn = QtWidgets.QPushButton("Download")
                btn.clicked.connect(partial(webbrowser.open, url))
                self.liste_files.setItem(row, 0, item_name)
                self.liste_files.setCellWidget(row, 1, btn)

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

# === LANCEMENT ===

def launch_freecad_downloader():
    global freecad_downloader_window

    if freecad_downloader_window is None or not freecad_downloader_window.isVisible():
        freecad_downloader_window = FreeCADDownloader()
        freecad_downloader_window.setWindowFlags(QtCore.Qt.Window)
        freecad_downloader_window.setWindowIcon(QtGui.QIcon(":/icons/freecad"))
        freecad_downloader_window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        freecad_downloader_window.destroyed.connect(lambda: clear_reference())
        freecad_downloader_window.show()
    else:
        freecad_downloader_window.raise_()
        freecad_downloader_window.activateWindow()

def clear_reference():
    global freecad_downloader_window
    freecad_downloader_window = None

def run():
    if App.GuiUp:
        check_for_updates()
    else:
        print("Cette macro nécessite l'interface graphique.")

freecad_downloader_window = None
