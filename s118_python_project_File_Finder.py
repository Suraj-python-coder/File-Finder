# project info:we are creating programe which is automatically create
#              folders according to files available in folder and save the files in it
#              according to its extensions.

import os,shutil

# NOTE: you can write every single extension inside tuples
dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document_extension' : ('.doc','.pdf','.txt'),
    'images_extension' :('.jpg'),
}


folderpath = input('enter the folder path :')  # folder path on which you want to work

def file_finder(folder_path,file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extensions
    if file.endswith(extension) ]

# print(file_finder(folderpath, video_extension))


# ****** this is old code ,in which there is a problem which create empty folders, which is solved bellow ********************
# for extension_type, extension_tuple in dict_extensions.items():  
#     folder_name = extension_type.split('_')[0] + 'Files' 
#     folder_path = os.path.join(folderpath, folder_name)  
#     os.mkdir(folder_path)  # here we create folder
# ****************************************************************************************************

for extension_type, extension_tuple in dict_extensions.items():    # here we apply loop on our dictionary
    if len(file_finder(folderpath,extension_tuple)) > 0:        # this is the improvement in code which is not create empty folder
        folder_name = extension_type.split('_')[0] + 'Files'  # here we create folder name
        folder_path = os.path.join(folderpath, folder_name)   # here we create folder path
        os.mkdir(folder_path)  # here we create folder

    for item in file_finder(folderpath,extension_tuple):     # here we call file_finder function
        item_path = os.path.join(folderpath,item)   # here we join user entered folder path with item and become item path where it present
        item_new_path = os.path.join(folder_path,item) # here we join create folder path with item and it gives items new path
        shutil.move(item_path,item_new_path)  # here we move item in their extension wise in folder,
                #(path of item which we want to move,path of folder where we want to move our item ) 
   
    # print('calling file finder')
    # print(file_finder(folderpath,extension_tuple))   
