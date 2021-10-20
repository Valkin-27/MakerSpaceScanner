import time
import sys
import os

#11 = admin
#10 = space captain
#01 = general user
#Admin = {}
#global SpaceCaptain = {}
#global GeneralUser = {}

class access_codes:
  def __init__(self, id):
    self.name = ""
    self.info = id

class user:
  def __init__(self, id):
    self.name = ""
    self.number = ""
    self.userID = id
    self.access = ""

def main():
  GettingID = True
  while(GettingID):
    os.system('clear')
    print('For Testing: \n   Admin code = 11.01, \n   Space Captain Code = 10.01, \n   General User code = 01.01')
    print('[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]')
    print('[=-=-=-=-=-=-=-=Hello=-=-=-=-=-=-=-=]')
    print('[=-=-=Please Scan Card to Start=-=-=]')
    print('[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]')
    GettingID = options_selections()
  if(current_user.access == "Admin"):
    adminMain()
  elif(current_user.access == "SpaceCaptain"):  
    spaceCaptainMain()
  elif(current_user.access == "GeneralUser"):  
    generalUser_Main()
    
  main()

def options_selections():
  global current_user
  id = str(input("(Type Code)---> "))
  current_user = user(id)
  
  if(id in A_data.info):
    current_user.name = A_data.info[current_user.userID][0]
    current_user.number = A_data.info[current_user.userID][1]
    current_user.access = "Admin"
    return False
  elif(id in SC_data.info):
    current_user.name = SC_data.info[current_user.userID][0]
    current_user.number = SC_data.info[current_user.userID][1]
    current_user.access = "SpaceCaptain"
    return False
  elif(id in G_data.info):
    current_user.name = G_data.info[current_user.userID][0]
    current_user.number = G_data.info[current_user.userID][1]
    current_user.access = "GeneralUser"
    return False
    
  invalid()
  return True

def adminMain():
  os.system('clear')
  print("Welcome, %s(%s)" %(current_user.name, current_user.access))
  print("Number: %s" %current_user.number)
  print("Options:")
  print("1.) Emergency Open All (Will be made in person)")
  print("2.) Interact with printers(open/lock)(Will be made in person)")
  print("3.) Add New User/SpaceCaptain")
  print("4.) Remove User/SpaceCaptain")
  print("5.) Start a Print(Incomplete)")
  print("6.) Unpdate User Information(change ID/Name/Number)")
  print("7.) Delete All Registered Users(General/SpaceCaptain)(Incomplete)")
  print("8.) Signout")
  i = int(input("--->"))
  if(i == 1):
    print("This option has not been added yet...")
    time.sleep(1)
    adminMain()
  elif(i == 2):
    print("This option has not been added yet...")
    time.sleep(1)
    adminMain()
  elif(i == 3): #add new ueser
    AddNewUser()
    adminMain()
  elif(i == 4):
    removeUser()
    adminMain()
  elif(i == 5):
    print("This option has not been added yet...")
    time.sleep(1)
    adminMain()
  elif(i == 6):
    print("This option has not been added yet...")
    time.sleep(1)
    adminMain()
  elif(i == 7):
    print("This option has not been added yet...")
    time.sleep(1)
    adminMain()
  elif(i == 8):
    print("Logging out...")
    time.sleep(1)
    del current_user.name
  else:
    print("Invalid input...") 
    time.sleep(1)
    adminMain()
  
def spaceCaptainMain():
  os.system('clear')
  print("Welcome, %s(%s)" %(current_user.name, current_user.access))
  print("Number: %s" %current_user.number)
  print("Options:")
  print("1.) Interact with printers(open/lock)(Will be made in person)")
  print("2.) Add New User")
  print("3.) Remove New User")
  print("4.) Start a Print(Incomplete)")
  print("5.) Unpdate User Information(change ID/Name/Number)")
  print("6.) Signout")
  i = int(input("--->"))
  if(i == 1):
    print("This option has not been added yet...")
    time.sleep(1)
    spaceCaptainMain()
  elif(i == 2):
    AddNewUser()
    spaceCaptainMain()
  elif(i == 3): #add new ueser
    print("This option has not been added yet...")
    spaceCaptainMain()
  elif(i == 4):
    print("This option has not been added yet...")
    time.sleep(1)
    spaceCaptainMain()
  elif(i == 5):
    print("This option has not been added yet...")
    time.sleep(1)
    spaceCaptainMain()
  elif(i == 6):
    print("Logging out...")
    time.sleep(1)
    del current_user.name
  else:
    print("Invalid input...") 
    time.sleep(1)
    spaceCaptainMain()
    
