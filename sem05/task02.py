# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


nums = '1 3 4 5 7 9'
nums = list(map(int, nums.split()))

output = []
for i in range(len(nums)):
    if nums[i]+1 == nums[i]:
        # lst[i-1] c конца начинается
        output.append(nums[i]+1)
print(output)

# a = [['1', '2'], ['2', '3'], ['6', '9'], ['16', '19']]
# b = []
# for i in a:
#     for j in i:
#         b.append(int(j))
# print(b)
