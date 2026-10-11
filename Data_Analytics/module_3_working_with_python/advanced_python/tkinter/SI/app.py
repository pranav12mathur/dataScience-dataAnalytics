
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import Image, ImageTk


# ================= CONFIGURATION =================

APP_NAME = "TOPS | Simple Interest Calculator"

BLUE = "#326783"
DARK_BLUE = "#173E59"
GREEN = "#0EAD98"
BG = "#F1F5F9"
WHITE = "#FFFFFF"
TEXT = "#203344"
MUTED = "#718096"
BORDER = "#DCE5ED"


# ================= RESOURCE PATH =================

def resource_path(filename):
    """Find files both in Python and in a PyInstaller executable."""
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / filename


# ================= WINDOW =================

root = tk.Tk()
root.title(APP_NAME)
root.geometry("760x850")
root.minsize(650, 750)
root.configure(bg=BG)


# ================= STYLES =================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Modern.TEntry",
    font=("Segoe UI", 12),
    padding=10,
    fieldbackground=WHITE,
    foreground=TEXT,
    bordercolor=BORDER
)

style.map(
    "Modern.TEntry",
    bordercolor=[("focus", GREEN)]
)

style.configure(
    "Modern.TCombobox",
    font=("Segoe UI", 11),
    padding=8,
    fieldbackground=WHITE,
    background=WHITE,
    foreground=TEXT
)


# ================= HEADER =================

header = tk.Frame(
    root,
    bg=DARK_BLUE,
    height=170
)
header.pack(fill="x")
header.pack_propagate(False)


# ================= LOGO =================

try:
    logo_path = resource_path("TOPS-logo-light.png")

    logo_image = Image.open(logo_path).convert("RGBA")
    logo_image.thumbnail((260, 75), Image.Resampling.LANCZOS)

    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(
        header,
        image=logo_photo,
        bg=DARK_BLUE,
        borderwidth=0
    )
    logo_label.image = logo_photo
    logo_label.pack(pady=(10, 3))

except Exception as error:
    print("Logo loading failed:", error)

    tk.Label(
        header,
        text="TOPS TECHNOLOGIES",
        font=("Segoe UI", 22, "bold"),
        fg=WHITE,
        bg=DARK_BLUE
    ).pack(pady=(20, 5))


tk.Label(
    header,
    text="Simple Interest Calculator",
    font=("Segoe UI", 22, "bold"),
    fg=WHITE,
    bg=DARK_BLUE
).pack(pady=(3, 2))

tk.Label(
    header,
    text="Calculate interest and total returns with ease",
    font=("Segoe UI", 10),
    fg="#D4E3EE",
    bg=DARK_BLUE
).pack()


# ================= MAIN CONTENT =================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=15
)


# ================= INPUT CARD =================

card = tk.Frame(
    main,
    bg=WHITE,
    padx=25,
    pady=15,
    highlightbackground=BORDER,
    highlightthickness=1
)

card.pack(fill="x")


tk.Label(
    card,
    text="Enter your details",
    font=("Segoe UI", 17, "bold"),
    bg=WHITE,
    fg=TEXT
).pack(anchor="w", pady=(0, 4))


tk.Label(
    card,
    text="Fill in the values below to calculate simple interest.",
    font=("Segoe UI", 10),
    bg=WHITE,
    fg=MUTED
).pack(anchor="w", pady=(0, 15))


def create_label(text):
    return tk.Label(
        card,
        text=text,
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    )


# Principal
create_label(
    "Principal Amount (₹)"
).pack(anchor="w", pady=(0, 5))

principal_entry = ttk.Entry(
    card,
    style="Modern.TEntry"
)
principal_entry.pack(fill="x")


# Interest Rate
create_label(
    "Annual Interest Rate (%)"
).pack(anchor="w", pady=(10, 5))

rate_entry = ttk.Entry(
    card,
    style="Modern.TEntry"
)
rate_entry.pack(fill="x")


# Time
create_label(
    "Time"
).pack(anchor="w", pady=(10, 5))

time_row = tk.Frame(
    card,
    bg=WHITE
)
time_row.pack(fill="x")

