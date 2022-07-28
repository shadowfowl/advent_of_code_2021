# Power consumption = Gamma * Epsilon
# Gamma Rate = most common bit in the corresponding position, and the resultant binary is gamma
# Epsilon Rate = less common bit in position.

# because i'm using 1's and 0's i can made a sum of number in each position and if number > 500 (more than half) is the number most common, less common is the inverse.




binary = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

with open('./Input_Day3.txt', 'r') as inputs:
    while inputs:
        line = inputs.readline()
        if line == "":
            break
        else:
            for n in range(len(line)):
                if line[n] == '1':
                    binary[n] += 1

for n in range(len(binary)):
    if binary[n] > 500: #means that 1 appears more than 0
        gamma[n] = 1
        epsilon[n] = 0
    else:
        gamma[n] = 0
        epsilon[n] = 1

g_rate = int(''.join(map(str, gamma)), 2)
e_rate = int(''.join(map(str,epsilon)), 2)


print(g_rate*e_rate)
