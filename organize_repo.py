"""
organize_repo.py – Assistant Launch Pack Organizer

Auto-organizes files into v1.1–v1.6 structure:
- Creates version folders
- Moves files based on prefix
- Builds /tabs, /audit, /handoffs, /idea_log inside each version
"""

import os
import shutil

BASE_DIR = os.getcwd()
VERSIONS = ["v1.1", "v1.2", "v1.3", "v1.4", "v1.5", "v1.6"]
SUBFOLDERS = ["tabs", "audit", "handoffs", "idea_log"]

def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file_to_version(file, version):
    target_dir = os.path.join(BASE_DIR, version)
    safe_mkdir(target_dir)

    # Handle by suffix
    if "tab_" in file:
        dest = os.path.join(target_dir, "tabs")
    elif "_audit" in file:
        dest = os.path.join(target_dir, "audit")
    elif "handoff" in file:
        dest = os.path.join(target_dir, "handoffs")
    elif "idea_log" in file or "idea" in file:
        dest = os.path.join(target_dir, "idea_log")
    else:
        dest = target_dir

    safe_mkdir(dest)
    shutil.move(file, os.path.join(dest, file))

def organize_repo():
    files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(f)]

    for version in VERSIONS:
        safe_mkdir(os.path.join(BASE_DIR, version))
        for sub in SUBFOLDERS:
            safe_mkdir(os.path.join(BASE_DIR, version, sub))

    for file in files:
        for version in VERSIONS:
            if file.startswith(version) or f"_{version.replace('.', '')}" in file:
                move_file_to_version(file, version)
                break
            if file.endswith(".py") and version in file:
                move_file_to_version(file, version)
                break

if __name__ == "__main__":
    organize_repo()
    print("✅ Assistant Launch Pack repo organized by version.")
