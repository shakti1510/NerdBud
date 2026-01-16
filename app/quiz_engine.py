import json
import random
import time


class QuizEngine:
    def __init__(self, quiz_path, level="Beginner", num_questions=10):
        # Load question bank
        with open(quiz_path, "r") as f:
            bank = json.load(f)

        # Flatten questions and tag difficulty level
        all_questions = []
        for lvl, questions in bank.items():
            for q in questions:
                q_copy = q.copy()
                q_copy["level"] = lvl
                all_questions.append(q_copy)

        # Filter questions based on selected level
        if level == "Beginner":
            eligible = [q for q in all_questions if q["level"] == "Beginner"]
        elif level == "Intermediate":
            eligible = [q for q in all_questions if q["level"] in ["Beginner", "Intermediate"]]
        else:
            eligible = all_questions


        # Randomly select questions
        self.questions = random.sample(
            eligible,
            min(num_questions, len(eligible))
        )

        # Shuffle options for each question
        for q in self.questions:
            shuffled_options = q["options"].copy()
            random.shuffle(shuffled_options)
            q["options"] = shuffled_options

        # Quiz state
        self.current_q = 0
        self.correct = 0
        self.responses = []
        self.start_time = None

    def get_question(self):
        """
        Returns the current question and starts timing
        """
        if self.current_q < len(self.questions):
            self.start_time = time.time()
            return self.questions[self.current_q]
        return None

    def submit_answer(self, selected):
        """
        Stores user response and calculates time taken
        """
        end_time = time.time()
        time_taken = round(end_time - self.start_time, 2)

        q = self.questions[self.current_q]
        correct_answer = q["answer"]

        self.responses.append({
            "question": q["question"],
            "selected": selected,
            "correct": correct_answer,
            "is_correct": selected == correct_answer,
            "topic": q.get("topic", "General"),
            "time_taken": time_taken
        })

        if selected == correct_answer:
            self.correct += 1

        self.current_q += 1

    def is_finished(self):
        """
        Checks if quiz is completed
        """
        return self.current_q >= len(self.questions)

    def results(self):
        """
        Returns results for metrics calculation
        """
        return {
            "total_questions": len(self.questions),
            "correct": self.correct,
            "responses": self.responses
        }
