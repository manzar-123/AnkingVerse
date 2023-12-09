
import pyperclip

def loop_output():
    first_iteration = False  # Flag to track the first iteration
    while True:
        if first_iteration:
            print("Disclaimer: This app is a product of Dr. Manzar Abbas, AKU '022.")
            print("It has been developed independently and is not affiliated with any organization or institution.")
            print("For any queries, feedback, or support related to the app, please feel free to contact Dr. Manzar Abbas via email at manzar.abbas22@alumni.aku.edu.")
            print("Your feedback is valuable and will help improve the app's quality and user experience.")
            print()
            first_iteration = False

        numbers_input = input("Enter multiple numbers separated by commas, and press Enter (or 'q' to quit): ")
        if numbers_input.lower() == 'q':
            break

        numbers_list = numbers_input.split(",")
        numbers = [int(num) for num in numbers_list]

        output = ""
        for num in numbers:
            if num >= 0 and num <= 400000:
                output += f"tag:#AK\_Step1\_v12::#UWorld::{num}"
                output += " OR "
        
        output = output[:-4]
        # Create a window to store the output and copy it to the clipboard
        pyperclip.copy(output)
        print(f"Output copied to clipboard. Paste that in Anki browser window.")
        # return output


loop_output()


