import flet as ft

def main(page: ft.Page):
    page.title = 'Привет мир'
    
    def change_name(e):
        print(name_input.value)

    name_input = ft.TextField(
        label = 'Введите ваше имя',
        on_change=change_name
    )
    page.add(name_input)

ft.app(main)