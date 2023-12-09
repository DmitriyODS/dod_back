from app.models.ResponseModels import BaseResponse


class Statistic(BaseResponse):
    class GetStatistics(BaseResponse):
        all_count: int
        mk_web: int
        mk_game: int

    data: list[GetStatistics]