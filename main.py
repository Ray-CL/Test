dict = {"KW": {"1": "int", "2": "void", "3": "return", "4": "const", "5": "main"},
        "OP": {"6": "+", "7": "-", "8": "*", "9": "/", "10": "%", "11": "=", "12": "" > "", "13": "<", "14": "==", "15": "<=", "16": ">=", "17": "!=", "18": "&&", "19": "||"},
        "SE": {"20": "(", "21": ")", "22": "{", "23": "}", "24": ";", "25": ","},
        }

f = open("1.txt")
line = f.readline()
while line:
    line = line.strip("\n")
    list = line.split(" ")
    t1 = list[0]
    t2 = list[1][1:len(list[1]) - 1]
    t2 = t2.split(",")
    key = t2[0]
    value = t2[1]
    if key in dict.keys():
        try:
            print(f"此处为key={key} ", dict[key][value])
        except KeyError:
            print("判断此处为内容为空，默认打印KW的int")
    elif key == "INT":
        print(f"判断此处为INT,打印出value={value}")
    elif key == "IDN":
        print(f"判断此处为IDN,打印出value={value}")
    line = f.readline()
f.close()
