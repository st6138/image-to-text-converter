
import tkinter as tk
from tkinter import filedialog #used for creating window
from tkinter.filedialog import askopenfile
 #gives permission to open a file
from PIL import Image, ImageTk
import boto3 #for using aws textract services


wind=tk.Tk() #creating window
wind.geometry("450x400")
wind.title("AWS Texttract")
l1=tk.Label(wind,text="Upload an Image", width=30,font=('times',18,'bold')) #creating label
l1.pack()
b1=tk.Button(wind,text="Upload a file",width=30,command=lambda:uploadfile())#creating button
b1.pack()

def uploadfile():
    aws_mag_con=boto3.session.Session(profile_name='st6138')
    boto3.client=aws_mag_con.client(service_name='textract',region_name='ap-south-1')
    global img
    f_types=[('Jpg Files',"*.jpg")]
    filename=filedialog.askopenfile(filetype=f_types)
    img=Image.open(filename)#opening image
    img_resize=img.resize((400,200))
    img=ImageTk.PhotoImage(img_resize)
    imgbytes=get_image_byte(filename)
   
    b2=tk.Button(wind,image=img)
    b2.pack()
    response=boto3.client.detect_document_text(Document={'Bytes':imgbytes})
    for item in response['Blocks']:
          if item['Blocktype']=='WORD':
              print(item['Text'])
def get_image_byte(filename):
    with open(filename,'rb') as imgfile:
              return imgfile.read()



wind.mainloop()









