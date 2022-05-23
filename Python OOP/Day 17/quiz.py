class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            exit()

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Question.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        print(user_answer.lower(), correct_answer.lower())
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right Answer")
        else:
            print('Wrong Answer')
        print(f"Correct Answer is {correct_answer.lower()}")
        print(f"Correct Answer {self.score} Out of {self.question_number} Questions. \n")
