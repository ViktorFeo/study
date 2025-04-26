def print_menu():
    print('\n1. Добавить задачу\n2. Показать все задачи\n3. Отметить как выполненную\n4. Удалить задачу\n5. Выход')


def append_with_line_numbers(filename, new_data):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            existing_lines = file.readlines()
            start_line = len(existing_lines) + 1
    except FileNotFoundError:
        start_line = 1

    with open(filename, 'a', encoding='utf-8') as file:
        for i, line in enumerate(new_data, start_line):
            file.write(f"{i}. {line}\n")


def mark_as_completed(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = file.readlines()

        print("\nТекущие задачи:")
        for task in tasks:
            print(task.strip())

        task_num = int(input('\nВведите номер задачи для отметки как выполненной: '))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1].replace('\n', '') + ' ✓\n'

            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(tasks)
            print("Задача отмечена как выполненная!")
        else:
            print("Неверный номер задачи!")

    except FileNotFoundError:
        print("Список задач пуст!")


def delete_task(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = file.readlines()

        print("\nТекущие задачи:")
        for task in tasks:
            print(task.strip())

        task_num = int(input('\nВведите номер задачи для удаления: '))

        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]

            # Перезаписываем файл с обновленной нумерацией
            with open(filename, 'w', encoding='utf-8') as file:
                for i, task in enumerate(tasks, 1):
                    # Сохраняем текст задачи без старого номера
                    task_text = task.split('. ', 1)[1] if '. ' in task else task
                    file.write(f"{i}. {task_text}")
            print("Задача удалена!")
        else:
            print("Неверный номер задачи!")

    except FileNotFoundError:
        print("Список задач пуст!")


def main():
    filename = 'task_to-do_list.txt'

    while True:
        print_menu()
        try:
            action_select = int(input('Введите номер действия: '))

            if action_select == 1:
                new_line = [input('Введите задачу для добавления в список: ')]
                append_with_line_numbers(filename, new_line)

            elif action_select == 2:
                try:
                    with open(filename, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if content:
                            print("\nСписок задач:")
                            print(content)
                        else:
                            print("\nСписок задач пуст!")
                except FileNotFoundError:
                    print("\nСписок задач пуст!")

            elif action_select == 3:
                mark_as_completed(filename)

            elif action_select == 4:
                delete_task(filename)

            elif action_select == 5:
                print("Выход из программы")
                break

            else:
                print("Неверный номер действия! Попробуйте снова.")

        except ValueError:
            print("Ошибка: введите число от 1 до 5!")


if __name__ == "__main__":
    main()