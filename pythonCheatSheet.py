##Datei: pythoncheatsheet.py
##ausfueren: python pythoncheatsheet.py
##BZW: py pythoncheatsheet.py
 
##Dies ist ein kleines Cheat-Sheet fuer die Verwendung von python fuer C und C++ Programmierer
 
#Variable
#int einezuahl = 43;
eineVariable = 13
print("eineVariable", eineVariable)
eineVariable = "blablabla"
print("eineVariable", eineVariable)
 
# typisierung in python: ducktyping
 
# daher: bitte immer nach möglichkeit typisieren
eineZweiteVariable : int = 14
print("eineZweiteVariable", eineZweiteVariable)
eineZweiteVariable = "Text"
#print("eineZweiteVariable", eineZweiteVariable**3)

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)
eineVariable = 15

datenTyp = type(eineVariable)
print ("Datentyp von eineVariable: ", datenTyp)

# formatierte Ausgabe
print("Zahl lautet %i \n und ist Cool!", eineVariable)
# formatierte Strings
einText = f"Zahl lautet {eineVariable**2} \n und ist Cool!"
print(einText)

# Eingabe von der Kommandozeile:

