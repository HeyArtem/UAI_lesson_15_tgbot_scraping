from .hello import dp
from .test import dp
from .fsmtest import dp
from .buttons_fsm import dp
from .buttons_fsm_inline import dp
from .no_eat import dp

from .error import dp # это реакция бота на неизвестную команду и должна ПОСЛЕ ВСЕХ КОМАНД



# __all__ - список параметров которые можно импортировать с папки users 
__all__ = ['dp']
