import yaml
import json

def load_rules(file):
    with open(file) as f:
        return yaml.safe_load(f)

def load_layout(file):
    with open(file) as f:
        return json.load(f)

def validate_layout(layout, rules):
    for block in layout:
        if block["spacing"] < rules["spacing"]:
            print(f"[Spacing Violation] Block {block['id']} spacing = {block['spacing']}")
        if block["enclosure"] < rules["enclosure"]:
            print(f"[Enclosure Violation] Block {block['id']} enclosure = {block['enclosure']}")
        if rules.get("connectivity") and not block.get("connected", False):
            print(f"[Connectivity Violation] Block {block['id']} is not connected")

if __name__ == "__main__":
    rules = load_rules("rules.yaml")
    layout = load_layout("layout.json")
    validate_layout(layout, rules)
