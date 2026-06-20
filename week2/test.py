def func3(index):
    #判斷是不是數字
    if not isinstance(index, int) or index < 0:
        print("輸入錯誤")
        return

    sequence = [25]
    a=25

    #如果sequence數量少於index指定的數字
    while len(sequence) < index:
        a1 = a - 2
        a2 = a1 - 3
        a3 = a2 + 1
        a4 = a3 + 2
        #把四個都加進sequence裡面
        sequence.extend([a1,a2,a3,a4])
        a = a4

    print(sequence[index])


func3(50)