# Quiz on Ancient History

# Module for randomness
import random
# Module for minor spelling mistakes
import difflib

# Function to allow for minor spelling mistakes
def close_enough(user_answer, correct_answer):
    # Normalize the answers by converting to lower case and stripping spaces
    user_answer = user_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()

    # Use difflib to check for close matches, allowing for minor spelling mistakes
    return difflib.SequenceMatcher(None, user_answer, correct_answer).ratio() > 0.8

# Quiz function
def quiz():
    # Dictionary of questions and answers
    questions = {
        "Who was the first emperor of Rome?": "Augustus",
        "In which year did the ancient Olympic Games start?": "776 BC",
        "Who built the Great Wall of China?": "Qin Shi Huang",
        "What is the name of the ancient Egyptian writing system?": "Hieroglyphics",
        "Which ancient civilization built the Machu Picchu?": "Inca",
        "Who was the king of Macedonia who created a vast empire in the 4th century BC?": "Alexander the Great",
        "Which Greek philosopher taught Alexander the Great?": "Aristotle",
        "What is the name of the battle in which 300 Spartans fought against a much larger Persian army?": "Battle of Thermopylae",
        "What ancient city was buried under volcanic ash in 79 AD?": "Pompeii",
        "Who was the ruler of the Byzantine Empire during the construction of the Hagia Sophia?": "Justinian I"
    }

    # Randomly select 5 questions
    selected_questions = random.sample(list(questions.items()), 5)

    # Initialize score
    score = 0

    # Ask questions
    for question, answer in selected_questions:
        print(question)
        user_answer = input("Your answer: ")

        if close_enough(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
        print()

    # Print the final score
    print(f"Your final score is: {score}/5")

# Run it
if __name__ == "__main__":
    quiz()
