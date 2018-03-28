# Thea Murtagh Collatz Conjecture

x = 17

if x == 1:
    print(x)
    
while x > 1:
    if x % 2 == 0:
        x = x / 2
        print(x)
    else:
        x = 3 * x + 1
        print(x)
