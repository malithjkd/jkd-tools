# capture image using libcamera-still

from capture_image import capture_image
from check_for_human import check_for_human
from send_file_to_storage import send_to_network_storage

import datetime
import time
import os

def capture_and_process():
    '''Capturing image and identify pricens of people on the image, if there is any person save the image to network storage'''
    # capture image
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    full_filename = "/home/malithjkd/Documents/data/" + filename
    capture_image(full_filename)
    time.sleep(1)  # Add a delay to ensure the file is saved before processing
    person_detected = check_for_human(full_filename)
    if person_detected:
        # Send the file to network storage
        remote_host = "192.168.3.30"
        remote_user = "malithjkd"
        remote_password = "R&Dtest_mj"
        remote_directory = "/home/malithjkd/Documents/image_data/"
        send_to_network_storage(full_filename, remote_host, remote_user, remote_password, remote_directory)
    else:
        #remove the file from local storage
        os.remove(full_filename)

    # Add the filename to the log file
    with open("/home/malithjkd/Documents/data/log.txt", "a+") as log_file:
        log_file.write(full_filename +"\t" + str(person_detected) + "\n")
        log_file.flush()
    
    return person_detected


def main():
    '''run capture_and_process function every 5 seconds until timer finish'''
    time_now = datetime.datetime.now()
    #end_time = time(2024, 11, 22, 8, 30, 00)
    end_time = time_now + datetime.timedelta(minutes=90)
    #end_time  = time_now + datetime.timedelta(days=10)
    person_detected = False

    while datetime.datetime.now() < end_time:
        person_detected = capture_and_process()
        if person_detected:
            time.sleep(3)  # Adjust the sleep time as needed
        else:
            time.sleep(6)


if __name__ == "__main__":
    main()
