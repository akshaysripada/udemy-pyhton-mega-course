def c_to_f(c):
    if c < -273.15:
        return "Temperature entered doesn't make sense!"
    else:
        return c * (9.0/5.0) + 32.0


temperatures = [10,-20,-289,100]

for i in temperatures:
    print(c_to_f(i))
