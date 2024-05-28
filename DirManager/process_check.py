from psutil import process_iter

def process_check(process_name: str) -> bool:
    for process in process_iter(['name']):
        if process.info['name'] == process_name:
            return True
        
    return False