import json
import time

class QuizEngine:
    def __init__(self, quiz_path):
        with open(quiz_path, "r") as f:
            self.quiz_data = json.load(f)["Beginner"]

        self.current_q = 0
        self.responses = []
        self.start_time = None

    def get_question(self):
        q = self.quiz_data[self.current_q]
        self.start_time = time.time()
        return q

    def submit_answer(self, selected):
        q = self.quiz_data[self.current_q]
        time_taken = round(time.time() - self.start_time, 2)
        correct = selected == q["answer"]

        self.responses.append({
            "topic": q["topic"],
            "correct": int(correct),
            "time_taken": time_taken
        })

        self.current_q += 1
        return self.current_q < len(self.quiz_data)

    def results(self):
        return self.responses
