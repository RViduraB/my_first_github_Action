import os
from datetime import datetime
from my_info import Me as personal



def generate_log():
    # current time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    log_message = f"[{current_time}] Automated Task executed successfully!\n"

    
    with open("log_report.txt", "a", encoding="utf-8") as file:
        file.write(log_message)
        
    print(f"Log added: {log_message}")






if __name__ == "__main__":
    me = personal()
    me.run()
    generate_log()
