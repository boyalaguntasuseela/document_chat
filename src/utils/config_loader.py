import os
import yaml
from pathlib import Path


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_config(config_path: str = None):
    env_path = os.getenv("CONFIG_PATH")

    # Use env variable if config_path not provided
    if config_path is None:
        config_path = env_path

    if config_path is None:
        raise ValueError("Config path is not provided")

    path = Path(config_path)

    # Convert relative path to absolute path
    if not path.is_absolute():
        path = _project_root() / path

    # Check file exists
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    # Load YAML
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}
