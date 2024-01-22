
################## You have to Create the tables in Mysql ##########################
from tkinter import messagebox
from datetime import datetime
from tkinter import *
from tkinter import ttk , font
import mysql.connector
from PIL import Image, ImageTk
class CentreDeSante:
    def __init__(self, master):
        self.master = master
        master.title('CENTRE DE SANTE SMAALA')
        master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}+0+0')


        self.images = {}  # Dictionnaire pour stocker les objets PhotoImage

        self.create_main_window()

    def create_main_window(self):
        frameTop = Frame(self.master, bg='#1b9ea4')
        frameTop.pack(fill=X)
        custom_font = font.Font(family="tahoma", size=50, weight="bold", slant="italic")

        # Créer un label avec la police italique
        Label(frameTop, text='CENTRE DE SANTE SMAALA', bg='#77B5FE', fg='white', font=custom_font, pady=80).pack(fill=X)

        frame_principale = Frame(self.master)
        frame_principale.pack(fill=X)

        # Boutons
        self.init_bouton(frame_principale, 'images/Unite.png', 'Unite', self.create_unite_info)
        self.init_bouton(frame_principale, 'images/patient_couleur.png', 'Patient', self.create_patient_info)
        self.init_bouton(frame_principale, 'images/rendez-vous-medical.png', 'Rendez-vous', self.create_rendez_vous_info)
        self.init_bouton(frame_principale, 'images/ordonnance_couleur.png', 'Ordonnance', self.create_ordonnance_info)
        self.init_bouton(frame_principale, 'images/bilan-de-sante.png', 'Fiche', self.create_fiche_info)

    def init_bouton(self, parent, image_path, text, command):
        frame = Frame(parent, pady=200, padx=100)
        frame.grid(row=0, column=len(parent.grid_slaves()) + 1)

        img = Image.open(image_path)
        img.thumbnail((140, 120))
        self.images[image_path] = ImageTk.PhotoImage(img)  # Stocker l'objet PhotoImage dans le dictionnaire

        label_img = Label(frame, image=self.images[image_path])
        label_img.pack()

        bouton = Button(frame, text=text, padx=3, command=command)
        bouton.pack(fill =X)

    def create_patient_info(self):
        fenetre_patient = Toplevel(self.master)
        fenetre_patient.title('CENTRE DE SANTE SMAALA - Info Patient')
        fenetre_patient.geometry(f'{fenetre_patient.winfo_screenwidth()}x{fenetre_patient.winfo_screenheight()}+0+0')
        #########" AJOUT LES LABELS  LES TITIRES .... ##############
                #==============DROITE==============#
        droite= Frame(fenetre_patient,bg='#77B5FE',width=600)
        droite.pack(fill=Y,side=LEFT)
        label_titre_informations = Label(droite, text="Entrer les Informations du patient : ", bg='#77B5FE', font=('Arial', 20, 'bold'),fg='white',bd = 0)
        label_titre_informations.place(x=10, y=40)
        label_nom_patient = Label(droite, text="Nom du patient", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_nom_patient.place(x=10, y=100)

        label_prenom_patient = Label(droite, text="Prenom du patient", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_prenom_patient.place(x=10, y=140)

        label_num_patient = Label(droite, text="Numero du dossier", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                    bd=0)
        label_num_patient.place(x=10, y=180)

        label_annes_patient = Label(droite, text="Annee de naissance", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                   bd=0)
        label_annes_patient.place(x=10, y=220)

        label_date_patient = Label(droite, text="Date de naissance", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_date_patient.place(x=10, y=260)

        # Entry
        self.entry_font = font.Font(size=14)
        self.entry_nom_patient = Entry(droite,font = self.entry_font)
        self.entry_nom_patient.place(x=270, y=100)

        self.entry_prenom_patient = Entry(droite,font = self.entry_font)
        self.entry_prenom_patient.place(x=270, y=140)

        self.entry_dnumero_patient = Entry(droite, font = self.entry_font)
        self.entry_dnumero_patient.place(x=270, y=180)

        self.entry_annee_patient = Entry(droite, font=self.entry_font)
        self.entry_annee_patient.place(x=270, y=220)

        self.entry_date_patient = Entry(droite, font = self.entry_font)
        self.entry_date_patient.place(x=270, y=260)
        # Button

        search = Button(droite,text='chercher',command = self.chercher,width=25)
        search.place(x =30,y = 295)

        actualiser = Button(droite, text='actualiser', command=self.actualiser,width=25)
        actualiser.place(x=30, y=323)
        afficher = Button(droite, text='Afficher tout', command=self.afficher_tout,width=25)
        afficher.place(x=290, y=295)
        ############# AJOUT un Patient #######################
        ajlable = Label(droite, text='Ajouter un nouveau patient',padx=10,pady=10,fg='white',bg = '#77B5FE',font=('tahoma',20,'bold'))
        ajlable.place(x = 100 , y = 350)
        # ...

        # Labels et Entry pour les informations d'ajout d'un nouveau patient
          ################"     LABELS       ##########################"
        label_id_patient = Label(droite, text="Id du patient", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_patient.place(x=10, y=400)
        self.entry_id_patient = Entry(droite, font=self.entry_font)
        self.entry_id_patient.place(x=270, y=400)


        label_nom_patient1 = Label(droite, text="Nom du patient", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_nom_patient1.place(x=10, y=440)
        self.entry_nom_patient1 = Entry(droite, font=self.entry_font)
        self.entry_nom_patient1.place(x=270, y=440)


        label_prenom_patient1 = Label(droite, text="Prenom du patient", bg='#77B5FE', font=('tahoma', 17), fg='white',bd=0)
        label_prenom_patient1.place(x=10, y=480)
        self.entry_prenom_patient1 = Entry(droite, font=self.entry_font)
        self.entry_prenom_patient1.place(x=270, y=480)


        label_couverture_medicale = Label(droite, text="Couverture médicale", bg='#77B5FE', font=('tahoma', 17),fg='white', bd=0)
        label_couverture_medicale.place(x=10, y=520)
        options_couverture_medicale = ["Mutualiste", "Ramediste"]
        self.couverture_medicale_var = StringVar()
        #self.couverture_medicale_var.set(options_couverture_medicale[0])  # Valeur par défaut
        dropdown_couverture_medicale = ttk.Combobox(droite, textvariable=self.couverture_medicale_var,
                                                    values=options_couverture_medicale, font=('tahoma', 14))
        dropdown_couverture_medicale.place(x=270, y=520)


        label_lien_de_parente = Label(droite, text="Lien de parenté", bg='#77B5FE', font=('tahoma', 17), fg='white',bd=0)
        label_lien_de_parente.place(x=10, y=560)
        options_lien_de_parente = ["Époux", "Épouse", "Fille", "Fils"]
        self.lien_de_parente_var = StringVar()
        #self.lien_de_parente_var.set(options_lien_de_parente[0])  # Valeur par défaut
        dropdown_lien_de_parente = ttk.Combobox(droite, textvariable=self.lien_de_parente_var,
                                                values=options_lien_de_parente, font=('tahoma', 14))
        dropdown_lien_de_parente.place(x=270, y=560)


        label_prof_patient = Label(droite, text="Profession du patient", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_prof_patient.place(x=10, y=600)
        self.entry_prof_patient = Entry(droite, font=self.entry_font)
        self.entry_prof_patient.place(x=270, y=600)


        label_niveau_scolaire = Label(droite, text="Niveau scolaire", bg='#77B5FE', font=('tahoma', 17), fg='white',bd=0)
        label_niveau_scolaire.place(x=10, y=640)
        options_niveau_scolaire = ["Supérieur", "Secondaire", "Primaire"]
        self.niveau_scolaire_var = StringVar()
        #self.niveau_scolaire_var.set(options_niveau_scolaire[0])  # Valeur par défaut
        dropdown_niveau_scolaire = ttk.Combobox(droite, textvariable=self.niveau_scolaire_var,
                                                values=options_niveau_scolaire, font=('tahoma', 14))
        dropdown_niveau_scolaire.place(x=270, y=640)


        label_datenais_patient = Label(droite, text="Date naissance", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_datenais_patient.place(x=10, y=680)
        self.entry_datenais_patient = Entry(droite, font=self.entry_font)
        self.entry_datenais_patient.place(x=270, y=680)


        label_num_dossier = Label(droite, text="Num dossier", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_num_dossier.place(x=10, y=720)
        self.entry_num_dossier = Entry(droite, font=self.entry_font)
        self.entry_num_dossier.place(x=270, y=720)


        label_date_ouverture = Label(droite, text="Date d'ouverture", bg='#77B5FE', font=('tahoma', 17), fg='white',bd=0)
        label_date_ouverture.place(x=10, y=760)
        self.entry_date_ouverture = Entry(droite, font=self.entry_font)
        self.entry_date_ouverture.place(x=270, y=760)


        label_medecin_id = Label(droite, text="Medecin famille", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_medecin_id.place(x=10, y=800)
        options_medecin_id = ["1", "2", "3"]
        self.medecin_id_var = StringVar()
        #self.medecin_id_var.set(options_medecin_id[0])  # Valeur par défaut
        dropdown_medecin_id = ttk.Combobox(droite, textvariable=self.medecin_id_var, values=options_medecin_id,
                                           font=('tahoma', 14))
        dropdown_medecin_id.place(x=270, y=800)
        ajouter_patient = Button(droite, text='Ajouter Patient', command=self.ajout_patient,width=25)
        ajouter_patient.place(x=270, y=840)

        # ...

        ################ Gauche ######################

        gauche = Frame(fenetre_patient, width=1200)
        gauche.pack(fill=BOTH, side=RIGHT)
        frame_info_patient = Frame(gauche, height=240,width=1200)
        frame_info_patient.place(x = 0 , y = 0,width=1200)
        Label(frame_info_patient, text='INFO PATIENT', pady=35, padx=30, font=('tahoma', 20, 'bold'), bg='#77B5FE',
              fg='white').place(x=400,y=0)
        bouton_tri_nom = Button(droite, text="Trier par nom", command=self.tri_par_nom , width=25)
        bouton_tri_nom.place(x = 10, y = 10)

        # Ajout du bouton de tri par date de naissance
        bouton_tri_date_naissance = Button(droite, text="Trier par date de naissance",width=25,
                                              command=self.tri_par_date_naissance)
        bouton_tri_date_naissance.place(x = 270 , y = 10)


        # Label(gauche,text='Information patient \n cela reste modifiable',pady=20,padx=20,font=('tahoma',20,'bold'),bg='gray',fg='white').place(x=320,y=40)
        ######### AJOUT DU TREEVIEW ###############
        self.table = ttk.Treeview(gauche, columns=('id', 'nom', 'prenom' , 'couverture medicale' , 'lien de parente' ,'profession','niveau scolaire' , 'numero dossier','date naissance'), height=30, show='headings')
        self.table.place(x = 0,y = 100)
        self.table.heading("id", text="id")  # Colonne d'ID (si nécessaire)
        self.table.heading("nom", text="nom")
        self.table.heading("prenom", text="prenom")
        self.table.heading("couverture medicale", text="couverture medicale")
        self.table.heading("lien de parente", text="lien de parente")
        self.table.heading('profession',text='profession')
        self.table.heading('niveau scolaire',text='niveau scolaire')
        self.table.heading('numero dossier',text='numero dossier')
        self.table.heading("date naissance", text="date naissance")
        self.table.column('id', width=50)
        self.table.column('nom',width=100)
        self.table.column('prenom', width=100)
        self.table.column('couverture medicale', width=150)
        self.table.column('lien de parente', width=110)
        self.table.column('profession',width=110)
        self.table.column('niveau scolaire',width=110)
        self.table.column('numero dossier',width = 110)
        self.table.column('date naissance',width=130)
        scrollbar = ttk.Scrollbar(gauche, orient="vertical", command=self.table.yview)
        scrollbar.place(x =970,y=100,width=20,height=635)

    def mettre_a_jour(self,newdata):
        for row in self.table.get_children():
            self.table.delete(row)
        for row in newdata:
            self.table.insert('', 'end', values=row)

    def tri_par_nom(self):
        # Récupérer toutes les données actuellement affichées dans le Treeview
        children = self.table.get_children()
        all_data = [self.table.item(child, 'values') for child in children]

        # Trier les données par la colonne 'nom'
        data_trie = sorted(all_data, key=lambda x: str(x[1]).casefold())

        # Mettre à jour le Treeview avec les données triées
        self.mettre_a_jour(data_trie)

    def tri_par_date_naissance(self):
            # Tri par la colonne "Date de naissance"
            children = self.table.get_children()
            all_data = [self.table.item(child, 'values') for child in children]


            data_trie = sorted(all_data,
                               key=lambda x: x[8])

            # Mettre à jour le Treeview avec les données triées
            self.mettre_a_jour(data_trie)

    def tri_par_id(self):
        children = self.table.get_children()
        all_data = [self.table.item(child, 'values') for child in children]

        # Trier les données par la colonne 'nom'
        data_trie = sorted(all_data,
                           key=lambda x: x[0])  # Supposons que la colonne 'nom' est à l'index 1

        # Mettre à jour le Treeview avec les données triées
        self.mettre_a_jour(data_trie)

    ##### les methodes pour les fonctionnalites des bouttons #####
    def afficher_tout(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()
        sql =('select * from patient')
        mycursor.execute(sql)
        res = mycursor.fetchall()
        for i in res:
            self.table.insert('','end',values=i)
        my_data.close()
        mycursor.close()
    def actualiser(self):
        for row in self.table.get_children():
            self.table.delete(row)

    def chercher(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()
        sql = 'SELECT * FROM patient WHERE '
        conditions= []
        val = []


        if self.entry_nom_patient.get():
            conditions.append('nom_patient = %s')
            val.append(self.entry_nom_patient.get())
        if self.entry_prenom_patient.get():
            conditions.append('prenom_patient = %s')
            val.append(self.entry_prenom_patient.get())
        if self.entry_dnumero_patient.get():
            conditions.append('dossier_numero = %s')
            val.append(int(self.entry_dnumero_patient.get()))
        if self.entry_annee_patient.get():
            conditions.append('YEAR(date_naissance) = %s')
            val.append(int(self.entry_annee_patient.get()))
        if self.entry_date_patient.get():
            entry_date = self.entry_date_patient.get()
            conditions.append('date_naissance = %s')
            valeur_date = datetime.strptime(entry_date, "%Y-%m-%d").date()
            val.append(valeur_date)


        if not conditions:
            messagebox.showinfo(title='Erreur', message="Veuillez remplir au moins un champ.")
            return

        sql += ' AND '.join(conditions)


        mycursor.execute(sql, tuple(val))
        res = mycursor.fetchall()

        for i in res:
            self.table.insert('', 'end', values=i)
        if not res:
            messagebox.showinfo('Erreur',"Aucun patient trouvé avec les informations fournies.")
        my_data.close()
        mycursor.close()


    def ajout_patient(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()

        # Récupérer les valeurs des Entry
        valeur_id_patient = self.entry_id_patient.get()
        valeur_nom_patient = self.entry_nom_patient1.get()
        valeur_prenom_patient = self.entry_prenom_patient1.get()
        valeur_couverture_medicale = self.couverture_medicale_var.get()
        valeur_lien_de_parente = self.lien_de_parente_var.get()
        valeur_prof_patient = self.entry_prof_patient.get()
        valeur_niveau_scolaire = self.niveau_scolaire_var.get()
        valeur_datenais_patient = self.entry_datenais_patient.get()
        valeur_num_dossier = self.entry_num_dossier.get()
        valeur_date_ouverture = self.entry_date_ouverture.get()
        valeur_medecin_id = self.medecin_id_var.get()

        if not valeur_id_patient or not valeur_nom_patient or not valeur_prenom_patient or not valeur_datenais_patient or not valeur_num_dossier:
            messagebox.showinfo('Erreur', "Veuillez remplir tous les champs obligatoires.")
            my_data.close()
            return
        existing_ids = mycursor.execute("SELECT * FROM patient WHERE pid = %s", (int(self.entry_id_patient.get()),))
        existing_ids = mycursor.fetchone()
        if existing_ids:
            messagebox.showinfo('Erreur', "L'ID du patient est déjà pris.")
            return

        if not valeur_prof_patient:
            valeur_prof_patient = None

        if not valeur_niveau_scolaire:
            valeur_niveau_scolaire = None

        try:
            # Ajout du patient sans le numéro de dossier
            if not valeur_date_ouverture :
                sql_insert_patient = "INSERT INTO patient (pid, nom_patient, prenom_patient, couverture_medicale, " \
                                     "lien_de_parente, profession, niveau_scolaire,dossier_numero,date_naissance) " \
                                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"

                values_patient = (
                    int(valeur_id_patient), valeur_nom_patient, valeur_prenom_patient, valeur_couverture_medicale,
                    valeur_lien_de_parente, valeur_prof_patient, valeur_niveau_scolaire, int(valeur_num_dossier),
                    datetime.strptime(valeur_datenais_patient, "%Y-%m-%d").date())
                mycursor.execute(sql_insert_patient, values_patient)
                my_data.commit()
            else :
                existing_ids1 = mycursor.execute("SELECT * FROM patient WHERE dossier_numero = %s",
                                                (int(valeur_num_dossier),))
                existing_ids1 = mycursor.fetchone()
                if existing_ids1:
                    messagebox.showinfo('Erreur', "L'ID du dossier est déjà pris.")
                    return

                sql_insert_patient = "INSERT INTO patient (pid, nom_patient, prenom_patient, couverture_medicale, " \
                                 "lien_de_parente, profession, niveau_scolaire, date_naissance) " \
                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                values_patient = (
                int(valeur_id_patient), valeur_nom_patient, valeur_prenom_patient, valeur_couverture_medicale,
                valeur_lien_de_parente, valeur_prof_patient, valeur_niveau_scolaire,
                datetime.strptime(valeur_datenais_patient, "%Y-%m-%d").date())
                mycursor.execute(sql_insert_patient, values_patient)
                my_data.commit()

            # Ajout du dossier familial
                sql_insert_dossier = "INSERT INTO dossier_famille (dnumero, date_ouverture, medecin_id, patient_id) " \
                                 "VALUES (%s, %s, %s, %s)"
                values_dossier_famille = (int(valeur_num_dossier),
                                      datetime.strptime(valeur_date_ouverture, "%Y-%m-%d").date(),
                                      int(valeur_medecin_id),
                                      int(valeur_id_patient))
                mycursor.execute(sql_insert_dossier, values_dossier_famille)
                my_data.commit()

            # Mise à jour du patient avec l'ID du dossier familial
                sql_update_patient = "UPDATE patient SET dossier_numero = %s WHERE pid = %s"
                values_update_patient = (int(valeur_num_dossier), int(valeur_id_patient))
                mycursor.execute(sql_update_patient, values_update_patient)
                my_data.commit()

                messagebox.showinfo('Succès', "Patient ajouté avec succès.")
        except Exception as e:
            messagebox.showinfo('Erreur', f"Erreur lors de l'ajout du patient : {e}")
        finally:
            my_data.close()
            mycursor.close()

    def misarendervous(self,newdata):
        for row in self.table_rendez_vous.get_children():
            self.table_rendez_vous.delete(row)
        for row in newdata:
            self.table_rendez_vous.insert('', 'end', values=row)

    def triedate(self):
        children = self.table_rendez_vous.get_children()
        all_data = [self.table_rendez_vous.item(child, 'values') for child in children]

        # Trier les données par la colonne 'date ordonnance'
        data_trie = sorted(all_data, key=lambda x: datetime.strptime(x[1], '%Y-%m-%d'))

        # Mettre à jour le Treeview avec les données triées
        self.misarendervous(data_trie)
    def triId(self):
        children = self.table_rendez_vous.get_children()
        all_data = [self.table_rendez_vous.item(child, 'values') for child in children]

        # Trier les données par la colonne 'id'
        data_trie = sorted(all_data, key=lambda x: int(x[0]))

        # Mettre à jour le Treeview avec les données triées
        self.misarendervous(data_trie)
    def create_rendez_vous_info(self):
        fenetre_rendez_vous = Toplevel(self.master)
        fenetre_rendez_vous.title('CENTRE DE SANTE SMAALA - Rendez-vous')
        fenetre_rendez_vous.geometry(
            f'{fenetre_rendez_vous.winfo_screenwidth()}x{fenetre_rendez_vous.winfo_screenheight()}+0+0')

        # Frame droit pour l'interface utilisateur
        droite = Frame(fenetre_rendez_vous, bg='#77B5FE', width=600)
        droite.pack(fill=Y, side=LEFT)

        # Labels, entries et boutons pour la recherche des rendez-vous
        label_titre_informations = Label(droite, text="Entrer les Informations sur le rendez vous : ", bg='#77B5FE',
                                         font=('Arial', 20, 'bold'), fg='white', bd=0)
        label_titre_informations.place(x=10, y=40)
        botonatri = Button(droite,text ='trie par date',width=25,command=self.triedate)
        botonatri.place(x = 10,y = 10)
        botonatri1 = Button(droite,text='trie par id',command=self.triId,width=25)
        botonatri1.place(x = 270, y = 10)
        # ...

        # Boutons

        search_button = Button(droite, text='Chercher', command=self.chercher_rendez_vous, width=25)
        search_button.place(x=30, y=350)

        show_all_button = Button(droite, text='Afficher tout', command=self.afficher_tout_rendez_vous, width=25)
        show_all_button.place(x=290, y=350)

        refresh_button = Button(droite, text='Actualiser', command=self.actualiser_rendez_vous, width=25)
        refresh_button.place(x=30, y=380)
        ajlable = Label(droite, text='Prendre un RDV', padx=10, pady=10, fg='white', bg='#77B5FE',
                        font=('tahoma', 20, 'bold'))
        ajlable.place(x=150, y=410)

        # Frame gauche pour afficher les rendez-vous
        gauche = Frame(fenetre_rendez_vous, width=1200)
        gauche.pack(fill=BOTH, side=RIGHT)
        frame_info_rdv = Frame(gauche, height=240, width=1200)
        frame_info_rdv.place(x=-210, y=0, width=1200)
        Label(frame_info_rdv, text='INFO RDV', pady=35, padx=30, font=('tahoma', 20, 'bold'), bg='#77B5FE',
              fg='white').place(x = 600,y = 0)

        # Table pour afficher les rendez-vous
        self.table_rendez_vous = ttk.Treeview(gauche,
                                         columns=('rid', 'date_rendez_vous', 'horaire', 'nom_patient', 'prenom_patient',
                                                  'nom_service'),
                                         height=30, show='headings')
        self.table_rendez_vous.place(x=0, y=100)

        # Colonnes de la table
        self.table_rendez_vous.heading("rid", text="RID")
        self.table_rendez_vous.heading("date_rendez_vous", text="Date Rendez-vous")
        self.table_rendez_vous.heading("horaire", text="Horaire")
        self.table_rendez_vous.heading("nom_patient", text="Nom du Patient")
        self.table_rendez_vous.heading("prenom_patient", text="Prénom du Patient")
        self.table_rendez_vous.heading("nom_service", text="Nom du Service")

        # Largeurs des colonnes
        self.table_rendez_vous.column('rid', width=50)
        self.table_rendez_vous.column('date_rendez_vous', width=200)
        self.table_rendez_vous.column('horaire', width=200)
        self.table_rendez_vous.column('nom_patient', width=155)
        self.table_rendez_vous.column('prenom_patient', width=155)
        self.table_rendez_vous.column('nom_service', width=200)

        # Ajout de la scrollbar
        scrollbar = ttk.Scrollbar(gauche, orient="vertical", command=self.table_rendez_vous.yview)
        scrollbar.place(x=960, y=100, width=20, height=635)

        # Configuration de la scrollbar
        self.table_rendez_vous.configure(yscrollcommand=scrollbar.set)


        label_date_annee = Label(droite, text="Année du RDV :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_date_annee.place(x=10, y=100)

        label_date_mois = Label(droite, text="Mois du RDV :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_date_mois.place(x=10, y=140)

        label_date_jour = Label(droite, text="Jour du RDV :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_date_jour.place(x=10, y=180)

        label_horaire = Label(droite, text="Horaire (h-*h*) :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_horaire.place(x=10, y=220)

        label_numero_patient = Label(droite, text="Numéro Patient :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                     bd=0)
        label_numero_patient.place(x=10, y=260)

        label_service = Label(droite, text="Numéro Service :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_service.place(x=10, y=300)
        self.entry_font = font.Font(size=14)
        self.entry_date_annee = Entry(droite, font=self.entry_font)
        self.entry_date_annee.place(x=270, y=100)

        self.entry_date_mois = Entry(droite, font=self.entry_font)
        self.entry_date_mois.place(x=270, y=140)

        self.entry_date_jour = Entry(droite, font=self.entry_font)
        self.entry_date_jour.place(x=270, y=180)

        self.entry_horaire = Entry(droite, font=self.entry_font)
        self.entry_horaire.place(x=270, y=220)

        self.entry_numero_patient = Entry(droite, font=self.entry_font)
        self.entry_numero_patient.place(x=270, y=260)

        self.entry_service = Entry(droite, font=self.entry_font)
        self.entry_service.place(x=270, y=300)


        # Entrées pour la création du rendez-vous
        label_id_rdv = Label(droite, text="ID RDV :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_rdv.place(x=10, y=460)

        label_date_rdv = Label(droite, text="Date RDV(YYYY-MM-DD):", bg='#77B5FE', font=('tahoma', 17), fg='white',
                               bd=0)
        label_date_rdv.place(x=10, y=500)

        label_horaire_rdv = Label(droite, text="Horaire (h-*h*) :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                  bd=0)
        label_horaire_rdv.place(x=10, y=540)

        label_patient_id_rdv = Label(droite, text="ID du Patient :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                     bd=0)
        label_patient_id_rdv.place(x=10, y=580)

        label_service_id_rdv = Label(droite, text="ID du Service :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                     bd=0)
        label_service_id_rdv.place(x=10, y=620)

        self.entry_id_rdv = Entry(droite, font=self.entry_font)
        self.entry_id_rdv.place(x=270, y=460)

        self.entry_date_rdv = Entry(droite, font=self.entry_font)
        self.entry_date_rdv.place(x=270, y=500)

        self.entry_horaire_rdv = Entry(droite, font=self.entry_font)
        self.entry_horaire_rdv.place(x=270, y=540)

        self.entry_patient_id_rdv = Entry(droite, font=self.entry_font)
        self.entry_patient_id_rdv.place(x=270, y=580)

        self.entry_service_id_rdv = Entry(droite, font=self.entry_font)
        self.entry_service_id_rdv.place(x=270, y=620)

        # Bouton pour créer le rendez-vous
        create_rdv_button = Button(droite, text='Créer Rendez-vous', command=lambda: self.creer_rendez_vous(
            self.entry_id_rdv.get(), self.entry_date_rdv.get(), self.entry_horaire_rdv.get(),
            self.entry_patient_id_rdv.get(), self.entry_service_id_rdv.get()
        ), width=25)
        create_rdv_button.place(x=30, y=660)




    def chercher_rendez_vous(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()

        sql = '''
        SELECT rid, date_rendez_vous, horaire, nom_patient, prenom_patient, nom_service
        FROM rendez_vous
        JOIN patient ON rendez_vous.patient_id = patient.pid
        JOIN service ON rendez_vous.service_id = service.sid
        WHERE
        '''

        conditions = []
        val = []

        if self.entry_date_annee.get():
            conditions.append('YEAR(date_rendez_vous) = %s')
            val.append(int(self.entry_date_annee.get()))
        if self.entry_date_mois.get():
            conditions.append('MONTH(date_rendez_vous) = %s')
            val.append(int(self.entry_date_mois.get()))
        if self.entry_date_jour.get():
            conditions.append('DAY(date_rendez_vous) = %s')
            val.append(int(self.entry_date_jour.get()))
        if self.entry_horaire.get():
            conditions.append('horaire = %s')
            val.append(self.entry_horaire.get())
        if self.entry_numero_patient.get():
            conditions.append('patient_id = %s')
            val.append(int(self.entry_numero_patient.get()))
        if self.entry_service.get():
            conditions.append('service_id = %s')
            val.append(int(self.entry_service.get()))

        if not conditions:
            messagebox.showinfo(title='Erreur', message="Veuillez remplir au moins un champ.")
            return

        sql += ' AND '.join(conditions)


        mycursor.execute(sql, tuple(val))
        res = mycursor.fetchall()

        for i in res:
            self.table_rendez_vous.insert('', 'end', values=i)
        if not res:
            messagebox.showinfo('Erreur', "Les informations fournies sont erronées")
        my_data.close()
        mycursor.close()

    def afficher_tout_rendez_vous(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()
        sql =  '''
                SELECT rid, date_rendez_vous, horaire, nom_patient, prenom_patient, nom_service
                FROM rendez_vous
                JOIN patient ON rendez_vous.patient_id = patient.pid
                JOIN service ON rendez_vous.service_id = service.sid
                '''

        mycursor.execute(sql)
        res = mycursor.fetchall()
        for i in res:
            self.table_rendez_vous.insert('', 'end', values=i)
        my_data.close()
        mycursor.close()

    def actualiser_rendez_vous(self):
        for row in self.table_rendez_vous.get_children():
            self.table_rendez_vous.delete(row)

    # Fonction pour créer le rendez-vous
    def creer_rendez_vous(self, id_rdv, date_rdv, horaire_rdv, patient_id_rdv, service_id_rdv):
        try:
            # Vérifier si tous les champs sont remplis
            if not (id_rdv and date_rdv and horaire_rdv and patient_id_rdv and service_id_rdv):
                messagebox.showinfo('Erreur', "Veuillez remplir tous les champs.")
                return

            my_data = mysql.connector.connect(
                host="localhost",
                user="root",
                password="imadnasri123",
                database="centre_de_sante"
            )
            mycursor = my_data.cursor()

            # Vérifier si l'ID du rendez-vous est déjà pris
            mycursor.execute("SELECT * FROM rendez_vous WHERE rid = %s", (id_rdv,))
            existing_id = mycursor.fetchone()
            if existing_id:
                messagebox.showinfo('Erreur', "L'ID du rendez-vous est déjà pris.")
                return

            # Vérifier si la date et l'horaire sont déjà pris
            mycursor.execute(
                "SELECT * FROM rendez_vous WHERE date_rendez_vous = %s AND horaire = %s",
                (date_rdv, horaire_rdv)
            )
            existing_rdv = mycursor.fetchone()
            if existing_rdv:
                messagebox.showinfo('Erreur', "La date et l'horaire sont déjà pris.")
                return


            sql = "INSERT INTO rendez_vous (rid, date_rendez_vous, horaire, patient_id, service_id) VALUES (%s, %s, %s, %s, %s)"
            values = (id_rdv, date_rdv, horaire_rdv, patient_id_rdv, service_id_rdv)
            mycursor.execute(sql, values)
            my_data.commit()
            messagebox.showinfo('Succès', "Le rendez-vous a été créé avec succès.")

        except Exception as e:
            messagebox.showinfo('Erreur', f"Une erreur s'est produite : {str(e)}")
        finally:
            my_data.close()
            mycursor.close()

    def misafiche(self,newdata):
        for row in self.table_fiches.get_children():
            self.table_fiches.delete(row)
        for row in newdata:
            self.table_fiches.insert('', 'end', values=row)

    def triedatefiche(self):
        children = self.table_fiches.get_children()
        all_data = [self.table_fiches.item(child, 'values') for child in children]

        # Trier les données par la colonne 'date ordonnance'
        data_trie = sorted(all_data, key=lambda x: datetime.strptime(x[4], '%Y-%m-%d'))

        # Mettre à jour le Treeview avec les données triées
        self.misafiche(data_trie)
    def triIdfiche(self):
        children = self.table_fiches.get_children()
        all_data = [self.table_fiches.item(child, 'values') for child in children]

        # Trier les données par la colonne 'id'
        data_trie = sorted(all_data, key=lambda x: int(x[0]))

        # Mettre à jour le Treeview avec les données triées
        self.misafiche(data_trie)

    def create_fiche_info(self):
        fenetre_fiche = Toplevel(self.master)
        fenetre_fiche.title('CENTRE DE SANTE SMAALA - Fiche')
        fenetre_fiche.geometry(
            f'{fenetre_fiche.winfo_screenwidth()}x{fenetre_fiche.winfo_screenheight()}+0+0')


        droite = Frame(fenetre_fiche, bg='#77B5FE', width=600)
        droite.pack(fill=Y, side=LEFT)


        label_titre_informations = Label(droite, text="Entrer les Informations sur la fiche : ", bg='#77B5FE',
                                         font=('Arial', 20, 'bold'), fg='white', bd=0)
        label_titre_informations.place(x=10, y=200)


        # Boutons
        search_button = Button(droite, text='Chercher', command=self.chercher_fiche, width=25)
        search_button.place(x=30, y=580)
        botonatrie = Button(droite,text='trie par date',command=self.triedatefiche,width=25).place(x = 10,y=140)
        botonatrie1 = Button(droite,text='trie par id',command=self.triIdfiche,width=25).place(x = 275,y = 140)
        show_all_button = Button(droite, text='Afficher tout', command=self.afficher_tout_fiche, width=25)
        show_all_button.place(x=290, y=580)

        refresh_button = Button(droite, text='Actualiser', command=self.actualiser_fiche, width=25)
        refresh_button.place(x=30, y=640)

        # Frame gauche pour afficher les fiches
        gauche = Frame(fenetre_fiche, width=1200)
        gauche.pack(fill=BOTH, side=RIGHT)
        frame_info_fiche = Frame(gauche, height=240, width=1200)
        frame_info_fiche.place(x=-210, y=0, width=1200)
        Label(frame_info_fiche, text='INFO FICHE', pady=35, padx=30, font=('tahoma', 20, 'bold'), bg='#77B5FE',
              fg='white').place(x = 600,y=0)

        # Table pour afficher les fiches
        self.table_fiches = ttk.Treeview(gauche,
                                    columns=('id_patient','nom_patient','prenom_patient' ,'nom_service', 'date_service'),
                                    height=30, show='headings')
        self.table_fiches.place(x=0, y=100)

        # Colonnes de la table
        self.table_fiches.heading("id_patient", text="Id du Patient")
        self.table_fiches.heading("nom_patient", text="Nom du Patient")
        self.table_fiches.heading("prenom_patient", text="Prenom du Patient")
        self.table_fiches.heading("nom_service", text="Nom du Service")
        self.table_fiches.heading("date_service", text="Date Service")

        # Largeurs des colonnes
        self.table_fiches.column('id_patient', width=200)
        self.table_fiches.column('nom_patient', width=200)
        self.table_fiches.column('prenom_patient', width=200)
        self.table_fiches.column('nom_service', width=200)
        self.table_fiches.column('date_service', width=200)

        # Ajout de la scrollbar
        scrollbar = ttk.Scrollbar(gauche, orient="vertical", command=self.table_fiches.yview)
        scrollbar.place(x=970, y=100, width=20, height=635)

        # Configuration de la scrollbar
        self.table_fiches.configure(yscrollcommand=scrollbar.set)


        label_id_patient = Label(droite, text="ID du Patient :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_patient.place(x=10, y=280)

        label_id_service = Label(droite, text="ID du Service :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_service.place(x=10, y=340)

        # Ajout des labels pour l'année, le mois et le jour du service
        label_annee_service = Label(droite, text="Année du Service :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                    bd=0)
        label_annee_service.place(x=10, y=400)

        label_mois_service = Label(droite, text="Mois du Service :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                   bd=0)
        label_mois_service.place(x=10, y=460)

        label_jour_service = Label(droite, text="Jour du Service :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                   bd=0)
        label_jour_service.place(x=10, y=520)
        self.entry_font = font.Font(size=14)
        self.entry_id_patient = Entry(droite, font=self.entry_font)
        self.entry_id_patient.place(x=270, y=280)

        self.entry_id_service = Entry(droite, font=self.entry_font)
        self.entry_id_service.place(x=270, y=340)

        # Ajout des entries pour l'année, le mois et le jour du service
        self.entry_annee_service = Entry(droite, font=self.entry_font)
        self.entry_annee_service.place(x=270, y=400)

        self.entry_mois_service = Entry(droite, font=self.entry_font)
        self.entry_mois_service.place(x=270, y=460)

        self.entry_jour_service = Entry(droite, font=self.entry_font)
        self.entry_jour_service.place(x=270, y=520)

    def chercher_fiche(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()

        sql = '''
        SELECT pid,nom_patient, prenom_patient,nom_service, date_rendez_vous
        FROM rendez_vous
        JOIN patient ON rendez_vous.patient_id = patient.pid
        JOIN service ON rendez_vous.service_id = service.sid
        WHERE
        '''

        conditions = []
        val = []

        if self.entry_id_patient.get():
            # Vérifier si l'id_patient existe
            mycursor.execute('SELECT COUNT(*) FROM patient WHERE pid = %s', (int(self.entry_id_patient.get()),))
            if mycursor.fetchone()[0] == 0:
                messagebox.showinfo(title='Erreur', message="L'ID du patient n'existe pas.")
                my_data.close()
                mycursor.close()
                return
            conditions.append('patient_id = %s')
            val.append(int(self.entry_id_patient.get()))

        if self.entry_id_service.get():
            # Vérifier si l'id_service existe
            mycursor.execute('SELECT COUNT(*) FROM service WHERE sid = %s', (int(self.entry_id_service.get()),))
            if mycursor.fetchone()[0] == 0:
                messagebox.showinfo(title='Erreur', message="L'ID du service n'existe pas.")
                my_data.close()
                mycursor.close()
                return
            conditions.append('service_id = %s')
            val.append(int(self.entry_id_service.get()))



        # Ajout des conditions pour la recherche par année, mois, jour du service
        if self.entry_annee_service.get():
            conditions.append('YEAR(date_rendez_vous) = %s')
            val.append(int(self.entry_annee_service.get()))

        if self.entry_mois_service.get():
            conditions.append('MONTH(date_rendez_vous) = %s')
            val.append(int(self.entry_mois_service.get()))

        if self.entry_jour_service.get():
            conditions.append('DAY(date_rendez_vous) = %s')
            val.append(int(self.entry_jour_service.get()))

        if not conditions:
            messagebox.showinfo(title='Erreur', message="Veuillez remplir au moins un champ.")
            my_data.close()
            mycursor.close()
            return

        sql += ' AND '.join(conditions)

        # Créer la valeur pour la requête préparée
        mycursor.execute(sql, tuple(val))
        res = mycursor.fetchall()

        if not res:
            messagebox.showinfo('Aucun résultat', "Aucun service n'a été fait avec ces critères.")
        else:
            for i in res:
                self.table_fiches.insert('', 'end', values=i)

        my_data.close()
        mycursor.close()

    def afficher_tout_fiche(self):
            my_data = mysql.connector.connect(
                host="localhost",
                user="root",
                password="imadnasri123",
                database="centre_de_sante"
            )
            mycursor = my_data.cursor()
            sql = ' SELECT pid ,nom_patient,prenom_patient, nom_service, date_rendez_vous FROM rendez_vous JOIN patient ON rendez_vous.patient_id = patient.pid JOIN service ON rendez_vous.service_id = service.sid'
            mycursor.execute(sql)
            res = mycursor.fetchall()

            for i in res:
                self.table_fiches.insert('', 'end', values=i)
            my_data.close()
            mycursor.close()


    def actualiser_fiche(self):
        for row in self.table_fiches.get_children():
            self.table_fiches.delete(row)



    def create_ordonnance_info(self):
        fenetre_ordonnance = Toplevel(self.master)
        fenetre_ordonnance.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_ordonnance.geometry(f'{fenetre_ordonnance.winfo_screenwidth()}x{fenetre_ordonnance.winfo_screenheight()}+0+0')
        droite = Frame(fenetre_ordonnance, bg='#77B5FE', width=600)
        droite.pack(fill=Y, side=LEFT)





        # Frame gauche pour afficher les rendez-vous
        gauche = Frame(fenetre_ordonnance, width=1200)
        gauche.pack(fill=BOTH, side=RIGHT)
        frame_info_rdv = Frame(gauche, height=240, width=1200)
        frame_info_rdv.place(x=-210, y=0, width=1200)
        Label(frame_info_rdv, text='INFO ORDONNACE', pady=35, padx=30, font=('tahoma', 20, 'bold'), bg='#77B5FE',
              fg='white').place(x = 550,y = 0)

        botonatrie2 = Button(droite, text='trie par date', command=self.tri_par_id, width=25)
        botonatrie2.place(x=10, y=30)
        search_button = Button(droite, text='Chercher', command=self.chercher_ordonnance, width=25)
        search_button.place(x=30, y=420)

        show_all_button = Button(droite, text='Afficher tout', command=self.afficher_tout_ordonnace, width=25)
        show_all_button.place(x=290, y=420)

        refresh_button = Button(droite, text='Actualiser', command=self.actualiser_ordonnance, width=25)
        refresh_button.place(x=30, y=780)


        self.table_ordonnance = ttk.Treeview(gauche,
                                              columns=(
                                              'id', 'date ordonnace', 'nom medicament', 'type certificat','type analyse','nom_patient', 'prenom_patient',
                                              'nom medecin','prenom medecin'),
                                              height=30, show='headings')
        self.table_ordonnance.place(x=0, y=100)


        self.table_ordonnance.heading("id", text="ID")
        self.table_ordonnance.heading("date ordonnace", text="Date d'ordonnance")
        self.table_ordonnance.heading("nom medicament", text="Nom du médicament")
        self.table_ordonnance.heading("type certificat", text="Type de certificat")
        self.table_ordonnance.heading("type analyse", text="Type d'analyse")
        self.table_ordonnance.heading("nom_patient", text="Nom du patient")
        self.table_ordonnance.heading("prenom_patient", text="Prénom du patient")
        self.table_ordonnance.heading("nom medecin", text="Nom du médecin")
        self.table_ordonnance.heading("prenom medecin", text="Prénom du médecin")

        # Largeurs des colonnes
        self.table_ordonnance.column('id', width=30)
        self.table_ordonnance.column('date ordonnace', width=120)
        self.table_ordonnance.column('nom medicament', width=130)
        self.table_ordonnance.column('type certificat', width=130)
        self.table_ordonnance.column('type analyse', width=130)
        self.table_ordonnance.column('nom_patient', width=100)
        self.table_ordonnance.column('prenom_patient', width=100)
        self.table_ordonnance.column('nom medecin', width=110)
        self.table_ordonnance.column('prenom medecin', width=110)

        # Ajout de la scrollbar
        scrollbar = ttk.Scrollbar(gauche, orient="vertical", command=self.table_ordonnance.yview)
        scrollbar.place(x=970, y=100, width=20, height=635)

        # Configuration de la scrollbar
        self.table_ordonnance.configure(yscrollcommand=scrollbar.set)

        label_info = Label(droite, text="Entrer les informations de l'ordonnance :", bg='#77B5FE',font=('Arial', 20, 'bold'), fg='white')
        label_info.place(x =10,y=60)

        label_id_patient = Label(droite, text="ID Patient :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_patient.place(x=10, y=100)

        label_id_docteur = Label(droite, text="ID Docteur :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_id_docteur.place(x=10, y=140)

        label_jour_ordonnance = Label(droite, text="Jour Ordonnance :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                      bd=0)
        label_jour_ordonnance.place(x=10, y=180)

        label_mois_ordonnance = Label(droite, text="Mois Ordonnance :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                      bd=0)
        label_mois_ordonnance.place(x=10, y=220)

        label_annee_ordonnance = Label(droite, text="Année Ordonnance :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                       bd=0)
        label_annee_ordonnance.place(x=10, y=260)

        label_type_certificat = Label(droite, text="Type Certificat :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                      bd=0)
        label_type_certificat.place(x=10, y=300)

        label_type_analyse = Label(droite, text="Type Analyse :", bg='#77B5FE', font=('tahoma', 17), fg='white', bd=0)
        label_type_analyse.place(x=10, y=340)

        label_nom_medicament = Label(droite, text="Nom Médicament :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                     bd=0)
        label_nom_medicament.place(x=10, y=380)


        self.entry_font  = font.Font(size = 14)
        self.entry_id_patient = Entry(droite, font=self.entry_font)
        self.entry_id_patient.place(x=270, y=100)


        doctor_choices = ['1', '2', '3']
        self.doctor_id_var = StringVar()
        #self.doctor_id_var.set(doctor_choices[1])  # Valeur par défaut
        doctor_combobox = ttk.Combobox(droite, textvariable=self.doctor_id_var, values=doctor_choices, font=('tahoma',14))
        doctor_combobox.place(x=270, y=140)

        # Entrées pour le jour, le mois et l'année de l'ordonnance
        self.entry_jour_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_jour_ordonnance.place(x=270, y=180)

        self.entry_mois_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_mois_ordonnance.place(x=270, y=220)

        self.entry_annee_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_annee_ordonnance.place(x=270, y=260)

        # Utilisation d'un combobox pour le type de certificat
        certificat_choices = ['Certificat de repos', 'Certificat daptitude physique']
        self.certificat_var = StringVar()
        #self.certificat_var.set(certificat_choices[0])  # Valeur par défaut
        cert_combobox = ttk.Combobox(droite, textvariable=self.certificat_var, values=certificat_choices,
                                     font=('tahoma',14))
        cert_combobox.place(x=270, y=300)




        ###########################AJOUT ENTRY###################################
        label_ajout_ordonnance = Label(droite, text="Ajout d'une ordonnance :", bg='#77B5FE',
                                       font=('Arial', 20, 'bold'), fg='white')
        label_ajout_ordonnance.place(x=10, y=450)

        label_num_ordonnance = Label(droite, text="Numéro d'ordonnance :", bg='#77B5FE', font=('tahoma', 17),
                                     fg='white', bd=0)
        label_num_ordonnance.place(x=10, y=500)

        label_date_ordonnance = Label(droite, text="Date d'ordonnance :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                      bd=0)
        label_date_ordonnance.place(x=10, y=540)

        label_id_patient_ordonnance = Label(droite, text="ID Patient :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                            bd=0)
        label_id_patient_ordonnance.place(x=10, y=580)

        label_id_docteur_ordonnance = Label(droite, text="ID Docteur :", bg='#77B5FE', font=('tahoma', 17), fg='white',
                                            bd=0)
        label_id_docteur_ordonnance.place(x=10, y=620)

        label_type_certificat_ordonnance = Label(droite, text="Type Certificat :", bg='#77B5FE', font=('tahoma', 17),
                                                 fg='white', bd=0)
        label_type_certificat_ordonnance.place(x=10, y=660)

        label_type_analyse_ordonnance = Label(droite, text="Type Analyse :", bg='#77B5FE', font=('tahoma', 17),
                                              fg='white', bd=0)
        label_type_analyse_ordonnance.place(x=10, y=700)

        label_nom_medicament_ordonnance = Label(droite, text="Nom Médicament :", bg='#77B5FE', font=('tahoma', 17),
                                                fg='white', bd=0)
        label_nom_medicament_ordonnance.place(x=10, y=740)


        self.entry_font = font.Font(size=14)
        self.entry_num_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_num_ordonnance.place(x=270, y=500)

        self.entry_date_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_date_ordonnance.place(x=270, y=540)

        self.entry_id_patient_ordonnance = Entry(droite, font=self.entry_font)
        self.entry_id_patient_ordonnance.place(x=270, y=580)

        doctor_choices = ['1', '2', '3']
        self.entry_id_docteur_ordonnance = StringVar()

        doctor_combobox2 = ttk.Combobox(droite, textvariable=self.entry_id_docteur_ordonnance, values=doctor_choices,font=('tahoma', 14))
        doctor_combobox2.place(x=270, y=620)

        # Utilisation d'un combobox pour le type de certificat
        certificat_choices_ordonnance = ['Certificat de repos', 'Certificat daptitude physique']
        self.certificat_var_ordonnance = StringVar()
        # self.certificat_var_ordonnance.set(certificat_choices_ordonnance[0])  # Valeur par défaut
        cert_combobox_ordonnance = ttk.Combobox(droite, textvariable=self.certificat_var_ordonnance,
                                                values=certificat_choices_ordonnance, font=('tahoma', 14))
        cert_combobox_ordonnance.place(x=270, y=660)

        # Utilisation d'un combobox pour le type d'analyse
        analyse_choices_ordonnance = ['Analyse glycemie ajeun', 'Analyse creatinine', 'Analyse NFS', 'Analyse groupage']
        self.analyse_var_ordonnance = StringVar()
        # self.analyse_var_ordonnance.set(analyse_choices_ordonnance[0])  # Valeur par défaut
        analyse_combobox_ordonnance = ttk.Combobox(droite, textvariable=self.analyse_var_ordonnance,
                                                   values=analyse_choices_ordonnance, font=('tahoma', 14))
        analyse_combobox_ordonnance.place(x=270, y=700)

        medicament_choices = ['Amoxil 500mg', 'Doliprane 500mg', 'Xenid 50mg',
                              'Ventoline spray', 'insuline rapide', 'Altec 5mg', 'Exidep 10mg', 'Amiprim 50mg',
                              'Alpraz 0,5mg']
        self.entry_nom_medicament_ordonnance = StringVar()
        medi1_combobox = ttk.Combobox(droite, textvariable=self.entry_nom_medicament_ordonnance, values=medicament_choices,
                                     font=('tahoma', 14))
        medi1_combobox.place(x=270, y=740)

        # Bouton Ajouter
        bouton_ajouter = Button(droite, text="Ajouter", command=self.ajouter_ordonnance, width = 25)
        bouton_ajouter.place(x=270, y=780)

        # Utilisation d'un combobox pour le type d'analyse
        analyse_choices = ['Analyse glycemie ajeun', 'Analyse creatinine', 'Analyse NFS', 'Analyse groupage']
        self.analyse_var = StringVar()
        #self.analyse_var.set(analyse_choices[0])  # Valeur par défaut
        analyse_combobox = ttk.Combobox(droite, textvariable=self.analyse_var, values=analyse_choices,font=('tahoma',14))

        analyse_combobox.place(x=270, y=340)

        # Entrée pour le nom du médicament
        medicament_choices = ['Amoxil 500mg', 'Doliprane 500mg', 'Xenid 50mg',
                              'Ventoline spray', 'insuline rapide', 'Altec 5mg', 'Exidep 10mg', 'Amiprim 50mg',
                              'Alpraz 0,5mg']
        self.entry_nom_medicament = StringVar()
        medi_combobox = ttk.Combobox(droite, textvariable=self.entry_nom_medicament, values=medicament_choices,
                                        font=('tahoma', 14))
        medi_combobox.place(x=270, y=380)







        ################################## LES METHODES ###########################################

    def mettre_a_jour1(self, newdata):
        for row in self.table_ordonnance.get_children():
            self.table_ordonnance.delete(row)
        for row in newdata:
            self.table_ordonnance.insert('', 'end', values=row)

    def tri_par_date(self):
        children = self.table_ordonnance.get_children()
        all_data = [self.table_ordonnance.item(child, 'values') for child in children]

        # Trier les données par la colonne 'date ordonnance'
        data_trie = sorted(all_data, key=lambda x: datetime.strptime(x[1], '%Y-%m-%d'))

        # Mettre à jour le Treeview avec les données triées
        self.mettre_a_jour1(data_trie)

    def tri_par_id(self):
        children = self.table_ordonnance.get_children()
        all_data = [self.table_ordonnance.item(child, 'values') for child in children]

        # Trier les données par la colonne 'id'
        data_trie = sorted(all_data, key=lambda x: int(x[0]))

        # Mettre à jour le Treeview avec les données triées
        self.mettre_a_jour1(data_trie)



    def ajouter_ordonnance(self):
        my_data = None
        mycursor = None

        try:
            my_data = mysql.connector.connect(
                host="localhost",
                user="root",
                password="imadnasri123",
                database="centre_de_sante"
            )
            mycursor = my_data.cursor()

            # Récupérer les valeurs des champs d'entrée
            num_ordonnance = self.entry_num_ordonnance.get()
            date_ordonnance = self.entry_date_ordonnance.get()

            # Vérifier si les champs obligatoires sont vides
            id_patient_str = self.entry_id_patient_ordonnance.get()
            id_docteur_str = self.entry_id_docteur_ordonnance.get()

            if num_ordonnance:
                check_query = "SELECT * FROM ordonnance WHERE onumero = %s"
                mycursor.execute(check_query, (int(num_ordonnance),))
                existing_ordonnance = mycursor.fetchone()

                if existing_ordonnance:
                    messagebox.showerror("Erreur", f"Le numéro d'ordonnance {num_ordonnance} est déjà pris.")
                    return

            if not num_ordonnance or not date_ordonnance or not id_patient_str or not id_docteur_str:
                # Afficher un message d'erreur
                messagebox.showerror("Erreur", "Veuillez remplir les champs obligatoires.")
                return

            num_ordonnance = int(num_ordonnance)

            # Vérifier si les ID sont des valeurs numériques
            try:
                id_patient = int(id_patient_str)
                id_docteur = int(id_docteur_str)
            except ValueError:
                messagebox.showerror("Erreur", "Les ID Patient et Docteur doivent être des valeurs numériques.")
                return

            certificat = self.certificat_var_ordonnance.get()
            analyse = self.analyse_var_ordonnance.get()
            nom_medicament = self.entry_nom_medicament_ordonnance.get()

            # Vérifier si les champs facultatifs sont vides et affecter une valeur nulle si nécessaire
            if not certificat:
                certificat = None

            if not analyse:
                analyse = None

            if not nom_medicament:
                nom_medicament = None

            insert_query = "INSERT INTO ordonnance (onumero, date_ordonnance, patient_id, medecin_id, type_certificat, type_analyse, nom_commerciale_medicaments) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_values = (
            num_ordonnance, datetime.strptime(date_ordonnance, "%Y-%m-%d"), id_patient, id_docteur, certificat, analyse, nom_medicament)
            mycursor.execute(insert_query, insert_values)

            # Committer la transaction
            my_data.commit()

            # Afficher un message de succès
            messagebox.showinfo("Succès", "Ordonnance ajoutée avec succès.")
        except Exception as e:
            # En cas d'erreur, rollback pour annuler toutes les opérations
            my_data.rollback()
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout de l'ordonnance : {str(e)}")
        finally:
            # Fermer la connexion et le curseur après l'exécution de la requête
            if mycursor:
                mycursor.close()
            if my_data:
                my_data.close()

    # La fonction execute_query est fictive, vous devez adapter cette partie à votre code

    def afficher_tout_ordonnace(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()

        sql = """
            SELECT onumero,date_ordonnance, nom_commerciale_medicaments, 
                   type_certificat, type_analyse, 
                   nom_patient,  prenom_patient,
                   nom_medecin,prenom_medecin
            FROM ordonnance
             JOIN patient ON ordonnance.patient_id = pid
             JOIN medecin ON ordonnance.medecin_id = mid
        """
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print(res)
        for i in res:
            self.table_ordonnance.insert('', 'end', values=i)
        my_data.close()
        mycursor.close()
    def actualiser_ordonnance(self):
        for row in self.table_ordonnance.get_children():
            self.table_ordonnance.delete(row)

    def chercher_ordonnance(self):
        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            password="imadnasri123",
            database="centre_de_sante"
        )
        mycursor = my_data.cursor()

        sql = '''
        SELECT onumero, date_ordonnance, nom_commerciale_medicaments, type_certificat, type_analyse,
               nom_patient, prenom_patient, nom_medecin, prenom_medecin
        FROM ordonnance
        JOIN patient ON ordonnance.patient_id = patient.pid
        JOIN medecin ON ordonnance.medecin_id = medecin.mid
        WHERE
        '''

        conditions = []
        val = []

        if self.entry_annee_ordonnance.get():
            conditions.append('YEAR(date_ordonnance) = %s')
            val.append(int(self.entry_annee_ordonnance.get()))
        if self.entry_mois_ordonnance.get():
            conditions.append('MONTH(date_ordonnance) = %s')
            val.append(int(self.entry_mois_ordonnance.get()))
        if self.entry_jour_ordonnance.get():
            conditions.append('DAY(date_ordonnance) = %s')
            val.append(int(self.entry_jour_ordonnance.get()))
        if self.certificat_var.get():
            conditions.append('type_certificat = %s')
            val.append(self.certificat_var.get())
        if self.analyse_var.get():
            conditions.append('type_analyse = %s')
            val.append(self.analyse_var.get())
        if self.entry_nom_medicament.get():
            conditions.append('nom_medicament = %s')
            val.append(self.entry_nom_medicament.get())
        if self.entry_id_patient.get():
            conditions.append('patient_id = %s')
            val.append(int(self.entry_id_patient.get()))
        if self.doctor_id_var.get():
            conditions.append('medecin_id = %s')
            val.append(int(self.doctor_id_var.get()))

        if not conditions:
            messagebox.showinfo(title='Erreur', message="Veuillez remplir au moins un champ.")
            return

        sql += ' AND '.join(conditions)

        print("Requête SQL générée :", sql)  # Ajout de cet affichage

        # Exécuter la requête SQL
        mycursor.execute(sql, tuple(val))
        res = mycursor.fetchall()

        # Ajouter les résultats à la table
        for i in res:
            self.table_ordonnance.insert('', 'end', values=i)

        if not res:
            messagebox.showinfo('Erreur', "Les informations fournies sont erronées")

        my_data.close()
        mycursor.close()

    #################################################################################"""
    def create_unite_info(self):
        fenetre_unite = Toplevel(self.master)
        fenetre_unite.title('CENTRE DE SANTE SMAALA - Info Unite')
        fenetre_unite.geometry(f'{fenetre_unite.winfo_screenwidth()}x{fenetre_unite.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_unite, bg='#1b9ea4')
        frameTop.pack(fill=X)
        self.custom_font = font.Font(family="tahoma", size=50, weight="bold", slant="italic")
        Label(frameTop, text='UNITES CENTRE DE SANTE SMAALA', bg='#77B5FE', fg='white', font=self.custom_font, pady=80).pack(
            fill=X)

        frame_principale = Frame(fenetre_unite)
        frame_principale.pack(fill=X)

        # Boutons
        self.init_bouton_unite(frame_principale, 'images/accueil.png', 'Accueil', self.create_accueil_info)
        self.init_bouton_unite(frame_principale, 'images/psychiatre.png', 'Psychiatrie', self.create_psychiatrie_info)
        self.init_bouton_unite(frame_principale, 'images/pharmacie.png', 'pharmacie', self.create_pharmacie_info)
        self.init_bouton_unite(frame_principale, 'images/docteur.png', 'Medecine generale', self.create_medecine_info)
        self.init_bouton_unite(frame_principale, 'images/soins.png', 'Soins',self.create_soin_info)
        self.init_bouton_unite(frame_principale, 'images/maman.png', 'Mere & Enfant',self.create_mere_enfant_info)

    def init_bouton_unite(self, parent, image_path, text, command):
        frame = Frame(parent, pady=200, padx=70)
        frame.grid(row=0, column=len(parent.grid_slaves()) + 1)

        img = Image.open(image_path)
        img.thumbnail((140, 120))
        self.images[image_path] = ImageTk.PhotoImage(img)  # Stocker l'objet PhotoImage dans le dictionnaire

        label_img = Label(frame, image=self.images[image_path])
        label_img.pack()

        bouton = Button(frame, text=text, padx=3, command=command)
        bouton.pack(fill=X)
    def create_accueil_info(self):
        fenetre_accueil = Toplevel(self.master)
        fenetre_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_accueil.geometry(
            f'{fenetre_accueil.winfo_screenwidth()}x{fenetre_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='ACCUEIL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)

        frame_principale = Frame(fenetre_accueil)
        frame_principale.pack(fill=X)
        self.init_bouton_accueil(frame_principale, 'images/service_accueil.png', 'Service', self.create_service_accueil_info)
        self.init_bouton_accueil(frame_principale, 'images/personnel_accueil.png', 'Personnel', self.create_personnel_accueil_info)
    def init_bouton_accueil(self, parent, image_path, text, command):
        frame = Frame(parent, pady=200, padx=290)
        frame.grid(row=0, column=len(parent.grid_slaves()) + 1)

        img = Image.open(image_path)
        img.thumbnail((200, 200))
        self.images[image_path] = ImageTk.PhotoImage(img)  # Stocker l'objet PhotoImage dans le dictionnaire

        label_img = Label(frame, image=self.images[image_path])
        label_img.pack()

        bouton = Button(frame, text=text, padx=3, command=command)
        bouton.pack(fill=X)


    def create_service_accueil_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='SERVICE', bg='#77B5FE', fg='white',font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale, 'images/reception.png', 'Reception')
        self.init_label(frame_principale, 'images/orientation.png', 'Orientation')
    def create_personnel_accueil_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PERSONNEL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale,'images/infirmiereacc.png','Kaylouch fatma')
        self.init_label(frame_principale, 'images/infirmiereacc1.png', 'Ahloch oum')
    def init_label(self,parent, image_path, text):
        frame = Frame(parent, pady=200, padx=275)
        frame.grid(row=0, column=len(parent.grid_slaves()) + 1)

        img = Image.open(image_path)
        img.thumbnail((200, 200))
        self.images[image_path] = ImageTk.PhotoImage(img)  # Stocker l'objet PhotoImage dans le dictionnaire

        label_img = Label(frame,text = text ,image=self.images[image_path],font=('tahoma',20),compound=TOP)
        label_img.pack()

    def create_psychiatrie_info(self):
        fenetre_psy = Toplevel(self.master)
        fenetre_psy.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_psy.geometry(
            f'{fenetre_psy.winfo_screenwidth()}x{fenetre_psy.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_psy, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PSYCHIATRIE', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_psy)
        frame_principale.pack(fill=X)
        self.init_label2(frame_principale, 'images/psychiatreservice.png', 'Service Psy')
        self.init_label2(frame_principale, 'images/docpsy.png', 'Farkous Abdelah')
        self.init_label2(frame_principale, 'images/infirmiereacc.png', 'El alami Hasnae')

    def init_label2(self,parent, image_path, text):
        frame = Frame(parent, pady=200, padx=175)
        frame.grid(row=0, column=len(parent.grid_slaves()) + 1)

        img = Image.open(image_path)
        img.thumbnail((180, 180))
        self.images[image_path] = ImageTk.PhotoImage(img)  # Stocker l'objet PhotoImage dans le dictionnaire

        label_img = Label(frame,text = text ,image=self.images[image_path],font=('tahoma',20),compound=TOP)
        label_img.pack()
    def create_pharmacie_info(self):
        fenetre_pharmacie = Toplevel(self.master)
        fenetre_pharmacie.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_pharmacie.geometry(
            f'{fenetre_pharmacie.winfo_screenwidth()}x{fenetre_pharmacie.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_pharmacie, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PHARMACIE', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_pharmacie)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale, 'images/medicament.png', 'Distribution medicament')
        self.init_label(frame_principale, 'images/infirmierephar.png', 'Faik Aya')
    def create_medecine_info(self):
        fenetre_medecine = Toplevel(self.master)
        fenetre_medecine.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_medecine.geometry(
            f'{fenetre_medecine.winfo_screenwidth()}x{fenetre_medecine.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_medecine, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='MEDECINE GENERAL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)

        frame_principale = Frame(fenetre_medecine)
        frame_principale.pack(fill=X)
        self.init_bouton_accueil(frame_principale, 'images/service_accueil.png', 'Service',
                                 self.create_service_med_info)
        self.init_bouton_accueil(frame_principale, 'images/personnel_accueil.png', 'Personnel',
                                 self.create_personnel_med_info)
    def create_service_med_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='SERVICE', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale, 'images/chronique.png', 'Maladie Chronique')
        self.init_label(frame_principale, 'images/consultation.png', 'Consultation Curative')
    def create_personnel_med_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PERSONNEL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale,'images/docteurchro.png','Dadas Aziz')
        self.init_label(frame_principale, 'images/docteurcons.png', 'Boubker Rafik')
    def create_soin_info(self):
        fenetre_soin = Toplevel(self.master)
        fenetre_soin.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_soin.geometry(
            f'{fenetre_soin.winfo_screenwidth()}x{fenetre_soin.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_soin, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='SOINS', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_soin)
        frame_principale.pack(fill=X)
        self.init_bouton_accueil(frame_principale, 'images/service_soin.png', 'Service',
                                 self.create_service_soin_info)
        self.init_bouton_accueil(frame_principale, 'images/personnel_soin.png', 'Personnel',
                                 self.create_personnel_soin_info)
    def create_service_soin_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='SERVICE', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label2(frame_principale, 'images/tension.png', 'Tension/Sucre')
        self.init_label2(frame_principale, 'images/pansement.png', 'Pansement')
        self.init_label2(frame_principale, 'images/injection.png', 'Injection')
    def create_personnel_soin_info(self):
        fenetre_service_accueil = Toplevel(self.master)
        fenetre_service_accueil.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_service_accueil.geometry(
            f'{fenetre_service_accueil.winfo_screenwidth()}x{fenetre_service_accueil.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_service_accueil, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PERSONNEL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_service_accueil)
        frame_principale.pack(fill=X)
        self.init_label(frame_principale, 'images/infirmieresoin1.png', 'Dafir Asmae')
        self.init_label(frame_principale, 'images/infirmieresoin2.png', 'Onis Chaimaa')
    def create_mere_enfant_info(self):
        fenetre_mere_enfant = Toplevel(self.master)
        fenetre_mere_enfant.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_mere_enfant.geometry(f'{fenetre_mere_enfant.winfo_screenwidth()}x{fenetre_mere_enfant.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_mere_enfant, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='MERE & ENFANT', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_mere_enfant)
        frame_principale.pack(fill=X)
        self.init_bouton_accueil(frame_principale, 'images/service_accueil.png', 'Service',
                                 self.create_service_mere_info)
        self.init_bouton_accueil(frame_principale, 'images/personnel_accueil.png', 'Personnel',
                                 self.create_personnel_mere_info)
    def create_personnel_mere_info(self):
        fenetre_psy = Toplevel(self.master)
        fenetre_psy.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_psy.geometry(
            f'{fenetre_psy.winfo_screenwidth()}x{fenetre_psy.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_psy, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='PERSONNEL', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_psy)
        frame_principale.pack(fill=X)
        self.init_label2(frame_principale, 'images/infirmieremere1.png', 'Touil Majida')
        self.init_label2(frame_principale, 'images/infirmieremere2.png', 'Nasri Ahlam')
        self.init_label2(frame_principale, 'images/infirmieremere3.png', 'Douma Soumia')
    def create_service_mere_info(self):
        fenetre_psy = Toplevel(self.master)
        fenetre_psy.title('CENTRE DE SANTE SMAALA - Info Ordonnance')
        fenetre_psy.geometry(
            f'{fenetre_psy.winfo_screenwidth()}x{fenetre_psy.winfo_screenheight()}+0+0')
        frameTop = Frame(fenetre_psy, bg='#1b9ea4')
        frameTop.pack(fill=X)
        Label(frameTop, text='SERVICE', bg='#77B5FE', fg='white', font=self.custom_font,
              pady=80).pack(
            fill=X)
        frame_principale = Frame(fenetre_psy)
        frame_principale.pack(fill=X)
        self.init_label2(frame_principale, 'images/enceinte.png', 'Suivie de Grossesse')
        self.init_label2(frame_principale, 'images/vaccin.png', 'Vaccination')
        self.init_label2(frame_principale, 'images/famille.png', 'Plannification Famille')
def main():
    fenetre_principale = Tk()
    CentreDeSante(fenetre_principale)
    fenetre_principale.mainloop()

if __name__ == "__main__":
    main()


