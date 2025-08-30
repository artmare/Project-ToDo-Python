# 1. [ ] Купить молоко
# 2. [ ] Сделать домашку
# 3. [x] Пробежка утром

import json

tasks = {}

listt = 'tasks.json'

try:
    with open(listt, "r", encoding = 'utf-8') as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = {}

print("Команды: add, list, done, delete, exit")

while True:
    comm = input('write a command ')
    
    if comm == 'add':
        task = input('write a task ')
        tasks[task] = False
        print(f'task "{task}" was added ')
    elif comm == 'list':
        if not tasks:
            print('Your list is empty ')
        else:
            for i, (task, done) in enumerate(tasks.items(), start=1):
                status = '[x]' if done else '[ ]'
                print(f'{i}. {status} {task}')
    elif comm == 'done':
        task = input('write a task ')
        if task not in tasks:
            print('Here is not your task!')
        else:
            tasks[task] = True
            print(f'Task {task} is done ')
        
    elif comm == 'delete':
        task = input('write a task ')
        if task not in tasks:
            print('Here is not your task!')
        else:
            del tasks[task]
            print(f'Task {task} was deleted')
    elif comm == 'exit':
        with open(listt, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
        print("Exiting, tasks saved!")
        break