import logging

logger = logging.getLogger("CheckPrice")

logger.setLevel(level=logging.INFO)

handler = logging.FileHandler("info.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)