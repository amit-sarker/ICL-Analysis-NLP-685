import random

from sklearn.metrics import f1_score


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
    return model_responses


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

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/btlm_responses_for_sentiment.txt'
predicted_labels_model_btlm_normal = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/btlm_responses_for_sentiment_cot.txt'
predicted_labels_model_btlm_cot = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/btlm_responses_for_sentiment_no_demos.txt'
predicted_labels_model_btlm_no_demos = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/btlm_responses_for_sentiment_random_label.txt'
predicted_labels_model_btlm_random = parse_file(file_path)

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/llama_responses_for_sentiment.txt'
predicted_labels_model_llama_normal = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/llama_responses_for_sentiment_cot.txt'
predicted_labels_model_llama_cot = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/llama_responses_for_sentiment_no_demos.txt'
predicted_labels_model_llama_no_demos = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/llama_responses_for_sentiment_random_label.txt'
predicted_labels_model_llama_random = parse_file(file_path)

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_2.8b_responses_for_sentiment.txt'
predicted_labels_model_mamba_28_normal = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_2.8b_responses_for_sentiment_cot.txt'
predicted_labels_model_mamba_28_cot = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_2.8b_responses_for_sentiment_no_demos.txt'
predicted_labels_model_mamba_28_no_demos = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_2.8b_responses_for_sentiment_random_label.txt'
predicted_labels_model_mamba_28_random = parse_file(file_path)

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_7b_responses_for_sentiment.txt'
predicted_labels_model_mamba_7b_normal = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_7b_responses_for_sentiment_cot.txt'
predicted_labels_model_mamba_7b_cot = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_7b_responses_for_sentiment_no_demos.txt'
predicted_labels_model_mamba_7b_no_demos = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mamba_7b_responses_for_sentiment_random_label.txt'
predicted_labels_model_mamba_7b_random = parse_file(file_path)

file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mistral_responses_for_sentiment.txt'
predicted_labels_model_mistral_normal = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mistral_responses_for_sentiment_cot.txt'
predicted_labels_model_mistral_cot = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mistral_responses_for_sentiment_no_demos.txt'
predicted_labels_model_mistral_no_demos = parse_file(file_path)
file_path = '/home/amit/Desktop/Spring 24/NLP/Final project/Response/Sentiment/mistral_responses_for_sentiment_random_label.txt'
predicted_labels_model_mistral_random = parse_file(file_path)


macro_f1_btlm_normal = f1_score(true_labels, predicted_labels_model_btlm_normal, average='macro')
macro_f1_btlm_cot = f1_score(true_labels, predicted_labels_model_btlm_cot, average='macro')
macro_f1_btlm_no_demos = f1_score(true_labels, predicted_labels_model_btlm_no_demos, average='macro')
macro_f1_btlm_random = f1_score(true_labels, predicted_labels_model_btlm_random, average='macro')

macro_f1_llama_normal = f1_score(true_labels, predicted_labels_model_llama_normal, average='macro')
macro_f1_llama_cot = f1_score(true_labels, predicted_labels_model_llama_cot, average='macro')
macro_f1_llama_no_demos = f1_score(true_labels, predicted_labels_model_llama_no_demos, average='macro')
macro_f1_llama_random = f1_score(true_labels, predicted_labels_model_llama_random, average='macro')

macro_f1_mamba_28_normal = f1_score(true_labels, predicted_labels_model_mamba_28_normal, average='macro')
macro_f1_mamba_28_cot = f1_score(true_labels, predicted_labels_model_mamba_28_cot, average='macro')
macro_f1_mamba_28_no_demos = f1_score(true_labels, predicted_labels_model_mamba_28_no_demos, average='macro')
macro_f1_mamba_28_random = f1_score(true_labels, predicted_labels_model_mamba_28_random, average='macro')

macro_f1_mamba_7b_normal = f1_score(true_labels, predicted_labels_model_mamba_7b_normal, average='macro')
macro_f1_mamba_7b_cot = f1_score(true_labels, predicted_labels_model_mamba_7b_cot, average='macro')
macro_f1_mamba_7b_no_demos = f1_score(true_labels, predicted_labels_model_mamba_7b_no_demos, average='macro')
macro_f1_mamba_7b_random = f1_score(true_labels, predicted_labels_model_mamba_7b_random, average='macro')

