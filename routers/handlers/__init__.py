__all__ = ("router", )

from aiogram import Router

from .command import router as client_router

router = Router(name=__name__)

router.include_router(client_router)
