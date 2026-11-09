from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(selfself, biblioteca_id: int | None, genere: str | None) -> list[Libro]:
        #restituisce la lista di libri filtrati per biblioteca e/o genere
        #se un filtro è None, viene ignorato grazie a COALESCE

        #apre la connessione
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        #Crea il cursore come dizionario
        cursor = cnx.cursor(dictionary=True)
        lista_libri =[]

        try:
            #QUERY con COALESCE
            query="""
                SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca
                FROM libro
                WHERE genere = COALESCE( %s, genere)
                AND id_biblioteca = COALESCE( %s, id_biblioteca)
            """

            #esergui passando i valori nell'ordine esatto in cui compaiono
            cursor.execute(query, (genere, biblioteca_id))

            #leggi i risultati
            righe=cursor.fetchall()

            #Crea oggetti DTO
            for riga in righe:
                l = Libro(
                    riga["id"],
                    riga["titolo"],
                    riga["autore"],
                    riga["genere"],
                    riga["anno_pubblicazione"],
                    riga["id_biblioteca"]
                )
                lista_libri.append(l)
            return lista_libri

        except Exception as e:
            print(f"Errore DB nel LibroDAO: {e}")
            return []

        finally:
            #chiude tutto
            cursor.close()
            cnx.close()


















