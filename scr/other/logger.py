from logging import getLogger

logger = getLogger(__name__)

def debug_requests(f):
    from logging import getLogger
    logger = getLogger(__name__)

    def inner(*args, **kwargs):
        try:
            logger.info('Обращение в функцию {}'.format(f.__name__))
            return f(*args, **kwargs)
        except Exception:
            logger.exception('Ошибка в обработчике {}'.format(f.__name__))
            raise

    return inner