from os import listdir
from itertools import islice
import matplotlib.pyplot as plt
from statistics import median



def extract_time_stamps(file_name):
   
    # a function that opens a time-stamps.txt file and
    # extracts the time stamp on each line. returns a list.


    time_stamps = []
    with open(file_name, "r") as fname:

        lines = fname.readlines()
        for i in lines:
            time_stamps.append(float(i.replace("\n", " ").replace(",",""))) 

   # print(f"time stamp extraction from {file_name} is done!")

    return time_stamps

def create_graph(points, title):
#    files_path = "time-stamps/"
#
#    files = listdir(files_path)
#    
    output_location = "graphs/"
#    graph_names = [i[0:-16] for i in files]

#    for index, fichier in enumerate(files):
        
#    print(f"now working with {fichier}")

#    timestamps_list = extract_time_stamps(f"{files_path}{fichier}")
#
#    print(f"The time-stamp list is now {timestamps_list}")
    number_of_threads = [i for i in range(4, 66, 2)]
    number_of_threads.insert(0, 1) 
    plt.figure()
    plt.plot(number_of_threads, points, 'go-', color='black', linewidth=2)
    
#    plt.annotate(f" Original  p = {number_of_threads[0]}, execution time = {points[0]}", (number_of_threads[0], points[0]))
    plt.annotate(f" Original  p = {number_of_threads[0]}, execution time = {points[0]}", (number_of_threads[0], points[0]),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=4),
            horizontalalignment='right', verticalalignment='top',
            )

    shortest_time_thread_index = points.index(min(points))
    plt.annotate(f" shortest time  p = {number_of_threads[shortest_time_thread_index]}, execution time = {min(points)}", (number_of_threads[shortest_time_thread_index], min(points)),  xycoords='data',
            xytext=(0.9, 0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=4),
            horizontalalignment='right', verticalalignment='bottom',
            )

#   plt.annotate(f"  p = {number_of_threads[3]}, execution time = {points[3]} , ", (number_of_threads[3], points[3]))
    
    plt.xlabel("p-workers (threads)")
    plt.ylabel("Execution time /ms")
    plt.title(f"{title}")
    plt.savefig(f"{output_location}{title}.png")
     
def median_of_all_time_stamps(path):
    
    LIST_OF_FILES = listdir(path) 
    LIST_OF_TIME_STAMPS_LISTS = [] 
    LIST_OF_MEDIAN_TIME_STAMPS = []

    LIST_OF_ORDERED_TIME_STAMPS = []

    for file in LIST_OF_FILES:
       
        
        TEMP_LIST =  extract_time_stamps(path + file)
        LIST_OF_TIME_STAMPS_LISTS.append(TEMP_LIST)
   
    for TIME_STAMP in range(len(LIST_OF_TIME_STAMPS_LISTS[0])):
        TEMP_TIME_STAMP_LIST = []
        for LIST in LIST_OF_TIME_STAMPS_LISTS:
            TEMP_TIME_STAMP_LIST.append(LIST[TIME_STAMP])
        
        LIST_OF_ORDERED_TIME_STAMPS.append(TEMP_TIME_STAMP_LIST)
    
    for ORDERED_LIST in LIST_OF_ORDERED_TIME_STAMPS:
        LIST_OF_MEDIAN_TIME_STAMPS.append(median(ORDERED_LIST))

    

    return  LIST_OF_MEDIAN_TIME_STAMPS

if __name__ == "__main__":

    path = "time-stamps/"
    
    MEDIAN_TIME_STAMPS = median_of_all_time_stamps(path)
    print(MEDIAN_TIME_STAMPS)
    create_graph(MEDIAN_TIME_STAMPS, "vacation2 Original")

