import os
import pandas as pd

# -----------------------------
# Metrics computation
# -----------------------------
def compute_metrics(results):
    """
    Computes performance metrics from quiz results.
    Safely handles missing fields.
    """

    responses = results.get("responses", [])

    # Handle empty quiz case
    if not responses:
        return {
            "accuracy": 0,
            "avg_time": 0,
            "attempts": 0,
            "topic_perf": {}
        }

    df = pd.DataFrame(responses)

    # ✅ SAFETY: ensure time_taken exists
    if "time_taken" not in df.columns:
        df["time_taken"] = 0

    accuracy = results["correct"] / results["total_questions"]

    avg_time = round(df["time_taken"].mean(), 2)

    topic_perf = (
        df.groupby("topic")["is_correct"]
        .mean()
        .to_dict()
    )

    return {
        "accuracy": round(accuracy, 2),
        "avg_time": avg_time,
        "attempts": len(df),
        "topic_perf": topic_perf
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

