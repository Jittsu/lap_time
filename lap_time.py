import math
import datetime

def main():
    num_lane = []
    mem_time = {}
    num_mem = int(input("組の九大の人数入力："))
    for i in range(num_mem):
#        print("{0}人目のレーン番号入力".format(i+1))
        num_lane.append(input("{0}人目のレーン番号入力：".format(i+1)))
    for i in range(num_mem):
        mem_time[num_lane[i]] = []
    while True:
#        print("スプリットタイムを入力するレーンの番号を入力")
        print("登録済みレーン番号 => {0}".format(num_lane))
        in_lane = input("スプリットタイムを入力するレーンの番号を入力：")
        if in_lane in num_lane:
            print("第{0}レーンの".format(in_lane) + "{0}m時点のスプリットタイムを入力".format((int(len(mem_time[in_lane]))+1)*50))
            print("ex) 1:12:43, 26:43")
            time = input("TIME：")
            time_list = []
            time_list = time.split(":")
            if(len(time_list) == 2):
                min = 0
                sec = int(time_list[0])
                micro_sec = int(time_list[1]) * (10**4)
                mem_time[in_lane].append(datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec))
            elif(len(time_list) == 3):
                min = int(time_list[0])
                sec = int(time_list[1])
                micro_sec = int(time_list[2]) * (10**4)
                mem_time[in_lane].append(datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec))
            else:
                print("Input Error: 入力し直してください")
#            print("終了する場合は0を入力、続けて入力する場合は1を入力")
            branch = input("終了する場合は0を入力、続けて入力する場合は1を入力：")
            if(branch == "0"):
                break
        else:
            print("そのレーン番号は登録されていません")

    print("\n<<RESULT>>")
    for in_lane in num_lane:
        for i in range(int(len(mem_time[in_lane])) - 1):
            lap = []
            lap.append(mem_time[in_lane][i+1] - mem_time[in_lane][i])
        print("第{0}レーン".format(in_lane))
        print(str(mem_time[in_lane][0]))
        for i in range(int(len(mem_time[in_lane])) - 1):
            print(str(mem_time[in_lane][i+1]) + "({0})".format(lap[i]))

if __name__ == "__main__":
    Flag = 1
    while Flag:
        main()
#        print("終了する場合は0を入力、次のレースを入力する場合は1を入力")
        ch = input("\n終了する場合は0を入力、次のレースを入力する場合は1を入力：")
        if ch == "0":
            Flag = 0
        elif ch == "1":
            Flag = 1
        else:
            print("Input Error: 実行ファイルを再起動してください")
            Flag = 0