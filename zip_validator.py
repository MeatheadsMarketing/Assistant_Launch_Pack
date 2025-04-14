
import os
import zipfile
import json
import argparse
import shutil

PLACEHOLDER_KEYWORDS = ["TODO", "pass", "..."]
REQUIRED_FILES = ["run_ui.py", "README.md", "tabs"]
MIN_SIZE_BYTES = 100

def clean_content(content):
    for keyword in PLACEHOLDER_KEYWORDS:
        content = content.replace(keyword, f"# Removed placeholder: {keyword}")
    return content

def validate_zip(zip_path, output_dir="/tmp/validated_zip", fix=False, zip_output=True, json_output=True):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    audit_log = []
    fixed_files = []

    for root, _, files in os.walk(output_dir):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, output_dir)
            file_size = os.path.getsize(file_path)
            status = "✅ OK"

            if file.endswith(".py"):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                for keyword in PLACEHOLDER_KEYWORDS:
                    if keyword in content:
                        status = f"❌ Contains placeholder: {keyword}"
                        if fix:
                            content = clean_content(content)
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(content)
                            status = "✅ Auto-fixed"
                            fixed_files.append(rel_path)
                        break

            if file_size < MIN_SIZE_BYTES:
                status = f"⚠️ File too small: {file_size} bytes"

            audit_log.append({
                "file": rel_path,
                "size": file_size,
                "status": status
            })

    for req in REQUIRED_FILES:
        found = any(req in a['file'] for a in audit_log)
        if not found:
            audit_log.append({
                "file": req,
                "size": 0,
                "status": "❌ MISSING"
            })

    audit_md = os.path.join(output_dir, "validation_report.md")
    with open(audit_md, "w") as f:
        f.write("# ZIP Validation Report\n\n")
        f.write("| File | Size (bytes) | Status |\n")
        f.write("|------|---------------|--------|\n")
        for a in audit_log:
            f.write(f"| `{a['file']}` | {a['size']} | {a['status']} |\n")

    if json_output:
        audit_json = os.path.join(output_dir, "audit_log.json")
        with open(audit_json, "w") as f:
            json.dump(audit_log, f, indent=2)

    cleaned_zip_path = zip_path.replace(".zip", "-clean.zip")
    if zip_output:
        with zipfile.ZipFile(cleaned_zip_path, 'w') as bundle:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    bundle.write(file_path, os.path.relpath(file_path, output_dir))

    print(f"Validation complete.")
    print(f"Audit saved to: {audit_md}")
    if json_output:
        print(f"JSON log saved to: {audit_json}")
    if zip_output:
        print(f"Clean ZIP saved to: {cleaned_zip_path}")
    return audit_md, cleaned_zip_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path", help="Path to the .zip file to validate")
    parser.add_argument("--fix", action="store_true", help="Automatically fix placeholder code")
    parser.add_argument("--no-json", action="store_true", help="Skip JSON output")
    parser.add_argument("--no-zip", action="store_true", help="Skip output of cleaned zip")

    args = parser.parse_args()
    validate_zip(
        zip_path=args.zip_path,
        fix=args.fix,
        zip_output=not args.no_zip,
        json_output=not args.no_json
    )
