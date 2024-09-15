"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1316963576")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 23744491))
    CHAT = int(os.environ.get("CHAT", "-1002118359848"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1002118359848")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "")
    API_HASH = os.environ.get("API_HASH", "23988a755839feae93c3c3320bc0807f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7213018996:AAFQvdBK0MMZs6RLPiR0BaJyGn2SNYdgQVU") 
    SESSION = os.environ.get("SESSION_STRING", "BQFqT-sAhPyr7NjGBC16maWomVgRNiTulavUpM92HwMuiSPUsRM6CBzm6n4oeV8h2dlKagWfiyC6H4evMAPFaAbofztEKFfqi47dF2XCzeIoemxQNd2MBPgBl8dfGXb0001v5I5vu7_eaGmZElSaN08oWW_sQK53nZafGOcCjK-VM3ZVPxVbgYOjOHYy36iz3UONtg6lz7c9Tbaopb_cOp2VpGXdiXtGLYy4Rv13vyON88fcvD-KlUSTFkS1f1b-z4vzCXzpSASW0aO-VuONOdYogNA7kKjNUvptPrdzi6L-t4nxRJ6uBp8KMLNp5KG5sQuN7kgffBnYRMH_Nf37DI11uWhpowAAAAGnWKzYAA")

