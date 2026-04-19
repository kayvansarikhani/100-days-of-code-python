from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = [ Question(q1, a1),
#                   Question(q2, a2),
#                   Question(q3, a3)]

question_bank = []

# class Question:
#
#     def __init__(self, q_text, q_answer):
#
#         self.text = q_text
#         self.answer = q_answer

# new_q = Question("wtf", "False")
# print(new_q.text)
# new_q = Question("2 + 3 = 5", True)



for question in question_data:
# for Question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
    # question_bank.append(Question)

# print(question_bank[0].answer)
# print(question_bank[0].text, question_bank[0].answer)

quiz = QuizBrain(question_bank)
# quiz.next_question()

#quiz = QuizBrain(question_bank)
#
while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")