import logging


def configure_logging():
    root = logging.getLogger()
    if root.handlers:
        return
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s")
    handler.setFormatter(fmt)
    root.addHandler(handler)
    root.setLevel(logging.INFO)
