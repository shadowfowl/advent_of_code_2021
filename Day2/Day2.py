#Forward X increases the horizontal position by X units.
#Down X increases the depth by X units.
#Up X decreases the depth by X units.

#After this, with the horizontal position and depht, multply these together to get the answer.


horizontal = 0
depth = 0

with open ('./Input_Day2.txt', 'r') as inputs:
    while(inputs):
        line = inputs.readline()
        if line == "" :
            break
        data = line.split(' ')
        if data[0] == "forward":
            horizontal = horizontal + int(data[1])
        elif data[0] == "down":
            depth = depth + int(data[1])
        else:
            depth = depth - int(data[1])



answer = depth * horizontal

print(answer)
