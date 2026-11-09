import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None # Corretto con la 'o'

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        # 1. Popoliamo il menu della Biblioteca
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        # 2. Popoliamo il menu del Genere (MANCAVA!)
        generi = self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()

    # CALLBACKS DROPDOWN (quando l'utente clicca su un opzione)
    def cambia_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def cambia_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value # Corretto con la 'o'

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        # 1. Si recuperano i valori attuali (se non selezionati, saranno stringhe vuote o None)
        bib = self._view.dd_biblioteca.value
        gen = self._view.dd_genere.value

        # 2. Chiediamo i dati al Model
        libri = self._model.get_libri_filtrati(bib, gen)

        # 3. Svuotiamo la lista a schermo
        self._view.lista_libri.controls.clear()

        # 4. Se vuota, mostra alert
        if not libri:
            self._view.show_alert("Nessun libro trovato per i filtri selezionati.")
            self._view.update()
            return

        # 5. Altrimenti la popoliamo
        for libro in libri:
            self._view.lista_libri.controls.append(ft.Text(str(libro))) # Corretto!

        self._view.update()