from pathlib import Path
from pypdf import PdfReader, PdfWriter, PdfFileMerger
import copy


def rotating_pdf_simple():
    #every odd page is rotated counterclockwise by ninety degrees
    pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"ugly.pdf")
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    
    for i, page in enumerate(pdf_reader.pages):
        if i % 2 == 0:
            page.rotate(90)
            print(f"Rotating page {i} by 90 degrees")
        pdf_writer.add_page(page)
    pdf_writer.write("rotated_ugly_simple.pdf")

def rotating_pdf_advanced():
    #every odd page is rotated counterclockwise by ninety degrees
    pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"ugly.pdf")
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    
    first_page = pdf_reader.pages[0]
    second_page = pdf_reader.pages[1]
    print(first_page.rotation)
    print(second_page.rotation)
    
    for page in pdf_reader.pages:
        if page.rotation != 0:
            page.rotate(-page.rotation)
        pdf_writer.add_page(page)
    pdf_writer.write("rotated_ugly_advanced.pdf")
    

def cropping_pdf_simple():
    pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"half_and_half.pdf")
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    #first_page has a .mediabox attribute that represents a rectangular area defining the boundaries of the page
    first_page = pdf_reader.pages[0]
    
    #units of all of the values are user space units, which are equal to 1/72 of an inch
    #width of 792 user space units, or 11 inches, and a height of 612 user space units, or 8.5 inches
    #dimensions of a standard letter-sized page in landscape orientation
    #You can access individual coordinates with square brackets, just like you would do with any other Python tuple
    print(first_page.mediabox)
    print(first_page.mediabox.lower_left)
    print(first_page.mediabox.lower_right)
    print(first_page.mediabox.upper_left)
    print(first_page.mediabox.upper_right)
    
    #altering mediabox coordinates
    first_page.mediabox.upper_left = (0, 480)
    print(first_page.mediabox)
    pdf_writer.add_page(first_page)
    pdf_writer.write("cropped_half_and_half.pdf")
    
def cropping_pdf_advanced():
    
    #work with a copy of first page so that the page you just extracted stays intact
    #importing the copy module from Python’s standard library and using deepcopy() to make a copy of the page   
    pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"half_and_half.pdf")
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    first_page = pdf_reader.pages[0]
    
    #making copy of first page
    left_side = copy.deepcopy(first_page)
    
    #extract left page
    current_coords = left_side.mediabox.upper_right
    print(current_coords)
    #new coords is the middle of the page
    new_coords = [current_coords[0] / 2, current_coords[1]]
    left_side.mediabox.upper_right = new_coords
    
    #extract right side
    right_side = copy.deepcopy(first_page)
    right_side.mediabox.upper_left = new_coords
    
    #merging pages
    pdf_writer.add_page(left_side)
    pdf_writer.add_page(right_side)
    pdf_writer.write("first_page_cropped_advanced.pdf")
    
    
#Encrypting and Decrypting PDF Files With pypdf

#encrypt documents with password; use the .encrypt() method on a PdfWriter object
#decrypt an encrypted document by using the .decrypt() method on a PdfReader object

#user_password allows for opening and reading
#owner_password allows for opening and editing

def encrypting_pdf_simple():
    
    pdf_path = (Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_pdfs" /"newsletter.pdf")
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    
    pdf_writer.append_pages_from_reader(pdf_reader)
    #When only user_password, owner_password argument defaults to the same string
    #pdf_writer.encrypt(user_password="SuperSecret")
    user_pwd = "SuperSecret"
    owner_pwd = "ReallySuperSecret"
    pdf_writer.encrypt(user_password=user_pwd, owner_password=owner_pwd)
    output_path = Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_output/newsletter_protected.pdf"
    pdf_writer.write(output_path)
    

def decrypting_pdf_simple():
    
    pdf_path = Path.home()/"Projects/VSCode_Projects/Myfuture/PaperTiger/test_output" /"newsletter_protected.pdf"
    pdf_reader = PdfReader(pdf_path)
    
    pdf_reader.decrypt(password="SuperSecret")
    print(pdf_reader.pages[0])
    print(pdf_reader.pages[0].extract_text())
            

if __name__ == '__main__':
    print("Hello God!")
    #rotating_pdf_simple()
    #rotating_pdf_advanced()
    #cropping_pdf_simple()
    #cropping_pdf_advanced()
    #encrypting_pdf_simple()
    #decrypting_pdf_simple()