import os
import pandas as pd

# -----------------------------
# Metrics computation
# -----------------------------
def compute_metrics(responses):
    df = pd.DataFrame(responses)

    return {
        "accuracy": round(df["correct"].mean(), 2),
        "avg_time": round(df["time_taken"].mean(), 2),
        "attempts": len(df),
        "topic_perf": df.groupby("topic")["correct"].mean()
    }

# -----------------------------
# User progress persistence
# -----------------------------
def save_user_progress(username, metrics, decision):
    os.makedirs("data/user_progress", exist_ok=True)

    path = f"data/user_progress/{username}.csv"

    row = {
        "accuracy": metrics["accuracy"],
        "avg_time": metrics["avg_time"],
        "attempts": metrics["attempts"],
        "decision": decision
    }

    df = pd.DataFrame([row])

    if os.path.exists(path):
        df.to_csv(path, mode="a", header=False, index=False)
    else:
        df.to_csv(path, index=False)

def load_user_progress(username):
    path = f"data/user_progress/{username}.csv"

    if os.path.exists(path):
        return pd.read_csv(path)

    return None
