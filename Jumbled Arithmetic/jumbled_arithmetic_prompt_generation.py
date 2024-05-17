import random

def opposite_result(operation, a, b):
    if operation == '#':
        return a - b  # Normally would be a + b
    elif operation == '$':
        return a + b  # Normally would be a - b
    elif operation == '@':
        return (a + b) * (a - b)

def generate_prompt():
    operations = ['#', '$', '@']
    op = random.choice(operations)
    prompt = ""
    for i in range(2):
        num1 = random.randint(5, 100)
        num2 = random.randint(1, num1)
        result = opposite_result(op, num1, num2)
        prompt += f"{i+1}. Calculate {num1} {op} {num2}. The answer is {result}.\n"
    num1 = random.randint(5, 100)
    num2 = random.randint(1, num1)
    # op = random.choice(operations)
    prompt += "---\n"
    prompt += "Calculate the next problem and provide the answer:\n"
    prompt += f"Calculate {num1} {op} {num2}? The correct answer is:"
    return prompt


with open("jumbled_arithmetic_2.txt", "w", encoding="utf-8") as file:
    for i in range(50):
        prompt = generate_prompt()
        file.write(f"{prompt}\n\n")

# Example of one prompt

