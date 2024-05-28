import os

def get_oldest_dir(dst_dir: str) -> str:
    files = os.listdir(dst_dir)

    directories = []
    for file in files:
        path = os.path.join(dst_dir, file)
        if os.path.isdir(path):
            directories.append(path)
    
    if not directories:
        return None

    oldest_dir = min(directories, key=os.path.getctime)
    return oldest_dir