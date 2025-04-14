"""
organize_repo_v2.py – Enhanced Organizer for Assistant Launch Pack

This version:
- Creates v1.1–v1.6 folders
- Moves all matching files into their correct version and subfolder
- Prints move log
"""

import os
import shutil

BASE_DIR = os.getcwd()
VERSIONS = ["v1.1", "v1.2", "v1.3", "v1.4", "v1.5", "v1.6"]
SUBFOLDERS = {
    "tabs": ["tab_", "filter_panel", "tab_agent", "tab_usage"],
    "audit": ["_audit", "level5", "final_audit"],
    "handoffs": ["handoff"],
    "idea_log": ["idea_log", "idea"]
}

def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def match_subfolder(filename):
    for folder, keywords in SUBFOLDERS.items():
        for keyword in keywords:
            if keyword.lower() in filename.lower():
                return folder
    return None

def match_version(filename):
    for version in VERSIONS:
        clean = version.replace(".", "")
        if version in filename or f"_v{clean}" in filename or f"v{clean}_" in filename or f"v{clean}-" in filename:
            return version
    return None

def organize_repo():
    files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(f)]

    # Create versioned folders and subfolders
    for version in VERSIONS:
        version_path = os.path.join(BASE_DIR, version)
        safe_mkdir(version_path)
        for sub in SUBFOLDERS:
            safe_mkdir(os.path.join(version_path, sub))

    # Move files
    for file in files:
        version = match_version(file)
        if version:
            subfolder = match_subfolder(file)
            dest_dir = os.path.join(BASE_DIR, version, subfolder) if subfolder else os.path.join(BASE_DIR, version)
            safe_mkdir(dest_dir)
            dest_path = os.path.join(dest_dir, file)
            print(f"➡️ Moving: {file} → {dest_path}")
            shutil.move(os.path.join(BASE_DIR, file), dest_path)

if __name__ == "__main__":
    organize_repo()
    print("✅ Repo organization complete.")
