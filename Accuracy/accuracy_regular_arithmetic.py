import re


def calculate_answer(question):
    question = question.split('?')[0].strip()
    match = re.search(r'(\d+)\s*([-+*/])\s*(\d+)', question)
    if not match:
        return None
    num1, operator, num2 = match.groups()
    num1, num2 = int(num1), int(num2)

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2
    else:
        return None


def extract_number(response):
    response = response.replace(',', '')
    numbers = re.findall(r'[-]?\d+', response)
    if numbers:
        return int(numbers[-1])
    return None


def parse_file(file_path):
    questions = []
    model_responses = []
    correct_answers = []
    results = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        q_flag = False
        a_flag = False
        r_flag = False
        for i, line in enumerate(lines):
            line = line.strip()
            if "------------------------------------------" in line:
                q_flag = False
                a_flag = False
                r_flag = False
                continue
            if line.startswith("Calculate the next problem and provide the answer:"):
                continue
            if line.startswith("Calculate"):
                if q_flag == True:
                    continue
                question = line
                questions.append(question)
                correct_answer = calculate_answer(question)
                correct_answers.append(correct_answer)
                q_flag = True
            if "Model's response for question" in line:
                model_response = line.split(":")[1].strip().strip('.')

                numeric_response = extract_number(model_response)
                model_responses.append(numeric_response)

                if correct_answer == numeric_response:
                    results.append(True)
                else:
                    results.append(False)
    return questions, correct_answers, model_responses, results


def calculate_accuracy(results):
    total_questions = len(results)
    correct_answers = sum(results)
    accuracy = (correct_answers / total_questions) * 100
    return accuracy


def main():
    file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Regular Arithmetic/mistral_responses_for_arithmatic_8.txt'
    questions, correct_answers, model_responses, results = parse_file(file_path)

    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        print(f"Correct Answer: {correct_answers[i]}")
        print(f"Model's Response: {model_responses[i]}")
        print(f"Correct: {results[i]}")
        print("-" * 40)

    accuracy = calculate_accuracy(results)
    print(f"Model Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    main()
