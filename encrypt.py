#read text from test.txt and store text as list of characters
rdt = open("test.txt", "r")
text = list( rdt.read() ) 
rdt.close()

# change each character to go up by 1
for i in range(len(text)):
  text[i] = chr(ord(text[i]) + 1)

# store each character togethor as a string
strtext = ""
for i in range(len(text)):
  strtext += text[i]

#add encrpyted text into encrypt.txt
wre = open("encrypt.txt", "w")
wre.write(strtext)
wre.close()