def generalUser_Main():
  os.system('clear')
  print("Welcome, %s(%s)" %(current_user.name, current_user.access))
  print("Number: %s" %current_user.number)
  print("Options:")
  print("1.) Start a Print(Incomplete)")
  print("2.) Interact with printers(open)(Will be made in person)")
  print("3.) Unpdate User Information(change Name/Number)")
  print("4.) Signout")
  i = int(input("--->"))
  if(i == 1):
    print("This option has not been added yet...")
    time.sleep(1)
    spaceCaptainMain()
  elif(i == 2):
    print("This option has not been added yet...")
    time.sleep(1)
    spaceCaptainMain()
  elif(i == 3): #add new ueser
    AddNewUser()
    spaceCaptainMain()
  elif(i == 4):
    print("Logging out...")
    time.sleep(1)
    del current_user.name
  else:
    print("Invalid input...") 
    time.sleep(1)
    spaceCaptainMain()
    
def SelectAccessRoll():
  while(True):
    os.system('clear')
    print("What type of user are you adding?")
    print("1.) General User")
    if(current_user.access == "Admin"):
      print("2.) Space Captain")
      print("3.) Admin")
      print("4.) ~Cancel")
      i = str(input("--->"))
      if(i in ["1", "2", "3", "4"]):
        return i
    else:
      print("2.) ~Cancel")
      i = str(input("--->"))
      if(i == "1"):
        return i
      elif(i == "2"):
        return "4"
    print("Invalid input...") 
    time.sleep(1)
  
def AddNewUser():
  typeNum = SelectAccessRoll()
  typeStr = ""
  if(typeNum == "1"):
    typeStr = "General User"
  elif(typeNum == "2"):
    typeStr = "Space Captain"
  elif(typeNum == "3"):
    typeStr = "Admin"
  elif(typeNum == "4"):
    return True
  
  id = ""
  name = ""
  number = ""
  
  gettingInfo = True
  while(gettingInfo):
    os.system('clear')
    print("Scan Card you would like to add(type new ID)")
    id = str(input("--->"))
    os.system('clear')
    print("Enter the Name that will be associated with the card")
    name = str(input("--->"))
    os.system('clear')
    print("Enter the Phone Number that will be associated with the card")
    number = str(input("--->"))
    
    selecting = True
    while(selecting):
      os.system('clear')
      print("User Type: %s" %typeStr)
      print("Name: %s" %name)
      print("Name: %s" %number)
      print("Is the following information correct(y/n)")
      i = str(input("--->"))
      if(i == "y"):
        gettingInfo = False
        selecting = False
      elif(i == "n"):
        selecting = False
  
  if(typeNum == "3"):
    file = open("admin_Info.txt", "w")
    for x in A_data.info:
      file.write(x + "\n")
      file.write(A_data.info[x][0] + "\n")
      file.write(A_data.info[x][1] + "\n")
    file.write(id + "\n")
    file.write(name + "\n")
    file.write(number + "\n")
    file.close()
  elif(typeNum == "2"):
    file = open("spacecaptain_Info.txt", "w")
    for x in SC_data.info:
      file.write(x + "\n")
      file.write(SC_data.info[x][0] + "\n")
      file.write(SC_data.info[x][1] + "\n")
    file.write(id + "\n")
    file.write(name + "\n")
    file.write(number + "\n")
    file.close()
  elif(typeNum == "1"):
    file = open("general_user_Info.txt", "w")
    for x in G_data.info:
      file.write(x + "\n")
      file.write(G_data.info[x][0] + "\n")
      file.write(G_data.info[x][1] + "\n")
    file.write(id + "\n")
    file.write(name + "\n")
    file.write(number + "\n")
    file.close()
    
  start_up()

def removeUser():
  while(True):
    os.system('clear')
    print("Scan the card you would like to remove, or scan your own card to cancel.")
    i = int(input("(type id)---> "))
    if(i == current_user.id):
      return True
    else:
      if(id in A_data.info):
        print("cum")
      elif(id in SC_data.info):
        print("cum")
      elif(id in G_data.info):
        print("cum")
    print("Invalid input...") 
    time.sleep(1)

def invalid():
  os.system('clear')
  print('[=-=-=-=-=-=-=-=-=-=-=-=-=]')
  print('[=-=-=-=INVALID ID!=-=-=-=]')
  print('[=-=-=-=-=-=-=-=-=-=-=-=-=]')
  time.sleep(1)

def getUsers(file_name, text):
  print(text)
  time.sleep(.5)
  
  file = open(file_name)
  tempMap = {}
  id = ""
  name = ""
  for line in file:
    if(id == ""):
      id = line.strip()
    elif(name == ""):
      name = line.strip()
    else:
      tempMap[id] = [name,line.strip()]
      id = ""
      name = ""
  
  file.close()
  return tempMap

def start_up():
  global A_data
  A_data = access_codes(getUsers("admin_Info.txt", "Updating 'Admin' List"))
  global SC_data
  SC_data = access_codes(getUsers("spacecaptain_Info.txt", "Updating 'Space Captain' List"))
  global G_data
  G_data = access_codes(getUsers("general_user_Info.txt", "Updating 'General USer' List"))
  
start_up()
main()
