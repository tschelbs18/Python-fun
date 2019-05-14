import os
import pandas as pd

# Build an Excel Directory of All the Files and Folders Housed at the Directory Selected
# Output Excel will be built one level higher than the specified directory


######## CHANGE THE TARGET DIR AND XLSX FILE HERE ##########
path = r'C:\Users\tschelb\Desktop\Harvest'
excel_file_name = 'File_Directory.xlsx'
############################################################

def build_file_index(path):
    print("Processing File Path")
    file_index_df = pd.DataFrame(columns =['Full Path','Type','Name','Description'])

    for root, dirs, files in os.walk(path):
        for name in files:
            file_index_df = file_index_df.append({'Full Path':os.path.join(root,name),'Type':'File','Name':name},ignore_index=True)
        for name in dirs:
            file_index_df = file_index_df.append({'Full Path':os.path.join(root,name),'Type':'Folder','Name':name},ignore_index=True)

    print("Building Excel File")
    file_index_df.to_excel(os.path.join(os.path.dirname(path),excel_file_name))


if __name__ == '__main__':
    build_file_index(path)
    print("Complete!")
