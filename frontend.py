import flet
from flet import Page, View, Column, Text, TextField, ElevatedButton, icons, Image, Container, alignment

import backend  # import backend functions


def main(page: Page):
    page.title = "HERMETRIX"
    page.window_width = 360
    page.window_height = 720
    page.bgcolor = "#FFFFFF"  # white
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 20
    page.spacing = 20

    message_text = Text("", color="#B69548", size=14)

    def create_welcome_view():
        # Logo image centered within a Container
        logo = Container(
            content=Image(
                src="assets/HERMETRIXLOGOFIN.png",  # relative path to image in assets folder
                width=200,
                height=200,
                fit="contain",
            ),
            alignment=alignment.center,
            width=page.window_width,
            height=220,
        )

        btn_signup = ElevatedButton(
            "Sign Up",
            width=180,
            height=50,
            bgcolor="#32620E",  # emerald green
            color="#FFF2D2",  # beige text color for contrast
            on_click=lambda e: page.go("/signup")
        )
        btn_login = ElevatedButton(
            "Log In",
            width=180,
            height=50,
            bgcolor="#203D0A",  # darker green
            color="#FFF2D2",
            on_click=lambda e: page.go("/login")
        )

        col = Column(
            [logo, btn_signup, btn_login],
            alignment="center",
            horizontal_alignment="center",
            spacing=30,
            expand=True,
        )
        return View("/", [col])

    def create_signup_view():
        heading = Text("Sign Up", size=30, weight="bold", color="#32620E", text_align="center")

        input_username = TextField(label="Username", width=300, height=45)
        input_email = TextField(label="Email", width=300, height=45)
        input_password = TextField(label="Password", password=True, can_reveal_password=True, width=300, height=45)

        def on_register_click(e):
            message_text.value = ""
            username = input_username.value.strip()
            email = input_email.value.strip()
            password = input_password.value

            if not username or not email or not password:
                message_text.value = "Please fill in all fields."
                page.update()
                return

            success = backend.sign_up(username, email, password)
            if success:
                message_text.value = "Sign up successful! You can now log in."
                message_text.color = "#B69548"  # gold
            else:
                message_text.value = "Sign up failed. Try again."
                message_text.color = "red"
            page.update()

        btn_register = ElevatedButton(
            "Register",
            width=180,
            height=50,
            bgcolor="#32620E",
            color="#FFF2D2",
            on_click=on_register_click
        )
        btn_back = ElevatedButton(
            "Back",
            icon=icons.ARROW_BACK,
            bgcolor="#203D0A",
            color="#FFF2D2",
            on_click=lambda e: page.go("/")
        )

        col = Column([
            heading,
            input_username,
            input_email,
            input_password,
            btn_register,
            message_text,
            btn_back
        ], alignment="center", horizontal_alignment="center", spacing=15, expand=True)

        return View("/signup", [col])

    def create_login_view():
        heading = Text("Log In", size=30, weight="bold", color="#32620E", text_align="center")

        input_email = TextField(label="Email", width=300, height=45)
        input_password = TextField(label="Password", password=True, can_reveal_password=True, width=300, height=45)

        def on_login_click(e):
            message_text.value = ""
            email = input_email.value.strip()
            password = input_password.value

            if not email or not password:
                message_text.value = "Please fill in all fields."
                message_text.color = "red"
                page.update()
                return

            success = backend.log_in(email, password)
            if success:
                message_text.value = "Login successful! Welcome."
                message_text.color = "#B69548"  # gold
            else:
                message_text.value = "Invalid email or password."
                message_text.color = "red"
            page.update()

        btn_login = ElevatedButton(
            "Log In",
            width=180,
            height=50,
            bgcolor="#32620E",
            color="#FFF2D2",
            on_click=on_login_click
        )
        btn_back = ElevatedButton(
            "Back",
            icon=icons.ARROW_BACK,
            bgcolor="#203D0A",
            color="#FFF2D2",
            on_click=lambda e: page.go("/")
        )

        col = Column([
            heading,
            input_email,
            input_password,
            btn_login,
            message_text,
            btn_back
        ], alignment="center", horizontal_alignment="center", spacing=15, expand=True)

        return View("/login", [col])

    page.views.append(create_welcome_view())
    page.views.append(create_signup_view())
    page.views.append(create_login_view())

    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(create_welcome_view())
        elif page.route == "/signup":
            page.views.clear()
            page.views.append(create_signup_view())
        elif page.route == "/login":
            page.views.clear()
            page.views.append(create_login_view())
        else:
            page.views.clear()
            page.views.append(create_welcome_view())
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")


if __name__ == "__main__":
    flet.app(target=main)
