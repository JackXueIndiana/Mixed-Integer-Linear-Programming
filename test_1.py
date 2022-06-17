from mip import Model, xsum, maximize, BINARY

# profit
p = [10, 13, 18, 31, 7, 15]

# weight
w = [11, 15, 20, 35, 10, 33]

# knapsack capacity
c = 47

# index
I = range(len(w))
print("I: {}".format(I))

# empty model
m = Model("knapsack")
print("Emptymodel m:: {}".format(m))

# set up x
x = [m.add_var(var_type=BINARY) for i in I]
print("x: {}".format(x))

# set up model objective func
m.objective = maximize(xsum(p[i] * x[i] for i in I))

# set up constrains
m += xsum(w[i] * x[i] for i in I) <= c
print("Fully formulated m:: {}".format(m))

# solve the problem
m.optimize()

# get the solution
selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))

for i in I:
    print("selected item value: {}: {}".format(i, x[i].x))

print("Objective value: {}".format(m.objective_value))