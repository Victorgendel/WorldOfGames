import subprocess
import platform
import signal

flask_process = None  # Initialize a variable to store the Flask process

def start_flask_server():
    global flask_process  # Use the global variable

    system = platform.system()

    if system == "Linux":
        command = ["python", "main_score.py"]
        flask_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif system == "Windows":
        command = ["pythonw", "main_score.py"]
        flask_process = subprocess.Popen(command, shell=True)

def stop_flask_server():
    global flask_process

    if flask_process:
        flask_process.terminate()
        flask_process.wait()

if __name__ == "__main__":
    start_flask_server()
    print("Flask app started in the background.")

    try:
        input("Press Enter to stop the Flask app...")
    except KeyboardInterrupt:
        pass

    stop_flask_server()
    print("Flask app stopped.")