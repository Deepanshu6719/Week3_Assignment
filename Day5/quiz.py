"""A simple command-line Python quiz game"""

import random

class Question:
    """Represent a quiz question."""
    # pylint: disable=too-few-public-methods
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        """Check the user's answer."""
        return user_answer == self.answer.lower()

class QuizGame:
    """Represent and manage the quiz game."""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.questions = [
            Question(
                "Which keyword is used to define a function?",
                "def"
            ),
            Question(
                "Which data type stores key-value pairs?",
                "dictionary"
            ),
            Question(
                "Which symbol is used for comments?",
                "#"
            ),
        ]

        self.score = 0
        self.attempted = 0

    def start(self):
        """Start the quiz."""

        print("Welcome to Python Quiz!")
        choice = input(
            "Are you ready to play? (yes/no): "
        ).strip().lower()

        if choice == "yes":
            self.play()
        else:
            print("Maybe next time. Bye!")

    def play(self):
        """Run all quiz questions in random order."""

        question_queue = self.questions.copy()
        random.shuffle(question_queue)

        for number, question in enumerate(question_queue, start=1):

            print(f"\nQuestion {number}: {question.text}")

            answer = input("Your answer: ").strip().lower()

            self.attempted += 1

            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print(
                    f"Wrong! Correct answer: "
                    f"{question.answer}"
                )

        self.show_result()

    def calculate_score(self):
        """Return the score as a percentage."""

        if self.attempted == 0:
            return 0

        return self.score / self.attempted * 100

    def show_result(self):
        """Display the final result."""

        percentage = self.calculate_score()

        print("\nThank you for playing!")
        print(f"You attempted {self.attempted} questions.")
        print(f"Correct answers: {self.score}")
        print(f"Marks obtained: {percentage:.2f}%")
        print("BYE!")


def main():
    """Run the application."""

    game = QuizGame()
    game.start()


if __name__ == "__main__":
    main()
