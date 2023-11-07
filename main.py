from aiogram import Bot, Dispatcher

from config import TOKEN

from routers import start_router, project_router, bug_router, create_bug_router, edit_bug_router

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot=bot)

dp.include_routers(start_router.router)
dp.include_routers(project_router.router)
dp.include_routers(bug_router.router)
dp.include_routers(create_bug_router.router)
dp.include_routers(edit_bug_router.router)

if __name__ == '__main__':
    dp.run_polling(bot)
