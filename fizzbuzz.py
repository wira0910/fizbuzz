#! /usr/bin/python3

#! menerima input angka dari use
n = int(input("Masukkan angka yang diinginkan : " ))

for i in range(1, n+1):
    if i%15 == 0:
        print("fizzbuzz")
    elif i%3 ==0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(str(i))
