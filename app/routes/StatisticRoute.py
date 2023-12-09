from app import app
from app.models.Statistic import Statistic
from app.responseBuilder import response_ok
from db.queries.statistic import get_statistics_all_count


@app.route('api/statistics/', methods=['GET'])
async def get_statistics() -> Statistic:
    result = await get_statistics_all_count()

    return Statistic(**response_ok(result))


