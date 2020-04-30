print("這是一個算奶量的小程式，由PGY林協霆設計於2020四月\n")
print("說明：每輸入完一個值，請按enter繼續\n")
#定義function
def calc(weight,total_subtract_drug,feeding,freq):    
    oral = freq*feeding #自己總共可以吃的
    iv_need =  total_subtract_drug-oral #需額外給的Fluid
    iv_need_perh = round(iv_need/24,2) #每小時的量
    
    iv_show = ""
    if iv_need_perh <= 0:
        iv_show = "不用額外點滴，已經可以吃到" + str(round(oral/weight,2)) + "mL/kg/d 了！"
    else:
        iv_show = "還需要"+str(iv_need_perh)+"cc/hr的點滴"
    return [oral,iv_show]

def input_info():
    weight = float(input("Step 1. 請輸入今天的體重，單位為kg： "))
    print("Step 2. 如果小於37週，從80mL/kg/d開始，大於37周則從70mL/kg/d開始，每天加10mL")
    dailyTotal = float(input("\t依照出生天數，輸入目前Daily Total fluid，單位為mL/kg/d: "))
    print("Step 3. 目前的IV Drug...\n\tA.如果是從iv keep line給Ampi Q8H+Genta QD的話，為16mL")
    print("\tB.如果是iv for drug給Ampi Q8H +Genta QD的話，為40mL")
    ivdrug = float(input("\t請輸入目前的IV Drug，單位是mL: "))
    feeding = float(input("Step 4. 請輸入目前每餐可以吃的量，單位mL: "))
    freq = 8
    freq_q = int(input("Step 5. 請輸入頻率，Q3請輸3，Q4請輸4: "))
    if freq_q == 4:
        freq = 6
    else:
        pass #預設為Q3H
    total = round(weight*dailyTotal,2) 
    total_subtract_drug = total-ivdrug 
    result = calc(weight,total_subtract_drug,feeding,freq) #不加奶的結果
    result_5 = calc(weight,total_subtract_drug,feeding+5,freq) #加5西西
    result_10 = calc(weight,total_subtract_drug,feeding+10,freq) #加10西西

    print("\n結果：")
    print(f"\t寶寶今天至少需要 {total} mL的intake")
    print(f"\t如果今天不加奶，跟昨天一樣每餐吃{feeding}mL，一天吃{result[0]}mL\n\t減去藥物的{ivdrug}mL\n\t{result[1]}\n")
    print(f"\t加5mL，每餐吃{feeding+5}mL，一天吃{result_5[0]}mL\n\t減去藥物的{ivdrug}mL\n\t{result_5[1]}\n")
    print(f"\t加10mL，每餐吃{feeding+10}mL，一天吃{result_10[0]}mL\n\t減去藥物的{ivdrug}mL\n\t{result_10[1]}\n")
#執行
run = True
index = 1
while run:

    print(f"計算第 {index} 位寶寶的值~~")
    input_info()
    again = str(input("還要再一次嗎？要請按y，不要則按任意鍵: "))
    if again.lower() == "y":
        print("即將開始計算下一位的奶量...........................\n")
        index +=1
    else:
        print("再會!!!")
        run = False
