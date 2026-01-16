import streamlit as st
import os

from utils import compute_metrics, save_user_progress, load_user_progress
from quiz_engine import QuizEngine
from ai_engine import AIDecisionEngine
from utils import compute_metrics
import plotly.graph_objects as go

def accuracy_gauge(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value * 100,
        title={"text": "Accuracy (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#6c63ff"},
        }
    ))
    fig.update_layout(height=250, margin=dict(t=30, b=0))
    return fig



BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


QUIZ_PATH = os.path.join(BASE_PATH, "data", "quizzes", "python_basics.json")
MODEL_PATH = os.path.join(BASE_PATH, "models", "nerdbud_model.pkl")

st.set_page_config(page_title="NerdBud", layout="centered")

st.title("🤓 NerdBud – Personalized Learning AI")

st.markdown("""
<style>
.metric-card {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.user-card {
    background: linear-gradient(135deg, #6c63ff, #48c6ef);
    color: white;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="user-card">
        <h3>👤 {user_id}</h3>
        <p>Learning Dashboard</p>
    </div>
    """,
    unsafe_allow_html=True
)



username = st.text_input("Your Name")
user_id = st.text_input("Username (unique)")

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "show_results" not in st.session_state:
    st.session_state.show_results = False

if st.button("Start NerdBud"):
    st.session_state.quiz = QuizEngine(QUIZ_PATH)
    st.session_state.show_results = False

quiz = st.session_state.quiz

if quiz and not st.session_state.show_results:
    q = quiz.get_question()

    st.subheader(q["question"])
    answer = st.radio("Choose an option:", q["options"])

    if st.button("Submit"):
        has_next = quiz.submit_answer(answer)
        if not has_next:
            st.session_state.show_results = True
        st.rerun()


if st.session_state.show_results and quiz:
    # 1️⃣ Compute metrics FIRST
    metrics = compute_metrics(quiz.results())

    # 2️⃣ AI decisions
    ai = AIDecisionEngine(MODEL_PATH)
    rule = ai.rule_based(metrics)
    ml = ai.ml_based(metrics)

    # 3️⃣ Save user progress
    if user_id:
        save_user_progress(user_id, metrics, ml)

    # 4️⃣ Display results
    st.metric("Accuracy", metrics["accuracy"])
    st.metric("Avg Time", metrics["avg_time"])

    st.subheader("📊 Topic Performance")
    st.bar_chart(metrics["topic_perf"])

    st.subheader("🤖 AI Decision")
    st.write(f"Rule-Based: **{rule}**")
    st.write(f"ML-Based: **{ml}**")

    # 5️⃣ Load and show history
    if user_id:
        history = load_user_progress(user_id)
        if history is not None:
            st.subheader("📈 Your Learning History")
            st.line_chart(history["accuracy"])
    
    st.plotly_chart(
    accuracy_gauge(metrics["accuracy"]),
    use_container_width=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='metric-card'><h4>Attempts</h4><h2>{metrics['attempts']}</h2></div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-card'><h4>Avg Time (sec)</h4><h2>{metrics['avg_time']}</h2></div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='metric-card'><h4>Decision</h4><h2>{ml}</h2></div>",
            unsafe_allow_html=True
        )
    st.subheader("📊 Topic Performance")
    st.bar_chart(metrics["topic_perf"])

