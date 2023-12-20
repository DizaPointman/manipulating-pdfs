from pathlib import Path
from pypdf import PdfReader, PdfWriter, PdfFileMerger
import copy
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import LETTER, A4
from reportlab.lib.colors import blue


#pip install reportlab
#main interface for creating PDFs with ReportLab is the Canvas class, which you can find in the reportlab.pdfgen.canvas module

#Using the Canvas Class

def creating_pdf_with_canvas():
    canvas = Canvas("hello.pdf")
    
    #first two arguments to .drawString() determine the location where the text is written on the canvas
    # The first specifies the distance from the left edge of the canvas, and the second specifies the distance from the bottom edge
    # The values passed to .drawString() are measured in user space points. Since a point equals 1/72 of an inch, 
    # the above code draws the string "Hello, World!" one inch from the left and one inch from the bottom of the page.
    
    canvas.drawString(72, 72, "Hello God!")
    canvas.save()
    
    #define the page size with the pagesize optional argument. This parameter accepts a tuple of floating-point values 
    #representing the width and height of the page in points
    #because 8.5 times 72 is 612, and 11 times 72 is 792
    
    canvas2 = Canvas("hello_pagesize.pdf", pagesize=(612.0, 792.0))
    
    #cm and inch are floating-point values. They represent the number of points contained in each unit
    #Therefore, cm is 28.346456692913385 points, and inch is 72.0 points
    print(cm)
    print(inch)
    
    canvas3 = Canvas("hello_pagesize_units.pdf", pagesize=(8.5 * inch, 11 * inch))
    
    #reportlab.lib.pagesizes module
    
    canvas4 = Canvas("hello_pagesize_module.pdf", pagesize=LETTER)
    print(LETTER)
    
    #Font Properties
    
    canvas5 = Canvas("font_example.pdf", pagesize=A4)
    canvas5.setFont("Helvetica-BoldOblique", 20)
    canvas5.drawString(1 * inch, 10 * inch, "Helvetica-BoldOblique (20 pt)")
    canvas5.save()
    
    #Setting colors
    
    canvas6 = Canvas("color_example.pdf", pagesize=A4)
    canvas6.setFont("Times-Roman", 12)
    canvas6.setFillColor(blue)
    canvas6.drawString(1 * inch, 10 * inch, "Blue text")
    canvas6.save()


if __name__ == '__main__':
    print("Hello God!")
    creating_pdf_with_canvas()