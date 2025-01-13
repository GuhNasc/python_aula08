from loguru import logger

logger.debug("Aviso ao dev")
logger.info("Informaçoes importantes sobre o processo")
logger.warning("Aviso que algo vai parar de funcionar no futuro")
logger.error("Um erro aconteceu")
logger.critical("Aconteceu um erro de aborta a aplicação")