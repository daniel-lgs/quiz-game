from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data[0]["results"]:
    question_bank.append(Question(question["question"], question["correct_answer"]))

my_quiz = QuizBrain(question_bank)
my_quiz.start_quiz()

print("You've completed the quiz.")
print(f"Your final score was: {my_quiz.current_score}/{my_quiz.question_number}")
