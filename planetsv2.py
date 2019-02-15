# Planets

fMERCURY = .38
fVENUS =  .91
fMOON = .165
fMARS = .38
fJUPITER = 2.34
fSATURN = .93
fURANUS = .92
fNEPTUNE = 1.12
fPLUTO = .066


# input
sName = input("What is your name: ")
fWeight = float(input("what is your weight: "))


# compute

fSpaceWeight1 = fWeight * fMERCURY
fSpaceWeight2 = fWeight * fVENUS
fSpaceWeight3 = fWeight * fMOON
fSpaceWeight4 = fWeight * fMARS
fSpaceWeight5 = fWeight * fJUPITER
fSpaceWeight6 = fWeight * fSATURN
fSpaceWeight7 = fWeight * fURANUS
fSpaceWeight8 = fWeight * fNEPTUNE
fSpaceWeight9 = fWeight * fPLUTO

# Output


print("Here are your weights on our Solar System's Planets: ")
print("Weight on Mercury: ", format(fSpaceWeight1, '10.2f'))
print("Weight on Venus:   ", format(fSpaceWeight2, '10.2f'))
print("Weight on the Moon:", format(fSpaceWeight3, '10.2f'))
print("Weight on Mars:    ", format(fSpaceWeight4, '10.2f'))
print("Weight on Jupiter: ", format(fSpaceWeight5, '10.2f'))
print("Weight on Saturn:  ", format(fSpaceWeight6, '10.2f'))
print("Weight on Uranus:  ", format(fSpaceWeight7, '10.2f'))
print("Weight on Neptune: ", format(fSpaceWeight8, '10.2f'))
print("Weight on Pluto:   ", format(fSpaceWeight9, '10.2f'))


