import math
import datetime

def main():
    num_lane = []
    mem_time = {}
    num_mem = int(input("組の九大の人数入力："))

    for i in range(num_mem):
        num_lane.append(input("{0}人目のレーン番号入力：".format(i+1)))

    for i in range(num_mem):
        mem_time[num_lane[i]] = []


    dist = int(input("距離：")) // 50

    for roop in range(dist*num_mem):
        print("登録済みレーン番号 => {0}".format(num_lane))
        in_lane = input("スプリットタイムを入力するレーンの番号を入力：")

        if in_lane in num_lane:
            print("第{0}レーンの".format(in_lane) + "{0}m時点のスプリットタイムを入力".format((int(len(mem_time[in_lane]))+1)*50))
            print("ex) 1:12:43, 26:43")
            time = input("TIME：")
            time_list = []
            time_list = time.split(":")

            if len(time_list) == 2:
                min = 0
                sec = int(time_list[0])
                micro_sec = int(time_list[1]) * (10**4)
                mem_time[in_lane].append(datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec))
            elif len(time_list) == 3:
                min = int(time_list[0])
                sec = int(time_list[1])
                micro_sec = int(time_list[2]) * (10**4)
                mem_time[in_lane].append(datetime.timedelta(minutes=min, seconds=sec, microseconds=micro_sec))
            else:
                print("Input Error: 入力し直してください")

        else:
            print("そのレーン番号は登録されていません")

    print("\n<<RESULT>>")

    for in_lane in num_lane:
        lap = []

        for i in range(int(len(mem_time[in_lane])) - 1):
            lap.append(mem_time[in_lane][i+1] - mem_time[in_lane][i])

        print("第{0}レーン".format(in_lane))
        print(str(mem_time[in_lane][0]))

        for i in range(int(len(mem_time[in_lane])) - 1):

            if i % 2 == 1:
                print(str(mem_time[in_lane][i+1]) + "({0})".format(lap[i]))
            elif  (i % 2 == 0) & (i == 0):
                print(str(mem_time[in_lane][i+1]) + "({0}".format(lap[i]) + ", " + "{0})".format(mem_time[in_lane][0] + lap[i]))
            else:
                print(str(mem_time[in_lane][i+1]) + "({0}".format(lap[i]) + ", " + "{0})".format(lap[i-1] + lap[i]))

    with open("./result.txt", mode="a") as f:
        f.write("<<RESULT>>\n")

        for in_lane in num_lane:
            f.write("第{0}レーン\n".format(in_lane))
            f.write(str(mem_time[in_lane][0]) + "\n")

            for i in range(int(len(mem_time[in_lane])) - 1):

                if i % 2 == 1:
                    f.write(str(mem_time[in_lane][i+1]) + "({0})\n".format(lap[i]))
                elif (i % 2 == 0) & (i == 0):
                    f.write(str(mem_time[in_lane][i+1]) + "({0}".format(lap[i]) + ", " + "{0})\n".format(mem_time[in_lane][0] + lap[i]))
                else:
                    f.write(str(mem_time[in_lane][i+1]) + "({0}".format(lap[i]) + ", " + "{0})\n".format(lap[i-1] + lap[i]))

        f.write("\n")

if __name__ == "__main__":
    Flag = 1

    while Flag:
        main()
        ch = input("\n終了する場合は0を入力、次のレースを入力する場合は1を入力：")

        if ch == "0":
            Flag = 0
        elif ch == "1":
            Flag = 1
        else:
            print("Input Error: 実行ファイルを再起動してください")
            Flag = 0
