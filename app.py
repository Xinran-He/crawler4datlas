import os
from bs4 import BeautifulSoup


def get_file_path(fn_folder_path):
    fn_ls_file_name = os.listdir(fn_folder_path)  # read all files from selected folder
    fn_ls_file_path = []
    for i in fn_ls_file_name:
        fn_file_path = fn_folder_path + "\\" + i  # add full path of folder before file names
        fn_ls_file_path.append(fn_file_path)
    return fn_ls_file_path


folder_path = input("Please input folder path:")
ls_file_path = get_file_path(folder_path)

for file_path in ls_file_path:
    web = open(file_path, "r", encoding='UTF-8')  # open the file with read-only mode and an encoding method
    try:
        web_str = web.read()
        web_soup = BeautifulSoup(web_str, 'html.parser')
        ls_data_table = web_soup.find_all("tr", "art-table-row first even")  # find first row of two tables
        table_count = 0
        for data_table in ls_data_table:  # for each table in table list do:
            ls_item_attribute_soup = data_table.find_next_siblings("tr")  # find all other sibling rows below first row
            ls_item_attribute = []
            for item_attribute in ls_item_attribute_soup:
                final_output = file_path+", "+"{}".format(table_count)+", "+item_attribute.get_text(", ")
                print(final_output)
            table_count += 1

    finally:
        web.close()  # use try-finally to close file when any error occurs
