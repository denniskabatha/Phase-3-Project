from flashcard import add_card, view_cards, delete_card, update_card, get_progress

def display_menu():
    print("\nWelcome to the Flashcard Generator!")
    print("1. Add new card")
    print("2. Review cards")
    print("3. Manage cards")
    print("4. View progress")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def add_new_card():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    add_card(question, answer)
    print("Flashcard added successfully!")

def review_cards():
    cards = view_cards()
    if not cards:
        print("No cards available to review.")
        return

    for card in cards:
        print(f"Question: {card[1]}")
        input("(Press Enter to reveal the answer)")
        print(f"Answer: {card[2]}")
        result = input("Did you get it right? (Y/N): ").strip().upper()
        if result == 'Y':
            print("Great job! Card marked as correct.")
            

def view_progress():
    total, correct = get_progress()
    print(f"Total cards: {total}")
    print(f"Correct answers: {correct}")
    if total > 0:
        progress = (correct / total) * 100
        print(f"Progress: {progress:.2f}%")
    else:
        print("No cards available.")

def manage_cards():
    cards = view_cards()
    if not cards:
        print("No cards available to manage.")
        return

    for card in cards:
        print(f"ID: {card[0]}, Question: {card[1]}")

    card_id = int(input("Enter the ID of the card to delete or update (0 to cancel): "))
    if card_id == 0:
        return
    action = input("Do you want to (D)elete or (U)pdate this card? (D/U): ").strip().upper()
    if action == 'D':
        delete_card(card_id)
        print("Card deleted successfully.")
    elif action == 'U':
        question = input("Enter the new question: ")
        answer = input("Enter the new answer: ")
        update_card(card_id, question, answer)
        print("Card updated successfully.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_new_card()
        elif choice == '2':
            review_cards()
        elif choice == '3':
            manage_cards()
        elif choice == '4':
            view_progress()
        elif choice == '5':
            print("Thank you for using the Flashcard Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
