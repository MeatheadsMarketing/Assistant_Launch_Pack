"""
assistant_packager.py – Assistant Launch Pack v1.5

Exports full assistant packs by tag into a ZIP with metadata and relevant content.
"""

import os
import json
import zipfile
from datetime import datetime
import shutil

REGISTRY_PATH = "agent_registry.json"
EXPORT_DIR = "packs"
SOURCE_DIR = "assistant_modules"  # You can copy real agent folders here

def package_assistants(tag="gpt"):
    if not os.path.exists(REGISTRY_PATH):
        print("❌ No registry found.")
        return None

    with open(REGISTRY_PATH, "r") as f:
        data = json.load(f)

    matching = [a for a in data["agents"] if tag in a.get("tags", [])]
    if not matching:
        print(f"⚠️ No assistants found with tag: {tag}")
        return None

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    pack_name = f"assistant_pack_{tag}_{timestamp}.zip"
    pack_path = os.path.join(EXPORT_DIR, pack_name)
    os.makedirs(EXPORT_DIR, exist_ok=True)

    with zipfile.ZipFile(pack_path, "w") as zipf:
        # Export registry subset
        zipf.writestr("registry_subset.json", json.dumps({"agents": matching}, indent=2))

        # Optionally include assistant folders if they exist in /assistant_modules/
        for agent in matching:
            folder_name = agent.get("name", "").replace(" ", "_").lower()
            agent_dir = os.path.join(SOURCE_DIR, folder_name)
            if os.path.isdir(agent_dir):
                for root, _, files in os.walk(agent_dir):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, SOURCE_DIR)
                        zipf.write(full_path, os.path.join("modules", arcname))

    print(f"✅ Packaged {len(matching)} assistants to {pack_path}")
    return pack_path

# Example call
if __name__ == "__main__":
    package_assistants("gpt")
