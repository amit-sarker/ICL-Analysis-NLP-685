This project explores the In-context learning (ICL) capabilities of pre-trained language models on arithmetic tasks and sentiment analysis using synthetic datasets. The goal is to use different prompting strategies—zero-shot, few-shot, and chain-of-thought—to assess the performance of these models on the given tasks. We conducted two types of arithmetic tasks:

Regular Arithmetic: Involves basic arithmetic operations like addition, subtraction, multiplication, and division (using integer division).

Jumbled Arithmetic: Involves standard arithmetic operations but with new symbols introduced for each operation:

(1) "$" represents addition, so a $ b equals a + b.

(2) "\#" represents subtraction, so a # b equals a - b.

(3) "@" represents the operation (a + b) * (a - b), so a @ b equals this calculation.

Introducing jumbled arithmetic aims to determine if the model is learning from the prompts or merely recalling from its pre-trained knowledge.

For sentiment analysis, the task is to classify a given text's sentiment (Positive, Negative, or Neutral).
