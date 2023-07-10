import random

def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Введите число: "))
        attempts += 1

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
            break

def main():
    play_game()

if __name__ == '__main__':
    main()
