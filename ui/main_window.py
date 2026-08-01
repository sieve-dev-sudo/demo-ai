"""
ui/main_window.py
Commit 1: basic window scaffold only.
Sidebar, Chat panel, Lesson engine and Fix Code engine will be
wired in on later commits.
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐍 Nexus AI — Python Assistant")
        self.resize(1000, 720)
        self.setMinimumSize(800, 540)
        self._build()

    def _build(self):
        root = QWidget()
        self.setCentralWidget(root)

        lay = QVBoxLayout(root)
        lay.setAlignment(Qt.AlignCenter)

        title = QLabel("🐍 Nexus AI — Python Assistant")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Project scaffold ready — Lesson Mode and Fix Code Mode coming soon.")
        subtitle.setAlignment(Qt.AlignCenter)

        lay.addWidget(title)
        lay.addWidget(subtitle)
