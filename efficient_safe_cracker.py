import time
from random import randint, randrange

def fitness(combo, attempt):
    '''Compare items in two lists and count the number of matches.'''
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def main():
    '''Use hill climbing method to solve lock combination.'''
    combination = '6822858902'
    # Convert combination to list
    combo = [int(i) for i in combination]

    # generate guess and grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]

        # mutate
        lockwheel = randrange(0, len(combo))
        next_try[lockwheel] = randint(0, 9)

        # grade & select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try
            best_attempt_grade = next_try_grade

        count += 1
        print(best_attempt, next_try)

    print('Cracked! {}'.format(best_attempt), end=' ')
    print('in {} tries'.format(count))

    return best_attempt

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print('\nRuntime for this program was {:.5f} seconds'.format(duration))