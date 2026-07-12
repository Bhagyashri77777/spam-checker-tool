# SpamShield - Simple Spam Message Detector
# Created by: Bhagyashri Yogesh Gawali

def check_spam(message):
    """Check if a message contains spam keywords"""
    bad_words = ["lottery", "urgent", "otp", "free money", "click link", "password", "scam", "winner"]
    msg_lower = message.lower()
    
    spam_score = 0
    for word in bad_words:
        if word in msg_lower:
            spam_score += 1
    
    if spam_score >= 2:
        return "DANGER! 🚨 This looks like a spam message!"
    elif spam_score == 1:
        return "BE CAREFUL! ⚠️ It has some suspicious words."
    else:
        return "SAFE! ✅ No spam words found."


def main():
    print("=" * 45)
    print("          SpamShield - Spam Detector")
    print("=" * 45)
    print("Created by: Bhagyashri Yogesh Gawali\n")

    while True:
        print("\n--- Main Menu ---")
        print("1. Check a message for spam")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            message = input("\nEnter the message: ")
            result = check_spam(message)
            print(f"\nResult: {result}")

        elif choice == '2':
            print("\nExiting... Stay safe! ✨")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()