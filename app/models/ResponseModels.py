from enum import Enum
from pydantic import BaseModel


class ResponseStatus(Enum):
    success = 'success'
    error = 'error'


class BaseResponse(BaseModel):
    status: ResponseStatus
