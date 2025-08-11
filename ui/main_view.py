import flet as ft
from logic.memes import get_random_meme

def main_view_function(page: ft.Page):
    page.title = "PasswordXD"

    memes_text = ft.Text(value="", size=16, color="blue")

    def on_get_password_click(e):
        memes_text.value = get_random_meme()
        page.update()

    btn1 = ft.ElevatedButton(text="Get random password", on_click=on_get_password_click)
    btn2 = ft.ElevatedButton(text="Create new password")

    page.add(btn1, btn2, memes_text)
