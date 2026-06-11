# ------------------------------------------------------------
# Smart File Organiser
#
# This program scans a folder and organises files into
# Images, Documents, Videos, and Others based on their
# file extensions.
#
# Steps:
# 1. Check if the folder exists.
# 2. Scan all files (skip subfolders).
# 3. Create category folders if needed.
# 4. Move files into the correct folder.
# 5. Display a summary of files organised.
#
# Modules used:
# - pathlib : Handle file and folder paths
# - os      : Create folders
# - shutil  : Move files
# ------------------------------------------------------------


import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Others": []  
}


def get_category(extension: str) -> str:
    """
    Determine category based on file extension.
    """
    extension = extension.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organise_folder(folder_path: str) -> dict:
    """
    Scan folder, move files into category folders,
    and return summary dictionary.
    """

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return {}

    summary = {category: 0 for category in CATEGORIES}

    print(f"\nOrganising: {folder_path}")
    print("-" * 35)

    for item in folder.iterdir():

        if item.is_dir():
            continue

        category = get_category(item.suffix)

        destination_folder = folder / category
        os.makedirs(destination_folder, exist_ok=True)

        destination_file = destination_folder / item.name

        shutil.move(str(item), str(destination_file))

        summary[category] += 1

        print(f"Moved {item.name:<15} -> {category}/")

    return summary


def print_report(summary: dict) -> None:
    """
    Print formatted report.
    """

    if not summary:
        return

    print("-" * 35)
    print("Summary:")

    total = 0

    for category, count in summary.items():
        print(f"  {category:<10}: {count} files")
        total += count

    print(f"Total: {total} files organised.")


folder_path = input("Enter folder path: ")

summary = organise_folder(folder_path)
print_report(summary)