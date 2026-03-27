# A simple utility to check if a message contains spam words
print("--- Welcome to the Neural Knights Spam Checker ---")

while True:
    print("\n--- Main Menu ---")
    print("1. Check a message for spam")
    print("2. Exit the tool")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == '1':
        msg = input("Enter the message here: ")
        # Make the message lowercase so it's easier to check
        msg_lower = msg.lower() 
        
        # Our simple list of bad words
        bad_words = ["lottery", "urgent", "otp", "free money", "click link", "password", "scam", "winner"]
        
        # Count how many bad words are in the message
        spam_score = 0
        for word in bad_words:
            if word in msg_lower:
                spam_score = spam_score + 1
                
        # Give the result based on the score
        if spam_score >= 2:
            print("Result: DANGER! 🚨 This looks like a spam message!")
        elif spam_score == 1:
            print("Result: BE CAREFUL! ⚠️ It has some suspicious words.")
        else:
            print("Result: SAFE! ✅ No spam words found.")
            
    elif choice == '2':
        print("Bye! Exiting the tool...")
        print("Stay safe! ✨ - Built by Code_WithShri07")
        break
        
    else:
        print("Wrong choice. Please enter 1 or 2.")
