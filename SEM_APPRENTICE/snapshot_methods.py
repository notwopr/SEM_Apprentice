import win32gui
import win32ui
import win32con


class SnapShotMethods:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hwnd = None
        self.wDC = None
        self.dcObj = None
        self.cDC = None
        self.dataBitMap = None

    def win32_snap_save(self, path_to_img):
        if self.hwnd is None:
            self.hwnd = win32gui.GetDesktopWindow()

        # get image data and save to bmp
        if self.wDC is None:
            self.wDC = win32gui.GetWindowDC(self.hwnd)
        if self.dcObj is None:
            self.dcObj = win32ui.CreateDCFromHandle(self.wDC)
        if self.cDC is None:
            self.cDC = self.dcObj.CreateCompatibleDC()
        if self.dataBitMap is None:
            self.dataBitMap = win32ui.CreateBitmap()
            self.dataBitMap.CreateCompatibleBitmap(self.dcObj, self.screen_width, self.screen_height)

        self.cDC.SelectObject(self.dataBitMap)
        self.cDC.BitBlt((0,0),(self.screen_width, self.screen_height), self.dcObj, (0,0), win32con.SRCCOPY)

        # save to bitmap
        self.dataBitMap.SaveBitmapFile(self.cDC, path_to_img)

    def __del__(self):
        if self.dataBitMap is not None:
            win32gui.DeleteObject(self.dataBitMap.GetHandle())
        if self.cDC is not None:
            self.cDC.DeleteDC()
        if self.dcObj is not None:
            self.dcObj.DeleteDC()
        if self.wDC is not None:
            win32gui.ReleaseDC(self.hwnd, self.wDC)