import os
import matplotlib.pyplot as plt



def extract_time_stamps(file_name):
   
    # a function that opens a time-stamps.txt file and
    # extracts the time stamp on each line. returns a list.


    time_stamps = []
    with open(file_name, "r") as fname:

        lines = fname.readlines()
        for i in lines:
            time_stamps.append(i.replace("\n", " ").replace(",","")) 

   # print(f"time stamp extraction from {file_name} is done!")

    return time_stamps


if __name__ == "main":


    files_path = "time-stamps/"

    files = listdir(files_path)
    
    output_location = "graphs/"
    graph_names = (i[0:-16] for i in files)

    for index, fichier in enumerate(files):
        
        print(f"now working with {fichier}")
        timestamps_list = extract_time_stamps(f"{files_path}{fichier}")
        plt.plot(timestamps_list) 
        plt.xlabel("p-workers (threads)")
        plt.ylabel("Execution time /ms")
        plt.title(f"{graph_names[index]}")
        plt.savefig(f"{output_location}{graph_names[index]}.png")
    

