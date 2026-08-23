# Python File Organizer

A simple Python file organizer that automatically sorts files into different folders based on their file extensions.

## Features

* Organizes Python files into a `Codes` folder
* Organizes images (`.png`, `.jpg`) into an `Images` folder
* Organizes text and Markdown files (`.txt`, `.md`) into a `Doc` folder
* Automatically creates the required folders if they don't already exist
* Uses file paths so the organizer can be used with different folders

## How to Use

1. Download or clone this repository.
2. Open `file_organizer.py`.
3. Replace:

```python
file_path = "Write Folder path here"
```

with the path of the folder you want to organize.

Example:

```python
file_path = "C:\\Users\\YourName\\Desktop\\test"
```

4. Run the Python script.

The program will create:

```text
Codes/
Images/
Doc/
```

and move the appropriate files into each folder.

## Example

Before:

```text
test/
├── app.py
├── photo.png
├── notes.txt
└── README.md
```

After:

```text
test/
├── Codes/
│   └── app.py
├── Images/
│   └── photo.png
└── Doc/
    ├── notes.txt
    └── README.md
```

## Requirements

* Python 3
* No external packages are required.

The project uses Python's built-in `os` and `shutil` modules.

## What I Learned

This project helped me practice:

* Working with files and directories
* `os.listdir()`
* `os.path.join()`
* `os.path.splitext()`
* `os.makedirs()`
* `shutil.move()`
* `for` loops
* `if / elif / else`
* File extensions and paths
