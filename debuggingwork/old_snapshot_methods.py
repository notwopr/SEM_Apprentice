# import mss
import win32gui
import win32ui
import win32con
# import win32api
# import dxcam
# from machine_operations import MachineOperations
# from PIL import Image

class SnapShotMethods:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    # def mss_snap_save(self, path_to_img):
    #     sct = mss.mss()

    #     # Capture the screen
    #     monitor = {"top": 0, "left": 0, "width": self.screen_width, "height": self.screen_height}
    #     screenshot = sct.grab(monitor)

    #     # Save the screenshot to a file
    #     mss.tools.to_png(screenshot.rgb, screenshot.size, output=path_to_img)

    #     # Release the screen capture context
    #     sct.close()

    def win32_snap_save(self, path_to_img):
        hwnd = None

        # get image data and save to bmp
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.screen_width, self.screen_height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.screen_width, self.screen_height) , dcObj, (0,0), win32con.SRCCOPY)

        # save to bitmap
        dataBitMap.SaveBitmapFile(cDC, path_to_img)
    
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

    # def win32_snap_save_v2(self, path_to_img):
    #     # get the primary display's device context
    #     hwin = win32gui.GetDesktopWindow()
    #     hwindc = win32gui.GetWindowDC(hwin)
    #     srcdc = win32ui.CreateDCFromHandle(hwindc)
        
    #     # create a compatible memory device context where the screenshot will be stored
    #     memdc = srcdc.CreateCompatibleDC()
    #     width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    #     height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    #     bmp = win32ui.CreateBitmap()
    #     bmp.CreateCompatibleBitmap(srcdc, width, height)
    #     memdc.SelectObject(bmp)
        
    #     # copy the screen into the memory device context
    #     memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)
        
    #     # save the screenshot to the given file path
    #     bmp.SaveBitmapFile(memdc, path_to_img)
        
    #     # free up resources
    #     memdc.DeleteDC()
    #     win32gui.ReleaseDC(hwin, hwindc)
    #     win32gui.DeleteObject(bmp.GetHandle())

    # def win32_snap_save_v3(self, save_path):
    #     # Grab a handle to the main desktop window
    #     hdesktop = win32gui.GetDesktopWindow()

    #     # Create a device context
    #     desktop_dc = win32gui.GetWindowDC(hdesktop)
    #     img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    #     # Create a memory-based device context
    #     mem_dc = img_dc.CreateCompatibleDC()

    #     # Create a bitmap object
    #     screenshot = win32ui.CreateBitmap()
    #     screenshot.CreateCompatibleBitmap(img_dc, self.screen_width, self.screen_height)
    #     mem_dc.SelectObject(screenshot)

    #     # Copy the screen to the memory-based device context
    #     mem_dc.BitBlt((0, 0), (self.screen_width, self.screen_height), img_dc, (0, 0), win32con.SRCCOPY)

    #     # Save the bitmap to a file
    #     screenshot.SaveBitmapFile(mem_dc, save_path)

    #     # Clean up
    #     mem_dc.DeleteDC()
    #     win32gui.DeleteObject(screenshot.GetHandle())
    #     img_dc.DeleteDC()
    #     win32gui.ReleaseDC(hdesktop, desktop_dc)

    # def dxcamnumpy_snap_save(self, path_to_img):
    #     camera = dxcam.create()
    #     screenshot = camera.grab()
    #     if screenshot is not None:
    #         MachineOperations().savetopkl(path_to_img[:-4]+".pkl", screenshot)
            
    # def dxcam_snap_save(self, path_to_img):
    #     camera = dxcam.create()
    #     screenshot = camera.grab()
    #     if screenshot is not None:
    #         # Convert the numpy array to a Pillow image object
    #         image = Image.fromarray(screenshot)
    #         # Save the image as a PNG file to disk
    #         image.save(path_to_img)
