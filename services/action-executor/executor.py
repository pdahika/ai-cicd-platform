import subprocess
import os

REPO = "https://github.com/pdahika/ai-cicd-platform.git"

def apply_patch(file, change):
    subprocess.run(["git", "clone", REPO])
    os.chdir("ai-cicd-platform")

    with open(file, "w") as f:
        f.write(change)

    subprocess.run(["git", "checkout", "-b", "ai-fix"])
    subprocess.run(["git", "add", file])
    subprocess.run(["git", "commit", "-m", "AI auto-fix CI failure"])
    subprocess.run(["git", "push", "origin", "ai-fix"])

