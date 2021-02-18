
s = input()
s_int = int(s[:4])*10000+int(s[5:7])*100+int(s[8:10])
if s_int <= 20190430:
    print("Heisei")
else:
    print("TBD")