from dotenv import load_dotenv
load_dotenv()  # Loads .env for local runs (no effect in Docker/CI)

from slack_sdk import WebClient
import os
import time

# ---- Load configuration from environment ----

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#ci-alerts")

if not SLACK_TOKEN:
    raise RuntimeError("❌ SLACK_TOKEN is not set. Did you forget to load .env or secrets?")

# ---- Initialize Slack client ----

client = WebClient(token=SLACK_TOKEN)

# ---- Basic notification ----

def notify(msg: str):
    """
    Send a simple notification message to Slack.
    """
    client.chat_postMessage(channel=SLACK_CHANNEL, text=msg)


# ---- Human-in-the-loop approval request ----

def request_approval(pr_url: str) -> str:
    """
    Send a CI failure message with PR link and ask for approval.
    Returns the Slack message timestamp (ts) for tracking replies.
    """
    msg = client.chat_postMessage(
        channel=SLACK_CHANNEL,
        text=(
            "🚨 *CI Failed*\n"
            f"🤖 AI fix PR created: {pr_url}\n\n"
            "Approve? (yes/no)"
        )
    )

    return msg["ts"]


def wait_for_approval(timeout_sec: int = 300) -> bool:
    """
    Dummy approval waiter (polling simulation).
    In real systems, this is replaced by Slack Events API / Interactivity.
    """
    print("⏳ Waiting for human approval (simulated)...")

    waited = 0
    poll_interval = 10

    while waited < timeout_sec:
        time.sleep(poll_interval)
        waited += poll_interval

        # ---- Simulated approval result ----
        # Replace this later with real Slack Events API logic
        print("✅ Simulated approval received.")
        return True

    print("⏰ Approval timeout reached.")
    return False


# ---- Local test entrypoint ----

if __name__ == "__main__":
    pr_url = "https://github.com/org/repo/pull/42"

    print("📤 Sending approval request to Slack...")
    ts = request_approval(pr_url)
    print(f"Approval request sent. Slack ts={ts}")

    approved = wait_for_approval()

    if approved:
        notify("✅ Fix approved by human. Merging PR and redeploying.")
    else:
        notify("❌ Fix rejected by human. Manual intervention required.")
