import random


def parse_file(file_path):
    questions = []
    model_responses = []
    r_flag = False
    q_flag = False
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if "------------------------------------------" in line:
                r_flag = False
                q_flag = False
                continue
            if line.startswith("Classify the sentiment of the following statement:"):
                continue
            if line.startswith("Statement:"):
                if q_flag:
                    continue
                question = line
                questions.append(question)
                q_flag = True
            if "Model's response for question" in line:
                if r_flag:
                    continue
                model_response = line.split("Sentiment:")[1].strip().strip('.')
                if model_response == 'Positive' or model_response == 'Negative' or model_response == 'Neutral':
                    model_responses.append(model_response)
                else:
                    model_responses.append(random.choice(['Positive', 'Negative', 'Neutral']))
                r_flag = True
    return questions, model_responses


new_statements = [
    ("The sunset over the ocean was breathtaking.", "Positive"),
    ("The coffee machine broke down again.", "Negative"),
    ("Our meeting is scheduled for tomorrow.", "Neutral"),
    ("I am so proud of my team's hard work.", "Positive"),
    ("The traffic was horrendous this morning.", "Negative"),
    ("The instructions are clear and easy to follow.", "Positive"),
    ("My computer crashed and I lost all my work.", "Negative"),
    ("The train arrives at 8 PM.", "Neutral"),
    ("I can't wait to see the new exhibit at the gallery!", "Positive"),
    ("I didn't like the movie at all.", "Negative"),
    ("The website is easy to navigate.", "Positive"),
    ("The weather forecast is for rain all weekend.", "Negative"),
    ("Our team meeting is on Wednesday.", "Neutral"),
    ("She gave a brilliant presentation.", "Positive"),
    ("The restaurant was closed when we arrived.", "Negative"),
    ("The museum is open daily from 10 AM to 6 PM.", "Neutral"),
    ("I had a wonderful time at the concert.", "Positive"),
    ("My flight was delayed for several hours.", "Negative"),
    ("The library has a great selection of books.", "Positive"),
    ("The software update caused more problems than it solved.", "Negative"),
    ("The bus leaves every 30 minutes.", "Neutral"),
    ("I received a compliment on my work today.", "Positive"),
    ("The road was closed due to an accident.", "Negative"),
    ("The store opens at 9 AM on weekdays.", "Neutral"),
    ("I love spending time with my family.", "Positive"),
    ("The customer service was terrible.", "Negative"),
    ("The package arrived on time.", "Neutral"),
    ("The new park is a beautiful addition to the neighborhood.", "Positive"),
    ("The project is behind schedule.", "Negative"),
    ("The class starts at 10 AM.", "Neutral"),
    ("The holiday decorations are stunning.", "Positive"),
    ("I forgot my umbrella and got soaked.", "Negative"),
    ("The concert will be held on Saturday.", "Neutral"),
    ("I'm very happy with my new job.", "Positive"),
    ("The food was undercooked and tasteless.", "Negative"),
    ("The train station is just a few blocks away.", "Neutral"),
    ("I had a great workout this morning.", "Positive"),
    ("The noise from the construction site is unbearable.", "Negative"),
    ("The deadline for the project is next Monday.", "Neutral"),
    ("I am so grateful for your help.", "Positive"),
    ("The product broke after just one use.", "Negative"),
    ("The event will start at 7 PM.", "Neutral"),
    ("The kids had a blast at the amusement park.", "Positive"),
    ("The laundry machine stopped working midway.", "Negative"),
    ("The office is located on the third floor.", "Neutral"),
    ("I am impressed by your dedication.", "Positive"),
    ("The wifi signal is weak in my room.", "Negative"),
    ("The grocery store is open 24 hours.", "Neutral"),
    ("I had an amazing time on vacation.", "Positive"),
    ("The battery of my phone drains too quickly.", "Negative")
]
true_labels = []
for i in range(50):
    true_labels.append(new_statements[i][1])

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mistral_responses_for_sentiment_random_label.txt'
questions, model_responses = parse_file(file_path)
f = open("Mistral-7b/mistral_errors_random.txt", "w")

for i in range(50):
    if model_responses[i] != true_labels[i]:
        print(f"Question {i + 1}: {questions[i]}")
        f.write(f"Question {i + 1}: {questions[i]}\n")
        print(f"Correct Answer: {true_labels[i]}")
        f.write(f"Correct Answer: {true_labels[i]}\n")
        print(f"Model's Response: {model_responses[i]}")
        f.write(f"Model's Response: {model_responses[i]}\n")
        print("-" * 40)
        f.write("-" * 40)
        f.write("\n")
f.close()