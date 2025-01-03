
num = int(input("Enter a five-digit number: "))   #12345

d1 = num // 10000      #1
d2 = (num // 1000) % 10  #12 --> 2
d3 = (num // 100) % 10  #123 -->3
d4 = (num // 10) % 10 #1234 -->4
d5 = num % 10  # -->5


reversed_num = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1     #5* 10000 + 4*1000 +3*100+ 2*10+ 1
a= 5* 10000 + 4*1000 +3*100+ 2*10+ 1
print(a)

print(reversed_num)

if num == reversed_num:
    print("reversed numbers are equal.")
else:
    print("not equal.")
