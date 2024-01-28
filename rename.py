import os

def read_notepad(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_mp4_files():
    return [file for file in os.listdir('.') if file.lower().endswith('.mp4')]

script_directory = os.path.dirname(os.path.abspath(__file__))
notepad_filename = None

for file in os.listdir(script_directory):
    if file.lower().endswith('.txt'):
        notepad_filename = file
        break

if notepad_filename is None:
    print("Error: Notepad file (.txt) not found in the script directory.")
else:
    notepad_names = read_notepad(notepad_filename)
    mp4_files = get_mp4_files()

    if len(notepad_names) != len(mp4_files):
        print("Error: The number of names in the notepad and files do not match.")
    else:
        for filename in mp4_files:
            try:
                # Extract number from filename
                number = int(filename.split('lesson')[1].split('.mp4')[0])
                if 1 <= number <= len(notepad_names):
                    name = notepad_names[number - 1].strip()
                    # Replace spaces and slashes with underscores, and remove parentheses
                    new_name = f"{number}. {name.replace(' ', '_').replace('/', '-').replace('(','').replace(')','')}.mp4"

                    os.rename(filename, new_name)
                    print(f"Renamed '{filename}' to '{new_name}'.")
                else:
                    print(f"Error: Notepad name not found for file '{filename}'.")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
            except FileExistsError:
                print(f"Error: File '{new_name}' already exists.")
