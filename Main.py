from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import webbrowser
import sys
import string
import pyttsx3
from translate import Translator
import random
import PySimpleGUI as sg
from easygui import*
import subprocess
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageTk
from itertools import count
#import tkinter as tk
#from tkinter import *
#import customtkinter
import string
import pyttsx3
from translate import Translator
import os
#import main2


def voice():
           
    subprocess.Popen(["python", "main2.py"])
      #import main2
def pre_trainedrealtime():
    subprocess.call(["python", "camera with stt.py"])   

customtkinter.set_appearance_mode("dark")

root=customtkinter.CTk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("500x500")
root.title("Sign Language Detection System")
#root.attributes('-fullscreen', True)
#color = "Silver"
#color2 = "#0a2f49"
#color3 = "#196f90"
#color4 = '#11517c'
#root.configure(bg=color3)
#total_cost=0
#frame = Frame(root, width=200, height=100)
#frame.place(x=560,y=500)
#frame.pack()
#frame.place( relx=0.5, rely=0.5,x=-250,y=-230)
#img = ImageTk.PhotoImage(Image.open("WzqYRNF.jpg"))

#label = Label(frame, image = img)

#label.pack()
##scanned Items settings


# ==========================FRAMES=========================
# ======================menu-options on the left frame=============================

#camera_k_btn_btm_frame = customtkinter.CTkButton(master=root, text="Camera Scanning",command=camera_scanning, width=200,
                                 #height=50,font=("Candra", 15,"bold"))
#camera_k_btn_btm_frame.place(relx=0.5,rely=0.3,anchor=CENTER)

voice_k_btn_btm_frame = customtkinter.CTkButton(master=root, text="Voice Communication",command=voice, width=200,
                                 height=50,font=("Candra", 15,"bold"))
voice_k_btn_btm_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

voice_k_btn_btm_frame = customtkinter.CTkButton(master=root, text="Pretrained Realtime",command=pre_trainedrealtime, width=200,
                                 height=50,font=("Candra", 15,"bold"))
voice_k_btn_btm_frame.place(relx=0.5,rely=0.7,anchor=CENTER)

#camera_k_btn_btm_frame = Button(root, text="Camera Scanning", width=19,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=camera_scanning)
#camera_k_btn_btm_frame.place(x=180, y=120)

#camera_k_btn_btm_frame = Button(root, text="Pre_trained Realtime", width=19,height=2,bg=color4,bd=7,relief=RAISED,font=("Candra", 8,"bold") ,fg=color, command=pre_trainedrealtime)
#camera_k_btn_btm_frame.place(x=180, y=280)


# ============================TITLE on top FRAME=======================
#label_show = Lael(root, text="Sign Language Detection System", bd=7, relief=RIDGE, width=35, height=2,
   #                font=("Times", 12, "bold", "italic"), bg=color4, fg=color).place(x=120, y=0)

label = customtkinter.CTkLabel(master=root, text="Sign Language Detection System",width=200,
                               height=25,
                               font=("Times", 30, "bold", "italic"))
label.place(relx=0.5, rely=0.1, anchor=CENTER)


root.mainloop()

