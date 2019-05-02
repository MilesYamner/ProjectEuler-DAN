Dan = 0
with open("P11.txt") as file_:
	blob = file_.read()
# print(blob)
list_of_numbers = blob.split("\n")
for index, value in enumerate(list_of_numbers):
	list_of_numbers[index] = value.split()
for j in range(20):
	for i in range(17):
		x = int(list_of_numbers[j][i])*int(list_of_numbers[j][i+1])*int(list_of_numbers[j][i+2])*int(list_of_numbers[j][i+3])
		if (Dan < x):
			Dan = x
print(Dan)
Dan2 = 0
for j in range(17):
	for i in range(20):
		x = int(list_of_numbers[j][i])*int(list_of_numbers[j+1][i])*int(list_of_numbers[j+2][i])*int(list_of_numbers[j+3][i])
		if (Dan2 < x):
			Dan2 = x
print(Dan2)

Dan3 = 0
for j in range(17):
	for i in range(17):
		x = int(list_of_numbers[j][i])*int(list_of_numbers[j+1][i+1])*int(list_of_numbers[j+2][i+2])*int(list_of_numbers[j+3][i+3])
		if (Dan3 < x):
			Dan3 = x
print(Dan3)
Dan4 = 0
for j in range(17):
	for i in range(17):
		x = int(list_of_numbers[j+3][16-i])*int(list_of_numbers[j+2][17-i])*int(list_of_numbers[j+1][18-i])*int(list_of_numbers[j][19-i])
		if (Dan4 < x):
			Dan4 = x
print(Dan4)