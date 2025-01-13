
# trocar print pelo logger

from loguru import logger

logger.add("meu_app.log",level = 'CRITICAL')

def soma(x, y):
    try:
        soma = x + y
        logger.info(soma)
        return soma
    except:
        logger.critical("Digite um valor correto")

print(soma(2,15))