macro_f1_mistral_normal = f1_score(true_labels, predicted_labels_model_mistral_normal, average='macro')
macro_f1_mistral_cot = f1_score(true_labels, predicted_labels_model_mistral_cot, average='macro')
macro_f1_mistral_no_demos = f1_score(true_labels, predicted_labels_model_mistral_no_demos, average='macro')
macro_f1_mistral_random = f1_score(true_labels, predicted_labels_model_mistral_random, average='macro')

btlm = [round(macro_f1_btlm_normal * 100, 2), round(macro_f1_btlm_cot * 100, 2), round(macro_f1_btlm_no_demos * 100, 2), round(macro_f1_btlm_random * 100, 2)]
llama = [round(macro_f1_llama_normal * 100, 2), round(macro_f1_llama_cot * 100, 2), round(macro_f1_llama_no_demos * 100, 2), round(macro_f1_llama_random * 100, 2)]
mamba_28 = [round(macro_f1_mamba_28_normal * 100, 2), round(macro_f1_mamba_28_cot * 100, 2), round(macro_f1_mamba_28_no_demos * 100, 2), round(macro_f1_mamba_28_random * 100, 2)]
mamba_7b = [round(macro_f1_mamba_7b_normal * 100, 2), round(macro_f1_mamba_7b_cot * 100, 2), round(macro_f1_mamba_7b_no_demos * 100, 2), round(macro_f1_mamba_7b_random * 100, 2)]
mistral = [round(macro_f1_mistral_normal * 100, 2), round(macro_f1_mistral_cot * 100, 2), round(macro_f1_mistral_no_demos * 100, 2), round(macro_f1_mistral_random * 100, 2)]

print("btlm =", btlm)
print("llama =", llama)
print("mamba_28 =", mamba_28)
print("mamba_7b =", mamba_7b)
print("mistral =", mistral)

print(f'Macro-F1 Score for btlm normal: {round(macro_f1_btlm_normal * 100, 2)}%')
print(f'Macro-F1 Score for btlm cot: {macro_f1_btlm_cot * 100:.2f}%')
print(f'Macro-F1 Score for btlm no demos: {macro_f1_btlm_no_demos * 100:.2f}%')
print(f'Macro-F1 Score for btlm random: {macro_f1_btlm_random * 100:.2f}%')

print(f'Macro-F1 Score for llama normal: {round(macro_f1_llama_normal * 100, 2)}%')
print(f'Macro-F1 Score for llama cot: {macro_f1_llama_cot * 100:.2f}%')
print(f'Macro-F1 Score for llama no demos: {macro_f1_llama_no_demos * 100:.2f}%')
print(f'Macro-F1 Score for llama random: {macro_f1_llama_random * 100:.2f}%')

print(f'Macro-F1 Score for mamba_28 normal: {round(macro_f1_mamba_28_normal * 100, 2)}%')
print(f'Macro-F1 Score for mamba_28 cot: {macro_f1_mamba_28_cot * 100:.2f}%')
print(f'Macro-F1 Score for mamba_28 no demos: {macro_f1_mamba_28_no_demos * 100:.2f}%')
print(f'Macro-F1 Score for mamba_28 random: {macro_f1_mamba_28_random * 100:.2f}%')

print(f'Macro-F1 Score for mamba_7b normal: {round(macro_f1_mamba_7b_normal * 100, 2)}%')
print(f'Macro-F1 Score for mamba_7b cot: {macro_f1_mamba_7b_cot * 100:.2f}%')
print(f'Macro-F1 Score for mamba_7b no demos: {macro_f1_mamba_7b_no_demos * 100:.2f}%')
print(f'Macro-F1 Score for mamba_7b random: {macro_f1_mamba_7b_random * 100:.2f}%')

print(f'Macro-F1 Score for mistral normal: {round(macro_f1_mistral_normal * 100, 2)}%')
print(f'Macro-F1 Score for mistral cot: {macro_f1_mistral_cot * 100:.2f}%')
print(f'Macro-F1 Score for mistral no demos: {macro_f1_mistral_no_demos * 100:.2f}%')
print(f'Macro-F1 Score for mistral random: {macro_f1_mistral_random * 100:.2f}%')