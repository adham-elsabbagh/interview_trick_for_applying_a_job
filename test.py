pwdList = ["Ib#", "Blo", "F09", "Hkf", "Ev!", "K%2", "Awe", "Cve", "Lee", "J61", "Gvc", "Dde"]
skillList = ["Git", "Django", "Flask", "Ansible", "CI"]
pythonExperience,curiosity=0,0
for skill in skillList:
    my_skill = input("YOUR SKILL !")
    if skill in skillList == my_skill :
        pythonExperience += 1
    else:
        curiosity += 1
if pythonExperience + curiosity > 4:
    pwdList.sort()
    thePassword = ""
    for i in range(0, 5):

        thePassword += pwdList[i][1:]

    print("Give this password to Nathalie our HR manager: " + thePassword)