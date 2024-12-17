from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# 1-usul:
Menukeybord = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Menu', callback_data='menu'),
            
        ],
    ])

menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='👨🏻‍💻 About', callback_data='about'),
        InlineKeyboardButton(text='🌐Links', callback_data='links'),
    ],
    [
        InlineKeyboardButton(text='🧰Kursla', callback_data='kurs'),
        InlineKeyboardButton(text='🔗 Bog\'lanish', callback_data='boglanish'),
    ],
    [
        InlineKeyboardButton(text='📋Portfolio', callback_data='resume'),
    ],
    [
        InlineKeyboardButton(text='Ortga', callback_data='menu_cansel'),
    ]
    ]
)

menukeys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='GitHub', url="https://github.com/alimilhomov"),
            InlineKeyboardButton(text='LinkendIn', url="https://www.linkedin.com/in/alimilhomov/")
        ],
        [
            InlineKeyboardButton(text='Telegram', url="https://t.me/alimilhomov"),
            InlineKeyboardButton(text='LeetCode', url="https://leetcode.com/u/Alim2353/")
            
        ],
        [
            InlineKeyboardButton(text='Ortga', callback_data='cansel'),
        ]
    ])

course= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ortga', callback_data='cancel'),
            InlineKeyboardButton(text="🔗 Bog\'lanish",url="http://t.me/alimilhomov")
        ]
    ]
    )

