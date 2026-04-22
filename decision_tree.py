def get_valid_input(prompt, options):
    while True:
        ans = input(prompt).lower()
        if ans in options:
            return ans
        print("Invalid input. Try again.")

def reflection():
    day = get_valid_input("How was your day? (good/average/bad): ", ["good","average","bad"])

    if day == "good":
        task = get_valid_input("Completed tasks? (yes/no): ", ["yes","no"])
        if task == "yes":
            print("Excellent! Maintain consistency and try new challenges.")
        else:
            print("Plan tomorrow with 3 priority tasks.")

    elif day == "average":
        reason = get_valid_input("Main issue? (energy/distractions/planning): ", ["energy","distractions","planning"])
        print("Suggestion based on your input.")

    elif day == "bad":
        reason = get_valid_input("Main reason? (stress/work/personal): ", ["stress","work","personal"])
        print("Take care and improve step by step.")

reflection()