import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # список загаданных игроков букв, даже если они неправильные
    guessed_words = []  # список загаданных игроков слов, даже если они неправильные
    tries = 6

    print("Давайте сыграем в виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Попытайтесь угадать букву или слово целиком ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"\nВы уже загадывали букву {guess}")
            elif guess not in word:
                print(f"\nВ слове нет буквы {guess}")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"\nОтлично! В слове есть буква {guess}.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"\nВы уже загадывали слово {guess}.")
            elif guess != word:
                print("\nВы не угадали слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\nНеправильный ввод.")
        print(display_hangman(tries))
        print(word_completion + "\n")
    if guessed:
        print("Вы угадали слово. Поздравляем с победой!")
    else:
        print(f"К сожалению, ваши попытки закончились. "
              f"Было загадано слово {word}. Удачи в следующий раз!")


def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / 
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |      
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|
                 |      |
                 |     
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |     
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |    
                 |      
                 |     
                 -
              """,

              """
                 --------
                 |      |
                 |      
                 |    
                 |      
                 |     
                 -
              """]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Сыграем снова? Да/нет ").upper() == "ДА":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
