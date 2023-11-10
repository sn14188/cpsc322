import random
import numpy as np

generation_num = 1
init_pop = {
    'p0_1': [1, 1, 1, 1, 1, 1, 1, 1],
    'p0_2': [2, 2, 2, 2, 2, 2, 2, 2],
    'p0_3': [3, 3, 3, 3, 3, 3, 3, 3],
    'p0_4': [4, 4, 4, 4, 4, 4, 4, 4],
    'p0_5': [1, 2, 3, 4, 1, 2, 3, 4],
    'p0_6': [4, 3, 2, 1, 4, 3, 2, 1],
    'p0_7': [1, 2, 1, 2, 1, 2, 1, 2],
    'p0_8': [3, 4, 3, 4, 3, 4, 3, 4]
}

def fitness_cal(state):
    a, b, c, d, e, f, g, h = state
    constraints = [
        a > g,
        a <= h,
        abs(f - b) == 1,
        g < h,
        abs(g - c) == 1,
        abs(h - c) % 2 == 0,
        h != d,
        d >= g,
        d != c,
        e != c,
        e < d - 1,
        e != h - 2,
        g != f,
        h != f,
        c != f,
        d != f - 1,
        abs(e - f) % 2 == 1
    ]
    return sum(constraints)

def likelihood_cal(generation):
    fitness_scores = [fitness_cal(value) for value in generation.values()]
    sum_fitness = sum(fitness_scores)
    likelihood_array = [fitness_score / sum_fitness for fitness_score in fitness_scores]

    print('')
    print(f'Fitness scores: {fitness_scores}')
    print(f'Likelihoods: {[round(likelihood, 4) for likelihood in likelihood_array]}')

    return likelihood_array

def mutate(generation):
    mutate_status = [random.choices([0, 1], weights=[0.7, 0.3])[0] for _ in range(8)]
    print(f'Mutate_status: {mutate_status}')

    for key, state_mutated in zip(generation.keys(), mutate_status):
        if state_mutated == 1:
            selected_index = random.randint(0, len(generation.keys()) - 1)

            mutated_val = random.randint(1, 4)
            while generation[key][selected_index] == mutated_val:
                mutated_val = random.randint(1, 4)

            print(f'Mutation effect in \'{key}\'')
            print(f'    {generation[key]}')
            generation[key][selected_index] = mutated_val
            print(f' -> {generation[key]}')

    return generation

def generate_new_generation(curr_gen, counter):
    if counter == 0:
        return None
    new_generation = {}
    global generation_num
    key_counter = 1

    proba_array = likelihood_cal(curr_gen)
    selected_pairs = []

    while len(new_generation.keys()) < len(curr_gen.keys()):
        selected_pair = np.random.choice(list(curr_gen.keys()),
                                         size=2,
                                         replace=False,
                                         p=proba_array)
        rand_int = random.randint(1, 7)

        selected_pairs.append(selected_pair)
        print(f'Selected pair: {selected_pair}')
        print(f'Crossover point: {rand_int}')

        new_pair_first = (curr_gen[selected_pair[0]][:rand_int] + curr_gen[selected_pair[1]][rand_int:])
        new_pair_second = (curr_gen[selected_pair[1]][:rand_int] + curr_gen[selected_pair[0]][rand_int:])

        new_generation['p' + str(generation_num) + '_' + str(key_counter)] = new_pair_first
        new_generation['p' + str(generation_num) + '_' + str(key_counter + 1)] = new_pair_second
        print(f'Offsprings: ')
        print(f'    {new_pair_first}')
        print(f'    {new_pair_second}')

        key_counter += 2

    new_generation_mutated = mutate(new_generation)

    generation_num += 1

    print(f'New generation: ')
    for key in new_generation:
        print(f'    {key}: {new_generation[key]}')
    print('-' * 100)

    return generate_new_generation(new_generation_mutated, counter - 1)

iteration = 5
generate_new_generation(init_pop, iteration)
