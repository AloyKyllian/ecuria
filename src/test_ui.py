import unittest
from unittest.mock import patch, MagicMock
from src.ecuria 1.85 import (
    affichage_txt, vider_listebox, inserer_listbox, ajouteleve, ajoutuncheval, ajoutcheval,
    colorier, colorier_ancient_chevaux, colorier_chevaux, changer_heure, changement_heure,
    cmp_dates, recupperation_excel, sort_files_by_date, extract_date_from_filename, recup_donne,
    ecrire_fichier, add_heure, suppr_heure, add_eleve, add_cheval, suppr_cheval, suppr_eleve,
    add_moniteur, suppr_moniteur, remplirlisteboxmoniteur, ecrire_fichier_cavalier, ecrire_fichier_cheval,
    para_enregistrer, remplirlisteboxcheval, remplirlisteboxeleve, tri_heure, interface_default,
    interface_paramete, lire_fichier_chevaux, lire_fichier_cavalier, para_inserer_listebox,
    mode_parametre, mode_default, visualiser_fichier_cavalier, cmp_heure, cmp_heure_semaine,
    prochain_jour, add_centered_image, set_background, nouveau_fichier, affichejoursam, affichejoursmer,
    affichejourmar, choix_date, image, lire_parametre, mettre_a_jour, importer_param, exporter_param,
    on_enter_pressed, on_delete_pressed, on_right_pressed, on_left_pressed, on_crtls_pressed,
    fusion, on_info_clicked, on_info2_clicked, on_info_heure_clicked, on_info_cheval_clicked,
    on_info_eleve_clicked, correction, absent, items_selected, items_selected_cheval, rafraichir,
    ouvrir_excel, ecrire_mail, items_selected_heure_cheval, action, remplir_listbox_heure,
    items_selected_heure, items_selected_eleve, items_selected_cheval, action_base, sauvegarder_mail,
    toggle_entry_nbcarte, on_para_nbcarte_click, items_selected_moniteur
)

