def romanToInt(s: str) -> int:
    romVal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    
    for i in range(len(s)):
        if i + 1 <len(s) and romVal[s[i]] < romVal[s[i+1]]:
            total -= romVal[s[i]]
        else:
            total += romVal[s[i]]
            
    return total

romInp = str(input("Enter a Roman Value: "))

print("The number in integer is: " , romanToInt(romInp))     