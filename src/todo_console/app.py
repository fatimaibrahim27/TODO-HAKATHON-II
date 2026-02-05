"""
Main application module for the Todo Console App
Using only Python standard library components
"""
from .commands import CommandProcessor


def main():
    """
    Main entry point for the Todo Console App
    """
    print("Welcome to the Todo Console App!")
    print("Type 'help' for available commands, or 'exit' to quit.")

    processor = CommandProcessor()

    while True:
        try:
            # Display prompt and get user input
            command = input("\n> ").strip()

            # Process the command
            success, response = processor.process_command(command)

            # Handle exit specially
            if response == "exit":
                print("Goodbye!")
                break

            # Print the response
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