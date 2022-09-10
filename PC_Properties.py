print('''Hello,You Can Use This Script To Check Your Internet Speed,RAM Usage,Available Battery etc..''')
user_input=int(input('Enter Your Choice Of Operation.\n1.Internet_Speedtest\n2.RAM Usage\n3.Available Battery\n4.Available DISK Space\n5.System Information\n6.Virtual Memory\n'))


# Python code to test the internet speed
def speedtest():
	import speedtest
	st = speedtest.Speedtest()
	if(user_input==1):
		option = int(input('''What speed do you want to test?\n1.Download Speed\n2.Upload Speed\n'''))
		if option == 1:
			return f'Your Download Speed Is {st.download()/(1000000)} Mbps'
		elif option == 2:
			return f'Your Upload Speed Is {st.upload()/(1000000)} Mbps'
		else:
			return f'Enter The Correct Choice:( From The Options Provided In The Menu'

#Python code to check RAM Usage
def ram_usage():
	import psutil
	import winsound
	
	"""windound a have a handy Beep API, you can even choose the duration and the frequency of the beep. 
	   This is how you generate a 400z sound that lasts 5000 milliseconds:"""
	
	"""The function psutil.virutal_memory()  returns a named tuple about system memory usage.  
	The third field in tuple represents the percentage use of the memory(RAM). 
	It is calculated by (total – available)/total * 100 . 

	The total fields in the output of function are:
		total: total memory excluding swap
		available: available memory for processes
		percent: memory usage in per cent
		used: the memory used
		free: memory not used at and is readily available"""

	x=psutil.virtual_memory()[2] 	# Getting % usage of virtual_memory (3rd field)
	if(x>=85): #Warns Us If Our RAM Usage Is More Than 85% (here),We Don't Want Our PC To Crash:)
		winsound.Beep(400,5000)
	return f'RAM Memory Used:{x}'

#Python code to check available battery in Your PC
def available_battery():
	import psutil
	"""sensors_battery() function gives battery status information named as a tuple """
	return psutil.sensors_battery()	

#Python Code To Check DISK Usage 
def available_disk_space():
	import psutil
	"""disk_usage('PATH') This function gives disk usage statistics as a tuple for a given path. 
	Total, used and free space are expressed in bytes, along with the percentage usage."""
	if(user_input==4):
		PATH_SPECIFIED=input('Enter The PATH Of The DISK To Check For Available DISK Space.\n')
		disk_info={}
		x=psutil.disk_usage(PATH_SPECIFIED)
		print('Note: Space Shown Is In GigaBytes:)')
		disk_info={'Total Space:':x[0]/(1024*1024*1024),'Used Space:':x[1]/(1024*1024*1024),'Free space':x[2]/(1024*1024*1024)}
	return disk_info


def system_info():
	import subprocess
	#Traverse the ipconfig information
	data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')

	# Arrange the bytes data
	for item in data:
		print(item.split('\r')[:-1])


def virtual_memory():
	"""Virtual Memory is a storage mechanism which offers user an illusion of having a very big main memory. 
	   It is done by treating a part of secondary memory as the main memory. 
	   In Virtual memory, the user can store processes with a bigger size than the available main memory.
       Therefore, instead of loading one long process in the main memory, the OS loads the various parts of more than one process in the main memory. 
       Virtual memory is mostly implemented with demand paging and demand segmentation.

       Virtual Memory is a memory management technique that is implemented using both hardware and software. 
	   It is also a feature of an Operating System (OS) that allows a computer to compensate for shortages of physical memory by temporarily transferring pages of data from Random Access Memory (RAM) to Hard disk storage.
	   The process is known as Paging or Swapping and the temporary storage space on the hard disk is called a Page file or a swap file.
		"""
	
	import psutil
	x=psutil.virtual_memory()
	print('Space is shown in Gigabytes:)')
	virtual_mem_info={}
	virtual_mem_info={'Total Space':x[0]/(1024*1024*1024),'Available Space':x[1]/(1024*1024*1024),'Used Sapce':x[3]/(1024*1024*1024),'Free space':x[4]/(1024*1024*1024)}
	return virtual_mem_info

def operation(user_input):
	if(user_input==1):
		return speedtest()
	elif(user_input==2):
		return ram_usage()
	elif(user_input==3):
		return available_battery()	
	elif(user_input==4):
		return available_disk_space()
	elif(user_input==5):
		return system_info()
	else:
		return virtual_memory()


print(operation(user_input))



