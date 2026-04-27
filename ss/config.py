import tomllib
import os
from pathlib import Path

DEFAULT_CONFIG = {
    "decoder": {
        "model": "gpt-4o",
        "base_url": "https://api.openai.com/v1",
        "api_key": ""
    },
    "inference": {
        "model": "gpt-4o",
        "base_url": "https://api.openai.com/v1",
        "api_key": ""
    }
}

def load_config(config_path: str = "config.toml"):
    path = Path(config_path)
    if not path.exists():
        return DEFAULT_CONFIG
    
    with open(path, "rb") as f:
        config = tomllib.load(f)
    
    # Merge with defaults
    merged = DEFAULT_CONFIG.copy()
    for section in ["decoder", "inference"]:
        if section in config:
            merged[section].update(config[section])
            
    return merged
