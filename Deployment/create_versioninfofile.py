"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="./SEM_APPRENTICE/versionfile.txt",
    version="2.5.0.0",
    company_name="Anudha Mittal and David Choi",
    file_description="SEM Apprentice",
    legal_copyright="© 2023 Anudha Mittal and David Choi. All rights reserved.",
    original_filename="SEM_Apprentice.exe",
    product_name="SEM Apprentice",
    translations=[0x0409, 1200],
)