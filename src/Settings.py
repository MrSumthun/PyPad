import json
import os
import platform
from pathlib import Path
from src.Console_Handler import log_event
DEFAULTS = {
    "geometry": "780x434",
    "theme": "auto",   # "auto", "light", "dark"
    "last_file": ""
}

def config_dir():
    sys = platform.system()
    home = Path.home()
    if sys == "Darwin":
        return home / "Library" / "Application Support" / "PyPad"
    if sys == "Windows":
        return Path(os.getenv("APPDATA", home)) / "PyPad"
    return home / ".config" / "pypad"

def settings_path():
    d = config_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d / "settings.json"

def load_settings():
    p = settings_path()
    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return DEFAULTS.copy()
            # merge defaults to ensure keys exist
            merged = DEFAULTS.copy()
            merged.update(data)
            return merged
    except FileNotFoundError:
        log_event("Settings file not found, loading defaults.")
        return DEFAULTS.copy()
    except Exception:
        log_event("Error loading settings, loading defaults.")
        return DEFAULTS.copy()

def save_settings(d):
    p = settings_path()
    try:
        with p.open("w", encoding="utf-8") as f:
            json.dump(d, f, indent=2)
    except Exception:
        log_event("Error saving settings.")
        pass