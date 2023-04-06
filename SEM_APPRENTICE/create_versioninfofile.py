import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version="2.4.0.0",
    company_name="Anudha Mittal and David Choi",
    file_description="SEM Apprentice",
    legal_copyright="© 2023 Anudha Mittal and David Choi. All rights reserved.",
    original_filename="SEM_Apprentice.exe",
    product_name="SEM Apprentice",
    translations=[0x0409, 1200],
)