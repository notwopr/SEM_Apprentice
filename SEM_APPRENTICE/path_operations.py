"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
class PathOperations:
    # create pathstring from list of path elements
    def create_path_string(self, list_of_path_elements):
        if all(map(lambda x: isinstance(x, str), list_of_path_elements)):
            return '/'.join(list_of_path_elements)
        else:
            raise ValueError("All pathnames must be strings.")