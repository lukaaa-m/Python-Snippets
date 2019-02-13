def ask(question, expected_answers):
    validAnswer = False
    answer = " " + (input(question)).lower() + " "
    for i in range(len(expected_answers)):
        if (" " + expected_answers[i].lower() + " ") in answer:
                validAnswer = True
    if not validAnswer:
            ask(question, expected_answers)

