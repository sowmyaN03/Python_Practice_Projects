import os, shutil
path = r"D:\Downloads"
file_name = os.listdir(path)
os.path.exists(path + '\\' +  'csv files')
folder_names = ['csv files', 'image files', 'text files', 'pdf files', 'word files', 'excel files', 'powerpoint files', 'audio files', 'video files', 'compressed files', 'programming files', 'other files']
for folder in folder_names:
    if not os.path.exists(path + '\\' + folder):
        os.mkdir(path + '\\' + folder)
for file in file_name:
    if ".csv" in file:
        shutil.move(path + '\\' + file, path + '\\csv files')
    elif ".jpg" in file or ".jpeg" in file or ".png" in file or ".gif" in file or ".bmp" in file or ".tiff" in file:
        shutil.move(path + '\\' + file, path + '\\image files')
    elif ".txt" in file or ".rtf" in file:
        shutil.move(path + '\\' + file, path + '\\text files')
    elif ".pdf" in file:
        shutil.move(path + '\\' + file, path + '\\pdf files')
    elif ".docx" in file:
        shutil.move(path + '\\' + file, path + '\\word files')
    elif ".xlsx" in file:
        shutil.move(path + '\\' + file, path + '\\excel files')
    elif ".pptx" in file:
        shutil.move(path + '\\' + file, path + '\\powerpoint files')
    elif ".mp3" in file or ".wav" in file or ".aac" in file or ".flac" in file:
        shutil.move(path + '\\' + file, path + '\\audio files')
    elif ".mp4" in file or ".mkv" in file or ".avi" in file or ".mov" in file or ".wmv" in file:
        shutil.move(path + '\\' + file, path + '\\video files')
    elif ".zip" in file or ".rar" in file or ".7z" in file or ".tar" in file or ".gz" in file:
        shutil.move(path + '\\' + file, path + '\\compressed files')
    elif ".py" in file or ".java" in file or ".c" in file or ".cpp" in file or ".js" in file or ".html" in file or ".css" in file:
        shutil.move(path + '\\' + file, path + '\\programming files')
    else:
        shutil.move(path + '\\' + file, path + '\\other files')