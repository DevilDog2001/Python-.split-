#PE4_1
str = "Python 123"
print(str)
print(str[0])
print(str[-1])
print(str[:])
print()
#PE_6
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[-1] + n[-2])
print(n[9] - n[1])
print(n[2] * n[5])
print(n[8] / n[2])
print(len(n), n[:len(n)], sep = '\n')
print(min(n), max(n), type(n), sep = '\t')
print()
#PE_7
myList = ['apple','banana','cherry',]
print(myList[-4:-1])
print()

#PE4_4 
#pratice
grades = []
grades.append(92)
grades.append(51)
grades.append(83)
grades.append(37)
grades.append(72)
print(grades)
total = grades[0]+grades[1]+grades[2]+grades[3]+grades[4]
avg = total//len(grades)
print(f'Average: {avg:.2f}') #First way
print()
print('Average: {:.2f}'.format(avg)) #Second way           #All 3 ways get same result
print()
print('Average: %.2f'%avg) #Third way
print()
del grades[1]
y = grades.pop(2)
print('updated list', grades)
print(f'Updated Average: {sum(grades)/len(grades):.3f}')
a = "Hi Bye"
print(a)
b = a.split()
print(b)
c = f'{b[0]}? {b[-1]}'
print(c)

#Practice PE4_5
#5
full_name = input("Enter the full name of your favorite US president: ")
a = full_name.split()
print(f'{"First Name:"} {a[0].title()}')
print(f'{"Last Name:"} {a[1].title()}')

print()

president = input("Enter the full name of your favorite US president: ")
b = president.split()
print(f'{"First Name:"} {b[0].title()}')
print(f'{"Last Name:"} {b[2].title()}')

