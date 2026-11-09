from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO


class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca: str, genere: str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        id_bib = None
        if biblioteca and biblioteca != "Nessun filtro":
            id_bib = int(biblioteca)

        gen = None
        if genere and genere != "Nessun filtro":
            gen = genere

        return self._libro_dao.get_libri_filtrati(id_bib, gen)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        tutti_i_libri = self.get_libri_filtrati(None, None)

        # AGGIUNTA DI SICUREZZA: se il DAO restituisce None, evitiamo il crash
        if tutti_i_libri is None:
            return []

        generi_unici = set()
        for libro in tutti_i_libri:
            if libro.genere:
                generi_unici.add(libro.genere)

        return sorted(list(generi_unici))

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # CORREZIONE: get_biblioteche (plurale) non get_biblioteca
        return self._biblioteca_dao.get_biblioteche()