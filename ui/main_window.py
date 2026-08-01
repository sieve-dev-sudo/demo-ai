"""
ui/main_window.py
Commit 2: Lesson Mode wired in with a simple chat box.
Sidebar and the polished ChatPanel/MessageBubble UI arrive in a later commit.
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt

from LessonCodePython.theme import C
from LessonCodePython.lesson_engine import LessonEngine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐍 Nexus AI — Python Assistant")
        self.resize(1000, 720)
        self.setMinimumSize(800, 540)
        self._engine = LessonEngine()
        self._build()

    def _build(self):
        root = QWidget()
        root.setStyleSheet(f"background:{C['bg_main']}; color:{C['text_primary']};")
        self.setCentralWidget(root)

        lay = QVBoxLayout(root)

        title = QLabel("📚 Lesson Mode — Python AI Assistant")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        lay.addWidget(title)

        self._history = QTextEdit()
        self._history.setReadOnly(True)
        self._history.setStyleSheet(
            f"background:{C['bg_input']}; color:{C['text_primary']}; padding:8px;"
        )
        self._history.setText(self._engine.get_response("/start"))
        lay.addWidget(self._history)

        input_row = QHBoxLayout()
        self._input = QLineEdit()
        self._input.setPlaceholderText("Ask a Python question…")
        self._input.returnPressed.connect(self._on_send)

        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self._on_send)

        input_row.addWidget(self._input)
        input_row.addWidget(send_btn)
        lay.addLayout(input_row)

    def _on_send(self):
        text = self._input.text().strip()
        if not text:
            return
        reply = self._engine.get_response(text)
        self._history.append(f"\n🧑 {text}\n\n🤖 {reply}\n")
        self._input.clear()
