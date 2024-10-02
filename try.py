import customtkinter
from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO
import pygame

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

def Mainapp():

    def change(text,src,dest):
        text1=text
        src1=src
        dest1=dest
        translation=GoogleTranslator(source=src1, target=dest).translate(text)
        return translation

    def speak(text, language):
        mp3_fo = BytesIO()
        tts = gTTS(text, lang=language)
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)
        sound = pygame.mixer.Sound(mp3_fo)
        sound.play()
        
    def data():
        selected_language=send_from_optionmenu.get()
        selected_language2=send_only_optionmenu.get()

        if selected_language in languages:
            s = languages[selected_language]
        if selected_language2 in languages:
            d= languages[selected_language2]
        
        text_widget2.config(state=NORMAL)
        
        msg=text_widget .get(1.0,END)
        text_get=change(text=msg,src=s,dest=d)
        text_widget2.delete(1.0,END)
        text_widget2.insert(END,text_get)
        pygame.init()
        pygame.mixer.init()
        text_widget2.config(state=DISABLED)
        speak(text=text_get,language=d)
        customtkinter.set_appearance_mode("dark")  # Set dark mode using customtkinter
        customtkinter.set_default_color_theme("dark-blue")  # Set the dark color theme
    global a
    a = True


    def toggle_mode():
        global a
        if a:
            customtkinter.set_appearance_mode("light")  # Set light mode using customtkinter
            customtkinter.set_default_color_theme("dark-blue")  # Set the dark color theme
            app.mode = "light"
            a=False
        else:
            customtkinter.set_appearance_mode("dark")  # Set dark mode using customtkinter
            customtkinter.set_default_color_theme("dark-blue")  # Set the dark color theme
            app.mode = "dark"
            a=True
        
    
    app = customtkinter.CTk()
    app.title("Translate")
    app.resizable(False,False)
    
    
    
    customtkinter.set_appearance_mode("dark")  
    customtkinter.set_default_color_theme("dark-blue")  

    #app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1
    #app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1#app_frame1

        
    app_frame1 = customtkinter.CTkFrame(master=app)
    app_frame1.grid(row=0, column=0, padx=20, pady=(20,0), sticky="EW")

    label = customtkinter.CTkLabel(app_frame1, text="Translate", font=("Arial", 30), fg_color="transparent")
    label.grid(row=0, column=0, padx=20,pady=20, sticky="ew")
    
    toggle_button = customtkinter.CTkButton(app_frame1, text="Toggle Mode", command=toggle_mode, width=20)
    toggle_button.grid(row=0, column=1, padx=(250,0), pady=20, sticky="e")

    # app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2
    # app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2# app_frame2
    app_frame2 = customtkinter.CTkFrame(master=app)
    app_frame2.grid(row=1, column=0, padx=20,pady=20, sticky="ew")

    # app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3
    # app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3# app_frame3
    app_frame3 = customtkinter.CTkFrame(master=app_frame2)
    app_frame3.grid(row=2, column=0, padx=20,pady=10, sticky="ew")
    
    send_from_label = customtkinter.CTkLabel(app_frame3, text="FROM ", fg_color="transparent")
    send_from_label.grid(row=0, column=0)
    send_from_optionmenu = customtkinter.CTkOptionMenu(app_frame3, values=list(languages.keys()))
    send_from_optionmenu.grid(row=1, column=0, padx=10, sticky="ew")
    send_from_optionmenu.set("English")  
    
    send_from_label1 = customtkinter.CTkLabel(app_frame3, text="<------------------------------------------>", fg_color="transparent")
    send_from_label1.grid(row=0, column=1)
    
    send_from_label2 = customtkinter.CTkLabel(app_frame3, text="<------------------------------------------>", fg_color="transparent")
    send_from_label2.grid(row=1, column=1)
    
    send_only_label = customtkinter.CTkLabel(app_frame3, text="TO", fg_color="transparent")
    send_only_label.grid(row=0, column=2)
    send_only_optionmenu = customtkinter.CTkOptionMenu(app_frame3, values=list(languages.keys()))
    send_only_optionmenu.grid(row=1, column=2, padx=20, sticky="ew")
    send_only_optionmenu.set("English") 
    
    text_widget = tk.Text(app_frame2, wrap=customtkinter.WORD,height=10)
    text_widget.grid(row=1, column=0, padx=(10,0),pady=20, sticky="ew")
    
    text_widget2 = tk.Text(app_frame2, wrap=customtkinter.WORD,height=10)
    text_widget2.grid(row=3, column=0, padx=(10,0),pady=20, sticky="ew")
    text_widget2.config(state=DISABLED)

    send_button = customtkinter.CTkButton(app_frame2, text="RUN",command=data)
    send_button.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="ew")

    app.mainloop()

Mainapp()

