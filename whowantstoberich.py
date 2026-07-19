import random

quiz_questions = [
    {
        "question": "In the UK, what is the traditional gift for a 25th wedding anniversary?",
        "options": ["A) Gold", "B) Silver", "C) Diamond", "D) Ruby"],
        "correct_answer": "B"
    },
    {
        "question": "Which of these is the chemical symbol for the element Gold?",
        "options": ["A) Gd", "B) Go", "C) Ag", "D) Au"],
        "correct_answer": "D"
    },
    {
        "question": "Which planet in our solar system is known for its prominent ring system?",
        "options": ["A) Saturn", "B) Mars", "C) Neptune", "D) Mercury"],
        "correct_answer": "A"
    },
    {
        "question": "Who is credited with painting the famous 16th-century portrait 'Mona Lisa'?",
        "options": ["A) Michelangelo", "B) Raphael", "C) Leonardo da Vinci", "D) Vincent van Gogh"],
        "correct_answer": "C"
    },
    {
        "question": "Which country is the natural habitat of the marsupial known as the Koala?",
        "options": ["A) South Africa", "B) Australia", "C) Brazil", "D) India"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["A) Kyoto", "B) Osaka", "C) Seoul", "D) Tokyo"],
        "correct_answer": "D"
    },
    {
        "question": "How many bones are there in an adult human body?",
        "options": ["A) 156", "B) 206", "C) 256", "D) 306"],
        "correct_answer": "B"
    },
    {
        "question": "Which English author wrote the famous fantasy novel 'The Hobbit'?",
        "options": ["A) J.K. Rowling", "B) C.S. Lewis", "C) J.R.R. Tolkien", "D) George R.R. Martin"],
        "correct_answer": "C"
    },
    {
        "question": "What is the primary currency used in the United Kingdom?",
        "options": ["A) Euro", "B) Dollar", "C) Pound Sterling", "D) Franc"],
        "correct_answer": "C"
    },
    {
        "question": "Which of the following is the largest ocean on Planet Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "correct_answer": "D"
    },
    {
        "question": "In Greek mythology, who is considered the King of the Gods?",
        "options": ["A) Poseidon", "B) Zeus", "C) Apollo", "D) Hades"],
        "correct_answer": "B"
    },
    {
        "question": "Which historical figure was the first President of the United States?",
        "options": ["A) Thomas Jefferson", "B) Abraham Lincoln", "C) George Washington", "D) John Adams"],
        "correct_answer": "C"
    },
    {
        "question": "What pigment gives leaves and plants their characteristic green color?",
        "options": ["A) Carotene", "B) Chlorophyll", "C) Hemoglobin", "D) Melanin"],
        "correct_answer": "B"
    },
    {
        "question": "Which European city is widely known as the 'City of Canals'?",
        "options": ["A) Paris", "B) Venice", "C) Amsterdam", "D) Vienna"],
        "correct_answer": "B"
    },
    {
        "question": "What is the name of the longest river in the world?",
        "options": ["A) Amazon", "B) Yangtze", "C) Mississippi", "D) Nile"],
        "correct_answer": "D"
    },
    {
        "question": "Which playwright wrote the classic tragedy 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Oscar Wilde"],
        "correct_answer": "A"
    },
    {
        "question": "What is the hardest naturally occurring substance known on Earth?",
        "options": ["A) Quartz", "B) Diamond", "C) Titanium", "D) Granite"],
        "correct_answer": "B"
    },
    {
        "question": "Which monumental structure is located near Agra, India?",
        "options": ["A) Taj Mahal", "B) Colosseum", "C) Petra", "D) Machu Picchu"],
        "correct_answer": "A"
    },
    {
        "question": "What basic mathematical term describes the distance around a circle?",
        "options": ["A) Radius", "B) Diameter", "C) Area", "D) Circumference"],
        "correct_answer": "D"
    },
    {
        "question": "In what year did the historic Titanic passenger ship sink?",
        "options": ["A) 1905", "B) 1912", "C) 1920", "D) 1933"],
        "correct_answer": "B"
    }
]

money_levels = [
    100, 200, 300, 500, 1500, 3000, 5000, 9000, 15000, 25000, 30000, 50000, 75000, 100000
]

def run_game():

    print("Hello and welcome to... Who Wants to be a Millionare!")
    print("Answer 15 questions correctly and get 100k dollars!\n")


    random.shuffle(quiz_questions)
    game_questions = quiz_questions[:15]

    current_prize = 0

    for index, current_question in enumerate(game_questions):
        print(f"Question {index + 1} for ${money_levels[index]}:")
        print(current_question["question"])
        
        for option in current_question["options"]:
            print(option)
            
        player_choice = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if player_choice == current_question["correct_answer"]:
            current_prize = money_levels[index]
            print(f"\nCorrect! You have won ${current_prize:,}.\n")
        else:
            print(f"\nWrong answer! The correct choice was {current_question['correct_answer']}.")
            print("Game Over!")
            break
    else:
        print("CONGRATULATIONS! You answered all questions correctly!")
        print(f"You are officially a millionaire: ${current_prize:,}!")

# Start the game loop
if __name__ == "__main__":
    run_game()