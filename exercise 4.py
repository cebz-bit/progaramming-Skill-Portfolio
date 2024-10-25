# Define the quiz questions and answers
quiz = {
    "What is the capital of France?": "Paris",
    }

# Loop through each question in the quiz
for question, correct_answer in quiz.items():
    # Asking the user the question
    user_answer = input(question + " ").strip()
    
    # Checking if the user's answer is correct (ignoring capitalization)
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")



