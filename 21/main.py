import copy
import itertools

foods = []
allergen_foods = []

for l in open("input.txt"):
    ingredients, allergens = l.strip().split(" (contains ")
    ingredients = ingredients.split(" ")
    allergens = allergens.replace(")", "").split(", ")
    foods.append((ingredients, allergens))


def eliminate(foods, lvl=""):
    if not any([a for i,a in foods]):
        return foods
    
    for f in foods:
        if not f[1]:
            continue

        for i,a in itertools.product(*f):
            if all([i in i2 for (i2,a2) in foods if a in a2]):
                # i,a possible comb
                f_copy = copy.deepcopy(foods)
                for fc in f_copy:
                    if i in fc[0]:
                        fc[0].remove(i)
                    if a in fc[1]:
                        fc[1].remove(a)

                elim_foods = eliminate(f_copy, lvl+" ")
                if elim_foods:
                    allergen_foods.append((i, a))
                    return elim_foods

        # no solution from here on, early exit
        return


def p1():
    eliminated_foods = eliminate(foods)
    assert any([a for i,a in eliminated_foods]) == False

    safe_ingredients = set()
    [safe_ingredients.update(i) for (i,a) in eliminated_foods]

    print(sum([1 for si in safe_ingredients for i,_ in foods if si in i]))

p1()

def p2():
    allergen_foods.sort(key=lambda x: x[1])
    print(",".join([i for i,_ in allergen_foods]))

p2()