numbers = [10,20,30,40,50]
num = [10, "Rahul", 10.20]

print(type(numbers))

print(numbers[1])

# print(numbers[5])

print(len(numbers))
print(numbers[len(numbers)-1])

print(numbers[-2])

numbers.append(60)

print(numbers)
numbers.insert(1, 15)
print(numbers)

print(numbers.index(30))

numbers.remove(15)
print(numbers)

numbers.reverse()
print(numbers)

lst = [13,4,23,10,25,20]
lst.sort()
print(lst)

lst.pop()
print(lst)

a = [1,2,3]
b = [4,5,6]

a.extend(b)
print(a)

print(70 in numbers)

numbers1= []
numbers2 = list()

numbers.clear()
