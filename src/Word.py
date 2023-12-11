from docx import Document
import docx
from docx.enum.section import WD_ORIENT
# Create an instance of a word document


def word(nom_fichier, liste_eleve, dico_cheval, nouveau_fichier):
    print(nom_fichier)

    if nouveau_fichier == 1:
        doc = docx.Document(nom_fichier)
        section = doc.sections[-1]
        new_width, new_height = section.page_height, section.page_width
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = new_width
        section.page_height = new_height

        table = doc.add_table(rows=1, cols=5)
        table.style = 'Table Grid'
    # Adding heading in the 1st row of the table
    column = table.add_column().cells
    column = table.column[0].cells
    for ind in range(liste_eleve):
        column[ind].text = liste_eleve[ind]
    row = table.rows[0].cells
    row[0].text = 'jour/heure'
    row[1].text = 'date1'
    row[2].text = 'date2'
    row[3].text = 'date3'
    row[4].text = 'date4'

    # Adding data from the list to the table
    for id, name in data:

        # Adding a row and then adding data in it.
        row = table.add_row().cells
        # Converting id to string as table can only take string input
        row[0].text = str(id)
        row[1].text = name

    row = table.add_row().cells
    row[0].text = 'jour/heure'
    row[1].text = 'date1'
    row[2].text = 'date2'
    row[3].text = 'date3'
    row[4].text = 'date4'
    row = table.add_row().cells
    row[0].text = '\r\r'
    row[1].text = 'date1'
    row[2].text = 'date2'
    row[3].text = 'date3'
    row[4].text = 'date4'
    # Now save the document to a location
    doc.save(nom_fichier)


word("fichierteste.docx", ["LENA", "KYLLIAN", "test"], [
     "SARA", "YOUSS", "HUGO"], True)
