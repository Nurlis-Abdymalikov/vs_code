import flet as ft

def main(page: ft.Page):
    page.title = 'Приложение для управления списком дел'
    todo_list = []

    title = ft.Text('Список дел на день', size=30, weight=ft.FontWeight.BOLD)
    
    def change_todo(e):
        print(todo_input.value)
    a = 'dgi'
        

    def click_button(e):
        print(todo_input.value)
        todo_list.append(todo_input.value),
        todo_list_area.controls = [
            ft.Text(value=todo) for todo in todo_list] 
        ft.Text(a.value)
        page.update()


    todo_input= ft.TextField(
        label = 'Введите что-нибудь',
        on_change=change_todo
    )

    add_button = ft.ElevatedButton(
        'сохранить',
        on_click = click_button,
        color=ft.Colors.PINK,
        bgcolor=ft.Colors.AMBER
        
        )
    
    todo_list_area = ft.Column()

    page.add(title,todo_input,add_button,todo_list_area)

    

ft.app(main)