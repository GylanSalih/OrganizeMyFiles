import os
import shutil
import logging

# Path to your download folder (modify this accordingly)
download_folder = 'C:/Users/YourUsername/Downloads'

# Define how files should be sorted
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.tiff', '.ico', '.psd', '.raw', '.heic'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.tex'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.3gp'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso', '.cab'],
    'Coding': ['.json', '.scss', '.css', '.html', '.js', '.py', '.java', '.c', '.cpp', '.php', '.xml', '.sql', '.rb', '.go', '.sh', '.ts', '.md'],
    'Installation Files': ['.msi', '.exe', '.dmg', '.pkg', '.deb', '.rpm', '.app', '.bat', '.sh', '.bin'],
    'E-Books': ['.epub', '.mobi', '.azw', '.azw3', '.djvu', '.ibooks'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fon'],
    'Databases': ['.db', '.sqlite', '.sql', '.mdb', '.accdb'],
    'CAD Files': ['.dwg', '.dxf', '.step', '.stl', '.igs', '.iges'],
    '3D Models': ['.obj', '.fbx', '.dae', '.3ds', '.blend'],
    'Vector Graphics': ['.ai', '.eps', '.svg', '.cdr'],
    'Design Projects': ['.psd', '.ai', '.xd', '.fig', '.sketch'],
    'Saved Web Pages': ['.html', '.htm', '.mhtml', '.webarchive'],
    'Configurations': ['.ini', '.cfg', '.conf', '.yaml', '.yml'],
    'Log Files': ['.log', '.out'],
    'PDF Files': ['.pdf'],  # In case you want to handle PDFs as a separate category
    'Miscellaneous': []  # For file types that do not fit into other categories
}

# Logging configuration
logging.basicConfig(filename='OrganizeMyFiles.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def sort_files():
    try:
        for filename in os.listdir(download_folder):
            file_path = os.path.join(download_folder, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                destination_folder = None
                
                # Determine the destination folder based on the file extension
                for folder, extensions in file_types.items():
                    if file_ext in extensions:
                        destination_folder = os.path.join(download_folder, folder)
                        break

                if destination_folder:
                    # Create the destination folder if it doesn't exist
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    # Check if the file already exists in the destination folder
                    dest_file_path = os.path.join(destination_folder, filename)
                    if os.path.exists(dest_file_path):
                        base_name, ext = os.path.splitext(filename)
                        counter = 1
                        new_filename = f"{base_name}_{counter}{ext}"
                        while os.path.exists(os.path.join(destination_folder, new_filename)):
                            counter += 1
                            new_filename = f"{base_name}_{counter}{ext}"
                        dest_file_path = os.path.join(destination_folder, new_filename)

                    # Move the file to the destination folder
                    shutil.move(file_path, dest_file_path)
                    logging.info(f'Successfully moved: {filename} -> {destination_folder}')

        # Remove empty folders
        remove_empty_folders(download_folder)

    except Exception as e:
        logging.error(f"Error occurred: {e}")


def remove_empty_folders(path):
    # Recursively deletes empty folders
    if not os.path.isdir(path):
        return

    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            remove_empty_folders(folder_path)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                logging.info(f'Removed empty folder: {folder_path}')


if __name__ == "__main__":
    sort_files()
