def func1(name):
    coordinate = {"辛巴" : (-3,3),
            "貝吉塔" : (-4,-1),
            "悟空" : (0,0),
            "特南克斯" : (1,-2),
            "丁滿" : (-1,4),
            "弗利沙" : (4,-1)}
    
    #設定線段右邊一組
    group_right = ("丁滿","弗利沙")

    #判斷是不是同一組
    name_in_group = name in group_right

    distance_list = []
    distance_dist = {}

    #判斷有沒有符合名字
    if name in coordinate:
        main_point = coordinate[name]

        
        for i_name , i_values in coordinate.items():
            #跳過自己
            if i_name == name:
                continue
            #計算距離 並把在線段另一側的都加2距離
            else:
                x_point = i_values[0] - main_point[0]
                y_point = i_values[1] - main_point[1]
                distance = abs(x_point) + abs(y_point)
                if (i_name in group_right) != name_in_group:
                    distance = distance + 2
                distance_list.append(distance)
                distance_dist[i_name] = distance

        #找最大最小值
        max_values =max(distance_dist.values())
        min_values =min(distance_dist.values())

        #根據最大最小值找相符的名字
        max_person = [person for person, d in distance_dist.items() if d == max_values]
        min_person = [person for person, d in distance_dist.items() if d == min_values]

        #處理文字
        max_str = "、".join(max_person)
        min_str = "、".join(min_person)
            
        print(f"最遠{max_str};最近{min_str}")
    
    else:
        print("輸入錯誤，請輸入座標名字")

# func1("辛巴") # print 最遠弗利沙；最近丁滿、貝吉塔
# func1("悟空") # print 最遠丁滿、弗利沙；最近特南克斯
# func1("弗利沙") # print 最遠辛巴，最近特南克斯
# func1("特南克斯") # print 最遠丁滿，最近悟空

def func2(ss, start, end, criteria):

    #確認start,end都是數字
    if (type(start) is not int) or (type(end) is not int):
        print("預約時間必須要是數字喔")
        return
    
    if start < 0 or start >= 24 or end < 1 or end >24:
        print("預約時間請填寫正確")
        return
    
    if start >= end:
        print("預約起始時間不可大於或等於結束時間")

    #確認輸入運算符號是對的
    check_op = ["=", ">=" ,"<="]
    if not any(op in criteria for op in check_op):
        print("'criteria'運算符有誤")
        return

    #分析criteria
    op = ""
    if ">=" in criteria:
        op = ">="
        field, val_str = criteria.split(">=")
        val = float(val_str)
    elif "<=" in criteria:
        op = "<="
        field, val_str = criteria.split("<=")
        val = float(val_str)
    elif "=" in criteria:
        op = "="
        field, val_str = criteria.split("=")
        #如果field是name就是字串 如果是其他就轉成浮點數
        val = val_str if field == "name" else float(val_str)

    best_service = None
    
    #用來找差距最小的
    min_diff = float('inf')

    for s in ss:
        #如果還沒有紀錄 就新增{"bookings" : []}
        if "bookings" not in s:
            s["bookings"] = []

        #檢查預約時間與紀錄時間有沒有衝突
        is_available = True
        for b_start, b_end in s["bookings"]:
            if start < b_end and end > b_start:
                is_available = False
                break
        
        # 如果時間衝突is_available會被改成false 就會跳到下一個
        if not is_available:
            continue
        
        #抓取價格
        s_val = s[field]

        matches = False
        diff = float('inf')

        if op == "=":
            if s_val == val:
                matches = True
                diff = 0
        elif op == ">=":
            if s_val >= val:
                matches = True
                diff = abs(s_val - val)
        elif op == "<=":
            if s_val <= val:
                matches = True
                diff = abs(s_val - val)

        #找差值最小的
        if matches:
            if diff < min_diff:
                min_diff = diff
                best_service = s

    #更新預約狀態
    if best_service:
        #把這段時間加入這個服務的預約紀錄
        best_service["bookings"].append((start, end))
        print(best_service["name"])
    else:
        print("Sorry")

# services=[
#     {"name":"S1","r":4.5,"c":1000},
#     {"name":"S2","r":3,"c":1200},
#     {"name":"S3","r":3.8,"c":800}
# ]
# func2(services, 15, 17, "c>=800")  # S3
# func2(services, 11, 13, "r<=4")    # S3
# func2(services, 10, 12, "name=S3") # Sorry
# func2(services, 15, 18, "r>=4.5")  # S1
# func2(services, 16, 18, "r>=4")    # Sorry
# func2(services, 13, 17, "name=S1") # Sorry
# func2(services, 8, 9, "c<=1500")   # S2

def func3(index):
    #判斷是不是數字
    if not isinstance(index, int) or index < 0:
        print("輸入錯誤")
        return

    sequence = [25]
    a=25

    #如果sequence數量少於index指定的數字
    while len(sequence) <= index:
        a1 = a - 2
        a2 = a1 - 3
        a3 = a2 + 1
        a4 = a3 + 2
        #把四個都加進sequence裡面
        sequence.extend([a1,a2,a3,a4])
        a = a4

    print(sequence[index])
    return

# func3(1) # print 23
# func3(5) # print 21
# func3(10) # print 16
# func3(30) # print 6

def func4(sp, stat, n):
    best_idx = -1
    best_diff = float('inf')
    
    fallback_idx = -1
    max_space = -1

    #擋掉輸入負數或True,False
    for i in sp:
        if type(i) is not int or i<0:
            print("'sp'輸入錯誤")
            return
    #如果stat不是輸入1,0就擋掉
    for i in stat:
        if i not in ["0","1"]:
            print("車廂狀態'stat'輸入錯誤")
            return
            
    #如果sp數量與stat數量不符就擋掉
    if len(sp) != len(stat):
        print(f"輸入錯誤，車廂數量({len(sp)})與狀態數量({len(stat)})不符合")
        return
    
    #如果n不是整數或小於等於0就擋掉
    if type(n) is not int or n <= 0:
        print("'n'輸入錯誤")
        return
    
    for i in range(len(sp)):
        #確認座位能不能使用
        if stat[i] == "0":
            #可以容納得話
            if sp[i] >= n:
                #這邊diff是座位數大於乘客多幾位
                diff = sp[i] - n
                if diff < best_diff:
                    best_diff = diff
                    best_idx = i
            
            else:
                #記錄目前找到空位最多的
                if sp[i] > max_space:
                    max_space = sp[i]
                    fallback_idx = i
                    
    #如果有找到能容納的車廂 就輸出best_idx 不然就輸出fallback_idx
    result = best_idx if best_idx != -1 else fallback_idx
    print(result)
    return result

# func4([3, 1, 5, 4, 3, 2],"101000", 2) # print 5
# func4([1, 0, 5, 1, 3],"10100", 4) # print 4
# func4([4, 6, 5, 8],"1000", 4) # print 2









