s1, s2= input(), input()

print(f'Вы ввели строку \"{s1}\" и \"{s2}\"')
print(f'Их длина соответственно {len(s1)} и {len(s2)}')
print('Первый символ первой строки', s1[0])
print('Последний символ последней строки', s2[-1])

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)