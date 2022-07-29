# life support rating = oxygen * CO2

#consider just first bit to bit criteria
#oxygen bit criteria: mostcommon, keep only numbers with this.


def most_common(array, bit):
    bc1 = []
    bc0 = []
    for y in range(len(array)):
        line = array[y]
        if line[bit] == '1':
            bc1.append(line)
        else:
            bc0.append(line)
    if len(bc1) >= len(bc0):
        array = bc1
        
    else:
        array = bc0
        
    return array

def less_common(array, bit):
    bc1 = []
    bc0 = []
    for y in range(len(array)):
        line = array[y]
        if line[bit] == '1':
            bc1.append(line)
        else:
            bc0.append(line)
    if len(bc1) < len(bc0):
        array = bc1
        
    else:
        array = bc0        
    return array


data = []


with open ('./Input_Day3.txt','r') as inputs:
    while inputs:
        line = inputs.readline()
        if line == "":
            break
        else:
            data.append(line)

#iteration to discover oxygen
bit = 0
ox = data
while len(ox) > 1:
    ox = most_common(ox,bit)
    bit += 1
bit = 0
co2 = data
while len(co2) > 1:
    co2 = less_common(co2,bit)
    bit += 1

print("co2")
print(int(co2[0],2))
print("oxygen")
print(int(ox[0],2))
print(int(co2[0],2)*int(ox[0],2))
