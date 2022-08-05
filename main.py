#Import Google Text to Speech converter & PDF READER
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2
import os
#opening the file
file = open('file.pdf','rb') #rb = reading

#creating the object
pdf_reader = PyPDF2.PdfFileReader(file)

#Get the number of pages
num_of_pages = pdf_reader.numPages
textlist=[]

#Get the data from each page - each character
for i in range(num_of_pages):
    try:
        page = pdf_reader.getPage(i)
        textlist.append(page.extractText())
    except:
        pass

#Converting the multiline text to single line text
textstring = " ".join(textlist)

#Setting the language to English
language ="en"

#Call GTTS
audio = gTTS(text=textstring,lang=language,slow=False)
audio.save('audio.mp3')
os.system('start audio.mp3')
