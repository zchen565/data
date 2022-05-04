import random

lines = open('train_0.txt').read().split('\n')
print(len(lines))

train = []
dev = []
for line in lines:
    temp = random.randint(1,100)
    if temp > 5:
        train.append(line)
    else:
        dev.append(line)
    


print(len(dev))

with open('t0_train.txt', 'w') as f:
    f.writelines([line + '\n' for line in train])

with open('t0_dev.txt','w') as f:
    f.writelines([line + '\n' for line in dev]) 
