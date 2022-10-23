from typing import Optional
from logger import log
from json import loads
PREFIX: str = loads(open('config.json', 'r').read())['prefix']

def validate(msg: str) -> bool:
    if msg.startswith(PREFIX):
        return True
    return False

def processCommands(msg: str) -> Optional[str]:
    if not validate(msg):
        log('commandProcessor').error(f"'{msg}' is not a valid command.")
        return