class TestUI(unittest.TestCase):

    @patch('src.ecuria 1.85.print')
    def test_affichage_txt(self, mock_print):
        affichage_txt("Mercredi", {})
        mock_print.assert_called_once_with("Mercredi", {})

    @patch('src.ecuria 1.85.Listbox')
    def test_vider_listebox(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        vider_listebox(mock_listbox_instance)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')

    @patch('src.ecuria 1.85.Listbox')
    def test_inserer_listbox(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        inserer_listbox(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'élément')

    @patch('src.ecuria 1.85.Listbox')
    def test_ajouteleve(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        ajouteleve(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'élève')

    @patch('src.ecuria 1.85.Listbox')
    def test_ajoutuncheval(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        ajoutuncheval(mock_listbox_instance, 1)
        mock_listbox_instance.insert.assert_called_once_with('end', 'cheval 1')

    @patch('src.ecuria 1.85.Listbox')
    def test_ajoutcheval(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        ajoutcheval(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'cheval')

    @patch('src.ecuria 1.85.Listbox')
    def test_colorier(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        colorier(mock_listbox_instance)
        mock_listbox_instance.itemconfig.assert_called_once_with(0, {'bg': 'red'})

    @patch('src.ecuria 1.85.Listbox')
    def test_colorier_ancient_chevaux(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        colorier_ancient_chevaux(mock_listbox_instance, {'cheval': 'ancien'})
        mock_listbox_instance.itemconfig.assert_called_once_with(0, {'bg': 'blue'})

    @patch('src.ecuria 1.85.Listbox')
    def test_colorier_chevaux(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        colorier_chevaux(mock_listbox_instance)
        mock_listbox_instance.itemconfig.assert_called_once_with(0, {'bg': 'green'})

    @patch('src.ecuria 1.85.Listbox')
    def test_changer_heure(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        changer_heure(mock_listbox_instance)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')
        mock_listbox_instance.insert.assert_called_once_with('end', 'heure')

    @patch('src.ecuria 1.85.Listbox')
    def test_changement_heure(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        changement_heure(mock_listbox_instance, 1)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')
        mock_listbox_instance.insert.assert_called_once_with('end', 'heure 1')

    @patch('src.ecuria 1.85.datetime')
    def test_cmp_dates(self, mock_datetime):
        mock_datetime.now.return_value = "2023-10-01"
        self.assertEqual(cmp_dates("2023-10-02"), 1)

    @patch('src.ecuria 1.85.pandas')
    def test_recupperation_excel(self, mock_pandas):
        mock_pandas.read_excel.return_value = "data"
        self.assertEqual(recupperation_excel("file.xlsx"), "data")

    @patch('src.ecuria 1.85.os')
    def test_sort_files_by_date(self, mock_os):
        mock_os.listdir.return_value = ["file1.txt", "file2.txt"]
        self.assertEqual(sort_files_by_date("path"), ["file1.txt", "file2.txt"])

    @patch('src.ecuria 1.85.re')
    def test_extract_date_from_filename(self, mock_re):
        mock_re.search.return_value = MagicMock()
        mock_re.search.return_value.group.return_value = "2023-10-01"
        self.assertEqual(extract_date_from_filename("file_2023-10-01.txt"), "2023-10-01")

    @patch('src.ecuria 1.85.pandas')
    def test_recup_donne(self, mock_pandas):
        mock_pandas.read_excel.return_value = "data"
        self.assertEqual(recup_donne(), "data")

    @patch('src.ecuria 1.85.open')
    def test_ecrire_fichier(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        ecrire_fichier("data")
        mock_file.write.assert_called_once_with("data")

    @patch('src.ecuria 1.85.Listbox')
    def test_add_heure(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        add_heure(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'heure')

    @patch('src.ecuria 1.85.Listbox')
    def test_suppr_heure(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        suppr_heure(mock_listbox_instance, "heure")
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')

    @patch('src.ecuria 1.85.Listbox')
    def test_add_eleve(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        add_eleve(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'élève')

    @patch('src.ecuria 1.85.Listbox')
    def test_add_cheval(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        add_cheval(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'cheval')

    @patch('src.ecuria 1.85.Listbox')
    def test_suppr_cheval(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        suppr_cheval(mock_listbox_instance)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')

    @patch('src.ecuria 1.85.Listbox')
    def test_suppr_eleve(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        suppr_eleve(mock_listbox_instance)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')

    @patch('src.ecuria 1.85.Listbox')
    def test_add_moniteur(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        add_moniteur(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'moniteur')

    @patch('src.ecuria 1.85.Listbox')
    def test_suppr_moniteur(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        suppr_moniteur(mock_listbox_instance)
        mock_listbox_instance.delete.assert_called_once_with(0, 'end')

    @patch('src.ecuria 1.85.Listbox')
    def test_remplirlisteboxmoniteur(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        remplirlisteboxmoniteur(mock_listbox_instance, "mail")
        mock_listbox_instance.insert.assert_called_once_with('end', 'moniteur')

    @patch('src.ecuria 1.85.open')
    def test_ecrire_fichier_cavalier(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        ecrire_fichier_cavalier("data")
        mock_file.write.assert_called_once_with("data")

    @patch('src.ecuria 1.85.open')
    def test_ecrire_fichier_cheval(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        ecrire_fichier_cheval("data")
        mock_file.write.assert_called_once_with("data")

    @patch('src.ecuria 1.85.open')
    def test_para_enregistrer(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        para_enregistrer("data")
        mock_file.write.assert_called_once_with("data")

    @patch('src.ecuria 1.85.Listbox')
    def test_remplirlisteboxcheval(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        remplirlisteboxcheval(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'cheval')

    @patch('src.ecuria 1.85.Listbox')
    def test_remplirlisteboxeleve(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        remplirlisteboxeleve(mock_listbox_instance)
        mock_listbox_instance.insert.assert_called_once_with('end', 'élève')

    @patch('src.ecuria 1.85.Listbox')
    def test_tri_heure(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        tri_heure(mock_listbox_instance, "jour")
        mock_listbox_instance.insert.assert_called_once_with('end', 'heure')

    @patch('src.ecuria 1.85.Tk')
    def test_interface_default(self, mock_tk):
        interface_default()
        mock_tk.assert_called_once()

    @patch('src.ecuria 1.85.Tk')
    def test_interface_paramete(self, mock_tk):
        interface_paramete()
        mock_tk.assert_called_once()

    @patch('src.ecuria 1.85.pandas')
    def test_lire_fichier_chevaux(self, mock_pandas):
        mock_pandas.read_excel.return_value = "data"
        self.assertEqual(lire_fichier_chevaux("file.xlsx"), "data")

    @patch('src.ecuria 1.85.pandas')
    def test_lire_fichier_cavalier(self, mock_pandas):
        mock_pandas.read_excel.return_value = "data"
        self.assertEqual(lire_fichier_cavalier("jour"), "data")

    @patch('src.ecuria 1.85.Listbox')
    def test_para_inserer_listebox(self, mock_listbox):
        mock_listbox_instance = mock_listbox.return_value
        para_inserer_listebox(mock_listbox_instance, "data")
        mock_listbox_instance.insert.assert_called_once_with('end', 'élément')

    @patch('src.ecuria 1.85.Tk')
    def test_mode_parametre(self, mock_tk):
        mode_parametre()
        mock_tk.assert_called_once()

    @patch('src.ecuria 1.85.Tk')
    def test_mode_default(self, mock_tk):
        mode_default()
        mock_tk.assert_called_once()

    @patch('src.ecuria 1.85.pandas')
    def test_visualiser_fichier_cavalier(self, mock_pandas):
        mock_pandas.read_excel.return_value = "data"
        visualiser_fichier_cavalier("data")

    @patch('src.ecuria 1.85.datetime')
    def test_cmp_heure(self, mock_datetime):
        mock_datetime.now.return_value = "10:00"
        self.assertEqual(cmp_heure("11:00"), 1)

    @patch('src.ecuria 1.85.datetime')
    def test_cmp_heure_semaine(self, mock_datetime):
        mock_datetime.now.return_value = "10:00"
        self.assertEqual(cmp_heure_semaine("11:00"), 1)

    @patch('src.ecuria 1.85.datetime')
    def test_prochain_jour(self, mock_datetime):
        mock_datetime.now.return_value = "2023-10-01"
        self.assertEqual(prochain_jour("semaine", "2023-10-01"), "2023-10-02")

    @patch('src.ecuria 1.85.Tk')
    def test_add_centered_image(self, mock_tk):
        add_centered_image(mock_tk, "image.png", 100, 100)

    @patch('src.ecuria 1.85.Tk')
    def test_set_background(self, mock_tk):
        set_background(mock_tk, "image.png")

    @patch('src.ecuria 1.85.Tk')
    def test_nouveau_fichier(self, mock_tk):
        nouveau_fichier()

    @patch('src.ecuria 1.85.Tk')
    def test_affichejoursam(self, mock_tk):
        affichejoursam()

    @patch('src.ecuria 1.85.Tk')
    def test_affichejoursmer(self, mock_tk):
        affichejoursmer()

    @patch('src.ecuria 1.85.Tk')
    def test_affichejourmar(self, mock_tk):
        affichejourmar()

    @patch('src.ecuria 1.85.Tk')
    def test_choix_date(self, mock_tk):
        choix_date()

    @patch('src.ecuria 1.85.Tk')
    def test_image(self, mock_tk):
        image(mock_tk, "image.png", 100, 100)

    @patch('src.ecuria 1.85.open')
    def test_lire_parametre(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = "data"
        self.assertEqual(lire_parametre(), "data")

    @patch('src.ecuria 1.85.Tk')
    def test_mettre_a_jour(self, mock_tk):
        mettre_a_jour()

    @patch('src.ecuria 1.85.Tk')
    def test_importer_param(self, mock_tk):
        importer_param()

    @patch('src.ecuria 1.85.Tk')
    def test_exporter_param(self, mock_tk):
        exporter_param()

    @patch('src.ecuria 1.85.Event')
    def test_on_enter_pressed(self, mock_event):
        on_enter_pressed(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_delete_pressed(self, mock_event):
        on_delete_pressed(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_right_pressed(self, mock_event):
        on_right_pressed(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_left_pressed(self, mock_event):
        on_left_pressed(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_crtls_pressed(self, mock_event):
        on_crtls_pressed(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_fusion(self, mock_tk):
        fusion()

    @patch('src.ecuria 1.85.Event')
    def test_on_info_clicked(self, mock_event):
        on_info_clicked(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_info2_clicked(self, mock_event):
        on_info2_clicked(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_info_heure_clicked(self, mock_event):
        on_info_heure_clicked(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_info_cheval_clicked(self, mock_event):
        on_info_cheval_clicked(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_on_info_eleve_clicked(self, mock_event):
        on_info_eleve_clicked(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_correction(self, mock_tk):
        correction()

    @patch('src.ecuria 1.85.Tk')
    def test_absent(self, mock_tk):
        absent()

    @patch('src.ecuria 1.85.Event')
    def test_items_selected(self, mock_event):
        items_selected(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_cheval(self, mock_event):
        items_selected_cheval(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_rafraichir(self, mock_tk):
        rafraichir()

    @patch('src.ecuria 1.85.Tk')
    def test_ouvrir_excel(self, mock_tk):
        ouvrir_excel()

    @patch('src.ecuria 1.85.Tk')
    def test_ecrire_mail(self, mock_tk):
        ecrire_mail()

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_heure_cheval(self, mock_event):
        items_selected_heure_cheval(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_action(self, mock_event):
        action(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_remplir_listbox_heure(self, mock_tk):
        remplir_listbox_heure()

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_heure(self, mock_event):
        items_selected_heure(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_eleve(self, mock_event):
        items_selected_eleve(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_cheval(self, mock_event):
        items_selected_cheval(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_action_base(self, mock_tk):
        action_base()

    @patch('src.ecuria 1.85.Event')
    def test_action(self, mock_event):
        action(mock_event)

    @patch('src.ecuria 1.85.Tk')
    def test_sauvegarder_mail(self, mock_tk):
        sauvegarder_mail()

    @patch('src.ecuria 1.85.Tk')
    def test_ouvrir_excel(self, mock_tk):
        ouvrir_excel()

    @patch('src.ecuria 1.85.Tk')
    def test_toggle_entry_nbcarte(self, mock_tk):
        toggle_entry_nbcarte()

    @patch('src.ecuria 1.85.Event')
    def test_on_para_nbcarte_click(self, mock_event):
        on_para_nbcarte_click(mock_event)

    @patch('src.ecuria 1.85.Event')
    def test_items_selected_moniteur(self, mock_event):
        items_selected_moniteur(mock_event)

if __name__ == '__main__':
    unittest.main()