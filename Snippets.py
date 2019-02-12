def ask(question, expected_answers):
    validAnswer = False
    answer = input(question)
    for i in range(len(expected_answers)):
        if expected_answers[i].lower() in answer.lower():
                validAnswer = True
    if not validAnswer:
            ask(question, expected_answers)

