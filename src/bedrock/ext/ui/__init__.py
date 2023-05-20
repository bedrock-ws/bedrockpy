"""
This module contains a variety of unicode characters and colors
to use inside Minecraft. They can be used everywhere where text is
used: chat, signs, titles etc. The appearance may be changed
by resource packs.


Useful Links & Reference
========================

- https://wiki.bedrock.dev/concepts/emojis.html
- https://github.com/Partymann2000/bedrock-edition-symbols
- https://minecraft.fandom.com/wiki/Formatting_codes#Color_codes
- https://minecraft.fandom.com/wiki/Formatting_codes#Formatting_codes


Example
=======

.. code-block:: python

    >>> from bedrock.ext import ui
    >>> f"{ui.red:Hello} {ui.blue:Player}! {ui.CODE_BUILDER_BUTTON}"
"""

# TODO: extend and/or rename from https://wiki.bedrock.dev/concepts/emojis.html
# TODO: include emojis in docstring


from attrs import define


@define
class Style:
    """A class used to style text in the game.
    
    Attributes
    ----------
    code
        The code used for the style.
    """

    _code: str

    @property
    def code(self) -> str:
        return self._code

    def __call__(self, text: str, /) -> str:
        """Styles text.

        Parameters
        ----------
        text
            The text to style.
        
        Returns
        -------
        The text prefixed by the formatting code and suffixed with the reset code.
        """
        return f"§{self.code}{text}§r"

    def __format__(self, format_spec: str, /) -> str:
        return self(format_spec)


black = Style("0")
"""Black colored text."""

dark_blue = Style("1")
"""Dark blue colored text."""

dark_green = Style("2")
"""Dark green colored text."""

dark_aqua = Style("3")
"""Dark aqua colored text."""

dark_red = Style("4")
"""Dark red colored text."""

dark_purple = Style("5")
"""Dark purple colored text."""

gold = Style("6")
"""Gold colored text."""

gray = Style("7")
"""Gray colored text."""

dark_gray = Style("8")
"""Dark gray colored text."""

blue = Style("9")
"""Blue colored text."""

green = Style("a")
"""Green colored text."""

aqua = Style("b")
"""Aqua colored text."""

red = Style("c")
"""Red colored text."""

light_purple = Style("d")
"""Light purple colored text."""

yellow = Style("e")
"""Yellow colored text."""

white = Style("f")
"""White colored text."""

minecoin_gold = Style("g")
"""Minecoin gold colored text."""

material_quartz = Style("h")
"""Material quartz colored text."""

meterial_iron = Style("i")
"""Material iron colored text."""

material_netherite = Style("j")
"""Material netherite colored text."""

obfuscated = Style("k")
"""Obfuscated text."""

bold = Style("l")
"""Bold text."""

material_redstone = Style("m")
"""Material redstone colored text."""

material_copper = Style("n")
"""Material copper colored text."""

italic = Style("o")
"""Italic text."""

material_gold = Style("p")
"""Material gold colored text."""

material_emerald = Style("q")
"""Material emerald colored text."""

reset = Style("r")
"""Reset all styles."""

material_diamond = Style("s")
"""Material diamond colored text."""

material_lapis = Style("t")
"""Material lapis colored text."""

material_amethyst = Style("u")
"""Material amethyst colored text."""


# The `#:` below are required to include the constants in the
# documentation.

XBOX_A_BUTTON = chr(0xE000)  #:
XBOX_B_BUTTON = chr(0xE001)  #:
XBOX_X_BUTTON = chr(0xE002)  #:
XBOX_Y_BUTTON = chr(0xE003)  #:
XBOX_LB_BUTTON = chr(0xE004)  #:
XBOX_RB_BUTTON = chr(0xE005)  #:
XBOX_LT_BUTTON = chr(0xE006)  #:
XBOX_RT_BUTTON = chr(0xE007)  #:
XBOX_SELECT_BUTTON = chr(0xE008)  #:
XBOX_START_BUTTON = chr(0xE009)  #:
XBOX_LEFT_STICK_BUTTON = chr(0xE00A)  #:
XBOX_RIGHT_STICK_BUTTON = chr(0xE00B)  #:
XBOX_D_PAD_UP_BUTTON = chr(0xE00C)  #:
XBOX_D_PAD_LEFT_BUTTON = chr(0xE00D)  #:
XBOX_D_PAD_DOWN_BUTTON = chr(0xE00E)  #:
XBOX_D_PAD_RIGHT_BUTTON = chr(0xE00F)  #:

