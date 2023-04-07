import pyinstaller_versionfile
import os

pyinstaller_versionfile.create_versionfile(
    output_file=os.path.join(os.path.dirname(__file__), "versionfile.txt"),
    version="2.5.0.0",
    company_name="Anudha Mittal and David Choi",
    file_description="SEM Apprentice",
    legal_copyright="© 2023 Anudha Mittal and David Choi. All rights reserved.",
    original_filename="SEM_Apprentice.exe",
    product_name="SEM Apprentice",
    translations=[0x0409, 1200],
)