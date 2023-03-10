import time
from random import randint, randrange
import statistics
import matplotlib.pyplot as plt


def fitness(combo, attempt):
    '''Compare items in two lists and count the number of matches.'''
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def original_safe_cracker(lock_combo):
    # generate guess & grade fitness
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]

        # mutate
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)

        # grade & select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        count += 1

    return best_attempt, count

def efficient_safe_cracker(lock_combo):
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
            elif next_try_grade < best_attempt_grade: # checks if changed wheel FROM correct digit
                solved_wheel[lock_wheel] = best_attempt[lock_wheel]
                locked_wheels.append(lock_wheel)
            count += 1

    return best_attempt, count

def collect_data():

    original_start_time = time.time()
    original_attempt = original_safe_cracker(combo)[1]
    original_end_time = time.time()
    original_duration = original_end_time - original_start_time

    original_durations.append(original_duration)
    original_attempts.append(original_attempt)

    efficient_start_time = time.time()
    efficient_attempt = efficient_safe_cracker(combo)[1]
    efficient_end_time = time.time()
    efficient_duration = efficient_end_time - efficient_start_time

    efficient_durations.append(efficient_duration)
    efficient_attempts.append(efficient_attempt)

if __name__ == '__main__':
    '''Use hill climbing method to solve lock combination.'''
    # Generate random combination
    combination = ''
    for i in range(10):
        combination += str(randint(0,9))
    # Convert combination to list
    combo = [int(i) for i in combination]

    original_durations = []
    original_attempts = []
    efficient_durations = []
    efficient_attempts = []
    for i in range(100):
        collect_data()

    avg_original_attempts = statistics.mean(original_attempts)
    avg_original_duration = statistics.mean(original_durations)
    avg_efficient_attempts = statistics.mean(efficient_attempts)
    avg_efficient_duration = statistics.mean(efficient_durations)

    print('\nAverage program runtime for original safe cracker = {:.5f} seconds'.format(avg_original_duration))
    print('Average attempts for original safe cracker = {}'.format(int(avg_original_attempts)))
    print('\nAverage program runtime for efficient safe cracker = {:.5f} seconds'.format(avg_efficient_duration))
    print('Average attempts for efficient save cracker = {}'.format(int(avg_efficient_attempts)))

    x_list = [i for i in range(1, 101)]

    fig, ax = plt.subplots()
    ax.plot(x_list, original_attempts, label='Orignal')
    ax.plot(x_list, efficient_attempts, label='New')
    ax.set_xlabel('Program run number')
    ax.set_ylabel('Number of attempts to crack safe')
    ax.set_title('Attempts to crack safe vs. Program run')
    ax.set_ylim(0, 800)
    ax.legend()
    plt.savefig('imgs/attempts_vs_program_run.png', format='png')
    plt.show()







