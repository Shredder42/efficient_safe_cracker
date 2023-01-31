import time
from random import randint, randrange, choice

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
    unlocked_wheels = [i for i in range(len(combo))]
    locked_wheels = []
    solved_wheel = ['-' for i in range(len(combo))]

    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]

        # mutate
        lock_wheel = randrange(0, len(combo))
        if lock_wheel not in locked_wheels:
            next_try[lock_wheel] = randint(0, 9)

            # grade & select
            next_try_grade = fitness(combo, next_try)
            if next_try_grade > best_attempt_grade:
                best_attempt = next_try
                best_attempt_grade = next_try_grade
                solved_wheel[lock_wheel] = next_try[lock_wheel]
                locked_wheels.append(lock_wheel)
                print(solved_wheel)
                print(locked_wheels)
            count += 1


    print('Cracked! {}'.format(best_attempt), end=' ')
    print('in {} tries'.format(count))

    return best_attempt

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print('\nRuntime for this program was {:.5f} seconds'.format(duration))