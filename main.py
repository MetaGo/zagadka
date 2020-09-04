import random
# указывается диапазон загаданного числа
secret_number = random.randint(1,20)

print('Я загадал число от  1 до 20 попробуй угадать его. У тебя 5 попыток')

for guess_taken in range(1,6):
    # выше указывается количество попыток которыми можно воспользоваться
    print('Ваш вариант?  -  ')
    guess = int(input())

    if guess > secret_number:
        print('Ваше число больше задуманного')
    elif guess < secret_number:
        print('Ваше число меньше задуманного')
    else:
        break
if guess == secret_number:
    print('Супер!!! Ты угадал!!!\n' + 'Было задумано --- ' + str(secret_number) +
          '\n Количество попыток: ' + str(guess_taken))
else:
    print('Было загадано число ' + str(secret_number) + ' Ты не справился')