MOBILE_JUMP = chr(0xE014)  #:
MOBILE_ATTACK = chr(0xE015)  #:
MOBILE_JOY_STICK = chr(0xE016)  #:
MOBILE_CROSS_HAIR = chr(0xE017)  #:
MOBILE_PLACE = chr(0xE018)

PLAYSTATION_CROSS_BUTTON = chr(0xE020)  #:
PLAYSTATION_CIRCLE_BUTTON = chr(0xE021)  #:
PLAYSTATION_SQUARE_BUTTON = chr(0xE022)  #:
PLAYSTATION_TRIANGLE_BUTTON = chr(0xE023)  #:
PLAYSTATION_L1_BUTTON = chr(0xE024)  #:
PLAYSTATION_R1_BUTTON = chr(0xE025)  #:
PLAYSTATION_L2_BUTTON = chr(0xE026)  #:
PLAYSTATION_R2_BUTTON = chr(0xE027)  #:
PLAYSTATION_SELECT_BUTTON = chr(0xE028)  #:
PLAYSTATION_START_BUTTON = chr(0xE029)  #:
PLAYSTATION_LEFT_STICK_BUTTON = chr(0xE02A) #:
PLAYSTATION_RIGHT_STICK_BUTTON = chr(0xE02B)  #:
PLAYSTATION_D_PAD_UP_BUTTON = chr(0xE02C)  #:
PLAYSTATION_D_PAD_LEFT_BUTTON = chr(0xE02D)  #:
PLAYSTATION_D_PAD_DOWN_BUTTON = chr(0xE02E)  #:
PLAYSTATION_D_PAD_RIGHT_BUTTON = chr(0xE02F)  #:

SWITCH_A_BUTTON = chr(0xE040)  #:
SWITCH_B_BUTTON = chr(0xE041)  #:
SWITCH_X_BUTTON = chr(0xE042)  #:
SWITCH_Y_BUTTON = chr(0xE043)  #:
SWITCH_L_BUTTON = chr(0xE044)  #:
SWITCH_R_BUTTON = chr(0xE045)  #:
SWITCH_ZL_BUTTON = chr(0xE046)  #:
SWITCH_ZR_BUTTON = chr(0xE047)  #:
SWITCH_MINUS_BUTTON = chr(0xE048)  #:
SWITCH_PLUS_BUTTON = chr(0xE049)  #:
SWITCH_LEFT_STICK_BUTTON = chr(0xE04A)  #:
SWITCH_RIGHT_STICK_BUTTON = chr(0xE04B)  #:
SWITCH_D_PAD_UP_BUTTON = chr(0xE04C)  #:
SWITCH_D_PAD_LEFT_BUTTON = chr(0xE04D)  #:
SWITCH_D_PAD_DOWN_BUTTON = chr(0xE04E)  #:
SWITCH_D_PAD_RIGHT_BUTTON = chr(0xE04F)  #:

MOBILE_SMALL_JUMP_BUTTON = chr(0xE059)  #:
MOBILE_SMALL_CROUCH_BUTTON = chr(0xE05A)  #:
MOBILE_SMALL_FLY_UP_BUTTON = chr(0xE05C)  #:
MOBILE_SMALL_FLY_DOWN_BUTTON = chr(0xE05D)  #:
MOBILE_SMALL_LEFT_ARROW_BUTTON = chr(0xE056)  #:
MOBILE_SMALL_RIGHT_ARROW_BUTTON = chr(0xE058)  #:
MOBILE_SMALL_UP_ARROW_BUTTON = chr(0xE055)  #:
MOBILE_SMALL_DOWN__ARROW_BUTTON = chr(0xE057)  #:
MOBILE_SMALL_INVENTORY_BUTTON = chr(0xE05B)  #:

