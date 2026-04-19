import os 
import csv
from datetime import datetime

def log_chat(session_id: str, query: str, response: str):
    log_file = "chat_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file,"a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp","session_id","query","response"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            session_id,
            query,
            response,
            ])