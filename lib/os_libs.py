
def check_mkdirs(dir:str):
    import os
    
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        pass
    
def send_line_notification(message:str):
    import os, requests
    
    now_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(now_dir, "../config/config.ini")

    from configparser import ConfigParser
    
    config = ConfigParser()
    config.read(config_dir)
    token = config.get("LINE_NOTIFICATION", "token")

    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"message" : message}
        response = requests.post(url, headers=headers, data=data)
        return response
    
    except Exception as e:
        print(f"Exception Appeared - {e}")

def send_line_notification_thread(message:str):
    from threading import Thread
    
    thread = Thread(target=send_line_notification, args=(message,))
    thread.start()
