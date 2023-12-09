import pyperclip
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser

# def display_disclaimer():
#     disclaimer_text = "This app is a product of Dr. Manzar Abbas, founder of SPIE-MedTech.\n" \
#                       "If you like this app, kindly consider buying me a coffee by becoming my patron!\n\n" \
#                       "For any queries, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.\n" \
#                       "Your feedback is valuable and will help improve the app's quality and user experience."

#     def open_website():
#         webbrowser.open("https://www.patreon.com/user/membership?u=94442676")
#         disclaimer_window.destroy()
#         # Add code here to handle the case when the user clicks on "Become a Patron"
#         # For example, you could perform any other desired action after the window is closed.

#     def on_close():
#         disclaimer_window.destroy()
#         choose_version()
#             # Add code here to handle the case when the user closes the window without clicking on "Become a Patron"
#             # For example, you could call the choose_version() function or perform any other desired action.

#     disclaimer_window = tk.Toplevel()
#     disclaimer_window.title("Disclaimer")
#     disclaimer_window.protocol("WM_DELETE_WINDOW", on_close)

#     disclaimer_label = tk.Label(disclaimer_window, text=disclaimer_text, justify="left")
#     disclaimer_label.pack(padx=20, pady=20)

#     patron_button = tk.Button(disclaimer_window, text="Become a Patron", command=open_website)
#     patron_button.pack(pady=10)

#     # Center the window on the screen
#     window_width = 650
#     window_height = 180
#     screen_width = disclaimer_window.winfo_screenwidth()
#     screen_height = disclaimer_window.winfo_screenheight()
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     disclaimer_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


#     disclaimer_window.mainloop()

# def display_disclaimer():
#     disclaimer_text = "This app is a product of Dr. Manzar Abbas, founder of SPIE-MedTech.\n" \
#                       "If you like this app, kindly consider buying me a coffee by becoming my patron!\n\n" \
#                       "For any queries, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.\n" \
#                       "Your feedback is valuable and will help improve the app's quality and user experience."

#     def open_website():
#         webbrowser.open("https://www.patreon.com/user/membership?u=94442676")

#     disclaimer_window = tk.Toplevel()
#     disclaimer_window.title("Disclaimer")

#     disclaimer_label = tk.Label(disclaimer_window, text=disclaimer_text, justify="left")
#     disclaimer_label.pack(padx=20, pady=20)

#     patron_button = tk.Button(disclaimer_window, text="Become a Patron", command=open_website)
#     patron_button.pack(pady=10)

#     disclaimer_window.mainloop()

# Function to display the disclaimer
# def display_disclaimer():
#     messagebox.showinfo("Disclaimer",
#         "This app is a product of Dr. Manzar Abbas, founder of SPIE-MedTech.\n\n"
#         "It has been developed independently and is not affiliated with any organization or institution.\n"
#         "For any queries, feedback, or support related to the app, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.\n"
#         "Your feedback is valuable and will help improve the app's quality and user experience.")

# Function to prompt the user to choose the version
# def choose_version():
#     root = tk.Tk()
#     root.withdraw()
#     version_window = tk.Toplevel(root)
#     version_window.title("Choose Anking Version")
#     version_window.geometry("300x200")  # Set the dimensions of the window
#     version_label = tk.Label(version_window, text="Please choose Anking version:")
#     version_label.pack()
#     version_button_10 = tk.Button(version_window, text="Version 10", command=lambda: select_version(10))
#     version_button_10.pack()
#     version_button_11 = tk.Button(version_window, text="Version 11", command=lambda: select_version(11))
#     version_button_11.pack()
#     version_button_12 = tk.Button(version_window, text="Version 12", command=lambda: select_version(12))
#     version_button_12.pack()    
#     # Center the window on the screen
#     window_width = 300
#     window_height = 200
#     screen_width = version_window.winfo_screenwidth()
#     screen_height = version_window.winfo_screenheight()
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     version_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#     version_window.mainloop()

# def select_version(version):
#     global selected_version
#     selected_version = version
#     step_selection()

# Function to prompt the user to choose between Step 1 and Step 2
# def step_selection():
#     root = tk.Tk()
#     root.withdraw()
#     step_window = tk.Toplevel(root)
#     step_window.title("Choose Step")
#     step_window.geometry("300x200")  # Set the dimensions of the window
#     step_label = tk.Label(step_window, text="Please choose Step:")
#     step_label.pack()
#     step_button_1 = tk.Button(step_window, text="Step 1", command=lambda: select_step(1))
#     step_button_1.pack()
#     step_button_2 = tk.Button(step_window, text="Step 2", command=lambda: select_step(2))
#     step_button_2.pack()
#     # Center the window on the screen
#     window_width = 300
#     window_height = 200
#     screen_width = step_window.winfo_screenwidth()
#     screen_height = step_window.winfo_screenheight()
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     step_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#     step_window.mainloop()

# def select_step(step):
#     global selected_step
#     selected_step = step
#     if selected_step == 1:
#         process_step1(selected_version)
#     elif selected_step == 2:
#         process_step2(selected_version)

version = 12

message = "Relevant Anki Tags are copied to clipboard. You can directly paste them into Anki Browser."
# Function to process step 1
def process_step1():
    # Step 1 logic goes here
    while True:
        numbers_input = simpledialog.askstring(f"Anking version 12",
            "Enter multiple numbers separated by commas (or 'q' to quit):")
        if numbers_input is None or numbers_input.lower() == 'q':
            break

        numbers_list = numbers_input.split(",")
        numbers = [int(num) for num in numbers_list]

        output = ""
        for num in numbers:
            if version == 12:
                if num >= 0 and num <= 400000:
                    output += f"tag:#AK\_Step2\_v12::#UWorld::{num}"
                    output += " OR "

            elif version == 10:
                if num >= 0 and num <= 99:
                    output += f"tag:#AK\_Step1\_v10::#UWorld::0-99::{num}"
                    output += " OR "
                elif num >= 100 and num <= 999:
                    if num >= 100 and num <= 199:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::100-199::{num}"
                    elif num >= 200 and num <= 299:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::200-299::{num}"
                    elif num >= 300 and num <= 399:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::300-399::{num}"
                    elif num >= 400 and num <= 499:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::400-499::{num}"
                    elif num >= 500 and num <= 599:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::500-599::{num}"
                    elif num >= 600 and num <= 699:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::600-699::{num}"
                    elif num >= 700 and num <= 799:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::700-799::{num}"
                    elif num >= 800 and num <= 899:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::800-899::{num}"
                    elif num >= 900 and num <= 999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::100-999::900-999::{num}"
                    output += " OR "
                elif num >= 1000 and num <= 9999:
                    if num >= 1000 and num <= 1999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::1000-1999::{num}"
                    elif num >= 2000 and num <= 2999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::2000-2999::{num}"
                    elif num >= 3000 and num <= 3999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::3000-3999::{num}"
                    elif num >= 4000 and num <= 4999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::4000-4999::{num}"
                    elif num >= 5000 and num <= 5999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::5000-5999::{num}"
                    elif num >= 6000 and num <= 6999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::6000-6999::{num}"
                    elif num >= 7000 and num <= 7999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::7000-7999::{num}"
                    elif num >= 8000 and num <= 8999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::8000-8999::{num}"
                    elif num >= 9000 and num <= 9999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::1000-9999::9000-9999::{num}"
                    output += " OR "
                elif num >= 10000 and num <= 99999:
                    if num >= 10000 and num <= 10999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::10000-10999::{num}"
                    elif num >= 11000 and num <= 11999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::11000-11999::{num}"
                    elif num >= 12000 and num <= 12999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::12000-12999::{num}"
                    elif num >= 13000 and num <= 13999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::13000-13999::{num}"
                    elif num >= 14000 and num <= 14999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::14000-14999::{num}"
                    elif num >= 15000 and num <= 15999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::15000-15999::{num}"
                    elif num >= 16000 and num <= 16999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::16000-16999::{num}"
                    elif num >= 17000 and num <= 17999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::17000-17999::{num}"
                    elif num >= 18000 and num <= 18999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::18000-18999::{num}"
                    elif num >= 19000 and num <= 19999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::19000-19999::{num}"
                    elif num >= 20000 and num <= 20999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::20000-20999::{num}"
                    elif num >= 21000 and num <= 21999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::21000-21999::{num}"
                    elif num >= 22000 and num <= 22999:
                        output += f"tag:#AK\_Step1\_v10::#UWorld::10000-99999::22000-22999::{num}"
                    output += " OR "
            elif version == 11:
                if num >= 0 and num <= 99:
                    output += f"tag:#AK\_Step1\_v11::#UWorld::0-99::{num}"
                    output += " OR "
                elif num >= 100 and num <= 999:
                    if num >= 100 and num <= 199:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::100-199::{num}"
                    elif num >= 200 and num <= 299:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::200-299::{num}"
                    elif num >= 300 and num <= 399:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::300-399::{num}"
                    elif num >= 400 and num <= 499:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::400-499::{num}"
                    elif num >= 500 and num <= 599:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::500-599::{num}"
                    elif num >= 600 and num <= 699:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::600-699::{num}"
                    elif num >= 700 and num <= 799:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::700-799::{num}"
                    elif num >= 800 and num <= 899:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::800-899::{num}"
                    elif num >= 900 and num <= 999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::100-999::900-999::{num}"
                    output += " OR "
                elif num >= 1000 and num <= 9999:
                    if num >= 1000 and num <= 1999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::1000-1999::{num}"
                    elif num >= 2000 and num <= 2999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::2000-2999::{num}"
                    elif num >= 3000 and num <= 3999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::3000-3999::{num}"
                    elif num >= 4000 and num <= 4999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::4000-4999::{num}"
                    elif num >= 5000 and num <= 5999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::5000-5999::{num}"
                    elif num >= 6000 and num <= 6999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::6000-6999::{num}"
                    elif num >= 7000 and num <= 7999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::7000-7999::{num}"
                    elif num >= 8000 and num <= 8999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::8000-8999::{num}"
                    elif num >= 9000 and num <= 9999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::1000-9999::9000-9999::{num}"
                    output += " OR "
                elif num >= 10000 and num <= 99999:
                    if num >= 10000 and num <= 10999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::10000-10999::{num}"
                    elif num >= 11000 and num <= 11999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::11000-11999::{num}"
                    elif num >= 12000 and num <= 12999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::12000-12999::{num}"
                    elif num >= 13000 and num <= 13999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::13000-13999::{num}"
                    elif num >= 14000 and num <= 14999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::14000-14999::{num}"
                    elif num >= 15000 and num <= 15999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::15000-15999::{num}"
                    elif num >= 16000 and num <= 16999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::16000-16999::{num}"
                    elif num >= 17000 and num <= 17999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::17000-17999::{num}"
                    elif num >= 18000 and num <= 18999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::18000-18999::{num}"
                    elif num >= 19000 and num <= 19999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::19000-19999::{num}"
                    elif num >= 20000 and num <= 20999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::20000-20999::{num}"
                    elif num >= 21000 and num <= 21999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::21000-21999::{num}"
                    elif num >= 22000 and num <= 22999:
                        output += f"tag:#AK\_Step1\_v11::#UWorld::10000-99999::22000-22999::{num}"
                    output += " OR "

        output = output[:-4]
        # Create a window to store the output and copy it to the clipboard
        pyperclip.copy(output)

        # Show the output message in a popup window
        messagebox.showinfo("Copied", message)


