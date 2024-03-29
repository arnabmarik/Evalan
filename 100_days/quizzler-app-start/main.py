
# age: int
# # name: str
# # height: float
# # is_human: bool
# #
# # def police_check(age:int) -> str:
# #     if age > 18:
# #         can_drive = True
# #     else:
# #         can_drive = False
# #     return "can_drve"





from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain
from ui import  QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
