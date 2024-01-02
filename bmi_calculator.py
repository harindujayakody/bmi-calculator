import os
import platform
import time
import pyfiglet

def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 16.9:
        return "Underweight"
    elif 17 <= bmi < 18.4:
        return "Mildly underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal (healthy) weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class 1 (Moderate)"
    elif 35 <= bmi < 39.9:
        return "Obesity Class 2 (Severe)"
    else:
        return "Obesity Class 3 (Very Severe)"

def styled_text(text, style):
    # Dracula theme ANSI escape codes
    dracula_theme = {
        "reset": "\033[0m",
        "purple_text": "\033[0;35m",
        "green_text": "\033[0;32m",
        "yellow_text": "\033[0;33m",
        "blue_text": "\033[0;34m",
        "purple_bg": "\033[0;45m",
        "blue_bg": "\033[0;44m",
    }
    
    return f"{dracula_theme[style]}{text}{dracula_theme['reset']}"

def custom_heading(text):
    custom_figlet = pyfiglet.Figlet()
    return custom_figlet.renderText(text)

def main():
    while True:
        # Clear the terminal screen
        clear_screen()

        # Display styled hero section with Dracula theme
        heading = custom_heading("BMI Calculator")
        print(styled_text(heading, "purple_text"))
        print(f"Made with ❤️ by {styled_text('Harindu Jayakody', 'green_text')}")
        print(f"GitHub: {styled_text('https://github.com/harindujayakody/bmi-calculator', 'blue_text')}\n")

        weight_kg = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        
        height_m = height_cm / 100  # Convert height from centimeters to meters

        bmi = calculate_bmi(weight_kg, height_m)
        interpretation = interpret_bmi(bmi)

        print(f"Your BMI is: {styled_text(f'{bmi:.2f}', 'yellow_text')}")
        print(f"This is categorized as: {styled_text(interpretation, 'purple_bg')}\n")

        choice = input("Enter 'r' to run again or 'q' to quit: ")
        if choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()