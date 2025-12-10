import csv
from datetime import datetime
from pathlib import Path

class BatchProcessor:
    def __init__(self, csv_path, log_path="journal.log"):
        self.csv_path = Path(csv_path)
        self.log_path = Path(log_path)

    def __enter__(self):
        try:
            self.csv_file = self.csv_path.open("r", newline="", encoding="utf-8")
        except Exception as e:
            raise RuntimeError(f"Impossible d’ouvrir le fichier CSV : {e}")

        try:
            self.log_file = self.log_path.open("a", encoding="utf-8")
        except Exception as e:
            self.csv_file.close()
            raise RuntimeError(f"Impossible d’ouvrir le fichier journal : {e}")

        self._journaliser(f"Démarrage du traitement du fichier {self.csv_path.name}")
        self.reader = csv.reader(self.csv_file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._journaliser(f"Fin du traitement du fichier {self.csv_path.name}")
        try:
            self.csv_file.close()
        except Exception as e:
            self._journaliser(f"Erreur lors de la fermeture du CSV : {e}")
        try:
            self.log_file.close()
        except Exception as e:
            print(f"Erreur lors de la fermeture du journal : {e}")

        return False

    def _journaliser(self, message):
        timestamp = datetime.now()
        self.log_file.write(f"[{timestamp}] {message}\n")
        self.log_file.flush()

    def traiter(self, fonction_traitement):
        for ligne in self.reader:
            try:
                fonction_traitement(ligne)
            except Exception as e:
                self._journaliser(f"Erreur lors du traitement de la ligne {ligne} : {e}")


if __name__ == "__main__":
    with open("operations.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["op1", "val1"])
        writer.writerow(["op2", "val2"])
        writer.writerow(["op3", "val3"])

    def traitement_simule(ligne):
        print(f"Traitement de la ligne : {ligne}")

    with BatchProcessor("operations.csv") as bp:
        bp.traiter(traitement_simule)
