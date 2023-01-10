# 1* Задано N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось
# условие A[i] - 1 = A[i-1]. Найдите это число.
# *' 1 2 3 4 6 7 -> 5
# *' 1 3 -> 2

# with open('file.txt', 'w') as f:  # создаем файл
#     f.write('1 3 4 5 7 9')  # и записываем
# f.close()  # закрываем файл
# file = 'file.txt'
# f = open(file, 'r')  # открываю файл


def func(lst):
    output = []
    for i in range(1, len(lst)):
        if lst[i]-1 != lst[i-1]:
            # lst[i-1] c конца начинается
            output.append(lst[i]-1)
    return output


# nums = 1, 3, 4, 5, 7, 9
num = '1 3 4 5 7 9'
nums = list(map(int, num.split()))

# nums = list(map(int, f.read().split()))  # из (str) делаем (int)

print(func(nums))
