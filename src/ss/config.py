import tomllib
import os
from pathlib import Path
import sys

def load_config(config_path: str = "config.toml"):
    path = Path(config_path)
    if not path.exists():
        print(f"Error: Configuration file not found at {path.absolute()}")
        print("Please create a config.toml based on the documentation.")
        sys.exit(1)
    
    with open(path, "rb") as f:
        config = tomllib.load(f)
    
    # Use [llm] as the base for everything
    base = config.get("llm", {})
        
    # Resulting sections (merging overrides if they exist)
    decoder = base.copy()
    decoder.update(config.get("decoder", {}))
    
    inference = base.copy()
    inference.update(config.get("inference", {}))
            
    # Validation: Ensure critical fields exist
    for section_name, section in [("decoder", decoder), ("inference", inference)]:
        missing = [field for field in ["model", "base_url"] if field not in section]
        if missing:
            print(f"Error: Missing required fields {missing} in [{section_name}] or [llm] section of {config_path}")
            sys.exit(1)
            
    return {
        "decoder": decoder,
        "inference": inference
    }
