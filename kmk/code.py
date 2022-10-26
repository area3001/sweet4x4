print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB

rgb = RGB(pixel_pin=board.D6, num_pixels=9)

# rotary 4+5

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.row_pins = (board.D7,board.D8,board.D9,board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(rgb)

keyboard.keymap = [
    [KC.RGB_MODE_RAINBOW,KC.B,KC.C,KC.D,
     KC.E,KC.F,KC.G,KC.H,
     KC.I,KC.J,KC.K,KC.L,
     KC.M,KC.N,KC.O,KC.P,
     ]
]

if __name__ == '__main__':
    keyboard.go()