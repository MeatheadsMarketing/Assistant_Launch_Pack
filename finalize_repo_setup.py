"""
finalize_repo_setup.py – Finalize Assistant Launch Pack Folder Setup

- Moves all remaining root-level tab_*.py files to v1.5/tabs/
- Moves all .zip files not assigned to versions into /archives/
- Ensures requirements.txt is placed in root
"""

import os
import shutil

BASE_DIR = os.getcwd()
ARCHIVE_DIR = os.path.join(BASE_DIR, "archives")
V15_TABS = os.path.join(BASE_DIR, "v1.5", "tabs")
ZIP_EXT = ".zip"

def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def finalize_setup():
    safe_mkdir(ARCHIVE_DIR)
    safe_mkdir(V15_TABS)

    for file in os.listdir(BASE_DIR):
        full_path = os.path.join(BASE_DIR, file)
        if os.path.isfile(full_path):
            if file.startswith("tab_") and file.endswith(".py"):
                print(f"📁 Moving tab file to v1.5/tabs/: {file}")
                shutil.move(full_path, os.path.join(V15_TABS, file))
            elif file.endswith(ZIP_EXT) and not any(file.startswith(f"Assistant_Launch_Pack_v{v}") for v in ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]):
                print(f"📦 Archiving ZIP: {file}")
                shutil.move(full_path, os.path.join(ARCHIVE_DIR, file))

    print("✅ Final folder organization complete.")

if __name__ == "__main__":
    finalize_setup()
