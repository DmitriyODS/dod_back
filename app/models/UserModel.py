from app.models.ResponseModels import BaseResponse


class User(BaseResponse):
    user_id: int
    fio: str
    email: str
    city: str
    school: str
    is_finished: bool
    type_mk: int


class GetUsersCount(BaseResponse):
    data: list[User]


class GetSelectedUser(BaseResponse):
    data: list[User]
