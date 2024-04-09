espiri_mesaj = [
    "To have this many bots in your room for 6 hours (500g) pm @karainek"
]

laf_mesaj = [
    "Welcome to the grabs! Give it a spin!"
]

sarki_mesaj = [
    "If you want to have bots pm @karainek"
]



rizz_mesaj = [
    "To have this many bot in ur grab room for an hour pm @karainek"
]


    async def send_periodic_messages(self):
        while True:
            try:
                message_list = random.choice([espiri_mesaj, laf_mesaj, sarki_mesaj, rizz_mesaj])
  
                message = random.choice(message_list)
              
                wait_time = random.choice([45, 60, 90])

                await asyncio.sleep(wait_time)

                await self.highrise.chat(message)
            except Exception as e:
                print(f"Caught Periodic Message Error: {e}")