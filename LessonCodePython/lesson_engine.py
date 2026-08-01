"""
LessonCodePython/lesson_engine.py — 11 topics
Order matters: more-specific keywords first to avoid wrong matches.
"""
import json
from pathlib import Path

LESSONS_PATH = Path(__file__).resolve().parent / "lessons.json"

# ── ordered list so specific topics match BEFORE generic ones ─────────
# Each entry: (tuple_of_keywords, topic_key)
TOPIC_KEYWORDS = [
    # ── specific first ──────────────────────────────────────────────
    (("data structure","tuple","set","dictionary","dict","key value",
      "hashmap","data_structure"),                       "data_structures"),
    (("*args","**kwargs","kwargs","lambda","higher order",
      "map(","filter(","advanced function","default param",
      "functions_advanced","function advanced"),         "functions_advanced"),
    (("file handling","file_handling","open(","readline","readlines",
      "writelines","encoding","file mode","read file","write file",
      "append file","csv","txt file"),                   "file_handling"),
    (("oop","class","object","inherit","__init__","self.",
      "polymor","encapsul","instance of","override",
      "magic method","__str__","super()"),               "oop"),
    # ── generic topics after ────────────────────────────────────────
    (("basic","comment","indentation","hello world","syntax",
      "python basic","first program"),                   "basic"),
    (("variable","data type","int(","float(","bool","none",
      "type conversion","ប្រភេទ","var ","assign"),        "variables"),
    (("operator","arithmetic","math","calculation","modulo",
      "floor div","bitwise","operator"),                 "operators"),
    (("if ","else:","elif","condition","conditional",
      "ternary","លក្ខខណ្ឌ"),                              "conditional"),
    (("for ","while ","iterate","range(",
      "break","continue","repeat"),                      "loop"),
    (("array","list","append","pop(","sort(","index","slice",
      "បញ្ជី","remove(","insert("),                       "array"),
    (("function","def ","return","parameter","argument",
      "អនុគមន៍","func"),                                  "function"),
]

START_TRIGGERS = ("/start","/help","help","menu","start","មុខងារ")


class LessonEngine:
    def __init__(self, path: Path = LESSONS_PATH):
        self.lessons = json.loads(path.read_text(encoding="utf-8"))

    def get_response(self, user_input: str) -> str:
        text = user_input.strip().lower()

        if text in START_TRIGGERS:
            return self._render(self.lessons["/start"])

        # Exact key match (user typed the key directly)
        for key, value in self.lessons.items():
            if key != "/start" and text == key:
                return self._render(value)

        # Keyword match — ordered list, first match wins
        for keywords, topic in TOPIC_KEYWORDS:
            if any(kw in text for kw in keywords):
                if topic in self.lessons:
                    return self._render(self.lessons[topic])

        return self._fallback(user_input)

    @staticmethod
    def _render(entry) -> str:
        if isinstance(entry, dict):
            theory  = entry.get("theory",  "")
            example = entry.get("example", "")
            return f"{theory}\n\n📝 ឧទាហរណ៍ (Example):\n\n```python\n{example}\n```"
        return entry

    def _fallback(self, user_input: str) -> str:
        topics  = [k for k in self.lessons if k != "/start"]
        listing = "\n".join(f"  • {t}" for t in topics)
        return (
            f'🤔 ខ្ញុំមិនយល់ពី: "{user_input[:60]}"\n\n'
            f"💡 Topics ({len(topics)}):\n\n{listing}\n\n"
            f"👉 វាយ /start ដើម្បីមើល menu ពេញ"
        )
