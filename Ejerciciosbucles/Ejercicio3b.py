import random

question = input('Question:    ')

random_number = random.randint(1,9)

if random_number == 1:
    print('Answer:    Yes - Definitely')
elif random_number == 2:
    print('Answer:    It is decidedly so')
elif random_number == 3:
    print('Answer:    Without a doubt')
elif random_number == 4:
    print('Answer:    Ask again later')
elif random_number == 5:
    print('Answer:    Better not tell you now')
elif random_number == 6:
    print('Answer: My source say no')
elif random_number == 7:
    print('Answer: Outlook not so good')
else:
    print('Answer: Very doubtful')
