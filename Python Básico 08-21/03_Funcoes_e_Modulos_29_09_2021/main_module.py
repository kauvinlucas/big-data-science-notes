import logging

log = logging.getLogger(__name__)

def filtr_n_mult(lista, factor = 3):
    por_tres = "Error"
    try:
        impares = [a for a in lista if a%2 !=0]
        por_tres = [n*factor for n in impares]
        log.info('Function has completed executing')
        log.warning('Only uneven integers are filtered!')
        if factor == 3:
            log.debug('Factor is set to 3 by default')
    except:
        log.error('Error executing the function!')
    else:
        return por_tres
