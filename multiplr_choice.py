questions = [
    "1. what is the full form of ML ?",
    "2. what is the full form of AI ?",
    "3. what is the full form of LLM ?",
    "4.what is the full form of DL ?"

]

answers = [
    "1. Machine Learning 2. Machine learner 3. Machanism Learny 4. Mechanism Learner",
    "1. Artificial Learner 2. Ardinal Learner 3. Artifact Learning 4. ARtificial Intteligence",
    "1.large langchain Learner 2. Large Langauge Module 3.Large Language Model 4.Large Engine",
    "1.Deep Nueral Network 2. Deep Learning 3. Deep Learner 4. Deep lauch"
    ]


correct_input = [1,4,3,2]
correct_answer = ['machine learning' , 'Artificial intteligence' , 'Large Language Model ', 'Deep Learning']

def display_question(questions, correct_answer):
    user_input = []
    for question in questions:
        print(question)
        user = int(input("Enter the answer: "))
        user_input.append(correct_answer[user-1])
    return user_input


def compare_and_result(questions , correct_input , correct_answer):
    score = 0
    user_input = display_question(questions , correct_answer)
    for i in range(len(correct_input)):
        if correct_answer[i].lower() == user_input[i].lower():
            score += 10
    percentage = (score *100)/(len(correct_input)*10)

    for i in range(len(correct_input)):
        print(f"Qeustion : {i+1} : {questions[i]} ")
        print(f"correct Answer : {correct_answer[i]} User Answer :{user_input[i]}")

    print(f"Correctly Answered {score/10} out of {len(correct_input)}")
    print(f"Percentage Score : {percentage}")

compare_and_result(questions , correct_input , correct_answer)





