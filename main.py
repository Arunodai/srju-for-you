from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

print("Hey well i just try this code, \n i hope you like it")

print("\n")

sruju = input("can i ask you something but please dont angey. If its 'yes' then type y or  : ").lower()
if sruju == "y":
    print("\n")
    print("I dont know how you feeling about me. i did mistake that big one but i want you in my life .\n if you still cant get it over its ok i will wait")
else:
    print("I dont know how you feeling about me. i did mistake that big one but i want you in my life .\n if you still cant get it over its ok i will wait")

print("\n")

hey = input("one more thing enter somthing: ")
if hey == "":
    print("\n")
    print("sometimes i thing like you act like my mom, sometimes you like good frined, You are really cool, i think im gonna cry lol ")
else:
    print("sometimes i thing like you act like my mom, sometimes you like good frined, You are really cool, i think im gonna cry lol")

print("\n")

print("call me after seeing this")
