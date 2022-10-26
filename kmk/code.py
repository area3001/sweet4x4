import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys


# rotary 4+5

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.row_pins = (board.D7,board.D8,board.D9,board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# LED's
rgb = RGB(pixel_pin=board.D6, num_pixels=9)
keyboard.extensions.append(rgb)
keyboard.extensions.append(MediaKeys())

# Rotary Encoder
# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/encoder.md
from kmk.modules.encoder import EncoderHandler
# from kmk.modules import layers
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
encoder_handler.pins = (
    (board.D4, board.D5, None,), # encoder #1 
    )
encoder_handler.map = [ (( KC.VOLD, KC.VOLU, None), ) ]

keyboard.keymap = [
    [KC.RGB_MODE_RAINBOW,KC.B,KC.C,KC.D,
     KC.E,KC.F,KC.G,KC.H,
     KC.I,KC.J,KC.K,KC.L,
     KC.M,KC.N,KC.O,KC.P,
     ]
]

if __name__ == '__main__':
    keyboard.go()