from typing import NoReturn
from tortoise import Tortoise


async def setup_db() -> NoReturn:
    await Tortoise.init(
        db_url="sqlite://db.sqlite",
        modules={"models": []}
    )
    await Tortoise.generate_schemas()
