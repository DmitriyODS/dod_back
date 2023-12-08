from enum import Enum
from pydantic import BaseModel


class ResponseStatus(Enum):
    success = 'success'
    error = 'error'


class BaseResponse(BaseModel):
    status: ResponseStatus


class User(BaseResponse):
    user_id: int
    fio: str
    city: str
    school: str
    email: str
    type_mk: int
