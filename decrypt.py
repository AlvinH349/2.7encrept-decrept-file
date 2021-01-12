#read encrypt.txt and store text as list of characters
rdd = open("encrypt.txt", "r")
textd = list( rdd.read() ) 
rdd.close()

# change each character to go down by 1
for i in range(len(textd)):
  textd[i] = chr(ord(textd[i]) - 1)

# store each character togethor as a string
strtextd = ""
for i in range(len(textd)):
  strtextd += textd[i]

#add encrpyted text into decrypt.txt
wre = open("decrypt.txt", "w")
wre.write(strtextd)
wre.close()