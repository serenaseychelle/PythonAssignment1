sh = input("enter hours: ")
sr = input("enter rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if fh > 40 :
   # print("overtime")
    reg = fr * fh
    otp = (fh - 40.00) * (fr *0.5)
  #  print(reg,otp)
    xp = reg + otp
else:
  #  print("regular")
    xp = fh * fr
print("pay:",xp)
