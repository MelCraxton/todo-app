import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


# Check to see all is working
# if __name__ == "__main__":
#     extract_archive(r'C:\Users\melis\PycharmProjects\python\file_extract\compressed.zip',
#                     dest_dir=r'\Users\melis\PycharmProjects\python\file_extract\files')
#
