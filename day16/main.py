import sys
import datetime
date = datetime.date.today().strftime("%d-%m-%y")


inpt = sys.argv[1:]
# print(inpt)
jn = " ".join(inpt)
# print(len(jn))
spl = jn.split("-")
# print(spl)

if "-" not in sys.argv:
    print("wrong")
elif spl[-1] == "-":
    print("wrong2")
elif spl[-1] == "":
    print("wrong3")
elif len(spl) != 2:
    print("wrong4")
else:
    print(f"Book name: {spl[0]} \nWriter: {spl[1]} \nAdded in : {date}")

