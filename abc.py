from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO
import pygame


def speak(text, language):
mp3_fo = BytesIO()
tts = gTTS(text, lang=language)
tts.write_to_fp(mp3_fo)
mp3_fo.seek(0)
sound = pygame.mixer.Sound(mp3_fo)
sound.play()


def change(text,src,dest):
text1=text
src1=src
dest1=dest
translation=GoogleTranslator(source=src1, target=dest).translate(text)
return translation
def data():
s=comb_sor.get()
d=comb_dest.get()
msg=sor_text.get(1.0,END)
text_get=change(text=msg,src=s,dest=d)
dest_text.delete(1.0,END)
dest_text.insert(END,text_get)
pygame.init()
pygame.mixer.init()
speak(text=translation,language=d)

languages = {
"English": "en",
"Hindi": "hi",
"Japanese": "ja",
"Afrikaans": "af",
"Albanian": "sq",
"Amharic": "am",
"Arabic": "ar",
"Armenian": "hy",
"Azerbaijani": "az",
"Basque": "eu",
"Belarusian": "be",
"Bengali": "bn",
"Bosnian": "bs",
"Bulgarian": "bg",
"Catalan": "ca",
"Cebuano": "ceb",
"Chinese (Simplified)": "zh-CN",
"Chinese (Traditional)": "zh-TW",
"Corsican": "co",
"Croatian": "hr",
"Czech": "cs",
"Danish": "da",
"Dutch": "nl",
"Esperanto": "eo",
"Estonian": "et",
"Finnish": "fi",
"French": "fr",
"Frisian": "fy",
"Galician": "gl",
"Georgian": "ka",
"German": "de",
"Greek": "el",
"Gujarati": "gu",
"Haitian Creole": "ht",
"Hausa": "ha",
"Hawaiian": "haw",
"Hebrew": "he",
"Hindi": "hi",
"Hmong": "hmn",
"Hungarian": "hu",
"Icelandic": "is",
"Igbo": "ig",
"Indonesian": "id",
"Irish": "ga",
"Italian": "it",
"Japanese": "ja",
"Kannada": "kn",
"Kazakh": "kk",
"Khmer": "km",
"Korean": "ko",
"Kurdish": "ku",
"Lao": "lo",
"Latvian": "lv",
"Lithuanian": "lt",
"Luxembourgish": "lb",
"Macedonian": "mk",
"Malagasy": "mg",
"Malay": "ms",
"Malayalam": "ml",
"Maltese": "mt",
"Maori": "mi",
"Marathi": "mr",
"Mongolian": "mn",
"Nepali": "ne",
"Norwegian": "no",
"Pashto": "ps",
"Persian": "fa",
"Polish": "pl",
"Portuguese": "pt",
"Punjabi": "pa",
"Romanian": "ro",
"Russian": "ru",
"Samoan": "sm",
"Scots Gaelic": "gd",
"Serbian": "sr",
"Sesotho": "st",
"Sindhi": "sd",
"Sinhala": "si",
"Slovak": "sk",
"Slovenian": "sl",
"Somali": "so",
"Spanish": "es",
"Sundanese": "su",
"Swahili": "sw",
"Swedish": "sv",
"Tajik": "tg",
"Tamil": "ta",
"Telugu": "te",
"Thai": "th",
"Turkish": "tr",
"Ukrainian": "uk",
"Urdu": "ur",
"Uzbek": "uz",
"Vietnamese": "vi",
"Welsh": "cy",
"Xhosa": "xh",
"Yiddish": "yi",
"Yoruba": "yo",
"Zulu": "zu"
}







root=tk.Tk()
root.resizable(False,False)
root.title("Language Translator")
root.geometry("500x600")

frame=Frame(root,width=500,height=700,relief=RIDGE,borderwidth=5 ,bg="#F7DC6F")
frame.place(x=0,y=0)
Label(root,text="Translator",font=("Helvetica 20 bold"),fg="black",bg="#F7DC6F").pack(pady=10)

sor_txt = Label(frame,text="Source",font=("Time New Roman",20,"bold"),fg="Black",bg="#F7DC6F")
sor_txt.place(x=100,y=100,height=25,width=300)

sor_text = Text(frame,font=("Time New Roman",10),wrap=WORD)
sor_text.place(x=4,y=130,height=150,width=480)

list_items=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,values=list_items)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")


btn1=Button(frame,text="Translate",relief=RAISED,borderwidth=2,font=("Time New Roman",20,"bold"),bg="#248aa2",fg="white",cursor="hand2",command=data)
btn1.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,values=list_items)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

dest_txt = Label(frame,text="Destination",font=("Time New Roman",20,"bold"),fg="Black",bg="#F7DC6F")
dest_txt.place(x=100,y=360,height=25,width=300)

dest_text = Text(frame,font=("Time New Roman",10),wrap=WORD)
dest_text.place(x=4,y=400,height=150,width=480)

root.mainloop()