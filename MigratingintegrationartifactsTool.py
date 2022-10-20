import os

userpath = input("Enter path for project artifacts(i.e the src folder path C:/bla/bla/bla): ")
print(userpath)
basepath="/src/main/synapse-config/"
subfolders=["api","endpoints","inbound-endpoints","local-entries","message-processors","message-stores","proxy-services","sequences","tasks","templates"]
def read_text_file(file_path):
    file1 = open(file_path, 'r')
    count = 0
    while True:
        count += 1
    
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            break
        if "<payloadFactory" in line :
            count += 1
            line2=file1.readline()
            while "<args"not in line2:
                if "$ctx:" in line2:
                    print("review file ",file_path," as it contains $ctx in a payloadfactory body in line: ",count)
                line2=file1.readline()
                count+=1
    file1.close()






for subfolderpath in subfolders:
    print("checking folder: ",subfolderpath)
    os.chdir(userpath+basepath+subfolderpath)
# iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".xml"):
            file_path = f"{userpath+basepath+subfolderpath}\{file}"
            # call read text file function
            read_text_file(file_path)
   
  
  

