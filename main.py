from highrise import *
from highrise.models import *
from asyncio import run as arun
from flask import Flask
from threading import Thread
from highrise.__main__ import *
import random
import asyncio
import time
from mesajlar import*
from kiy import*

class Bot(BaseBot):
    def __init__(self):
        super().__init__()



    async def on_start(self, session_metadata: SessionMetadata) -> None:
        # Call the method to change outfit every 30 minutes
        await self.change_outfit_periodically()

    async def change_outfit_periodically(self):
        while True:
            await self.change_outfit()
            # Wait for 30 minutes before changing outfit again
            await asyncio.sleep(5)  # 30 minutes in seconds

    async def change_outfit(self):
        # Randomly select active color palettes
        hair_active_palette = random.randint(0, 82)
        skin_active_palette = random.randint(0, 88)
        eye_active_palette = random.randint(0, 49)
        lip_active_palette = random.randint(0, 58)
        
        # Set the outfit with randomly chosen items and color palettes
        outfit = [
            Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=skin_active_palette),
            Item(type='clothing', amount=1, id=random.choice(item_shirt), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_bottom), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_accessory), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_shoes), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_freckle), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_eye), account_bound=False, active_palette=eye_active_palette),
            Item(type='clothing', amount=1, id=random.choice(item_mouth), account_bound=False, active_palette=lip_active_palette),
            Item(type='clothing', amount=1, id=random.choice(item_nose), account_bound=False, active_palette=-1),
            Item(type='clothing', amount=1, id=random.choice(item_hairback), account_bound=False, active_palette=hair_active_palette),
            Item(type='clothing', amount=1, id=random.choice(item_hairfront), account_bound=False, active_palette=hair_active_palette),
            Item(type='clothing', amount=1, id=random.choice(item_eyebrow), account_bound=False, active_palette=hair_active_palette)
        ]
        
        # Set the outfit for the character
        await self.highrise.set_outfit(outfit=outfit)

    
    async def on_chat(self, user: User, message: str) -> None:
        if message.lower() == "random":
            try:
                message_list = random.choice([espiri_mesaj, laf_mesaj, sarki_mesaj, rizz_mesaj])
                message = random.choice(message_list)
                await self.highrise.chat(message)
            except Exception as e:
                print(f"Caught Random Message Error: {e}")

  
    async def run(self, room_id, token) -> None:
        await __main__.main(self, room_id, token)
class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Alive"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()
    
class RunBot():
    room_id = "66120073266df7ec832b3d6a"

  
    bot_tokens = [
    "05cd61bbfce80c4b87a05b9ee14386c5cd1f241e4f0dd4315653134cc02c28b8",
    "b467994561c3a408afb180e54aeefa3725ef2cf886ed6068e9ecd3340529d31c",
    "037589ec724e29569dc66c359cb4d656ee1417cc5cc01637147db321d350c8bd",
    "f661f2ed3910aaa364dd214a5d41b31520c41de74a8a22153eca5c150c5ea34b",
    "88e811e62061c7dd82ac6e53834a70ffc04c71f16b30f9c084e72a52b325a4b1",
    "ea375b8d777669a9976cb88304a7f35ddbad73e6503b39c197a30e7ff0928166",
    "8dbd52b236c88e87a299ff8a02fe2f0dfa713a4402cfa309a6d26bcb5f033be6",
    "f1a613039969782118c701cd873e27960e104ea68395aeffaa0e952aab4c532a",
    "0d876223d08d5984880e61e9aa28ef1809a6eaa7dfe23004e3b2b7e8daa30fd1",
    "766f9f05518821666249bef2e78033ad8141a8d64e61b9b93aa7f03347ca90bc",
    "7708e61d980b46e16f3599147ffe2dea463a66db090d83318ecda10112626f77",
    "d0eb9f1aef9a72439330d68ef1f907759a895eeefcc258e642c2abaeb8a9fe1b",
    "9a523bcbcd1fa8ba6d3583cee0806e95d5547e582c49292a4c58aa862ebafa85",
    "e90d24759234a07a88a2b24ee232e8bb14cc34b92c6f99d93a7a5e91b974231c",
    "e9010a110a2a66ae3aaa1b68ca709a7ffa13058c66627d3034be6429cbf874ca",
    "d328d336d76612c27ab50f569dc9f131a6294181aad468d11307d2985e77df00",
    "83c2964baaa7e26748ba35caf909c50ff58c2022738279b22579b74407ad4416",
    "e5477e0751ec5c4e8a3d401cf07bd20e5d24f882ad49077105998137a421da2f",
    "19c0f3d426a0a7650487df9671e2ffb5f208aa6053f64142db7bfc085ee832a1",
    "b56dcdceb3816c41eb44f8589c68003e36576f469abc4724aea44c4370dc11fc",
    "2afac7f0a75e3056e6809742112b2ade8d2b780daee204cbe50e7915f85d9a94",
    "d2d2d461f503fb2439ba0762fec3c8bd20d3c1e2c7807c7fcc3d7b09323c9d1c",
    "c97486eab63dde5c6e8aa10092b7c843fbf8d803d0fbf252e51872050f82b97d",
    "d58d4cc6ec292d05c2d94ba0254a3d1bbbba3f9336409cf5e2ae2a7b0fda502e",
    "5be74ae3f5c7ec39e4ee1bfb6ffdb3465f3c2dc4b321554565462faa73bae73f",
    "3b0a3e28ac8ccb09406e36836cbc0849b31813298a65905c4c692ff591eeb834",
    "511d98de11346927da061b314ed5be7778b8e4b776d7c3e3bb1f1c13f69ca40d",
    "07c8e98f26636136cbd6ea341310252ff38cad684ab734cb11de133bcd42e732",
    "7d1b5dd0610310a7d4c0736dbdd5bf4481e17216c9982b6e926af94a26736af4",
    "727353235b37c4844aa1d11e5e98871382d069523375b1f9879dd195fc82784e",
    "4062708aebace55869e3088632cc6cec14d12125ad6e1a8e01c389f93fd7258b",
    "46544038fb9749933eedef945049e6a83c2fe3823524290c2c7e878cf28761a3",
    "f443c7ad0e8ce98edfd51c96538010594dfd3000eab0a14763fbeb7d3dd671c0",
    "c11fe016928317b1a85eff7935f88e716fcc9edea160efb02eaf124bfceba0e3",
    "4bd0df3947b89fa25b7552309beebe6abc35d3d28625019a9cc56795ab31ffe0",
    "f9097578b4679d0edfce4f9d8b9d6fe8e688e68757ad4412509c751a1f5b9640",
    "0f766e6bcde4f6b7d7b8c057e4fdbb1b7dd4caea7a23f9387d240bfb881e96e4",
    "e6877603e1bf5ded398acf2574e23fdd9e2677adf6519a0df6ce36f6eebf8e1c"

    ]

    bot_file = "main"
    bot_class = "Bot"

    def __init__(self) -> None:
        self.definitions = []
        for bot_token in self.bot_tokens:
            self.definitions.append(
                BotDefinition(
                    getattr(import_module(self.bot_file), self.bot_class)(),
                    self.room_id, bot_token)
            )
              
    def run_loop(self) -> None:
        while True:
            try:
                arun(main(self.definitions))
            except Exception as e:
                import traceback
                print("Caught an exception:")
                traceback.print_exc()
                time.sleep(1)
                continue


if __name__ == "__main__":
    WebServer().keep_alive()
    RunBot().run_loop()