import json
import re
import sys
import os

def extract(rpy_path, out_json_path):
    with open(rpy_path, "r", encoding="utf-8") as f:
        content = f.read()

    items = []
    
    # Dialogue pattern
    # translate indonesian <id>:\n\n    # <speaker> "<english>"\n    <speaker> "<target>"
    dialogue_pattern = re.compile(
        r'translate indonesian (\w+):\s*\n\s*# (?:([a-zA-Z0-9_]+) )?\"(.*?)\"\s*\n\s*(?:([a-zA-Z0-9_]+) )?\"(.*?)\"',
        re.DOTALL
    )
    
    for match in dialogue_pattern.finditer(content):
        label_id = match.group(1)
        orig_speaker = match.group(2) or ""
        orig_text = match.group(3)
        target_speaker = match.group(4) or ""
        target_text = match.group(5)
        
        items.append({
            "type": "dialogue",
            "id": label_id,
            "speaker": orig_speaker,
            "english": orig_text,
            "indonesian": target_text if target_text != orig_text else ""
        })

    # Strings pattern
    # old "<old>"\n    new "<new>"
    string_pattern = re.compile(r'old \"(.*?)\"\s*\n\s*new \"(.*?)\"', re.DOTALL)
    for match in string_pattern.finditer(content):
        old_text = match.group(1)
        new_text = match.group(2)
        items.append({
            "type": "string",
            "english": old_text,
            "indonesian": new_text if new_text != old_text else ""
        })

    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(items)} items from {rpy_path} into {out_json_path}")


def apply(in_json_path, rpy_path):
    with open(in_json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    with open(rpy_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Map dialogue by id
    dialogue_map = {item["id"]: item for item in items if item["type"] == "dialogue"}
    # Map string by english text
    string_map = {item["english"]: item for item in items if item["type"] == "string"}

    def replace_dialogue(match):
        label_id = match.group(1)
        speaker_comment = match.group(2)
        speaker_code = match.group(3)
        
        if label_id in dialogue_map:
            item = dialogue_map[label_id]
            indo = item.get("indonesian", "").strip()
            if indo:
                indo_escaped = ""
                i = 0
                while i < len(indo):
                    if indo[i] == '"' and (i == 0 or indo[i-1] != '\\'):
                        indo_escaped += '\\"'
                    else:
                        indo_escaped += indo[i]
                    i += 1
                spk = f"{speaker_code} " if speaker_code else ""
                return f'translate indonesian {label_id}:\n\n    # {speaker_comment}\n    {spk}"{indo_escaped}"'
        return match.group(0)

    dialogue_replace_pattern = re.compile(
        r'translate indonesian (\w+):\s*\n\s*# ([^\n]+)\n\s*([a-zA-Z0-9_]+ )?\"[^\n]*\"'
    )
    content = dialogue_replace_pattern.sub(replace_dialogue, content)

    def replace_string(match):
        old_text = match.group(1)
        if old_text in string_map:
            item = string_map[old_text]
            indo = item.get("indonesian", "").strip()
            if indo:
                indo_escaped = ""
                i = 0
                while i < len(indo):
                    if indo[i] == '"' and (i == 0 or indo[i-1] != '\\'):
                        indo_escaped += '\\"'
                    else:
                        indo_escaped += indo[i]
                    i += 1
                return f'old "{old_text}"\n    new "{indo_escaped}"'
        return match.group(0)

    string_replace_pattern = re.compile(r'old \"([^\n]+)\"\s*\n\s*new \"[^\n]*\"')
    content = string_replace_pattern.sub(replace_string, content)

    with open(rpy_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Applied translations from {in_json_path} to {rpy_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python translate_helper.py <extract|apply> <rpy_path> <json_path>")
        sys.exit(1)
    action = sys.argv[1]
    rpy_path = sys.argv[2]
    json_path = sys.argv[3]
    if action == "extract":
        extract(rpy_path, json_path)
    elif action == "apply":
        apply(json_path, rpy_path)
