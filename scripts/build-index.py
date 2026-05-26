import json
import glob
import yaml
import os

demos = []

for filepath in sorted(glob.glob("demos/*/demo.yaml")):
    with open(filepath) as f:
        data = yaml.safe_load(f)
        folder = os.path.dirname(filepath)
        data["path"] = folder + "/index.html"
        data["id"] = os.path.basename(folder)
        data["has_claude_md"] = os.path.exists(os.path.join(folder, "claude.md"))
        demos.append(data)

with open("demos.json", "w") as out:
    json.dump(demos, out, indent=2)

print(f"Built index with {len(demos)} demo(s).")