time_entry = ttk.Entry(
    time_row,
    style="Modern.TEntry"
)
time_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)

time_unit = ttk.Combobox(
    time_row,
    style="Modern.TCombobox",
    values=["Years", "Months", "Days"],
    state="readonly",
    width=12
)
time_unit.pack(side="right")
time_unit.current(0)


# ================= RESULT CARD =================

result_card = tk.Frame(
    main,
    bg="#E8F5F2",
    padx=20,
    pady=12,
    highlightbackground="#C9E7DF",
    highlightthickness=1
)

result_card.pack(
    fill="x",
    pady=(12, 0)
)


tk.Label(
    result_card,
    text="YOUR CALCULATION",
    font=("Segoe UI", 10, "bold"),
    bg="#E8F5F2",
    fg=MUTED
).pack(pady=(0, 6))


interest_result = tk.Label(
    result_card,
    text="Simple Interest: ₹0.00",
    font=("Segoe UI", 14, "bold"),
    bg="#E8F5F2",
    fg=GREEN
)
interest_result.pack(pady=4)


amount_result = tk.Label(
    result_card,
    text="Total Amount: ₹0.00",
    font=("Segoe UI", 17, "bold"),
    bg="#E8F5F2",
    fg=DARK_BLUE
)
amount_result.pack(pady=4)


# ================= CALCULATE FUNCTION =================

def calculate_interest():
    try:
        principal_text = principal_entry.get().strip()
        rate_text = rate_entry.get().strip()
        time_text = time_entry.get().strip()

        if not principal_text or not rate_text or not time_text:
            messagebox.showerror(
                "Missing Input",
                "Please fill in all three fields."
            )
            return

        principal = float(principal_text)
        rate = float(rate_text)
        time = float(time_text)

        if principal <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Principal must be greater than zero."
            )
            principal_entry.focus()
            return

        if rate < 0:
            messagebox.showerror(
                "Invalid Input",
                "Interest rate cannot be negative."
            )
            rate_entry.focus()
            return

        if time < 0:
            messagebox.showerror(
                "Invalid Input",
                "Time cannot be negative."
            )
            time_entry.focus()
            return

        # Convert time into years
        unit = time_unit.get()

        if unit == "Months":
            time = time / 12
        elif unit == "Days":
            time = time / 365

        # Simple Interest Formula
        interest = (principal * rate * time) / 100

        total_amount = principal + interest

        # Display results
        interest_result.config(
            text=f"Simple Interest: ₹{interest:,.2f}"
        )

        amount_result.config(
            text=f"Total Amount: ₹{total_amount:,.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in all fields."
        )

    except Exception as error:
        messagebox.showerror(
            "Calculation Error",
            str(error)
        )


# ================= CLEAR FUNCTION =================

def clear_fields():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

    time_unit.current(0)

    interest_result.config(
        text="Simple Interest: ₹0.00"
    )

    amount_result.config(
        text="Total Amount: ₹0.00"
    )

    principal_entry.focus()


# ================= BUTTONS =================

button_frame = tk.Frame(
    main,
    bg=BG
)

button_frame.pack(
    fill="x",
    pady=12
)


calculate_button = tk.Button(
    button_frame,
    text="Calculate Interest",
    command=calculate_interest,
    font=("Segoe UI", 12, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#128A75",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    pady=11,
    bd=0
)

calculate_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 8)
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Segoe UI", 12, "bold"),
    bg="#DFE7ED",
    fg=TEXT,
    activebackground="#CBD6DF",
    relief="flat",
    cursor="hand2",
    pady=11,
    bd=0
)

clear_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(8, 0)
)


# ================= FOOTER =================

tk.Label(
    main,
    text="TOPS Career Center  •  Simple Interest Calculator",
    font=("Segoe UI", 9),
    fg=MUTED,
    bg=BG
).pack(pady=(0, 3))


# ================= KEYBOARD SHORTCUTS =================

root.bind(
    "<Return>",
    lambda event: calculate_interest()
)

root.bind(
    "<Escape>",
    lambda event: clear_fields()
)


# ================= START APPLICATION =================

principal_entry.focus()

root.mainloop()