WINDOWS_LEFT_MOUSE_BUTTON = chr(0xE060)  #:
WINDOWS_RIGHT_MOUSE_BUTTON = chr(0xE061)  #:
WINDOWS_MIDDLE_MOUSE_BUTTON = chr(0xE062)  #:

MOBILE_FORWARD_ARROW_BUTTON = chr(0xE080)  #:
MOBILE_LEFT_ARROW_BUTTON = chr(0xE081)  #:
MOBILE_BACKWARDS_ARROW_BUTTON = chr(0xE082)  #:
MOBILE_RIGHT_ARROW_BUTTON = chr(0xE083)  #:
MOBILE_JUMP_BUTTON = chr(0xE084)  #:
MOBILE_CROUCH_BUTTON = chr(0xE085)  #:
MOBILE_FLY_UP_BUTTON = chr(0xE086)  #:
MOBILE_FLY_DOWN_BUTTON = chr(0xE087)  #:

CRAFTABLE_TOGGLE_ON = chr(0xE0A0)  #:
CRAFTABLE_TOGGLE_OFF = chr(0xE0A1)  #:
FOOD_ICON = chr(0xE100)  #:
ARMOR_ICON = chr(0xE101)  #:
MINECOIN = chr(0xE102)  #:
CODE_BUILDER_BUTTON = chr(0xE103)  #:
IMMERSE_READER_BUTTON = chr(0xE104)  #:
TOKEN = chr(0xE105)  #:

WINMR_LEFT_GRAB_BUTTON = chr(0xE0C0)  #:
WINMR_RIGHT_GRAB_BUTTON = chr(0xE0C1)  #:
WINMR_MENU_BUTTON = chr(0xE0C2)  #:
WINMR_LEFT_STICK_BUTTON = chr(0xE0C3)  #:
WINMR_RIGHT_STICK_BUTTON = chr(0xE0C4)  #:
WINMR_LEFT_TOUCHPAD_BUTTON = chr(0xE0C5)  #:
WINMR_LEFT_TOUCHPAD_HORIZONTAL_BUTTON = chr(0xE0C6)  #:
WINMR_LEFT_TOUCHPAD_VERTICAL_BUTTON = chr(0xE0C7)  #:
WINMR_RIGHT_TOUCHPAD_BUTTON = chr(0xE0C8)  #:
WINMR_RIGHT_TOUCHPAD_HORIZONTAL_BUTTON = chr(0xE0C9)  #:
WINMR_RIGHT_TOUCHPAD_VERTICAL_BUTTON = chr(0xE0CA)  #:
WINMR_LEFT_TRIGGER_BUTTON = chr(0xE0CB)  #:
WINMR_RIGHT_TRIGGER_BUTTON = chr(0xE0CC)  #:
WINMR_WINDOWS = chr(0xE0CD)  #:

RIFT_ZERO_BUTTON = chr(0xE0E0)  #:
RIFT_A_BUTTON = chr(0xE0E1)  #:
RIFT_B_BUTTON = chr(0xE0E2)  #:
RIFT_LEFT_GRAB_BUTTON = chr(0xE0E3)  #:
RIFT_RIGHT_GRAB_BUTTON = chr(0xE0E4)  #:
RIFT_LEFT_STICK_BUTTON = chr(0xE0E5)  #:
RIFT_RIGHT_STICK_BUTTON = chr(0xE0E6)  #:
RIFT_LEFT_TRIGGER_BUTTON = chr(0xE0E7)  #:
RIFT_RIGHT_TRIGGER_BUTTON = chr(0xE0E8)  #:
RIFT_X_BUTTON = chr(0xE0E9)  #:
RIFT_Y_BUTTON = chr(0xE0EA)  #:
