import pyperclip
import os

def step2_output(version):
    first_iteration = True  # Flag to track the first iteration
    while True:
        if first_iteration:
            print("Disclaimer: This app is a product of Dr. Manzar Abbas, AKU '022.")
            print("It has been developed independently and is not affiliated with any organization or institution.")
            print("For any queries, feedback, or support related to the app, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.")
            print("Your feedback is valuable and will help improve the app's quality and user experience.")
            print()
            first_iteration = False

        numbers_input = input(f"Enter multiple numbers separated by commas, and press Enter (or 'q' to quit) for Anking version {version}: ")

        if numbers_input.lower() == 'q':
            break

        numbers_list = numbers_input.split(",")
        numbers = [int(num) for num in numbers_list]

        output = ""

        for num in numbers:
            if version == 10:
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

        print(f"Output copied to clipboard:\n{output}\n")



def loop_output(version):
    first_iteration = True  # Flag to track the first iteration
    while True:
        if first_iteration:
            print("Disclaimer: This app is a product of Dr. Manzar Abbas, AKU '022.")
            print("It has been developed independently and is not affiliated with any organization or institution.")
            print("For any queries, feedback, or support related to the app, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.")
            print("Your feedback is valuable and will help improve the app's quality and user experience.")
            print()
            first_iteration = False

        numbers_input = input(f"Enter multiple numbers separated by commas, and press Enter (or 'q' to quit) for Anking version {version}: ")

        if numbers_input.lower() == 'q':
            break

        numbers_list = numbers_input.split(",")
        numbers = [int(num) for num in numbers_list]

        output = ""
        for num in numbers:
            if version == 10:
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

        print(f"Output copied to clipboard:\n{output}\n")




step = int(input("Enter the desired step (1 or 2): "))
version = int(input("Enter the desired Anking version (10 or 11): "))

if version == 10 or version == 11:
    if step == 1:
        loop_output(version)
    elif step == 2:
        step2_output(version)
    else:
        print("Invalid step entered. Please enter either 1 or 2.")
else:
    print("Invalid version entered. Please enter either 10 or 11.")

