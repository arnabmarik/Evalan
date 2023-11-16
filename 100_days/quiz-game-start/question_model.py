
from data import question_data
from quiz_brain import QuizBrain
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer




question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer  = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


print(question_bank[1].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score is {quiz.score}/{len(quiz.question_list)}")







