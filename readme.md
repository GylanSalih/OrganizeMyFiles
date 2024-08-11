# My Project

<p align="center">
    ![s-l1200_upscayl_1x_ultrasharp](https://github.com/user-attachments/assets/c52cb648-c19d-4368-89c1-13ddba2327ae)
</p>




<a id="readme-top"></a>

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>

<!-- Badges Shields -->
[contributors-shield]: https://custom-icon-badges.demolab.com/github/contributors/GylanSalih/OrganizeMyFiles?color=FF0000&logo=group&label=Contributors&logoColor=white&style=for-the-badge&labelColor=000000
[forks-shield]: https://custom-icon-badges.demolab.com/github/forks/GylanSalih/OrganizeMyFiles?color=FF0000&logo=repo-forked&label=Forks&logoColor=white&style=for-the-badge&labelColor=000000
[stars-shield]: https://custom-icon-badges.demolab.com/github/stars/GylanSalih/OrganizeMyFiles?color=FF0000&label=Stars&style=for-the-badge&logo=star&logoColor=white&labelColor=000000
[issues-shield]: https://custom-icon-badges.demolab.com/github/issues/GylanSalih/OrganizeMyFiles?color=FF0000&logo=issue-opened&label=Issues&logoColor=white&labelColor=000000&style=for-the-badge&
[license-shield]: https://custom-icon-badges.demolab.com/github/license/GylanSalih/OrganizeMyFiles?color=FF0000&logo=law&label=License&logoColor=white&style=for-the-badge&labelColor=000000

<!-- Badges Links -->
[contributors-url]: https://github.com/GylanSalih/OrganizeMyFiles/graphs/contributors
[forks-url]: https://github.com/GylanSalih/OrganizeMyFiles/network/members
[stars-url]: https://github.com/GylanSalih/OrganizeMyFiles/stargazers
[issues-url]: https://github.com/GylanSalih/OrganizeMyFiles/issues
[license-url]: https://github.com/GylanSalih/OrganizeMyFiles/blob/main/LICENSE

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
   git clone https://github.com/GylanSalih/OrganizeMyFiles
   ```

2. **Navigate to the project directory**:

   ```bash
   cd OrganizeMyFiles
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
   python OrganizeMyFiles.py
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

The script creates a `OrganizeMyFiles.log` file in the project directory, where it logs all actions such as successful file moves, error messages, and deleted empty folders.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
