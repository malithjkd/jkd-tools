# /rpi-cam/send_file_to_storage.py

import paramiko
from scp import SCPClient
import os

def send_to_network_storage(local_file_path, remote_host, remote_user, remote_password, remote_directory):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote host
        ssh.connect(remote_host, username=remote_user, password=remote_password)
        
        # Create an SCP client
        with SCPClient(ssh.get_transport()) as scp:
            # Copy the file to the remote directory
            scp.put(local_file_path, remote_path=remote_directory)
        
        print(f"File {local_file_path} successfully copied to {remote_host}:{remote_directory}")
    except Exception as e:
        print(f"Error occurred while copying file: {e}")
    finally:
        # Close the SSH connection
        ssh.close()

# Example usage
#local_file_path = "/home/malithjkd/Documents/data/2024-11-22-07-23-17.jpg"
base_dir = "/home/malithjkd/Documents/"
remote_host = "192.168.3.30"
remote_user = "malithjkd"
remote_password = "R&Dtest_mj"
remote_directory = "/home/malithjkd/Documents/image_data/"

# send all the files in the log file to the network storage
log_file_path = "/home/malithjkd/Documents/data/log.txt"

with open(log_file_path, "r") as log_file:
    for line in log_file:
        local_file_path = line.strip()
        local_file_path = base_dir + local_file_path
        # check if the file exists
        if not os.path.exists(local_file_path):
            print(f"File {local_file_path} does not exist")
        else:
            print(f"Sending file: {local_file_path}")
            send_to_network_storage(local_file_path, remote_host, remote_user, remote_password, remote_directory)
            #deleate file from local storage
            os.remove(local_file_path)
    # Clear the log file after processing all entries
    open(log_file_path, "w").close()
