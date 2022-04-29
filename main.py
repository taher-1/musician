import asyncio
from pytgcalls import idle
from config import call_py
from MusicTelethon.التشغيل import arq
async def main():
    await call_py.start()
    print("""    ------------------
   | ميوزك تليثون الان شغال ! |
    https://t.me/Dragon_2022_D
    ------------------"""    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
