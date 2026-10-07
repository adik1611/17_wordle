from game import WordleGame


def main():
    print("Wordle")
    print("Choose word length:")
    print("1. 4 letters")
    print("2. 5 letters")
    print("3. 6 letters")

    while True:
        choice = input("Select 1, 2, or 3: ").strip()

        if choice == "1":
            length = 4
            break
        elif choice == "2":
            length = 5
            break
        elif choice == "3":
            length = 6
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

    WordleGame(length).run()


if __name__ == "__main__":
    main()