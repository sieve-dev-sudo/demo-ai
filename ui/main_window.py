"""
ui/main_window.py
Commit 3: Fix Code Mode wired in alongside Lesson Mode, with a toggle button.
Sidebar and the polished ChatPanel/MessageBubble UI arrive in a later commit.
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt

from LessonCodePython.theme import C
from LessonCodePython.lesson_engine import LessonEngine
from FixCode.fix_code_engine import FixCodeEngine, INSTRUCTIONS as FIX_WELCOME

LESSON_WELCOME_TRIGGER = "/start"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐍 Nexus AI — Python Assistant")
        self.resize(1000, 720)
        self.setMinimumSize(800, 540)
        self._engine = LessonEngine()
        self._fix_engine = FixCodeEngine()
        self._mode = "lesson"
        self._build()

    def _build(self):
        root = QWidget()
        root.setStyleSheet(f"background:{C['bg_main']}; color:{C['text_primary']};")
        self.setCentralWidget(root)

        lay = QVBoxLayout(root)

        header = QHBoxLayout()
        self._title = QLabel("📚 Lesson Mode — Python AI Assistant")
        self._title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.addWidget(self._title)

        toggle_btn = QPushButton("🛠 Switch to Fix Code Mode")
        toggle_btn.clicked.connect(self._toggle_mode)
        self._toggle_btn = toggle_btn
        header.addWidget(toggle_btn)
        lay.addLayout(header)

        self._history = QTextEdit()
        self._history.setReadOnly(True)
        self._history.setStyleSheet(
            f"background:{C['bg_input']}; color:{C['text_primary']}; padding:8px;"
        )
        self._history.setText(self._engine.get_response(LESSON_WELCOME_TRIGGER))
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
        engine = self._engine if self._mode == "lesson" else self._fix_engine
        reply = engine.get_response(text)
        self._history.append(f"\n🧑 {text}\n\n🤖 {reply}\n")
        self._input.clear()

    def _toggle_mode(self):
        if self._mode == "lesson":
            self._mode = "fix"
            self._title.setText("🛠 Fix Code Mode — Python AI Assistant")
            self._toggle_btn.setText("📚 Switch to Lesson Mode")
            self._input.setPlaceholderText("Paste your Python code here to fix it…")
            self._history.setText(FIX_WELCOME)
        else:
            self._mode = "lesson"
            self._title.setText("📚 Lesson Mode — Python AI Assistant")
            self._toggle_btn.setText("🛠 Switch to Fix Code Mode")
            self._input.setPlaceholderText("Ask a Python question…")
            self._history.setText(self._engine.get_response(LESSON_WELCOME_TRIGGER))
