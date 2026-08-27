import sys
import re

def audit_curriculum(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # Check 1: Source Verification Table presence
    if "Source Verification Table" not in content:
        errors.append("FAIL: Missing 'Source Verification Table'.")

    # Check 2: Unverified status flag detection in student sections
    if "unverified" in content.lower() and "student-facing" in content.lower():
        errors.append("WARNING: Potential unverified claims detected near student sections.")

    # Check 3: Formative check density scan
    formative_count = content.lower().count("formative_check")
    if formative_count < 1:
        errors.append("FAIL: Insufficient formative check density detected.")

    if errors:
        print(f"QA Audit Failed for {file_path}:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print(f"QA Audit Passed: {file_path} meets pre-flight criteria.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit_curriculum(sys.argv[1])
    else:
        print("Please provide a file path to audit.")