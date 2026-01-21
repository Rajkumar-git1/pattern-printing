n= int(input("enter number of element"))
print("\n normal pyramid")
for i in range(n):
    x =' *'
    x = x*i
    print(f'{x:^10}')




print("\n invert pyramid")
for i in range(5):
    x =' *'
    x = x*(5-i)
    print(f'{x: ^10}')



print("\n left side pyramid")
for i in range(5):
    x =' *'
    x = x*i
    print(f'{x:<10}')




print("\n right side pyramid")
for i in range(5):
    x =' *'
    x = x*i
    print(f'{x:>10}')