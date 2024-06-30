import os

def main_menu():
    print("Select an option:")
    print("1. Scrape Data")
    print("2. Generate Heatmap")
    print("3. Generate Recording Statistics")
    print("4. Filter Recordings")
    print("5. Download Recordings")
    print("6. Create Spectrograms")
    print("7. Train and Save Model")
    print("8. Exit")

def execute_script(script_name):
    command = f"python {script_name}.py"
    os.system(command)

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            execute_script('src/scrape')
        elif choice == '2':
            execute_script('src/heatmap')
        elif choice == '3':
            execute_script('src/recordingstats')
        elif choice == '4':
            execute_script('src/filter')
        elif choice == '5':
            execute_script('src/downloadrecordings')
        elif choice == '6':
            execute_script('src/converttospectrogram')
        elif choice == '7':
            execute_script('src/trainandsave')
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
