# /rpi-cam/send_file_to_storage.py

import paramiko
from scp import SCPClient

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
local_file_path = "/path/to/local/file.jpg"
remote_host = "192.168.3.30"
remote_user = "malithjkd"
remote_password = "R&Dtest_mj"
remote_directory = "/path/to/remote/directory"

send_to_network_storage(local_file_path, remote_host, remote_user, remote_password, remote_directory)
