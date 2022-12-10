import tkinter as tk
from tkinter import END
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title
l1 = tk.Label(my_w,  text='Your Data', width=10 )  # added one Label
l1.grid(row=0,column=0,padx=10,pady=10)

t1 = tk.Text(my_w,  height=12, width=45,bg='yellow') # text box
t1.grid(row=1,column=0,padx=10)

b1=tk.Button(text='Generate PDF',command=lambda:gen_pdf())
b1.grid(row=2,column=0,padx=20,pady=10)

### get PDF file libraries
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import  A4

# add Paragraph style ##
my_Style = ParagraphStyle('My Para style',
     fontName="Times-Roman",
     fontSize=16,
     alignment=0,
     borderWidth=2,
     borderColor='#FFFF00',
     backColor = '#F1F1F1',
     borderPadding = (20, 20, 20),
     leading = 20
        )
width, height = A4 # size of the file
# path and file name ##
my_path='C:\\Users\Hanci\\Desktop\\my_pdf.pdf'

def gen_pdf():
    text=t1.get("1.0",END) # collect user enterd data
    text=text.replace('\n','<BR/>') # replace the line breaks
    p1 = Paragraph(text, my_Style) # add style
    c = canvas.Canvas(my_path, pagesize=A4) # create canvas
    p1.wrapOn(c, 300, 50) # width , height of Paragraph
    p1.drawOn(c, width-450,height-350) # location of Paragraph
    c.save()
    t1.delete('1.0',END)# Delete from position 0 till end
    t1.update()     # Update text widget
my_w.mainloop()  # Keep the window open