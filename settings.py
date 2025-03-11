import json

SETTINGS_FILE = "settings.json"

# Load settings from file
def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"use_bullet_points": False, 
                "min_length": 30,
                "max_length": 100}  # Default settings

# Save settings to file
def save_settings(new_settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(new_settings, f, indent=4)

# Get current settings
current_settings = load_settings()