functionsToSkip = []

with open("example1") as file:
    counter=0
    for line in file:
        if ("SubFolder=\"" in line):
            splittedLine=line.split("\"")
            subfolder=splittedLine[1]
        if ("FileName=\"" in line):
            splittedLine = line.split("\"")
            FileName = splittedLine[1]
        if ("StartLine=" in line):
            line=line.strip()
            splittedLine = line.split("StartLine=")
            StartLine = int(splittedLine[1])
        if ("EndLine=" in line):
            line=line.strip()
            splittedLine = line.split("EndLine=")
            EndLine = int(splittedLine[1])
            less = ""
            if (EndLine-StartLine+1)<15:
                less="less "
                functionsToSkip.append(counter)
                print("Function "+str(counter)+": "+subfolder+","+FileName+","+
                  str(StartLine)+","+str(EndLine)+ " has "+less+"than 15 lines.")
            counter+=1

with open("example2") as file: # Try to understand this function
    lineCount=0
    skip=False
    functionCount=0
    for line in file:
        lineCount+=1
        if lineCount==3 and 0 in functionsToSkip:
            skip=True
        if skip and line !="\n":
            continue
        if skip and line =="\n":
            skip=False
            startline_of_bc = lineCount # the startline can be obtained here
            functionCount+=1
            continue
        elif line=="\n":
            functionCount+=1
            endline_of_bc = lineCount # the endline of bc

        if (functionCount!=0 and functionCount in functionsToSkip):
            skip=True
            continue

        print(line.strip())

        # Write CSV for finding the substitute startline and endline

        # Produce 1 CSV file in the script
        ## 1. Information of the Javafile
        ## 2. Information of the bc file
        ### use it to compare it with the result from NiCad and exchange the information based on the created CSV (need another script)

        # example entry:
        # subfolder, javafilename, startline, endline, startline bc, endline bc, bc filename, subfolder bc
        # try to figure out how to get the startline and endline of the bc file