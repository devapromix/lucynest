# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt
from collections import namedtuple


def game():
    blt.set("window.title='LucynesT: in a dream'")

    width = blt.state(blt.TK_WIDTH)
    height = blt.state(blt.TK_HEIGHT)
    parts = 6
    left = width // 6
    right = width * (parts - 1) // parts
    middle = height // 2
    padding = 1

    story = [
        "Hi! I'm Avatar, actually I'm is who You are in this World",
        "Lets find out what we've got here in lucid dream",
        "Open Your mind and enter this evershining mental landscape",
    ]
    story_point = 0
    while True:
        blt.clear()

        blt.color("light gray")
        for y in range(height):
            blt.put(left, y, 0x2588)
            blt.put(right, y, 0x2588)
        for x in range(left, right):
            blt.put(x, middle, 0x2580)

        blt.color("white")
        # blt.put_ext(view_width * 4 + 1, 0, margin, margin, 0xE100)
        avatar_symbol = "@:"
        left_avatar = left + 1 + padding
        left_avatar_text = left_avatar + len(avatar_symbol) + 1

        blt.puts(left_avatar, middle // 5, f"[color=orange]{avatar_symbol}[/color]")
        blt.puts(left_avatar_text, middle // 5, f"{story[story_point]}",
                 right - 1 - padding - left_avatar_text, middle - 1 - padding - middle // 5,
                 blt.TK_ALIGN_LEFT)

        keys_footer()

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break
        elif key == blt.TK_ENTER:
            story_point += 1 if story_point < len(story) - 1 else 0




def keys_footer():
    height = blt.state(blt.TK_HEIGHT) - 1
    keys = {
        ("ESC", "Exit"),
        ("Enter", "Next"),
        ("PGUP", "Log up"),
        ("PGDN", "Log Down")
    }
    offset = 0
    for (key, value) in keys:
        blt.puts(offset, height, f"[bkcolor=grey][color=yellow]{key}[/color] [color=black]{value}[/color][/bkcolor]")
        offset += 2 + len(key) + len(value)


