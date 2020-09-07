import tasks

result = tasks.add.delay(2, 2)

print('get result')

print(result.get())
