import os

if os.path.exists('NoEducation.txt'):
    try:
        with open('NoEducatio.txt','r') as file:
            for line in file:
                print(line)
    except:
        print("Error")
else:
    print("No file")
    

    