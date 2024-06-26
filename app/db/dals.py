from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User

# BLOCK FOR INTERACTION WITH DATABASE IN BUSINESS CONTENT#


class UserDAL:
    """Data Access Lager for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: str) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
