from sqlalchemy import select
from app.models.UserModel import User
from db.models.User import Customer
from db.queries import async_session


async def users_count() -> list[User]:
    async with async_session() as session:
        result = await session.execute(
            select(
                Customer.user_id,
                Customer.fio,
                Customer.email,
                Customer.city,
                Customer.school,
                Customer.is_finished,
                Customer.type_mk
            )
        )
        return result.mapping().all()


async def selected_user(user_id: int) -> list[User]:
    async with async_session as session:
        result = await session.execute(
            select(
                Customer.user_id,
                Customer.fio,
                Customer.email,
                Customer.city,
                Customer.school,
                Customer.is_finished,
                Customer.type_mk
            )
            .where(Customer.user_id == user_id)
        )

        return result.mapping().all()