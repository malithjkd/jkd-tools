# capture image using libcamera-still

from capture_image import capture_image

import datetime
import time


log = [] # List to store the image file names


def capture_and_process():
    '''Capturing image and identify pricens of people on the image, if there is any person save the image to network storage'''
    
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    full_filename = "data/" + filename

    #image_lcoation = capture_image(full_filename)
    
    log.append(full_filename)

    # Save log to a text file
    with open("data/log.txt", "a") as log_file:
        for entry in log:
            log_file.write(entry + "\n")



def main():
    '''run capture_and_process function every 5 seconds until timer finish'''
    time_now = datetime.datetime.now()
    end_time = time_now + datetime.timedelta(hours=2)
    #end_time  = time_now + datetime.timedelta(days=10)
    
    while datetime.datetime.now() < end_time:
        capture_and_process()
        time.sleep(5)  # Adjust the sleep time as needed



if __name__ == "__main__":
    main()
