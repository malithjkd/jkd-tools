# capture image using libcamera-still

from capture_image import capture_image
from check_for_human import check_for_human
#from send_file_to_storage import send_to_network_storage, send_files_to_gs

import datetime
import time
import os

from google.cloud import storage


def capture_and_process(bucket):
    '''Capturing image and identify pricens of people on the image, if there is any person save the image to network storage'''
    # capture image
    file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    full_file_path = "/home/malithjkd/Documents/data/" + file_name
    capture_image(full_file_path)
    time.sleep(0.5)  # Add a delay to ensure the file is saved before processing
    person_detected = check_for_human(full_file_path)
    if person_detected:
        # Send the file to network storage
        remote_host = "192.168.3.30"
        remote_user = "malithjkd"
        remote_password = "R&Dtest_mj"
        remote_directory = "/home/malithjkd/Documents/image_data/"
        
        #send_to_network_storage(full_filename, remote_host, remote_user, remote_password, remote_directory)
        # send the file to google storage
        blob = bucket.blob(file_name)
        blob.upload_from_filename(full_file_path)

    else:
        #remove the file from local storage
        os.remove(full_file_path)

    # Add the filename to the log file
    with open("/home/malithjkd/Documents/data/log.txt", "a+") as log_file:
        log_file.write(full_file_path +"\t" + str(person_detected) + "\n")
        log_file.flush()

    return person_detected


def main():
    '''run capture_and_process function every 5 seconds until timer finish'''
    time_now = datetime.datetime.now()
    #end_time = time(2024, 11, 22, 8, 30, 00)
    end_time = time_now + datetime.timedelta(minutes=3)
    #end_time  = time_now + datetime.timedelta(days=10)
    person_detected = False

    # send the file to google storage
    client = storage.Client()
    bucket_name = "malith_storage_basket"
    bucket = client.get_bucket(bucket_name)

    while datetime.datetime.now() < end_time:
        person_detected = capture_and_process(bucket)
        if person_detected:
            time.sleep(30)  # Adjust the sleep time as needed
        else:
            time.sleep(6)


if __name__ == "__main__":
    main()
