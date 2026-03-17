logs = []

def save_log(log, result):
    logs.append({
        "log": log,
        "result": result
    })

def get_logs():
    return logs