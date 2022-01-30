import html
# using unescape method from html to parse the special characters like quotes, comma etc.

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        # total_questions = 12
        # score = 0
        # can_play = True
        # while can_play:
        self.current_question = self.q_list[self.question_no]
        self.question_no += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_no}: {q_text} (True/False): "

    def still_has_questions(self):
        return self.question_no < len(self.q_list)

    def check_answer(self, user_ans):
        correct_answer = self.current_question.answer
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            #print("Right")
            return True
        else:
            #print("Wrong")
            return False








