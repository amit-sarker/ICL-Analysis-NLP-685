# Sample data for statements and their sentiments
statements = [
    ("The meal was delicious and the service was excellent.", "Positive"),
    ("It rained all day during our outdoor event.", "Negative"),
    ("She arrived at the meeting on time.", "Neutral"),
    ("The flowers in the garden are blooming beautifully this spring.", "Positive"),
    ("My flight got canceled at the last minute.", "Negative"),
    ("The conference starts at 9 AM.", "Neutral"),
    ("This new book release has me so excited!", "Positive"),
    ("I was stuck in traffic for over two hours.", "Negative"),
    ("The instructions are included in the box.", "Neutral"),
    ("I won the lottery!", "Positive"),
    ("The concert was far too loud and chaotic.", "Negative"),
    ("His birthday is in July.", "Neutral"),
    ("The team did an outstanding job on the project!", "Positive"),
    ("They forgot my order at the restaurant.", "Negative"),
    ("The office closes at 6 PM.", "Neutral"),
    ("Watching the sunset calms my mind.", "Positive"),
    ("I lost my keys and couldn't get into my house last night.", "Negative"),
    ("The store is open until midnight.", "Neutral"),
    ("What a wonderful performance it was!", "Positive"),
    ("I am not happy with the current political situation.", "Negative"),
    ("The cat is sitting on the mat.", "Neutral"),
    ("They did a great job on that project, truly impressive!", "Positive"),
    ("I hate waiting for late flights.", "Negative"),
    ("The report came out as expected.", "Neutral"),
    ("Everyone at the party had a great time.", "Positive"),
    ("I'm upset because my vacation plans fell through.", "Negative"),
    ("Today is the longest day of the year.", "Neutral"),
    ("The surprise party was a huge success!", "Positive"),
    ("My phone died right when I needed it most.", "Negative"),
    ("The library is closed for renovations.", "Neutral"),
    ("I love how quiet it is in the countryside.", "Positive"),
    ("The loud construction noise is unbearable.", "Negative"),
    ("Parking is free on Sundays.", "Neutral"),
    ("Your gift was thoughtful and well received.", "Positive"),
    ("My soup was cold; I had to send it back.", "Negative"),
    ("Tomorrow's forecast calls for clear skies.", "Neutral"),
    ("I'm thrilled with the progress we've made.", "Positive"),
    ("I received a parking ticket today.", "Negative"),
    ("The gym is now open 24/7.", "Neutral"),
    ("The new movie was an absolute joy to watch.", "Positive"),
    ("I'm annoyed by how messy the kitchen is.", "Negative"),
    ("Interest rates will remain the same.", "Neutral"),
    ("Our team won the championship!", "Positive"),
    ("I can't stand the taste of this medicine.", "Negative"),
    ("There's a new exhibit at the museum.", "Neutral"),
    ("This is the best coffee I've ever had.", "Positive"),
    ("The wifi is down again.", "Negative"),
    ("It's a regular business day tomorrow.", "Neutral"),
    ("Seeing old friends is always a pleasure.", "Positive"),
    ("My laptop crashed during an important presentation.", "Negative")
]

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

file_content = ""
import random

for i in range(50):
    # Select indices ensuring they cycle through the examples
    idx1 = (i * 3) % len(statements)
    idx2 = (i * 3 + 1) % len(statements)
    idx3 = (i * 3 + 2) % len(statements)
    next_idx = (i * 3 + 3) % len(statements)  # For the statement to classify

    sentiments = ['Positive', 'Negative', 'Neutral']

    file_content += f"\
1. Statement: {statements[idx1][0]} Sentiment: {random.choice(sentiments)}.\n\
2. Statement: {statements[idx2][0]} Sentiment: {random.choice(sentiments)}.\n\
3. Statement: {statements[idx3][0]} Sentiment: {random.choice(sentiments)}.\n\
---\n\
Classify the sentiment of the following statement:\n\
Statement: {new_statements[i][0]} Sentiment:\n\n\n"

# Save to a file
with open('sentiment_prompts_random_label.txt', 'w', encoding="utf-8") as file:
    file.write(file_content)

