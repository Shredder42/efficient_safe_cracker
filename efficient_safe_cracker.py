import time
from random import randint, randrange

def fitness(combo, attempt):
    '''Compare items in two lists and count the number of matches.'''
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def show_digit_panel(solved_wheel):
    '''Simulates the digital panel solving the combo one number at a time.'''
    print(solved_wheel)

def main():
    '''Use hill climbing method to solve lock combination.'''
    combination = '6822858902'
    # Convert combination to list
    combo = [int(i) for i in combination]

    # generate guess and grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0
    locked_wheels = []
    solved_wheel = ['-' for i in range(len(combo))]

    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]

        # mutate
        lock_wheel = randrange(0, len(combo))
        if lock_wheel not in locked_wheels: # only go through attempt on unlocked wheels
            next_try[lock_wheel] = randint(0, 9)

            # grade & select
            next_try_grade = fitness(combo, next_try)
            if next_try_grade > best_attempt_grade: # checks if changed wheel TO correct digit
                best_attempt = next_try
                best_attempt_grade = next_try_grade
                solved_wheel[lock_wheel] = next_try[lock_wheel]
                locked_wheels.append(lock_wheel)
                show_digit_panel(solved_wheel)
            elif next_try_grade < best_attempt_grade: # checks if changed wheel FROM correct digit
                solved_wheel[lock_wheel] = best_attempt[lock_wheel]
                locked_wheels.append(lock_wheel)
                show_digit_panel(solved_wheel)
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