from ..random_strings import font_str as font
from . import *


@hell_cmd(pattern="font(?:\s|$)([\s\S]*)")
async def font(event):
    hell = await eor(event, "Changing font...")
    flag = event.text[6:]
    rply = await event.get_reply_message()
    if not rply:
        return await eod(hell, "Nothing given to change!")
    old = rply.text
    normie = font.normal.split(" ")
    if str(flag) == "01":
        to_ = font.one.split(" ")
        prev = "  ".join(old).lower()
        for normal in prev:
            if normal in normie:
                new_ = to_[normie.index(normal)]
                new = prev.replace(normal, to_)
    await hell.edit(new)
    
