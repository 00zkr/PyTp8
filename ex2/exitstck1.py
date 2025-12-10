from contextlib import ExitStack
from datetime import datetime
from connectionmanager import ConnectionManager


with ExitStack() as stack:
    log = stack.enter_context(open("log.txt", "a"))
    conn = stack.enter_context(ConnectionManager("Serveur X"))
    log.write(f"[{datetime.now()}] Tâche effectuée sur {conn.service_name}.\n")