value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000," ":0}



def convert_roman_to_value(n):
    result = 0
    for i in range(len(n)-1):
        if value[n[i]] < value[n[i+1]]:
            result = result - value[n[i]]
        elif value[n[i]] > value[n[i+1]]:
            result = result + value[n[i]]
        else:
            result = result + value[n[i]]
    return result

count = int(input("How many roman numbers you want to convert to value : "))
for i in range(count):
    convert_roman_to_value(input("Enter the Roman number : ")+" ")
