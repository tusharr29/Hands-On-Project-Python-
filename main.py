import os

def arrange_file(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    # pass
    for i, files in enumerate (files_with_ext):
        os.rename(files, f"photo-{i+1}{ext}")

if __name__ == "__main__":
    files = os.listdir()
    arrange_file(files, ".jpg")
