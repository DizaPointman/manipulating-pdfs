from pathlib import Path
import pdfrw
from pdfrw import PdfReader


pdf_path = (Path.home()/"Projects/VSCode_Projects/Tutorialhell/manipulating-pdfs/test_pdfs" /"antrag-sgb2_ba042689.pdf")
pdf_path_test = (Path.home()/"Projects/VSCode_Projects/Tutorialhell/manipulating-pdfs/test_pdfs" /"basic.pdf")


def check_and_extract_annotations():
    
    pdf_reader = PdfReader(pdf_path)
    
    print("next try")
    
    for i, page in enumerate(pdf_reader.pages):
        print(f"-----page {i+1} of form-----")
        annotations = page['/Annots']
        if annotations is None:
            continue

        for annotation in annotations:
            if annotation['/Subtype']=='/Widget':
                #print(annotation)
                if annotation['/T']:
                    key = annotation['/T'].to_unicode()
                    print(key)


in_path = (Path.home()/"Projects/VSCode_Projects/Tutorialhell/manipulating-pdfs/test_pdfs" /"basic.pdf")
#data = (Path.home()/"Projects/VSCode_Projects/Tutorialhell/manipulating-pdfs/test_pdfs" /"basic-data.json")
data = {"Name": "John Doe", "Address": "10101 Broadway", "City": "Some Town", "State": "SS", "Zip": "55555"}
out_path = (Path.home()/"Projects/VSCode_Projects/Tutorialhell/manipulating-pdfs/test_output" /"basic_filled.pdf")

def form_filler(in_path, data, out_path):
    
    pdf = PdfReader(in_path)
    #pdf = pdfrw.PdfReader(in_path)
    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations is None:
            continue

        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                key = annotation['/T'].to_unicode()
                if key in data:
                    pdfstr = pdfrw.objects.pdfstring.PdfString.encode(data[key])
                    annotation.update(pdfrw.PdfDict(V=pdfstr))
        pdf.Root.AcroForm.update(
            pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        pdfrw.PdfWriter().write(out_path, pdf)


if __name__ == '__main__':
    print("Hello God!")
    #check_and_extract_annotations()
    form_filler(in_path, data, out_path)