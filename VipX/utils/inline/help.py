from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🍁Αԃɱιɳ🍁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🔺Αυƚԋ🔺",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="♨️Ⴆʅσƈƙ♨️",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📣Ɠƈαʂƚ📣",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🚫ƓႦαɳ🚫",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🍷ʅყɾιƈʂ🍷",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️Ρʅαყʅιʂƚ🎙️",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="🎸ᴠσιƈҽ-Ƈԋαƚ🎸",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️Ρʅαყ🕹️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸ʂυԃσ🍸",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️ʂƚαɾƚ⚜️",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
