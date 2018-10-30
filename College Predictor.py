import pandas
import pandas as pd
import matplotlib.pyplot as plt
#Reading all the CSV Files
Kharagpur= pd.read_csv('Kharagpur.csv')
Bombay= pd.read_csv('Bombay.csv')
Kanpur= pd.read_csv('Kanpur.csv')
Madras= pd.read_csv('Madras.csv')
Delhi= pd.read_csv('Delhi.csv')
Guwahati= pd.read_csv('Guwahati.csv')
Roorkee= pd.read_csv('Roorkee.csv')
Ropar= pd.read_csv('Ropar.csv')
Bhubaneswar= pd.read_csv('Bhubaneswar.csv')
Gandhinagar= pd.read_csv('Gandhinagar.csv')
Hyderabad= pd.read_csv('Hyderabad.csv')
Jodhpur= pd.read_csv('Jodhpur.csv')
Patna= pd.read_csv('Patna.csv')
Indore= pd.read_csv('Indore.csv')
Mandi= pd.read_csv('Mandi.csv')
Varanasi  = pd.read_csv('Varanasi.csv')
Palakkad= pd.read_csv('Palakkad.csv')
Tirupati= pd.read_csv('Tirupati.csv')
Dhanbad= pd.read_csv('Dhanbad.csv')
Bhilai= pd.read_csv('Bhilai.csv')
Goa= pd.read_csv('Goa.csv')
Jammu= pd.read_csv('Jammu.csv')
Dharwad= pd.read_csv('Dharwad.csv')

#Welcome Message
print("Welcome to IIT College and Stream Predictor")

#Taking Rank input
Rank=float(input("Enter Your Rank:"))

#Function to display all records
def display():
  print("") 
  print("IIT Kharagpur")
  print("") 
  print(Kharagpur)
  print("") 
  print("IIT Bombay")
  print("") 
  print(Bombay)
  print("") 
  print("IIT Kanpur")
  print("") 
  print(Kanpur)
  print("") 
  print("IIT Madras")
  print("") 
  print(Madras)
  print("") 
  print("IIT Delhi")
  print("") 
  print(Delhi)
  print("") 
  print("IIT Guwahati")
  print("") 
  print(Guwahati)
  print("") 
  print("IIT Roorkee")
  print("") 
  print(Roorkee)
  print("") 
  print("IIT Ropar")
  print("") 
  print(Ropar)
  print("") 
  print("IIT Bhubaneswar")
  print("") 
  print(Bhubaneswar)
  print("") 
  print("IIT Gandhinagar")
  print("") 
  print(Gandhinagar)
  print("") 
  print("IIT Hyderabad")
  print("") 
  print(Hyderabad)
  print("") 
  print("IIT Jodhpur")
  print("") 
  print(Jodhpur)
  print("") 
  print("IIT Patna")
  print("") 
  print(Patna)
  print("") 
  print("IIT Indrore")
  print("") 
  print(Indore)
  print("") 
  print("IIT Mandi")
  print("") 
  print(Mandi)
  print("") 
  print("IIT Varanasi")
  print("") 
  print(Varanasi)
  print("") 
  print("IIT Palakkad")
  print("") 
  print(Palakkad)
  print("") 
  print("IIT Tirupati")
  print("") 
  print(Tirupati)
  print("") 
  print("IIT Dhanbad")
  print("") 
  print(Dhanbad)
  print("") 
  print("IIT Bhilai")
  print("") 
  print(Bhilai)
  print("") 
  print("IIT Goa")
  print("") 
  print(Goa)
  print("") 
  print("IIT Jammu")
  print("") 
  print(Jammu)
  print("") 
  print("IIT Dharwad")
  print("") 
  print(Dharwad)
  Continue()

#Rank Predictor Function for every IIT

