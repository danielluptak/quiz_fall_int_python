import random


class Question:
    def __init__(self):
        self.question = ''
        self.answer = ''
        self.wrong_answers = []
        self.category = ''
        self.difficulty = ''
        self.rpos = 0

    def display(self):
        print("Q: " + self.question)
        random.shuffle(self.wrong_answers)
        self.rpos = random.randint(0, 3)
        answers = self.wrong_answers.copy()
        answers.insert(self.rpos, self.answer)
        # print(self.rpos, answers)
        for i in range(0, 4):
            print(str(i+1) + ". " + answers[i])
        print("Choose: ")

    def check_answer(self, ans_no):
        if ans_no == self.rpos+1:
            return True
        else:
            return False