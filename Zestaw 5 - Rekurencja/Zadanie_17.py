# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić  
# wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.


a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

def is_prime(n):
    if n<2:
        return False
    if n==2 or n==3 or n==5:
        return True
    if not n%2 or not n%3 or not n%5: # if n%2 == 0 itd
        return False
    i=7
    while i*i<n:
        if not n%i:
            return False
        i+=4
        if not n%i:
            return False
        i+=2
    return True


def zad(a,b):
    odp = 0
    def NumBuild(a,b,x=0, potega=1):
        if a == b == 0 and is_prime(x):
             nonlocal odp 
             odp += 1
             #print(x)
        if a>0 and b>0:
             return NumBuild( a//10 , b, x + (a%10)*potega, potega*10) or NumBuild( a, b//10, x + (b%10)*potega, potega*10)
        if b>0 and a==0:
             return NumBuild( a, b//10, x + (b%10)*potega, potega*10)
        if a>0 and b==0:
             return NumBuild( a//10 , b, x + (a%10)*potega, potega*10)

    NumBuild(a,b)
    return odp

#NumBuild(a,b)
print(zad(a,b))
