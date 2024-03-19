# -- code: utf-8 --
import datetime
import pytz
import hashlib

class BaseModel:
    """
    description:
        Class to keep out some methods and variables. The domain valorant has some releative
        and each path need to be classifier
    """
    def __init__(self, data: str) -> None:
        self.created_at = datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%dT%H:%M:%S')
        self.hash_validator = hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    