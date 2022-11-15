f = open("c:/202141093/1115.list.txt", 'w')

list={}

while True:
    name = input("이름 : ")
    if name == "":
        break
    scores = {}
    scores['kor'] = input("국어 점수 : ")
    scores['eng'] = input("영어 점수 : ")
    scores['math'] = input("수학 점수 : ")
    list[name] = scores

    data = f"{name}, {scores['kor']}, {scores['eng']}, {scores['math']}\n"

    print(list)
    f.write(data)
f.close()