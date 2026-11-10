"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Helo, pleser eich cyfarfod.", "transliteration": "Helo, plesser ych kyfarfod."},
    {"english": "Thank you very much.", "native": "Diolch yn fawr iawn.", "transliteration": "Diolch yn fawr iawn."},
    {"english": "Good morning, have a great day.", "native": "Bore da, cael diwrnod gwych.", "transliteration": "Bore da, cael diwrnod gwych."},
    {"english": "I love learning new languages.", "native": "Dw i'n hoffi dysgu ieithoedd newydd.", "transliteration": "Doo ee'n hoffi dysgu ieithoedd newydd."},
    {"english": "Never give up on your dreams.", "native": "Peidiwch byth â rhoi'r gorau i'ch breuddwydion.", "transliteration": "Peidiwch byth ah roi'r gorau i'ch breuddwydion."},
    {"english": "Every day is a fresh start.", "native": "Bob dydd yw dechrau newydd.", "transliteration": "Bob dydd yw dechrau newydd."},
    {"english": "Believe in yourself always.", "native": "Credu ynoch chi'ch hun bob amser.", "transliteration": "Creddu ynoch chi'ch hun bob amser."},
    {"english": "Small steps lead to big changes.", "native": "Camau bach yn arwain at newidiadau mawr.", "transliteration": "Camau bach yn arwain at newidiadau mawr."},
    {"english": "You are stronger than you think.", "native": "Rydych chi'n gryfach nag yr ydych chi'n meddwl.", "transliteration": "Rydych chi'n gryfach nag yr ydych chi'n meddwl."},
    {"english": "Happiness is a choice, choose it.", "native": "Mae hapusrwydd yn ddewis, dewiswch ef.", "transliteration": "Mae hapusrwydd yn ddewis, dewiswch ef."},
    {"english": "What time is it please.", "native": "Pa bryd mae hi os gwelwch yn dda.", "transliteration": "Pa bryd mae hi os gwelwch yn dda."},
    {"english": "Where is the train station.", "native": "Ble mae'r orsaf trên.", "transliteration": "Ble mae'r orsaf trên."},
    {"english": "How much does this cost.", "native": "Faint mae hyn yn costio.", "transliteration": "Faint mae hyn yn costio."},
    {"english": "Can you help me please.", "native": "Allwch chi fy helpu os gwelwch yn dda.", "transliteration": "Allwch chi fy helpu os gwelwch yn dda."},
    {"english": "I would like a coffee please.", "native": "Byddwn i'n hoffi coffi os gwelwch yn dda.", "transliteration": "Byddwn ee'n hoffi coffi os gwelwch yn dda."},
    {"english": "The food is delicious today.", "native": "Mae'r bwyd yn flasus heddiw.", "transliteration": "Mae'r bwyd yn flasus heddiw."},
    {"english": "Have a wonderful weekend.", "native": "Cael penwythnos hyfryd.", "transliteration": "Cael penwythnos hyfryd."},
    {"english": "Take care of yourself.", "native": "Gofalwch amdanoch chi'ch hun.", "transliteration": "Gofalwch amdanoch chi'ch hun."},
    {"english": "See you tomorrow my friend.", "native": "Welwn ni ti yfory fy ffrind.", "transliteration": "Welwn ni ti yfory fy ffrind."},
    {"english": "The weather is beautiful outside.", "native": "Mae'r tywydd yn brydferth y tu allan.", "transliteration": "Mae'r tywydd yn brydferth y tu allan."},
    {"english": "I am very happy today.", "native": "Dw i'n hapus iawn heddiw.", "transliteration": "Doo ee'n hapus iawn heddiw."},
    {"english": "Learning a language opens new doors.", "native": "Mae dysgu iaith yn agor drysau newydd.", "transliteration": "Mae dysgu iaith yn agor drysau newydd."},
    {"english": "Keep practicing every single day.", "native": "Parhewch i ymarfer bob dydd.", "transliteration": "Parhewch i ymarfer bob dydd."},
    {"english": "You can achieve anything you want.", "native": "Gallwch gyflawni unrhyw beth yr ydych chi ei eisiau.", "transliteration": "Gallwch gyflawni unrhyw beth yr ydych chi ei eisiau."},
    {"english": "Rest when you are tired.", "native": "Gorffwyswch pan fyddwch chi'n flinedig.", "transliteration": "Gorffwyswch pan fyddwch chi'n flinedig."},
    {"english": "Focus on the positive things.", "native": "Canolbwyntiwch ar y pethau positif.", "transliteration": "Canolbwyntiwch ar y pethau positif."},
    {"english": "Learn from your mistakes.", "native": "Dysgwch o'ch camgymeriadau.", "transliteration": "Dysgwch o'ch camgymeriadau."},
    {"english": "Trust the process completely.", "native": "Ymddiried yn y broses yn llwyr.", "transliteration": "Ymddiried yn y broses yn llwyr."},
    {"english": "Breathe deeply and stay calm.", "native": "Anadlwch yn ddwfn ac arhoswch yn dawel.", "transliteration": "Anadlwch yn ddwfn ac arhoswch yn dawel."},
    {"english": "Enjoy the little moments in life.", "native": "Mwynhewch y munudau bach mewn bywyd.", "transliteration": "Mwynhewch y munudau bach mewn bywyd."},
    {"english": "Smile more, worry less.", "native": "Gwenwch yn fwy, peidiwch â phoeni llai.", "transliteration": "Gwenwch yn fwy, peidiwch ah phoeni llai."},
    {"english": "Be kind to everyone you meet.", "native": "Byddwch yn garedig â phawb yr ydych chi'n cwrdd â nhw.", "transliteration": "Byddwch yn garedig ah pawb yr ydych chi'n cwrdd â nhw."},
    {"english": "Help others without expecting anything back.", "native": "Helpwch eraill heb ddisgwyl dim yn ôl.", "transliteration": "Helpwch eraill heb ddisgwyl dim yn ôl."},
    {"english": "Forgive yourself and move forward.", "native": "Maddeuwch i chi'ch hun a symud ymlaen.", "transliteration": "Maddeuwch i chi'ch hun a symud ymlaen."},
    {"english": "Stay strong in difficult times.", "native": "Arhoswch yn gryf mewn amseroedd anodd.", "transliteration": "Arhoswch yn gryf mewn amseroedd anodd."},
    {"english": "Every moment is a new beginning.", "native": "Bob munud yw dechrau newydd.", "transliteration": "Bob munud yw dechrau newydd."},
    {"english": "Listen to your heart always.", "native": "Gwrandewch ar eich calon bob amser.", "transliteration": "Gwrandewch ar eich calon bob amser."},
    {"english": "Do what makes you happy.", "native": "Gwnewch yr hyn sy'n eich gwneud chi'n hapus.", "transliteration": "Gwnewch yr hyn sy'n eich gwneud chi'n hapus."},
    {"english": "Your potential is unlimited.", "native": "Mae eich potensial yn ddiderfyn.", "transliteration": "Mae eich potensial yn ddiderfyn."},
    {"english": "Be brave and take risks.", "native": "Byddwch yn ddewr a chymerwch risgiau.", "transliteration": "Byddwch yn ddewr a chymerwch risgiau."},
    {"english": "Celebrate your progress every day.", "native": "Dathlwch eich cynnydd bob dydd.", "transliteration": "Dathlwch eich cynnydd bob dydd."},
    {"english": "Surround yourself with good people.", "native": "Amgylchynwch eich hun â phobl dda.", "transliteration": "Amgylchynwch eich hun ah pobl dda."},
    {"english": "Read books and grow your mind.", "native": "Darllenwch lyfrau a thyfwch eich meddwl.", "transliteration": "Darllenwch lyfrau a thyfwch eich meddwl."},
    {"english": "Travel and discover new places.", "native": "Teithiwch a darganfyddwch leoedd newydd.", "transliteration": "Teithiwch a darganfyddwch leoedd newydd."},
    {"english": "Appreciate what you already have.", "native": "Gwerthfawrogwch yr hyn sydd gennych eisoes.", "transliteration": "Gwerthfawrogwch yr hyn sydd gennych eisoes."},
    {"english": "Dance like nobody is watching.", "native": "Dawnsiwch fel pe na bai neb yn gwylio.", "transliteration": "Dawnsiwch fel pe na bai neb yn gwylio."},
    {"english": "Sing from your heart out loud.", "native": "Cânwch o'ch calon yn uchel.", "transliteration": "Cânwch o'ch calon yn uchel."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Plannwch hadau caredigrwydd ym mhobman.", "transliteration": "Plannwch hadau caredigrwydd ym mhobman."},
    {"english": "Let go of what you cannot control.", "native": "Rhyddhewch yr hyn na allwch ei reoli.", "transliteration": "Rhyddhewch yr hyn na allwch ei reoli."},
    {"english": "Be present in the here and now.", "native": "Byddwch yn bresennol yn y fan a'r lle.", "transliteration": "Byddwch yn bresennol yn y fan ah'r lle."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
