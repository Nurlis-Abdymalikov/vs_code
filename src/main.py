import flet as ft

def main(page: ft.Page):
    page.title = 'Приложение для управления списком дел'
    todo_list = []

    title = ft.Text('Список дел на день', size=30, weight=ft.FontWeight.BOLD)
    
    def change_todo(e):
        print(todo_input.value)

    def click_button(e):
        print(todo_input.value)
        new_todo = {'todo': todo_input.value, 'category': category_input.value}
        todo_list.append(ft.Text(value=f"{new_todo['todo']}: {new_todo['category']}"))
        todo_list_area.controls = [t for t in todo_list]
        page.update()


    todo_input= ft.TextField(
        label = 'Введите что-нибудь',
        on_change=change_todo
    )
    category_input= ft.TextField(
        label = 'Введите категорию',
        on_change=change_todo
    )

    add_button = ft.ElevatedButton(
        'Добавить',
        on_click = click_button,
        color=ft.Colors.PINK,
        bgcolor=ft.Colors.AMBER
        
        )
    
    todo_list_area = ft.Column()

    page.add(title,todo_input,category_input,add_button,todo_list_area)

    

ft.app(main)