#Checking conditions for IIT Kharagpur
def Kharagpur_Rank():
  print("") 
  print("IIT Kharagpur")
  print("") 
  #COMPUTERS
  if(Kharagpur.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Kharagpur.loc[:,"COMPUTERS"].mean()-Rank)*100/Kharagpur.loc[:,"COMPUTERS"].mean())
      print("IIT Kharagpur : COMPUTERS PROBABILITY: "+str(probability))

  #EXTC
  if(Kharagpur.loc[:,"EXTC"].mean()>Rank):
      probability=((Kharagpur.loc[:,"EXTC"].mean()-Rank)*100/Kharagpur.loc[:,"EXTC"].mean())
      print("IIT Kharagpur : EXTC PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Kharagpur.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Kharagpur.loc[:,"ELECTRICAL"].mean()-Rank)*100/Kharagpur.loc[:,"ELECTRICAL"].mean())
      print("IIT Kharagpur : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Kharagpur.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Kharagpur.loc[:,"CHEMICAL"].mean()-Rank)*100/Kharagpur.loc[:,"CHEMICAL"].mean())
      print("IIT Kharagpur : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Kharagpur.loc[:,"CIVIL"].mean()>Rank):
      probability=((Kharagpur.loc[:,"CIVIL"].mean()-Rank)*100/Kharagpur.loc[:,"CIVIL"].mean())
      print("IIT Kharagpur : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Kharagpur.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Kharagpur.loc[:,"MECHANICAL"].mean()-Rank)*100/Kharagpur.loc[:,"MECHANICAL"].mean())
      print("IIT Kharagpur : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Bombay
def Bombay_Rank():
  print("") 
  print("IIT Bombay")
  print("") 
  #COMPUTERS
  if(Bombay.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Bombay.loc[:,"COMPUTERS"].mean()-Rank)*100/Bombay.loc[:,"COMPUTERS"].mean())
      print("IIT Bombay : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Bombay.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Bombay.loc[:,"ELECTRICAL"].mean()-Rank)*100/Bombay.loc[:,"ELECTRICAL"].mean())
      print("IIT Bombay : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Bombay.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Bombay.loc[:,"CHEMICAL"].mean()-Rank)*100/Bombay.loc[:,"CHEMICAL"].mean())
      print("IIT Bombay : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Bombay.loc[:,"CIVIL"].mean()>Rank):
      probability=((Bombay.loc[:,"CIVIL"].mean()-Rank)*100/Bombay.loc[:,"CIVIL"].mean())
      print("IIT Bombay : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Bombay.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Bombay.loc[:,"MECHANICAL"].mean()-Rank)*100/Bombay.loc[:,"MECHANICAL"].mean())
      print("IIT Bombay : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Kanpur
def Kanpur_Rank():
  print("") 
  print("IIT Kanpur")
  print("") 
  #COMPUTERS
  if(Kanpur.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Kanpur.loc[:,"COMPUTERS"].mean()-Rank)*100/Kanpur.loc[:,"COMPUTERS"].mean())
      print("IIT Kanpur : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Kanpur.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Kanpur.loc[:,"ELECTRICAL"].mean()-Rank)*100/Kanpur.loc[:,"ELECTRICAL"].mean())
      print("IIT Kanpur : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Kanpur.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Kanpur.loc[:,"CHEMICAL"].mean()-Rank)*100/Kanpur.loc[:,"CHEMICAL"].mean())
      print("IIT Kanpur : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Kanpur.loc[:,"CIVIL"].mean()>Rank):
      probability=((Kanpur.loc[:,"CIVIL"].mean()-Rank)*100/Kanpur.loc[:,"CIVIL"].mean())
      print("IIT Kanpur : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Kanpur.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Kanpur.loc[:,"MECHANICAL"].mean()-Rank)*100/Kanpur.loc[:,"MECHANICAL"].mean())
      print("IIT Kanpur : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Madras
def Madras_Rank():
  print("") 
  print("IIT Madras")
  print("") 
  #COMPUTERS
  if(Madras.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Madras.loc[:,"COMPUTERS"].mean()-Rank)*100/Madras.loc[:,"COMPUTERS"].mean())
      print("IIT Madras : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Madras.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Madras.loc[:,"ELECTRICAL"].mean()-Rank)*100/Madras.loc[:,"ELECTRICAL"].mean())
      print("IIT Madras : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Madras.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Madras.loc[:,"CHEMICAL"].mean()-Rank)*100/Madras.loc[:,"CHEMICAL"].mean())
      print("IIT Madras : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Madras.loc[:,"CIVIL"].mean()>Rank):
      probability=((Madras.loc[:,"CIVIL"].mean()-Rank)*100/Madras.loc[:,"CIVIL"].mean())
      print("IIT Madras : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Madras.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Madras.loc[:,"MECHANICAL"].mean()-Rank)*100/Madras.loc[:,"MECHANICAL"].mean())
      print("IIT Madras : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Delhi
def Delhi_Rank():
  print("") 
  print("IIT Delhi")
  print("") 
  #COMPUTERS
  if(Delhi.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Delhi.loc[:,"COMPUTERS"].mean()-Rank)*100/Delhi.loc[:,"COMPUTERS"].mean())
      print("IIT Delhi : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Delhi.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Delhi.loc[:,"ELECTRICAL"].mean()-Rank)*100/Delhi.loc[:,"ELECTRICAL"].mean())
      print("IIT Delhi : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Delhi.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Delhi.loc[:,"CHEMICAL"].mean()-Rank)*100/Delhi.loc[:,"CHEMICAL"].mean())
      print("IIT Delhi : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Delhi.loc[:,"CIVIL"].mean()>Rank):
      probability=((Delhi.loc[:,"CIVIL"].mean()-Rank)*100/Delhi.loc[:,"CIVIL"].mean())
      print("IIT Delhi : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Delhi.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Delhi.loc[:,"MECHANICAL"].mean()-Rank)*100/Delhi.loc[:,"MECHANICAL"].mean())
      print("IIT Delhi : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Guwahati
def Guwahati_Rank():
  print("") 
  print("IIT Guwahati")
  print("") 
  #COMPUTERS
  if(Guwahati.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Guwahati.loc[:,"COMPUTERS"].mean()-Rank)*100/Guwahati.loc[:,"COMPUTERS"].mean())
      print("IITGuwahati : COMPUTERS PROBABILITY: "+str(probability))

  #EXTC
  if(Guwahati.loc[:,"EXTC"].mean()>Rank):
      probability=((Guwahati.loc[:,"EXTC"].mean()-Rank)*100/Guwahati.loc[:,"EXTC"].mean())
      print("IITGuwahati : EXTC PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Guwahati.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Guwahati.loc[:,"ELECTRICAL"].mean()-Rank)*100/Guwahati.loc[:,"ELECTRICAL"].mean())
      print("IITGuwahati : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Guwahati.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Guwahati.loc[:,"CHEMICAL"].mean()-Rank)*100/Guwahati.loc[:,"CHEMICAL"].mean())
      print("IITGuwahati : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Guwahati.loc[:,"CIVIL"].mean()>Rank):
      probability=((Guwahati.loc[:,"CIVIL"].mean()-Rank)*100/Guwahati.loc[:,"CIVIL"].mean())
      print("IITGuwahati : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Guwahati.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Guwahati.loc[:,"MECHANICAL"].mean()-Rank)*100/Guwahati.loc[:,"MECHANICAL"].mean())
      print("IITGuwahati : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Roorkee
def Roorkee_Rank():
  print("") 
  print("IIT Roorkee")
  print("") 
  #COMPUTERS
  if(Roorkee.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Roorkee.loc[:,"COMPUTERS"].mean()-Rank)*100/Roorkee.loc[:,"COMPUTERS"].mean())
      print("IITRoorkee : COMPUTERS PROBABILITY: "+str(probability))

  #EXTC
  if(Roorkee.loc[:,"EXTC"].mean()>Rank):
      probability=((Roorkee.loc[:,"EXTC"].mean()-Rank)*100/Roorkee.loc[:,"EXTC"].mean())
      print("IITRoorkee : EXTC PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Roorkee.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Roorkee.loc[:,"ELECTRICAL"].mean()-Rank)*100/Roorkee.loc[:,"ELECTRICAL"].mean())
      print("IITRoorkee : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Roorkee.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Roorkee.loc[:,"CHEMICAL"].mean()-Rank)*100/Roorkee.loc[:,"CHEMICAL"].mean())
      print("IITRoorkee : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Roorkee.loc[:,"CIVIL"].mean()>Rank):
      probability=((Roorkee.loc[:,"CIVIL"].mean()-Rank)*100/Roorkee.loc[:,"CIVIL"].mean())
      print("IITRoorkee : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Roorkee.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Roorkee.loc[:,"MECHANICAL"].mean()-Rank)*100/Roorkee.loc[:,"MECHANICAL"].mean())
      print("IITRoorkee : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Ropar
def Ropar_Rank():
  print("") 
  print("IIT Ropar")
  print("") 
  #COMPUTERS
  if(Ropar.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Ropar.loc[:,"COMPUTERS"].mean()-Rank)*100/Ropar.loc[:,"COMPUTERS"].mean())
      print("IITRopar : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Ropar.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Ropar.loc[:,"ELECTRICAL"].mean()-Rank)*100/Ropar.loc[:,"ELECTRICAL"].mean())
      print("IITRopar : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Ropar.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Ropar.loc[:,"MECHANICAL"].mean()-Rank)*100/Ropar.loc[:,"MECHANICAL"].mean())
      print("IITRopar : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Bhubaneswar
def Bhubaneswar_Rank():
  print("") 
  print("IIT Bhubaneswar")
  print("") 
  #COMPUTERS
  if(Bhubaneswar.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Bhubaneswar.loc[:,"COMPUTERS"].mean()-Rank)*100/Bhubaneswar.loc[:,"COMPUTERS"].mean())
      print("IITBhubaneswar : COMPUTERS PROBABILITY: "+str(probability))

  #EXTC
  if(Bhubaneswar.loc[:,"EXTC"].mean()>Rank):
      probability=((Bhubaneswar.loc[:,"EXTC"].mean()-Rank)*100/Bhubaneswar.loc[:,"EXTC"].mean())
      print("IITBhubaneswar : EXTC PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Bhubaneswar.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Bhubaneswar.loc[:,"ELECTRICAL"].mean()-Rank)*100/Bhubaneswar.loc[:,"ELECTRICAL"].mean())
      print("IITBhubaneswar : ELECTRICAL PROBABILITY: "+str(probability))

  #CIVIL
  if(Bhubaneswar.loc[:,"CIVIL"].mean()>Rank):
      probability=((Bhubaneswar.loc[:,"CIVIL"].mean()-Rank)*100/Bhubaneswar.loc[:,"CIVIL"].mean())
      print("IITBhubaneswar : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Bhubaneswar.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Bhubaneswar.loc[:,"MECHANICAL"].mean()-Rank)*100/Bhubaneswar.loc[:,"MECHANICAL"].mean())
      print("IITBhubaneswar : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Gandhinagar
def Gandhinagar_Rank():
  print("") 
  print("IIT Gandhinagar")
  print("") 
 
  #ELECTRICAL
  if(Gandhinagar.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Gandhinagar.loc[:,"ELECTRICAL"].mean()-Rank)*100/Gandhinagar.loc[:,"ELECTRICAL"].mean())
      print("IITGandhinagar : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Gandhinagar.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Gandhinagar.loc[:,"CHEMICAL"].mean()-Rank)*100/Gandhinagar.loc[:,"CHEMICAL"].mean())
      print("IITGandhinagar : CHEMICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Gandhinagar.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Gandhinagar.loc[:,"MECHANICAL"].mean()-Rank)*100/Gandhinagar.loc[:,"MECHANICAL"].mean())
      print("IITGandhinagar : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Hyderabad
def Hyderabad_Rank():
  print("") 
  print("IIT Hyderabad")
  print("") 
  #COMPUTERS
  if(Hyderabad.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Hyderabad.loc[:,"COMPUTERS"].mean()-Rank)*100/Hyderabad.loc[:,"COMPUTERS"].mean())
      print("IIT Hyderabad : COMPUTERS PROBABILITY: "+str(probability))
 
  #ELECTRICAL
  if(Hyderabad.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Hyderabad.loc[:,"ELECTRICAL"].mean()-Rank)*100/Hyderabad.loc[:,"ELECTRICAL"].mean())
      print("IIT Hyderabad : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Hyderabad.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Hyderabad.loc[:,"CHEMICAL"].mean()-Rank)*100/Hyderabad.loc[:,"CHEMICAL"].mean())
      print("IIT Hyderabad : CHEMICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Hyderabad.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Hyderabad.loc[:,"MECHANICAL"].mean()-Rank)*100/Hyderabad.loc[:,"MECHANICAL"].mean())
      print("IIT Hyderabad : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Jodhpur
def Jodhpur_Rank():
  print("") 
  print("IIT Jodhpur")
  print("") 
  #COMPUTERS
  if(Jodhpur.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Jodhpur.loc[:,"COMPUTERS"].mean()-Rank)*100/Jodhpur.loc[:,"COMPUTERS"].mean())
      print("IIT Jodhpur : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Jodhpur.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Jodhpur.loc[:,"ELECTRICAL"].mean()-Rank)*100/Jodhpur.loc[:,"ELECTRICAL"].mean())
      print("IIT Jodhpur : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Jodhpur.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Jodhpur.loc[:,"MECHANICAL"].mean()-Rank)*100/Jodhpur.loc[:,"MECHANICAL"].mean())
      print("IIT Jodhpur : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Patna
def Patna_Rank():
  print("") 
  print("IIT Patna")
  print("") 
  #COMPUTERS
  if(Patna.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Patna.loc[:,"COMPUTERS"].mean()-Rank)*100/Patna.loc[:,"COMPUTERS"].mean())
      print("IIT Patna : COMPUTERS PROBABILITY: "+str(probability))
      
  #ELECTRICAL
  if(Patna.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Patna.loc[:,"ELECTRICAL"].mean()-Rank)*100/Patna.loc[:,"ELECTRICAL"].mean())
      print("IIT Patna : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Patna.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Patna.loc[:,"MECHANICAL"].mean()-Rank)*100/Patna.loc[:,"MECHANICAL"].mean())
      print("IIT Patna : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Indore
def Indore_Rank():
  print("") 
  print("IIT Indore")
  print("") 
  #COMPUTERS
  if(Indore.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Indore.loc[:,"COMPUTERS"].mean()-Rank)*100/Indore.loc[:,"COMPUTERS"].mean())
      print("IIT Indore : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Indore.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Indore.loc[:,"ELECTRICAL"].mean()-Rank)*100/Indore.loc[:,"ELECTRICAL"].mean())
      print("IIT Indore : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Indore.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Indore.loc[:,"MECHANICAL"].mean()-Rank)*100/Indore.loc[:,"MECHANICAL"].mean())
      print("IIT Indore : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Mandi
def Mandi_Rank():
  print("") 
  print("IIT Mandi")
  print("") 
  #COMPUTERS
  if(Mandi.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Mandi.loc[:,"COMPUTERS"].mean()-Rank)*100/Mandi.loc[:,"COMPUTERS"].mean())
      print("IIT Mandi : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Mandi.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Mandi.loc[:,"ELECTRICAL"].mean()-Rank)*100/Mandi.loc[:,"ELECTRICAL"].mean())
      print("IIT Mandi : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Mandi.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Mandi.loc[:,"MECHANICAL"].mean()-Rank)*100/Mandi.loc[:,"MECHANICAL"].mean())
      print("IIT Mandi : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Varanasi
def Varanasi_Rank():
  print("") 
  print("IIT Varanasi")
  print("") 
  #COMPUTERS
  if(Varanasi.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Varanasi.loc[:,"COMPUTERS"].mean()-Rank)*100/Varanasi.loc[:,"COMPUTERS"].mean())
      print("IIT Varanasi : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Varanasi.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Varanasi.loc[:,"ELECTRICAL"].mean()-Rank)*100/Varanasi.loc[:,"ELECTRICAL"].mean())
      print("IIT Varanasi : ELECTRICAL PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Varanasi.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Varanasi.loc[:,"CHEMICAL"].mean()-Rank)*100/Varanasi.loc[:,"CHEMICAL"].mean())
      print("IIT Varanasi : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Varanasi.loc[:,"CIVIL"].mean()>Rank):
      probability=((Varanasi.loc[:,"CIVIL"].mean()-Rank)*100/Varanasi.loc[:,"CIVIL"].mean())
      print("IIT Varanasi : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Varanasi.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Varanasi.loc[:,"MECHANICAL"].mean()-Rank)*100/Varanasi.loc[:,"MECHANICAL"].mean())
      print("IIT Varanasi : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Palakkad
def Palakkad_Rank():
  print("") 
  print("IIT Palakkad")
  print("") 
  #COMPUTERS
  if(Palakkad.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Palakkad.loc[:,"COMPUTERS"].mean()-Rank)*100/Palakkad.loc[:,"COMPUTERS"].mean())
      print("IIT Palakkad : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Palakkad.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Palakkad.loc[:,"ELECTRICAL"].mean()-Rank)*100/Palakkad.loc[:,"ELECTRICAL"].mean())
      print("IIT Palakkad : ELECTRICAL PROBABILITY: "+str(probability))

  #CIVIL
  if(Palakkad.loc[:,"CIVIL"].mean()>Rank):
      probability=((Palakkad.loc[:,"CIVIL"].mean()-Rank)*100/Palakkad.loc[:,"CIVIL"].mean())
      print("IIT Palakkad : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Palakkad.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Palakkad.loc[:,"MECHANICAL"].mean()-Rank)*100/Palakkad.loc[:,"MECHANICAL"].mean())
      print("IIT Palakkad : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Tirupati
def Tirupati_Rank():
  print("") 
  print("IIT Tirupati")
  print("") 
  #COMPUTERS
  if(Tirupati.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Tirupati.loc[:,"COMPUTERS"].mean()-Rank)*100/Tirupati.loc[:,"COMPUTERS"].mean())
      print("IIT Tirupati : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Tirupati.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Tirupati.loc[:,"ELECTRICAL"].mean()-Rank)*100/Tirupati.loc[:,"ELECTRICAL"].mean())
      print("IIT Tirupati : ELECTRICAL PROBABILITY: "+str(probability))

  #CIVIL
  if(Tirupati.loc[:,"CIVIL"].mean()>Rank):
      probability=((Tirupati.loc[:,"CIVIL"].mean()-Rank)*100/Tirupati.loc[:,"CIVIL"].mean())
      print("IIT Tirupati : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Tirupati.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Tirupati.loc[:,"MECHANICAL"].mean()-Rank)*100/Tirupati.loc[:,"MECHANICAL"].mean())
      print("IIT Tirupati : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Dhanbad
def Dhanbad_Rank():
  print("") 
  print("IIT Dhanbad")
  print("") 
  #COMPUTERS
  if(Dhanbad.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Dhanbad.loc[:,"COMPUTERS"].mean()-Rank)*100/Dhanbad.loc[:,"COMPUTERS"].mean())
      print("IIT Dhanbad : COMPUTERS PROBABILITY: "+str(probability))
 
  #EXTC
  if(Dhanbad.loc[:,"EXTC"].mean()>Rank):
      probability=((Dhanbad.loc[:,"EXTC"].mean()-Rank)*100/Dhanbad.loc[:,"EXTC"].mean())
      print("IIT Dhanbad : EXTC PROBABILITY: "+str(probability))

  #ELECTRONICS
  if(Dhanbad.loc[:,"ELECTRONICS"].mean()>Rank):
      probability=((Dhanbad.loc[:,"ELECTRONICS"].mean()-Rank)*100/Dhanbad.loc[:,"ELECTRONICS"].mean())
      print("IIT Dhanbad : ELECTRONICS PROBABILITY: "+str(probability))

  #CHEMICAL
  if(Dhanbad.loc[:,"CHEMICAL"].mean()>Rank):
      probability=((Dhanbad.loc[:,"CHEMICAL"].mean()-Rank)*100/Dhanbad.loc[:,"CHEMICAL"].mean())
      print("IIT Dhanbad : CHEMICAL PROBABILITY: "+str(probability))
  #CIVIL
  if(Dhanbad.loc[:,"CIVIL"].mean()>Rank):
      probability=((Dhanbad.loc[:,"CIVIL"].mean()-Rank)*100/Dhanbad.loc[:,"CIVIL"].mean())
      print("IIT Dhanbad : CIVIL PROBABILITY: "+str(probability))
  #MECHANICAL
  if(Dhanbad.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Dhanbad.loc[:,"MECHANICAL"].mean()-Rank)*100/Dhanbad.loc[:,"MECHANICAL"].mean())
      print("IIT Dhanbad : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Bhilai
def Bhilai_Rank():
  print("") 
  print("IIT Bhilai")
  print("") 
  #COMPUTERS
  if(Bhilai.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Bhilai.loc[:,"COMPUTERS"].mean()-Rank)*100/Bhilai.loc[:,"COMPUTERS"].mean())
      print("IIT Bhilai : COMPUTERS PROBABILITY: "+str(probability))
  
  #ELECTRICAL
  if(Bhilai.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Bhilai.loc[:,"ELECTRICAL"].mean()-Rank)*100/Bhilai.loc[:,"ELECTRICAL"].mean())
      print("IIT Bhilai : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Bhilai.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Bhilai.loc[:,"MECHANICAL"].mean()-Rank)*100/Bhilai.loc[:,"MECHANICAL"].mean())
      print("IIT Bhilai : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Goa
def Goa_Rank():
  print("") 
  print("IIT Goa")
  print("") 
  #COMPUTERS
  if(Goa.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Goa.loc[:,"COMPUTERS"].mean()-Rank)*100/Goa.loc[:,"COMPUTERS"].mean())
      print("IIT Goa : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Goa.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Goa.loc[:,"ELECTRICAL"].mean()-Rank)*100/Goa.loc[:,"ELECTRICAL"].mean())
      print("IIT Goa : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Goa.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Goa.loc[:,"MECHANICAL"].mean()-Rank)*100/Goa.loc[:,"MECHANICAL"].mean())
      print("IIT Goa : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Jammu
def Jammu_Rank():
  print("") 
  print("IIT Jammu")
  print("") 
  #COMPUTERS
  if(Jammu.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Jammu.loc[:,"COMPUTERS"].mean()-Rank)*100/Jammu.loc[:,"COMPUTERS"].mean())
      print("IIT Jammu : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Jammu.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Jammu.loc[:,"ELECTRICAL"].mean()-Rank)*100/Jammu.loc[:,"ELECTRICAL"].mean())
      print("IIT Jammu : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Jammu.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Jammu.loc[:,"MECHANICAL"].mean()-Rank)*100/Jammu.loc[:,"MECHANICAL"].mean())
      print("IIT Jammu : MECHANICAL PROBABILITY: "+str(probability))
  print("")

#Checking conditions for IIT Dharwad
def Dharwad_Rank():
  print("")  
  print("IIT Dharwad")
  print("") 
  #COMPUTERS
  if(Dharwad.loc[:,"COMPUTERS"].mean()>Rank):
      probability=((Dharwad.loc[:,"COMPUTERS"].mean()-Rank)*100/Dharwad.loc[:,"COMPUTERS"].mean())
      print("IIT Dharwad : COMPUTERS PROBABILITY: "+str(probability))

  #ELECTRICAL
  if(Dharwad.loc[:,"ELECTRICAL"].mean()>Rank):
      probability=((Dharwad.loc[:,"ELECTRICAL"].mean()-Rank)*100/Dharwad.loc[:,"ELECTRICAL"].mean())
      print("IIT Dharwad : ELECTRICAL PROBABILITY: "+str(probability))

  #MECHANICAL
  if(Dharwad.loc[:,"MECHANICAL"].mean()>Rank):
      probability=((Dharwad.loc[:,"MECHANICAL"].mean()-Rank)*100/Dharwad.loc[:,"MECHANICAL"].mean())
      print("IIT Dharwad : MECHANICAL PROBABILITY: "+str(probability))
  print("")

def Rank_Calculate():
    Kharagpur_Rank()
    Bombay_Rank()
    Kanpur_Rank()
    Madras_Rank()
    Delhi_Rank()
    Guwahati_Rank()
    Roorkee_Rank()
    Ropar_Rank()
    Bhubaneswar_Rank()
    Gandhinagar_Rank()
    Hyderabad_Rank()
    Jodhpur_Rank()
    Patna_Rank()
    Indore_Rank()
    Mandi_Rank()
    Varanasi_Rank()
    Palakkad_Rank()
    Tirupati_Rank()
    Dhanbad_Rank()
    Bhilai_Rank()
    Goa_Rank()
    Jammu_Rank()
    Dharwad_Rank()
    Continue()
    
def Graph():
    Kharagpur.plot(x='YEAR',title='IIT Kharagpur')
    Bombay.plot(x='YEAR',title='IIT Bombay')
    Kanpur.plot(x='YEAR',title='IIT Kanpur')
    Madras.plot(x='YEAR',title='IIT Madras')
    Delhi.plot(x='YEAR',title='IIT Delhi')
    Guwahati.plot(x='YEAR',title='IIT Guwahati')
    Roorkee.plot(x='YEAR',title='IIT Roorkee')
    Ropar.plot(x='YEAR',title='IIT Ropar')
    Bhubaneswar.plot(x='YEAR',title='IIT Bhubaneswar')
    Gandhinagar.plot(x='YEAR',title='IIT Gandhinagar')
    Hyderabad.plot(x='YEAR',title='IIT Hyderabad')
    Jodhpur.plot(x='YEAR',title='IIT Jodhpur')
    Patna.plot(x='YEAR',title='IIT Patna')
    Indore.plot(x='YEAR',title='IIT Indore')
    Mandi.plot(x='YEAR',title='IIT Mandi')
    Varanasi.plot(x='YEAR',title='IIT Varanasi')
    Palakkad.plot(x='YEAR',title='IIT Palakkad')
    Tirupati.plot(x='YEAR',title='IIT Tirupati')
    Dhanbad.plot(x='YEAR',title='IIT Dhanbad')
    Bhilai.plot(x='YEAR',title='IIT Bhilai')
    Goa.plot(x='YEAR',title='IIT Goa')
    Jammu.plot(x='YEAR',title='IIT Jammu')
    Dharwad.plot(x='YEAR',title='IIT Dharwad')
    
def Continue():
    print("DO YOU WANT TO CONTINUE?")
    choice=input("PLEASE ENTER Y FOR YES AND N FOR NO: ")
    if(choice=='y' or choice=='Y'):
        Menu1()
    if(choice=='n' or choice=='N'): 
        print("THANK YOU !!!!!!!!")
        
def Menu1() :
    print("SELECT ANY ONE OPTION: ")
    print("(1) VIEW ALL PASS YEAR RECORDS")
    print("(2) CHECK POSSIBLE COLLEGES")
    print("(3) VIEW THE GRAPHICAL ANALYSIS OF ALL PAST YEAR RECORDS")
    option=int(input("ENTER OPTION NUMBER: "))
    if(option==1):
        display()
    if(option==2):
        Rank_Calculate()    
    if(option==3):
        Graph()   
Menu1()