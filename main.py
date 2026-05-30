import json
import random
from datetime import datetime

# Load tips and quotes
def load_data():
    with open("tips.json", "r") as file:
        return json.load(file)

# Save output
def save_output(message):
    with open("output.txt", "a") as file:
        file.write(message + "\n")

# Display menu
def menu():
    print("\n========== SMART STUDENT ASSISTANT ==========")
    print("1. Get Study Tip")
    print("2. Get Motivation Quote")
    print("3. Show Current Date & Time")
    print("4. Daily Study Planner")
    print("5. View Saved History")
    print("6. Exit")
    print("============================================")

# Main Program
data = load_data()

name = input("Enter your name: ").title()

print(f"\n👋 Welcome {name}!")
print("Your AI-powered study companion is ready.")

save_output(f"\nSession Started by {name}")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = random.choice(data["tips"])
        print(f"\n📚 Study Tip: {tip}")
        save_output(f"Study Tip: {tip}")

    elif choice == "2":
        quote = random.choice(data["quotes"])
        print(f"\n💡 Motivation Quote: {quote}")
        save_output(f"Motivation Quote: {quote}")

    elif choice == "3":
        current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        print(f"\n🕒 Current Date & Time: {current}")
        save_output(f"Date & Time: {current}")

    elif choice == "4":
        subjects = input("\nEnter subjects separated by commas: ")
        subject_list = subjects.split(",")

        print("\n📖 Today's Study Plan:")
        for i, subject in enumerate(subject_list, start=1):
            print(f"{i}. {subject.strip()} - 1 Hour")

        save_output("Generated Study Plan")
        for subject in subject_list:
            save_output(subject.strip())

    elif choice == "5":
        print("\n📂 Saved History:")
        try:
            with open("output.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No history found.")

    elif choice == "6":
        print(f"\n🎉 Thank you, {name}! Keep Learning.")
        save_output("Program Closed")
        break

    else:
        print("❌ Invalid Choice! Please try again.")