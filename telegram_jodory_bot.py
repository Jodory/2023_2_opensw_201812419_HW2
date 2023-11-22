from datetime import datetime
import telegram
import asyncio
import platform
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import locale

# 시스템에 따라 'ko_KR.utf8'과 같이 적절한 로케일로 변경
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 

async def push_alert(bot, chat_id):
    time_data = datetime.now().strftime("현재 시간은 %H:%M:%S 입니다.")
    await bot.sendMessage(chat_id, time_data)

async def main():
    # bot 관련 설정
    bot_name = "jodory_bot"
    chat_id = "6646178775"
    bot_token = "6373203231:AAFovm19A_ggoL7GZH3Dz3h5Tkntfv6liw4"

    # 비동기 관련 설정(윈도우 전용)
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # 봇 객체 생성
    bot = telegram.Bot(bot_token)

    # 스케줄러 등록
    test = AsyncIOScheduler()
    # 매 초마다 출력 max instances를 10으로 두어 작업이 최대 10개의 인스턴스를 가질 수 있도록 설정
    # test.add_job(push_alert, 'cron', hour='*', minute='*', second='*', args=[bot, chat_id], max_instances=10)

    # 6시부터 
    test.add_job(push_alert, 'cron', hour='6-22', minute='*/30', args=[bot, chat_id])

    # 스케줄러 시작
    test.start()

    while True:
        await asyncio.sleep(1000)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        AsyncIOScheduler().shutdown()
        pass