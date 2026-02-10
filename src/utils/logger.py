import logging

def get_logger(name):
    return logging.getLogger(f"""mysystemdown.{name}""")