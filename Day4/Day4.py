# first line is draw numbers
# /n five numbers x five lines /n again to create the boards

# need to sum all unmarked numbers on the winning board and multiply by the number called when board won


with open ('./Input_Day4.txt','r') as inputs:
    data = inputs.readlines()

draw = data[0] #create draw
data[0] = '/0'
reference = 0


#separate grids
for n in range(len(data)):
    if data[n] != '/0':
        grid{reference} = []
        for x in range(5):
            grid{reference}.append(data[n])

            
print(grid[0])



#create function = draw a number
for n in range(len(data)):
    line = data[n]
    for m in range(len(line)):
        number = line[m]
        if number == draw[0]:
            number == 'X'
#create a function to check if any collum wins


