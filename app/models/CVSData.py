from app.models.ResponseModels import BaseResponse


class CVSData(BaseResponse):
    class CVSInfo(BaseResponse):
        url: str

    data: list[CVSInfo]
