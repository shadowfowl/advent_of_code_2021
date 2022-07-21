# Make a measurement with the inputs. 
#Count the number of times a number increases.

#1- Read the inputs and save as a table. 2- create increase var. 3- compare item n and n+1, if n+1 > than n, increase = increase + 1

data = []
increases = 0

with open('./Input_Day1.txt', 'r') as inputs:
    while inputs:
        line = inputs.readline()
        if line == "":
            break
        
        else:
            data.append(int(line))

lenght = len(data)
for n in range(lenght):
    if (data[n] > data[n-1] ):
        increases += 1

print(increases)
