from shutil import copyfile
from sys import exit
import csv

#### const

folders = ["Chroma_CQT", "Chroma_STFT", "CQT", "MFCC", "MFCC_DELTA", "STFT"]

source_pre_folder = "..\\5secWith50paOverlapping\\"
target_pre_folder = "..\\MLdata\\"
tail = ".jpg"
csv_path = "30s_500ms_valence_cont_average.csv"

def folder_choose(value):
	ts_folder = "\\" + str(round(value, 1))
	if ts_folder == "\\-0.0":
		ts_folder = "\\0.0"

	return ts_folder


def folder_classify(folder):
	csvFile = open(csv_path, "r")
	reader = csv.reader(csvFile)

	data = []
	list_id = 0

	for item in reader:
	    data.append([])
	    data[list_id].append(item[0])
	    for i in range(1,len(item)-6,5):
	        Tlist = (item[i:i+10])
	        for j in range(len(Tlist)):
	            Tlist[j] = float(Tlist[j])
	        Tsum = 0
	        Tsum = float(sum(Tlist))/10
	        data[list_id].append(Tsum)    
	    list_id += 1
	csvFile.close()

	for i in data:
	    song_id = i[0]
	    count = 0
	    g = len(i) - 1
	    for j in i:
	        if count == 0:
	            count += 1
	            continue
	        if count == g :
	            continue
	        else:    
	            class_folder = folder_choose(float(j))
	            file_name = str(song_id) + "_" + str(count)

	            count += 1       
	        source_path = source_pre_folder  + '\\' + folder + '\\' + file_name + tail
	        target_path = target_pre_folder +'\\' + folder + '\\' + "V\\RAW" + class_folder + '\\' + file_name + tail
	        copyfile(source_path, target_path)

for temp in folders:
	folder_classify(temp)