def process_step2(version):
    # Step 2 logic goes here
    while True:
        numbers_input = simpledialog.askstring(f"Anking version {version}",
            "Enter multiple numbers separated by commas (or 'q' to quit):")
        if numbers_input is None or numbers_input.lower() == 'q':
            break
        numbers_list = numbers_input.split(",")
        numbers = [int(num) for num in numbers_list]
        output = ""

        # Add logic for Step 2 based on the version
        for num in numbers:
            if version == 12:
                if num >= 0 and num <= 400000:
                    output += f"tag:#AK\_Step2\_v12::#UWorld::{num}"
                    output += " OR "
            elif version == 10:
                if num >= 0 and num <= 99:
                    output += f"tag:#AK\_Step2\_v10::#UWorld::0-99::{num}"
                    output += " OR "
                elif num >= 100 and num <= 999:
                    if num >= 100 and num <= 199:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::100-199::{num}"
                    elif num >= 200 and num <= 299:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::200-299::{num}"
                    elif num >= 300 and num <= 399:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::300-399::{num}"
                    elif num >= 400 and num <= 499:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::400-499::{num}"
                    elif num >= 500 and num <= 599:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::500-599::{num}"
                    elif num >= 600 and num <= 699:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::600-699::{num}"
                    elif num >= 700 and num <= 799:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::700-799::{num}"
                    elif num >= 800 and num <= 899:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::800-899::{num}"
                    elif num >= 900 and num <= 999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::100-999::900-999::{num}"
                    output += " OR "
                elif num >= 1000 and num <= 9999:
                    if num >= 1000 and num <= 1999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::1000-1999::{num}"
                    elif num >= 2000 and num <= 2999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::2000-2999::{num}"
                    elif num >= 3000 and num <= 3999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::3000-3999::{num}"
                    elif num >= 4000 and num <= 4999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::4000-4999::{num}"
                    elif num >= 5000 and num <= 5999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::5000-5999::{num}"
                    elif num >= 6000 and num <= 6999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::6000-6999::{num}"
                    elif num >= 7000 and num <= 7999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::7000-7999::{num}"
                    elif num >= 8000 and num <= 8999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::8000-8999::{num}"
                    elif num >= 9000 and num <= 9999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::1000-9999::9000-9999::{num}"
                    output += " OR "
                elif num >= 10000 and num <= 99999:
                    if num >= 10000 and num <= 10999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::10000-10999::{num}"
                    elif num >= 11000 and num <= 11999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::11000-11999::{num}"
                    elif num >= 12000 and num <= 12999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::12000-12999::{num}"
                    elif num >= 13000 and num <= 13999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::13000-13999::{num}"
                    elif num >= 14000 and num <= 14999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::14000-14999::{num}"
                    elif num >= 15000 and num <= 15999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::15000-15999::{num}"
                    elif num >= 16000 and num <= 16999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::16000-16999::{num}"
                    elif num >= 17000 and num <= 17999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::17000-17999::{num}"
                    elif num >= 18000 and num <= 18999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::18000-18999::{num}"
                    elif num >= 19000 and num <= 19999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::19000-19999::{num}"
                    elif num >= 20000 and num <= 20999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::20000-20999::{num}"
                    elif num >= 21000 and num <= 21999:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::21000-21999::{num}"
                    elif num >= 22000:
                        output += f"tag:#AK\_Step2\_v10::#UWorld::10000-99999::22000+::{num}"
                    output += " OR "
            elif version == 11:
                if num >= 0 and num <= 99:
                    output += f"tag:#AK\_Step2\_v11::#UWorld::0-99::{num}"
                    output += " OR "
                elif num >= 100 and num <= 999:
                    if num >= 100 and num <= 199:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::100-199::{num}"
                    elif num >= 200 and num <= 299:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::200-299::{num}"
                    elif num >= 300 and num <= 399:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::300-399::{num}"
                    elif num >= 400 and num <= 499:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::400-499::{num}"
                    elif num >= 500 and num <= 599:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::500-599::{num}"
                    elif num >= 600 and num <= 699:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::600-699::{num}"
                    elif num >= 700 and num <= 799:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::700-799::{num}"
                    elif num >= 800 and num <= 899:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::800-899::{num}"
                    elif num >= 900 and num <= 999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::100-999::900-999::{num}"
                    output += " OR "
                elif num >= 1000 and num <= 9999:
                    if num >= 1000 and num <= 1999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::1000-1999::{num}"
                    elif num >= 2000 and num <= 2999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::2000-2999::{num}"
                    elif num >= 3000 and num <= 3999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::3000-3999::{num}"
                    elif num >= 4000 and num <= 4999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::4000-4999::{num}"
                    elif num >= 5000 and num <= 5999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::5000-5999::{num}"
                    elif num >= 6000 and num <= 6999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::6000-6999::{num}"
                    elif num >= 7000 and num <= 7999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::7000-7999::{num}"
                    elif num >= 8000 and num <= 8999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::8000-8999::{num}"
                    elif num >= 9000 and num <= 9999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::1000-9999::9000-9999::{num}"
                    output += " OR "
                elif num >= 10000 and num <= 99999:
                    if num >= 10000 and num <= 10999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::10000-10999::{num}"
                    elif num >= 11000 and num <= 11999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::11000-11999::{num}"
                    elif num >= 12000 and num <= 12999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::12000-12999::{num}"
                    elif num >= 13000 and num <= 13999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::13000-13999::{num}"
                    elif num >= 14000 and num <= 14999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::14000-14999::{num}"
                    elif num >= 15000 and num <= 15999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::15000-15999::{num}"
                    elif num >= 16000 and num <= 16999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::16000-16999::{num}"
                    elif num >= 17000 and num <= 17999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::17000-17999::{num}"
                    elif num >= 18000 and num <= 18999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::18000-18999::{num}"
                    elif num >= 19000 and num <= 19999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::19000-19999::{num}"
                    elif num >= 20000 and num <= 20999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::20000-20999::{num}"
                    elif num >= 21000 and num <= 21999:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::21000-21999::{num}"
                    elif num >= 22000:
                        output += f"tag:#AK\_Step2\_v11::#UWorld::10000-99999::22000+::{num}"
                    output += " OR "

        output = output[:-4]
        # Create a window to store the output and copy it to the clipboard
        pyperclip.copy(output)

        # Show the output message in a popup window
        messagebox.showinfo("Copied", message)


# Display the disclaimer


# Prompt the user to choose the version
# choose_version()
process_step1()