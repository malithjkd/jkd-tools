# capture image using libcamera-still

from capture_image import capture_image

import datetime
import time




def capture_and_process():
    '''Capturing image and identify pricens of people on the image, if there is any person save the image to network storage'''
    
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    image_lcoation = capture_image(filename)
    log = [] 
    log.append(filename)








def main():
    '''run capture_and_process function every 5 seconds until timer finish'''
    time_now = datetime.datetime.now()
    end_time = time_now + datetime.timedelta(seconds=10)
    #end_time  = time_now + datetime.timedelta(days=10)


    while datetime.datetime.now() < end_time:
        capture_and_process()
        time.sleep(5)  # Adjust the sleep time as needed


if __name__ == "__main__":
    main()
