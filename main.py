import argparse
import sys
import numpy as np

sys.path.append("/c/Users/91949/numpy")

from utils.os_utils import (check_file_status,
                            read_file
                            )
from utils.list_utils import create_lists
from utils.type_utils import convert_all_lines
from utils.numpy_utils import (create_np_arrays,
                            get_whole_data_summary,
                            get_column_summary)
def main():
    print("-------------- 📊 WELCOME TO NUMPY DATA ANALYSIS REPORT -----------")
    parser = argparse.ArgumentParser(description= "help on numpy analyzer")
    parser.add_argument("--input_file",help = "please provide an input csv file",
                         default=r"C:\Users\91949\numpy\assets\numpy_random_numbers.csv")
    parser = parser.parse_args()

    input_file = parser.input_file
    status = check_file_status(input_file)
    if status:
        print("\n------- File is available -------")
    else:
        print("invalid data file..")
    
    lines = read_file(input_file)
    list_lines = create_lists(lines)
    converted_lines = convert_all_lines(list_lines)
    np_arrays = create_np_arrays(converted_lines)

    whole_data = np.array(np_arrays)

    # apply all operations as whole 2D , axis wise 0,1

    print("\nArray Shape:", whole_data.shape)
    print("Total Elements:", whole_data.size)
    get_whole_data_summary(whole_data)
    get_column_summary(whole_data.T)

if __name__=="__main__":
    main()