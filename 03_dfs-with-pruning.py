class Variable:
    def __init__(self, name):
        self.name = name
        self.domain = {1, 2, 3, 4}

variables = [Variable('A'), Variable('B'), Variable('C'), Variable('D'),
             Variable('E'), Variable('F'), Variable('G'), Variable('H')]

def constraint_ag(a, g):
    return a > g

def constraint_ah(a, h):
    return a <= h

def constraint_bf(b, f):
    return abs(f - b) == 1

def constraint_gh(g, h):
    return g < h

def constraint_cg(c, g):
    return abs(g - c) == 1

def constraint_ch(c, h):
    return abs(h - c) % 2 == 0

def constraint_dh(d, h):
    return h != d

def constraint_dg(d, g):
    return d >= g

def constraint_cd(c, d):
    return d != c

def constraint_ce(c, e):
    return e != c

def constraint_de(d, e):
    return e < d - 1

def constraint_eh(e, h):
    return e != h - 2

def constraint_fg(f, g):
    return g != f

def constraint_fh(f, h):
    return h != f

def constraint_cf(c, f):
    return c != f

def constraint_df(d, f):
    return d != f - 1

def constraint_ef(e, f):
    return abs(e - f) % 2 == 1

def level_4(assignment):
    global failures
    if constraint_cd(assignment[2], assignment[3]):
        return True
    else:
        # failures += 1
        return False


def level_5(assignment):
    global failures
    if (constraint_ce(assignment[2], assignment[4]) and
            constraint_de(assignment[3], assignment[4])):
        return True
    else:
        # failures += 1
        return False

def level_6(assignment):
    global failures
    if (constraint_bf(assignment[1], assignment[5]) and
            constraint_cf(assignment[2], assignment[5]) and
            constraint_df(assignment[3], assignment[5]) and
            constraint_ef(assignment[4], assignment[5])):
        return True
    else:
        # failures += 1
        return False

def level_7(assignment):
    global failures
    if (constraint_ag(assignment[0], assignment[6]) and
            constraint_cg(assignment[2], assignment[6]) and
            constraint_dg(assignment[3], assignment[6]) and
            constraint_fg(assignment[5], assignment[6])):
        return True
    else:
        # failures += 1
        return False

def level_8(assignment):
    global failures
    if (constraint_ah(assignment[0], assignment[7]) and
            constraint_ch(assignment[2], assignment[7]) and
            constraint_dh(assignment[3], assignment[7]) and
            constraint_eh(assignment[4], assignment[7]) and
            constraint_fh(assignment[5], assignment[7]) and
            constraint_gh(assignment[6], assignment[7])):
        return True
    else:
        failures += 1
        return False

# check constraints
def check_constraints(assignment):
    global failures
    assignment_length = len(assignment)
    if assignment_length <= 3:
        failures += 1
        return True
    elif assignment_length == 4:
        failures += 1
        return level_4(assignment)
    elif assignment_length == 5:
        failures += 1
        return level_5(assignment)
    elif assignment_length == 6:
        failures += 1
        return level_6(assignment)
    elif assignment_length == 7:
        failures += 1
        return level_7(assignment)
    elif assignment_length == 8:
        return level_8(assignment)

solutions = []
failures = 0

def print_tree_form(assignment):
    assignment_length = len(assignment)
    variable_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    formatted_assignments = ' '.join(
        f'{var}={value}' for var, value in zip(variable_names[:assignment_length], assignment))
    print(formatted_assignments)

def dfs_with_pruning(variables, assignment):
    global failures
    if len(assignment) == 8 and check_constraints(assignment):
        solutions.append(assignment)

    if len(assignment) < 8:
        curr_var = variables[len(assignment)]
        for val in curr_var.domain:
            new_assignment = assignment + [val]
            print_tree_form(new_assignment)
            if check_constraints(new_assignment):
                dfs_with_pruning(variables, new_assignment)

dfs_with_pruning(variables, [])

for i, solution in enumerate(solutions):
    print(f'Solution {i + 1}: {solution}')
print(f'Failures: {failures}')

print('')
exposure = 'ag ah fb gh gc hc hd dg dc ec ed eh gf hf cf df ef'
counter = {}
for char in exposure:
    if char == ' ':
        continue
    elif char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
print(counter)
sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(sorted_counter)
