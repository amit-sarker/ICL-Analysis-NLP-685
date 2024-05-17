# Sample data for statements and their sentiments with reasons
statements_with_reasons = [
    ("The meal was delicious and the service was excellent.", "Positive", "The statement describes enjoyment and good service."),
    ("It rained all day during our outdoor event.", "Negative", "The statement describes an unfavorable situation."),
    ("She arrived at the meeting on time.", "Neutral", "The statement provides a factual detail without emotional context."),
    ("The flowers in the garden are blooming beautifully this spring.", "Positive", "The statement expresses pleasure in the blooming flowers."),
    ("My flight got canceled at the last minute.", "Negative", "The statement conveys frustration and inconvenience."),
    ("The conference starts at 9 AM.", "Neutral", "The statement states a fact about the schedule."),
    ("This new book release has me so excited!", "Positive", "The statement expresses excitement about the new book."),
    ("I was stuck in traffic for over two hours.", "Negative", "The statement conveys frustration and inconvenience."),
    ("The instructions are included in the box.", "Neutral", "The statement provides factual information about the instructions."),
    ("I won the lottery!", "Positive", "The statement expresses joy and excitement about winning."),
    ("The concert was far too loud and chaotic.", "Negative", "The statement describes discomfort and disorder."),
    ("His birthday is in July.", "Neutral", "The statement provides a fact about a date."),
    ("The team did an outstanding job on the project!", "Positive", "The statement praises the team's excellent work."),
    ("They forgot my order at the restaurant.", "Negative", "The statement conveys disappointment and inconvenience."),
    ("The office closes at 6 PM.", "Neutral", "The statement provides a factual detail about the office hours."),
    ("Watching the sunset calms my mind.", "Positive", "The statement expresses tranquility and relaxation."),
    ("I lost my keys and couldn't get into my house last night.", "Negative", "The statement describes a frustrating and inconvenient situation."),
    ("The store is open until midnight.", "Neutral", "The statement provides a fact about store hours."),
    ("What a wonderful performance it was!", "Positive", "The statement expresses admiration and enjoyment."),
    ("I am not happy with the current political situation.", "Negative", "The statement expresses dissatisfaction with the situation."),
    ("The cat is sitting on the mat.", "Neutral", "The statement provides a factual detail without emotional context."),
    ("They did a great job on that project, truly impressive!", "Positive", "The statement praises the excellent work done."),
    ("I hate waiting for late flights.", "Negative", "The statement conveys frustration with delays."),
    ("The report came out as expected.", "Neutral", "The statement provides factual information about the report."),
    ("Everyone at the party had a great time.", "Positive", "The statement describes enjoyment and fun."),
    ("I'm upset because my vacation plans fell through.", "Negative", "The statement expresses disappointment with the failed plans."),
    ("Today is the longest day of the year.", "Neutral", "The statement provides a factual detail about the day."),
    ("The surprise party was a huge success!", "Positive", "The statement expresses joy and satisfaction with the outcome."),
    ("My phone died right when I needed it most.", "Negative", "The statement describes a frustrating and inconvenient situation."),
    ("The library is closed for renovations.", "Neutral", "The statement provides factual information about the library's status."),
    ("I love how quiet it is in the countryside.", "Positive", "The statement expresses enjoyment of the tranquility."),
    ("The loud construction noise is unbearable.", "Negative", "The statement describes discomfort with the noise."),
    ("Parking is free on Sundays.", "Neutral", "The statement provides factual information about parking."),
    ("Your gift was thoughtful and well received.", "Positive", "The statement expresses appreciation and satisfaction."),
    ("My soup was cold; I had to send it back.", "Negative", "The statement conveys disappointment with the food."),
    ("Tomorrow's forecast calls for clear skies.", "Neutral", "The statement provides factual information about the weather."),
    ("I'm thrilled with the progress we've made.", "Positive", "The statement expresses excitement and satisfaction with the progress."),
    ("I received a parking ticket today.", "Negative", "The statement describes a frustrating and inconvenient situation."),
    ("The gym is now open 24/7.", "Neutral", "The statement provides factual information about the gym's hours."),
    ("The new movie was an absolute joy to watch.", "Positive", "The statement expresses great enjoyment of the movie."),
    ("I'm annoyed by how messy the kitchen is.", "Negative", "The statement describes frustration with the mess."),
    ("Interest rates will remain the same.", "Neutral", "The statement provides factual information about interest rates."),
    ("Our team won the championship!", "Positive", "The statement expresses excitement and pride in the team's achievement."),
    ("I can't stand the taste of this medicine.", "Negative", "The statement conveys strong dislike for the medicine."),
    ("There's a new exhibit at the museum.", "Neutral", "The statement provides factual information about the exhibit."),
    ("This is the best coffee I've ever had.", "Positive", "The statement expresses great satisfaction with the coffee."),
    ("The wifi is down again.", "Negative", "The statement describes frustration with the unreliable wifi."),
    ("It's a regular business day tomorrow.", "Neutral", "The statement provides factual information about the schedule."),
    ("Seeing old friends is always a pleasure.", "Positive", "The statement expresses joy and satisfaction in seeing friends."),
    ("My laptop crashed during an important presentation.", "Negative", "The statement describes a frustrating and inconvenient situation.")
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
# Generate 50 unique prompts with reasons
for i in range(50):
    idx1 = (i * 3) % len(statements_with_reasons)
    idx2 = (i * 3 + 1) % len(statements_with_reasons)
    idx3 = (i * 3 + 2) % len(statements_with_reasons)
    next_idx = (i * 3 + 3) % len(statements_with_reasons)

    file_content += f"\
1. Statement: {statements_with_reasons[idx1][0]} Sentiment: {statements_with_reasons[idx1][1]}.\nReason: {statements_with_reasons[idx1][2]}\n\
2. Statement: {statements_with_reasons[idx2][0]} Sentiment: {statements_with_reasons[idx2][1]}.\nReason: {statements_with_reasons[idx2][2]}\n\
3. Statement: {statements_with_reasons[idx3][0]} Sentiment: {statements_with_reasons[idx3][1]}.\nReason: {statements_with_reasons[idx3][2]}\n\
---\n\
Classify the sentiment of the following statement:\n\
Statement: {new_statements[i][0]} Sentiment:\n\n\n"



    # prompts.append(prompt)

# Save prompts to a text file
with open('sentiment_prompts_cot.txt', 'w', encoding="utf-8") as file:
    file.write(file_content)
