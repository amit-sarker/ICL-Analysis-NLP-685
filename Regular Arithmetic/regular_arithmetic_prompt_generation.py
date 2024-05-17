import random

def generate_arithmetic_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operators = ['+', '-', '*', '//']
    operator = random.choice(operators)

    if operator == '//':
        num1 = num1 * num2

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '//':
        answer = num1 // num2

    question = f"Calculate {num1} {operator.replace('//', '/')} {num2}. The answer is {answer}."
    return question

def create_full_prompt():
    problems = [generate_arithmetic_problem() for _ in range(3)]
    prompt_problems = "\n".join(f"{i+1}. {p}" for i, p in enumerate(problems[:-1]))
    final_problem = problems[-1].split('. The answer')[0] + "?"

    full_prompt = f"""{prompt_problems}
---
Calculate the next problem and provide the answer:
{final_problem} The correct answer is:
"""
    return full_prompt

with open("regular_arithmetic_prompts_2_demos.txt", "w", encoding="utf-8") as file:
    for i in range(100):
        prompt = create_full_prompt()
        file.write(f"{prompt}\n\n")

print("All prompts have been successfully generated and saved to generated_arithmetic_prompts.txt.")
