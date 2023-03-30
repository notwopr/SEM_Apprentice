import win32com.client as wc
import pythoncom
from win32com.client import constants as win32com_client_constants
from getallclsidsofwindowscodecsdll import get_clsids

def get_wic_factory():
    try_CLSIDs = get_clsids()
    for CLSID in try_CLSIDs:
        # progID = pythoncom.ProgIDFromCLSID(CLSID)
        # print(f"progID: {progID}")
        try:
            progID = pythoncom.ProgIDFromCLSID(CLSID)
            print(f"progID: {progID}")
            # factory = wc.Dispatch(progID)
            # return factory.QueryInterface(win32com_client_constants.IID_IWICImagingFactory)
        except:
            pass
    raise Exception("Failed to create WIC imaging factory.")

print(get_wic_factory())