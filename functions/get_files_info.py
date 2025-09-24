import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_work_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
    if not abs_full_path.startswith(abs_work_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f"Error: {e}"
    files = os.listdir(full_path)
    result = ""
    for file in files:
        file_path = os.path.join(full_path, file)
        result += f"- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}\n"
    return result.rstrip()
