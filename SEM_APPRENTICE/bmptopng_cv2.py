import cv2
import os

def bmp_to_png_cv(source, destination):
    # Load BMP file
    bmp_image = cv2.imread(source)
    # Save as PNG
    cv2.imwrite(destination, bmp_image, [int(cv2.IMWRITE_PNG_STRATEGY), int(cv2.IMWRITE_PNG_STRATEGY_DEFAULT)])
    # remove original BMP
    os.remove(source)

def check_queue_for_bmp(queue):
    """
    Continuously check the queue for BMP filepaths and convert them to PNG
    """
    while True:
        try:
            bmp_path = queue.get()
        except:
            # Handle any errors that might occur during image conversion
            pass
        else:
            if bmp_path == "STOP RECORDING":
                break
            png_path = os.path.splitext(bmp_path)[0] + '.png'
            bmp_to_png_cv(bmp_path, png_path)
            queue.task_done()