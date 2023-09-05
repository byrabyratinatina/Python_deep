import logging


def log_info_triangle(text: str):
    """
    Метод логирования с заданными параметрами для записи информации
    """
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
             'в строке {lineno:03d} функция "{funcName}()" ' \
             'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(filename='project.log.', filemode='w', format=FORMAT, style='{',
                        level=logging.INFO)
    logger = logging.getLogger('Основной файл')
    logger.info(text)


def log_warning_triangle(text: str):
    """
    Метод логирования с заданными параметрами для записи предупреждения
    """
    FORMAT: str = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
             'в строке {lineno:03d} функция "{funcName}()" ' \
             'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(filename='project.log.', filemode='w', format=FORMAT, style='{',
                        level=logging.WARNING)
    logger = logging.getLogger('Основной файл')
    logger.warning(text)


"""
logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')
"""
