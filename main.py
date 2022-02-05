x = ['#', 'x', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
i_count = 0
for i in x:
    if i == ' ':
        i_count += 1
if i_count == 0:
    print('Ничья')
