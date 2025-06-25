#!/usr/bin/env "source .venv/bin/activate" python3
import os
import logging 

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# BOILERPLATE - Código repetitivo
#TODO: usar função pra configurar o log e não precisar ficar repetindo
#TODO: Depois disso acima, usar uma lib, biblioteca pra facilitar tudo
# criar nossa propria instancia de logger
log = logging.Logger("logs.py", log_level)  #é só a definição do nome que vai aparecer quando der o erro, posso usar qualquer nome na string
# level
ch = logging.StreamHandler() #console/terminal/stderr
ch.setLevel(log_level)
#formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s ' 
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)


"""
#logging # root logger (loger raiz/principal do programa que está rodando)
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro. Somente um aviso.")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral. Ex. O banco de dados sumiu")
"""

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))

