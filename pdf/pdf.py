from PyPDF2 import PdfReader, PdfWriter
import os
#from sys import argv

def modify():
    input_pdf = input("Input pdf: ")
    output_pdf = input("ouput pdf: ")
    i = int(input("Remove(0) or Select(1): "))
    modify = []

    try:
        while True:
            pg = input("Enter the page to Modify: ")
            modify.append(int(pg)-1)
    except:
    # Open the PDF file
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
    
    # Iterate through all pages and add those not in pages_to_remove
        for page_num in range(len(reader.pages)):
            if i == 1 :
                if page_num in modify:
                    writer.add_page(reader.pages[page_num])
            elif page_num not in modify:
                writer.add_page(reader.pages[page_num])
    
    # Save the new PDF without the removed pages
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

def merge():
    pdfs = []
    while True:
        pdf = input("Pdf: ")
        if pdf == "q":
            break
        pdfs.append("pdfs/"+pdf)
    writer = PdfWriter()
    output_pdf = input("Output pdf: ")
    for pdf in pdfs:
        reader = PdfReader(pdf)

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

    with open(output_pdf,"wb") as output_file:
        writer.write(output_file)


def detach():
    input_pdf = input("Input pdf: ")
    output_pdf = input("Output pdf: ")
    directary,filename = os.path.split(output_pdf)
    cout = os.path.join(directary,"c"+filename)
    ncout = os.path.join(directary,"nc"+filename)
    detach = []

    try:
        while True:
            pg = input("\n Enter the page to be deatach(coloured): ")
            if not pg.isdigit():
                break
            detach.append(int(pg)-1)
    except ValueError:
        pass
        # Open the PDF file
    reader = PdfReader(input_pdf)
    cwriter = PdfWriter()
    ncwriter = PdfWriter()

        # Iterate through all pages and add those not in pages_to_remove
    for page_num in range(len(reader.pages)):
        if page_num in detach:
            cwriter.add_page(reader.pages[page_num])
        else:
            ncwriter.add_page(reader.pages[page_num])

        # Save the new PDF without the removed pages
    with open(cout, "wb") as output_file:
        cwriter.write(output_file)

    with open(ncout,"wb") as output_file:
        ncwriter.write(output_file)

def blank():
    input_pdf = input("Input: ")
    output_pdf = input("Output: ")
    adds = []
    while True:
        add = input("Enter the pg no to Add: ")
        if not add.isdigit():
            break
        adds.append(int(add)-1)
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for pg in range(len(reader.pages)):
        if pg in adds:
            writer.add_blank_page()
        writer.add_page(reader.pages[pg])

    with open(output_pdf,"wb") as file:
        writer.write(file)




# Usage
def main():
    print(" 1. Delete \n 2. Detach \n 3.Merge \n 4.Add blank Page")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1: modify();
        case 2: detach();
        case 3: merge();
        case 4: blank();



if __name__ == "__main__":
    main()
