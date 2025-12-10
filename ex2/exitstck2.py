from contextlib import ExitStack
from connectionmanager import ConnectionManager

with ExitStack() as stack:
    log = stack.enter_context(open("log.txt", "a"))
    conn = stack.enter_context(ConnectionManager("Base Y"))
    raise RuntimeError("Erreur de traitement")