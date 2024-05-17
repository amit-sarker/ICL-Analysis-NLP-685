import random


def calculate_modified_arithmetic(a, b, operation):
    if operation == '#':
        return a - b
    elif operation == '$':
        return a + b
    elif operation == '@':
        return a * b


def generate_prompt():
    operations = ['#', '$', '@']
    operation_explanations = {
        '#': "# is subtraction. a # b = a - b.",
        '$': "$ is addition. a $ b = a + b.",
        '@': "@ is multiplication. a @ b = a * b."
    }

    prompt = ""
    for i in range(3):
        a = random.randint(5, 100)
        b = random.randint(1, a)
        op = operations[i]
        result = calculate_modified_arithmetic(a, b, op)
        prompt += f"{i + 1}. Calculate {a} {op} {b}. The answer is {result}.\n"
        prompt += f"Reason: {operation_explanations[op]} So, {a} {op} {b} = {result}\n"

    a, b = random.randint(1, 100), random.randint(1, 100)
    op = random.choice(operations)
    prompt += "---\nCalculate the next problem and provide the answer:\n"
    prompt += f"Calculate {a} {op} {b}? The correct answer is:"

    return prompt

with open("cot_jumbled_arithmatic_v2.txt", "w", encoding="utf-8") as file:
    for i in range(50):
        prompt = generate_prompt()
        file.write(f"{prompt}\n\n\n")

