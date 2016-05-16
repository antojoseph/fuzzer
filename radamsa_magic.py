import os 
def open_file_and_return_bite_array(path):
    with open(path, "rb") as sampleFile:
        f = sampleFile.read()
        b = bytearray(f)

    return b

def radamsa_do(sample_path,extension,num_sample):

	for x in range(0,int(num_sample)):
	#radamsa source.jpg -o output.jpg
		result = os.system("bin/radamsa "+sample_path+" -o generated_samples_folder/sample"+str(x)+extension)
		print result

def start():
    # sample_path = raw_input("Provide path to a sample file :")
    # only for testing, uncomment in prod
    sample_path = "mutation_sample/img.jpg"
    num_sample = raw_input("Provide the number of Samples to be Generated : ")
    # make threading dynamic , for now sticking to 4 threads
    # number_of_threads = raw_input("Number of Threads to be used :")
    extension = os.path.splitext(sample_path)[1]
    radamsa_do(sample_path,extension,num_sample)