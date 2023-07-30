import os

# Function to read the notepad file and extract names
def read_notepad(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Function to get a list of .mp4 files in the same directory
def get_mp4_files():
    return [file for file in os.listdir('.') if file.lower().endswith('.mp4')]

# Find the notepad file in the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
notepad_filename = None
for file in os.listdir(script_directory):
    if file.lower().endswith('.txt'):
        notepad_filename = file
        break

# Check if notepad file exists
if notepad_filename is None:
    print("Error: Notepad file (.txt) not found in the script directory.")
else:
    # Read the notepad file
    notepad_names = read_notepad(notepad_filename)

    # Fetch the .mp4 files in the same directory
    mp4_files = get_mp4_files()

    # Check if the number of names in notepad and files match
    if len(notepad_names) != len(mp4_files):
        print("Error: The number of names in the notepad and files do not match.")
    else:
        # Rename files
        for filename in mp4_files:
            number = int(filename.split('lesson')[1].split('.mp4')[0])
            if 1 <= number <= len(notepad_names):
                name = notepad_names[number - 1]
                split_name = ' '.join(name.split(' ', 1)[1:])
                new_name = f"{number}. {split_name}.mp4"

                try:
                    os.rename(filename, new_name)
                    print(f"Renamed '{filename}' to '{new_name}'.")
                except FileNotFoundError:
                    print(f"Error: File '{filename}' not found.")
                except FileExistsError:
                    print(f"Error: File '{new_name}' already exists.")
            else:
                print(f"Error: Notepad name not found for file '{filename}'.")
