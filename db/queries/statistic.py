from sqlalchemy import select, func

from app.models.Statistic import Statistic
from app.models.UserModel import User
from db.queries import async_session


async def get_statistics_all_count() -> list[Statistic]:
    async with async_session() as session:
        result = await session.execute(
            select(
                func.count(User.user_id),
                func.count(User.user_id).label(User.type_mk == 1),
                func.count(User.user_id).label(User.type_mk == 2),
                )
        )
        return result.mapping().all()
