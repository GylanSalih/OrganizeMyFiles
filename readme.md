```markdown
# File Sorter

This Python script automatically organizes files in a specified directory (e.g., your Downloads folder) into categorized subfolders based on their file types. The script supports a wide range of file extensions and can handle duplicates, empty folders, and logs its actions.

## Features

- **Automatic File Sorting**: Moves files into categorized folders based on their extensions.
- **Wide File Type Support**: Includes categories like Images, Documents, Videos, Audio, Archives, Coding files, and more.
- **Duplicate Handling**: Renames files if a file with the same name already exists in the destination folder.
- **Empty Folder Cleanup**: Automatically deletes empty folders after sorting.
- **Logging**: Logs all actions (e.g., file moves, errors) into a `file_sorting.log` file.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/file-sorter.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd file-sorter
   ```

3. **Install dependencies** (if any):
   The script requires Python 3.x. No additional Python packages are required.

## Usage

1. Open the script in your preferred text editor.

2. Modify the `download_folder` variable to point to the directory you want to organize:

   ```python
   download_folder = 'C:/Users/YourUsername/Downloads'
   ```

3. Run the script:

   ```bash
   python file_sorter.py
   ```

4. The script will organize files into subfolders within the specified directory based on their file types.

## Customization

You can customize the file types and categories by editing the `file_types` dictionary in the script:

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', ...],
    'Documents': ['.pdf', '.docx', ...],
    ...
}
```

Add or remove extensions as needed to fit your specific requirements.

## Logging

The script creates a `file_sorting.log` file in the project directory, where it logs all actions such as successful file moves, error messages, and deleted empty folders.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```