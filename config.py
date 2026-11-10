"""VELOCITY WELSH - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY WELSH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "WELSH"
HANDLE = "@velocitywelsh"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "cy",
    "name": "Welsh",
    "native_name": "Cymraeg",
    "history_key": "welsh",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "cy-GB-AledNeural",
    "native_fallback_voice": "cy-GB-NiaNeural",
    "native_engine": "edge",
    "native_lang_code": "cy",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "CYMRAEG",
    "translit_label": "SAY IT LIKE",
    "greeting": "Helo!",
    "encouragement": "Gwych!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Cyfarchion", "hand", "#1CB0F6"),
    ("Basic Phrases", "Brawddegau Sylfaenol", "chat", "#58CC02"),
    ("Common Expressions", "Ymadroddion Cyffredin", "chat", "#1CB0F6"),
    ("Travel", "Teithio", "plane", "#1CB0F6"),
    ("Restaurant", "Bwyty", "fork", "#FF7A00"),
    ("Shopping", "Siopa", "bag", "#E056A0"),
    ("Emergency", "Argyfwng", "siren", "#FF4B4B"),
    ("Family Terms", "Termau Teulu", "heart", "#E056A0"),
    ("Numbers", "Rhifau", "hash", "#A560E8"),
    ("Time", "Amser", "clock", "#00A889"),
    ("Motivation", "Cymhelliant", "rocket", "#A560E8"),
    ("Love", "Cariad", "heart", "#FF4B4B"),
    ("Success", "Llwyddiant", "trophy", "#F5A700"),
    ("Wisdom", "Doethineb", "book", "#A560E8"),
    ("Happiness", "Hapusrwydd", "smile", "#F5A700"),
    ("Self Improvement", "Hunangyflawniad", "leaf", "#58CC02"),
    ("Gratitude", "Diolchgarwch", "heart", "#FF7A00"),
    ("Friendship", "Cyfeillgarwch", "users", "#00A889"),
    ("Hope", "Gobaith", "sun", "#FF7A00"),
    ("Creativity", "Creadigrwydd", "palette", "#E056A0"),
    ("Inner Peace", "Heddwch Mewnol", "lotus", "#00A889"),
    ("Confidence", "Hunanddiffyg", "shield", "#1CB0F6"),
    ("Perseverance", "Dyfalbarhad", "mountain", "#FF7A00"),
    ("Inspiration", "Ysbrydoliaeth", "sparkles", "#A560E8"),
    ("Positive Life", "Bywyd Cadarnhaol", "sun", "#58CC02"),
    ("Courage", "Dewrder", "shield", "#FF4B4B"),
    ("Kindness", "Caredigrwydd", "heart", "#E056A0"),
    ("Patience", "Amynedd", "hourglass", "#00A889"),
    ("Forgiveness", "Maddeuant", "hands", "#FF7A00"),
    ("Strength", "Cryfder", "dumbbell", "#FF4B4B"),
    ("Joy", "Llawenydd", "smile", "#F5A700"),
    ("Balance", "Cydbwysedd", "scale", "#00A889"),
    ("Growth", "Twf", "sprout", "#58CC02"),
    ("Purpose", "Pwrpas", "target", "#A560E8"),
    ("Mindfulness", "Ymwybyddiaeth Ofalgar", "lotus", "#00A889"),
    ("Daily Routine", "Trefn Ddyddiol", "calendar", "#1CB0F6"),
    ("Weather", "Tywydd", "cloud", "#1CB0F6"),
    ("Feelings", "Teimladau", "smile", "#E056A0"),
    ("Food", "Bwyd", "fork", "#FF7A00"),
    ("Health", "Iechyd", "heart", "#58CC02"),
    ("Work", "Gwaith", "briefcase", "#1CB0F6"),
    ("Technology", "Technoleg", "chip", "#A560E8"),
    ("Nature", "Natur", "leaf", "#58CC02"),
    ("Animals", "Anifeiliaid", "paw", "#FF7A00"),
    ("Colors", "Lliwiau", "palette", "#E056A0"),
    ("Directions", "Cyfarwyddiadau", "compass", "#1CB0F6"),
    ("Body Parts", "Rhannau'r Corff", "hand", "#00A889"),
    ("Clothes", "Dillad", "shirt", "#E056A0"),
    ("Music", "Cerddoriaeth", "music", "#A560E8"),
    ("Sports", "Chwaraeon", "ball", "#FF7A00"),
    ("Holidays", "Gwyliau", "gift", "#FF4B4B"),
    ("Education", "Addysg", "book", "#1CB0F6"),
    ("Culture", "Diwylliant", "globe", "#00A889"),
    ("Finance", "Cyllid", "coin", "#58CC02"),
    ("Relationships", "Perthnasoedd", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnwelsh",
    "#welshlessons",
    "#welshforbeginners",
    "#languagelearning",
    "#welshvocabulary",
    "#velocitywelsh",
    "#dailywelsh",
    "#welsh",
    "#learnlanguages",
    "#speakwelsh",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
