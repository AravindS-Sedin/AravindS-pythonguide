import json
from pathlib import Path

DEFAULTS = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "auto_save": True
}

class ConfigManager:

    def __init__(self, path="config.json"):
        self.path = Path(path)
        self.config = self._load()

    def _load(self):

        if not self.path.exists():
            self._save(DEFAULTS)
            return DEFAULTS.copy()

        with open(self.path, "r") as file:
            return json.load(file)


    def _save(self, data):

        with open(self.path, "w") as file:
            json.dump(data, file, indent=2)


    def get(self, key, default=None):

        return self.config.get(key, default)


    def set(self, key, value):

        self.config[key] = value
        self._save(self.config)


    def delete(self, key):

        if key in self.config:
            del self.config[key]
            self._save(self.config)
            return True

        return False


    def reset(self):

        self.config = DEFAULTS.copy()
        self._save(self.config)



def main():

    config = ConfigManager()

    print("Current Config")
    print(config.config)

    print("\nTheme:", config.get("theme"))

    print("\nChanging Theme...")
    config.set("theme", "dark")
    print(config.config)

    print("\nChanging Font Size...")
    config.set("font_size", 18)
    print(config.config)

    print("\nDeleting Language...")
    deleted = config.delete("language")
    print("Deleted:", deleted)
    print(config.config)

    print("\nTrying to Delete Invalid Key...")
    deleted = config.delete("invalid_key")
    print("Deleted:", deleted)

    print("\nResetting Config...")
    config.reset()
    print(config.config)


if __name__ == "__main__":
    main()