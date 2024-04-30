import os

def create_folders_recursively(root_folder, folders):
    # Create root folder if it doesn't exist
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    # Iterate through each folder in the list
    for folder_info in folders:
        folder_name = folder_info["name"]
        folder_path = os.path.join(root_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Check if the folder has subfolders
        if "sub_folders" in folder_info:
            sub_folders = folder_info["sub_folders"]
            create_folders_recursively(folder_path, sub_folders)

if __name__ == "__main__":
    folders = [
        {
            "name": "bigbang",
            "sub_folders": [
                {
                    "name": "tools",
                    "sub_folders": [
                        {
                            "name": "scripts"
                        }
                    ]
                },
                {
                    "name": "docker"
                },
                {
                    "name": "repos"
                },
                {
                    "name": "assets"
                },
                {
                    "name": "github"
                },
            ]
        }
    ]

    root_folder = input("Enter the path where you want to create the folder structure: ")
    create_folders_recursively(root_folder, folders)
    print("Template folders created successfully!")

