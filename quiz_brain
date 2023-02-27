class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0

    def start_quiz(self):
        while self.question_number < len(self.question_list):
            question_text = self.question_list[self.question_number].text
            answer = input(f"Q.{self.question_number + 1}: {question_text} (True/False): ")
            if self.answer_is_correct(answer):
                self.current_score += 1
                print("You got it right!")
            else:
                print("That's wrong!")

            print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
            print(f"Your current score is: {self.current_score}/{self.question_number + 1}\n")

            self.question_number += 1

    def answer_is_correct(self, answer):
        if answer == self.question_list[self.question_number].answer:
            return True
        else:
            return False
