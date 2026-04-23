latest_results = []

def save_results(data):
    global latest_results
    latest_results = data

def get_results():
    return latest_results