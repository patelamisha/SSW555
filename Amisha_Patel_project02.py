tag = ["HEAD", "NOTE", "TRLR", "FAM", "INDI","NAME", "SEX", "BIRT", "DEAT", 
        "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
valid = ["Y" , "N"]   
fname = "Amisha_Patel_Project02.ged"
file = open(fname, encoding='utf-8-sig')
for line in file:
        print("-->" + line.strip())
        line = (line.rstrip()).split(' ')
        valid = "N"
        if line[0] == "0":
            if line[1] in tag:
                valid = "Y"
        if line[0] == "1":
            if line[1] in tag:
                valid = "Y"
        if line[0] == "2":
            if line[1] == "DATE":
                valid = "Y"
        print("<-- " + line[0] + " | " + line[1] + " | " + valid + " | ", end = ' ')
        num = 2
        for val in (line[2:]):
            print(line[num], end = ' ')
            num = num + 1
        print()