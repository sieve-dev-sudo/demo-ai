#!/usr/bin/env python3
"""
main.py — Entry point for Nexus AI Python Assistant
Run:
    pip install -r requirements.txt
    python main.py
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor

from ui.main_window import MainWindow

# Base dark palette colors (will move to LessonCodePython/theme.py in a later commit)
BG_MAIN    = "#0f1115"
BG_INPUT   = "#181b21"
BG_CARD    = "#1c1f26"
TEXT       = "#e6e6e6"
TEXT_MUTED = "#8a8f98"
ACCENT     = "#5865f2"


def build_dark_palette() -> QPalette:
    pal = QPalette()
    pal.setColor(QPalette.Window,          QColor(BG_MAIN))
    pal.setColor(QPalette.WindowText,      QColor(TEXT))
    pal.setColor(QPalette.Base,            QColor(BG_INPUT))
    pal.setColor(QPalette.AlternateBase,   QColor(BG_CARD))
    pal.setColor(QPalette.Text,            QColor(TEXT))
    pal.setColor(QPalette.ButtonText,      QColor(TEXT))
    pal.setColor(QPalette.Button,          QColor(BG_CARD))
    pal.setColor(QPalette.Highlight,       QColor(ACCENT))
    pal.setColor(QPalette.HighlightedText, QColor("#ffffff"))
    pal.setColor(QPalette.PlaceholderText, QColor(TEXT_MUTED))
    return pal


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Nexus AI — Python Assistant")
    app.setStyle("Fusion")
    app.setPalette(build_dark_palette())
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
