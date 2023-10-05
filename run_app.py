import subprocess
import platform

flask_process = None  # Initialize a variable to store the Flask process

def start_flask_server():
    global flask_process  # Use the global variable

    system = platform.system()
    script_name = "app.py"  # Replace with the correct script name if needed

    try:
        if system == "Linux":
            command = ["python", script_name]
            flask_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif system == "Windows":
            # Use "start" to run the script in a separate window
            command = ["start", "python", script_name]
            flask_process = subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
        flask_process = None

def stop_flask_server():
    global flask_process

    if flask_process:
        try:
            system = platform.system()
            if system == "Windows":
                # Use the taskkill command to forcefully terminate the Flask app
                subprocess.run(["taskkill", "/F", "/im", "python.exe"], check=True)
            else:
                flask_process.terminate()
                flask_process.wait()
        except Exception as e:
            print(f"Error stopping Flask app: {e}")

if __name__ == "__main__":
    # if flask_process:
    #     print("Flask app started in the background.")

        try:
            input("Press Enter to stop the Flask app...")
        except KeyboardInterrupt:
            pass

        stop_flask_server()
        print("Flask app stopped.")
    # else:
    #     print("Flask app was not started due to errors.")
#