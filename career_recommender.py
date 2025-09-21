# backend/career_recommender.py
import os
import json
from pathlib import Path

def load_careers():
    """
    Load career data from JSON file.
    Works regardless of where the app.py is located.
    """
    # Get path relative to this file (career_recommender.py)
    current_dir = Path(__file__).parent.parent  # go up from backend/ to root
    skills_file = current_dir / "data" / "skills.json"

    # Check if file exists
    if not skills_file.exists():
        raise FileNotFoundError(f"⚠️ skills.json not found at {skills_file}")

    # Load JSON data
    with open(skills_file, "r") as f:
        data = json.load(f)
    return data


def get_career_advice(career_goal: str):
    """
    Return career details if available.
    career_goal: string (e.g., "data scientist")
    """
    data = load_careers()
    key = career_goal.strip().lower()
    return data.get(key, None)
