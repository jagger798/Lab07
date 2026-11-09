from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca


class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self) -> list[Biblioteca]:
        """
        Restituisce la lista di tutte le biblioteche dal database.
        """
        # 1. Apri la connessione
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        # 2. Crea il cursore come dizionario
        cursor = cnx.cursor(dictionary=True)
        lista_biblioteche = []

        try:
            # 3. Esegui la query
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)

            # 4. Leggi i risultati
            righe = cursor.fetchall()

            # 5. Trasforma le righe in oggetti DTO
            for riga in righe:
                b = Biblioteca(riga["id"], riga["nome"], riga["indirizzo"])
                lista_biblioteche.append(b)

            return lista_biblioteche

        except Exception as e:
            print(f"Errore DB nel BibliotecaDAO: {e}")
            return []

        finally:
            cursor.close()
            cnx.close()