import os

filename = "c:/202141093/1115.list.txt"
list = {}
if os.path.isfile(filename):
    f = open(filename, 'r')

    while True:
        line = f.readline()
        if not line:
            break
        data = line.strip().split(',')
        scores = []
        if len(data) == 4:
            sum = int(data[1]) + int(data[2]) + int(data[3])
            aver = sum/3
            scores = [int(data[1]), int(data[2]), int(data[3])]
            list[data[0]] = scores
            print(f"{data[0]}, {scores}, 평균 : {aver:.1f}")

f.close()