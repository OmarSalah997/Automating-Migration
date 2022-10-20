import os

userpath = input("Enter path for project artifacts(i.e the src folder path C:/bla/bla/bla): ")
print(userpath)
basepath="/src/main/synapse-config/"
subfolders=["api","endpoints","inbound-endpoints","local-entries","message-processors","message-stores","proxy-services","sequences","tasks","templates"]
def read_text_file(file_path,filename):
    file1 = open(file_path, 'r')
    count = 0
    while True:
        count += 1
    
        # Get next line from file
        line = file1.readline()
        if not line:
            break
        if "<payloadFactory" in line :
            #start searching in payloadfactory body
            count += 1
            line2=file1.readline()
            while "<args"not in line2: #keep searching until you reach <args> tag
                if "$ctx:" in line2:
                    #ctx found inside body and need to be changed
                    print("review file ",filename," as it contains $ctx in a payloadfactory body in line: ",count)
                line2=file1.readline()
                count+=1        
    file1.close()






for subfolderpath in subfolders:
    print("checking folder: ",subfolderpath)
    os.chdir(userpath+basepath+subfolderpath)
# iterate through all files
    for file in os.listdir():
        # Check whether file is in xml format or not
        if file.endswith(".xml"):
            file_path = f"{userpath+basepath+subfolderpath}\{file}"
            # call read text file function
            read_text_file(file_path,file)
    print("done checking folder: ",subfolderpath)
  
  

