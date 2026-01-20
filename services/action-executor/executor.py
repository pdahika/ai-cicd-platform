import subprocess
import os

REPO = "https://github.com/pdahika/ai-cicd-platform.git"
GH_TOKEN = os.getenv("GH_TOKEN")

def apply_patch(file, change):
    if not GH_TOKEN:
        raise Exception("GH_TOKEN not set in environment")

    # Inject token into clone URL (secure automation pattern)
    auth_repo = REPO.replace(
        "https://", f"https://{GH_TOKEN}@"
    )

    subprocess.run(["git", "clone", auth_repo], check=True)
    os.chdir("ai-cicd-platform")

    # Configure git identity (required in CI containers)
    subprocess.run(["git", "config", "user.email", "ai-bot@company.local"])
    subprocess.run(["git", "config", "user.name", "ai-fix-bot"])

    # Apply patch
    with open(file, "w") as f:
        f.write(change)

    subprocess.run(["git", "checkout", "-b", "ai-fix"], check=True)
    subprocess.run(["git", "add", file], check=True)
    subprocess.run(["git", "commit", "-m", "AI auto-fix CI failure"], check=True)
    subprocess.run(["git", "push", "origin", "ai-fix"], check=True)

    print("✅ Auto-fix branch pushed successfully.")


