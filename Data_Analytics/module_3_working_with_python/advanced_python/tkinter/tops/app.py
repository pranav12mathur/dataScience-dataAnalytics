
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk


# ---------------- WINDOW ----------------

root = ttk.Window(themename="flatly")
root.title("TOPS - Login App")
root.geometry("700x750")
root.minsize(600, 650)

# Colors
BLUE = "#326783"
LIGHT_BG = "#F3F4F9"
WHITE = "#FFFFFF"
GREEN = "#0EAD98"
TEXT = "#243447"
MUTED = "#78869A"


# ---------------- BACKGROUND ----------------

canvas = tk.Canvas(
    root,
    highlightthickness=0,
    bg=LIGHT_BG
)
canvas.pack(fill="both", expand=True)


def draw_background(event=None):
    canvas.delete("background")

    width = root.winfo_width()
    height = root.winfo_height()

    # Blue upper section
    canvas.create_rectangle(
        0, 0, width, height * 0.62,
        fill=BLUE,
        outline="",
        tags="background"
    )

    # Slanted transition
    canvas.create_polygon(
        0, height * 0.60,
        width, height * 0.61,
        width, height,
        0, height,
        fill=LIGHT_BG,
        outline="",
        tags="background"
    )


root.bind("<Configure>", draw_background)


# ---------------- LOGIN CARD ----------------

card = ttk.Frame(
    root,
    padding=40,
    bootstyle="light"
)

card.place(
    relx=0.5,
    rely=0.63,
    anchor="center",
    relwidth=0.81,
    relheight=0.62
)


# ---------------- LOGO ----------------

try:
    logo_image = Image.open("TOPS-logo-light.png")

    # Resize logo while preserving aspect ratio
    logo_image.thumbnail((400, 100))

    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(
        root,
        image=logo_photo,
        bg=BLUE,
        borderwidth=0
    )

    logo_label.place(
        relx=0.5,
        rely=0.18,
        anchor="center"
    )

except FileNotFoundError:
    print("Logo not found. Check the filename and folder.")


# ---------------- WELCOME TEXT ----------------

welcome_label = ttk.Label(
    card,
    text="Welcome Back !",
    font=("Arial", 20),
    foreground="#315B9A",
    anchor="center"
)
welcome_label.pack(pady=(0, 8))

subtitle_label = ttk.Label(
    card,
    text="Sign in to continue to TOPS Career Center.",
    font=("Arial", 13),
    foreground=MUTED,
    anchor="center"
)
subtitle_label.pack(pady=(0, 38))


# ---------------- MOBILE NUMBER ----------------

mobile_label = ttk.Label(
    card,
    text="Mobile Number",
    font=("Arial", 12),
    foreground=TEXT
)
mobile_label.pack(anchor="w", pady=(0, 8))

mobile_entry = ttk.Entry(
    card,
    font=("Arial", 13)
)
mobile_entry.pack(fill="x", ipady=9)

mobile_entry.insert(0, "")


# ---------------- PASSWORD ----------------

password_header = ttk.Frame(card)
password_header.pack(fill="x", pady=(20, 8))

password_label = ttk.Label(
    password_header,
    text="Password",
    font=("Arial", 12),
    foreground=TEXT
)
password_label.pack(side="left")


def forgot_password():
    messagebox.showinfo(
        "Forgot Password",
        "Password recovery will be added later."
    )


forgot_button = ttk.Button(
    password_header,
    text="Forgot password?",
    bootstyle="link",
    command=forgot_password
)
forgot_button.pack(side="right")


password_entry = ttk.Entry(
    card,
    font=("Arial", 13),
    show="●"
)
password_entry.pack(fill="x", ipady=9)


# ---------------- SHOW / HIDE PASSWORD ----------------

show_password = False


def toggle_password():
    global show_password

    show_password = not show_password

    if show_password:
        password_entry.config(show="")
        eye_button.config(text="Hide")
    else:
        password_entry.config(show="●")
        eye_button.config(text="Show")


eye_button = ttk.Button(
    card,
    text="Show",
    bootstyle="secondary-outline",
    command=toggle_password
)
eye_button.pack(anchor="e", pady=(5, 0))


# ---------------- SIGN IN ----------------

def sign_in():
    mobile = mobile_entry.get().strip()
    password = password_entry.get()

    if not mobile:
        messagebox.showerror(
            "Missing Information",
            "Please enter your mobile number."
        )
        mobile_entry.focus()
        return

    if not password:
        messagebox.showerror(
            "Missing Information",
            "Please enter your password."
        )
        password_entry.focus()
        return

    # UI demonstration only.
    # Real authentication will be added later.
    messagebox.showinfo(
        "Sign In",
        "Login form submitted successfully!"
    )


sign_in_button = ttk.Button(
    card,
    text="Sign In",
    bootstyle="success",
    command=sign_in
)
sign_in_button.pack(
    fill="x",
    pady=(25, 0),
    ipady=10
)


# ---------------- START APP ----------------

root.mainloop()