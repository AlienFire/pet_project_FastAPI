from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models import UserCreate, Showuser
from app.db.dals import UserDAL
from app.db.session import get_db


user_router = APIRouter()


async def _create_new_user(body: UserCreate, db) -> Showuser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email,
            )
            return Showuser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active,
            )


@user_router.post("/", response_model=Showuser)
async def create_user(
    body: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> Showuser:
    return await _create_new_user(body, db)
