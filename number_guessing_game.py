
#Number guessing game only 5 attempts

import random
number = random.randint(1,50)
attempts = 5

while attempts > 0:
  try:
    guess_number = int(input('Guess the number: '))

    if number > guess_number:
      attempts -=1
      if attempts > 0:
        print(f'Enter higher number. You have {attempts} attempts left')

    elif number < guess_number:
      attempts -=1
      if attempts > 0:
        print(f'Enter lower number. You have {attempts} attempts left')

    else:
      print('Won!, You guessed it right')
      break

  except ValueError:
    print('Enter valid number')

  if attempts ==0:
    print(f"Sorry you've no attempts left, The correct number was {number}")
