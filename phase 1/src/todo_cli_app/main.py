"""
Main CLI layer for the Todo CLI App
Handles user input/output and presents information to the user
"""
from .controller import Controller


def main():
    """
    Main entry point for the Todo CLI App
    Implements the CLI loop that handles user input/output
    """
    print("Welcome to the Todo CLI App!")
    print("Enter commands (type 'help' for options, 'exit' to quit).")

    controller = Controller()

    while True:
        try:
            # Display prompt and get user input
            command = input("\n> ").strip()

            # Process the command through the controller
            success, response = controller.process_command(command)

            # Handle exit specially
            if response == "exit":
                print("Goodbye!")
                break

            # Print the response from the controller
            if success:
                print(response)
            else:
                print(f"Error: {response}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nReceived interrupt signal. Goodbye!")
            break
        except EOFError:
            # Handle Ctrl+D (or similar) gracefully
            print("\n\nEnd of input received. Goodbye!")
            break


if __name__ == "__main__":
    main()