def run_encoding(s):
    n = len(s)
    if n == 0:
        return ""
    encoded = ""
    runlen = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            runlen += 1
        else:
            encoded += str(runlen) + s[i-1]
            runlen = 1
    encoded += str(runlen) + s[n-1]
    return encoded.replace("1","")

#An example of input to print and can be changed:
string1 = "ddd"
string2 = "heloooooooo there"
string3 = "choosemeeky and tuition-free"
encoded_string1 = run_encoding(string1)
encoded_string2 = run_encoding(string2)
encoded_string3 = run_encoding(string3)

print(" ",encoded_string1,"\n", encoded_string2,"\n", encoded_string3 )