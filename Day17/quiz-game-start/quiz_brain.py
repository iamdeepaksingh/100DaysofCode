class Quiz:
    def __init__(self, q_list):
        self.question_no = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        # total_questions = 12
        # score = 0
        # can_play = True
        # while can_play:
        current_question = self.q_list[self.question_no]
        self.question_no += 1
        choice = input(f'Q.{self.question_no}: {current_question.text} (True/False): ')
        self.check_answer(choice, current_question.answer)
            # if choice == current_question.answer:
            #     score += 1
            #     print(f"Your current score is {score}/{total_questions}")
            # else:
            #     print("Incorrect Answer! Game over !!! ")
            #     can_play = False

    def still_has_questions(self):
        return self.question_no < len(self.q_list)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"correct answer: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no}")
        print("\n")






