import os

# for i in range(10):
#     f = open(f'file_{i}.txt', 'a')
#     f.write(f'Hello {i}\n')
#     f.close()

for i in range(10):
    os.remove(f'file_{i}.txt')
    print(f'file_{i}.txt removed')


    