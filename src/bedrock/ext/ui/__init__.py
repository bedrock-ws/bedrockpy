"""
.. role:: mc-black
.. role:: mc-dark-blue
.. role:: mc-dark-green
.. role:: mc-dark-aqua
.. role:: mc-dark-red
.. role:: mc-dark-purple
.. role:: mc-gold
.. role:: mc-gray
.. role:: mc-dark-gray
.. role:: mc-blue
.. role:: mc-green
.. role:: mc-aqua
.. role:: mc-red
.. role:: mc-light-purple
.. role:: mc-yellow
.. role:: mc-white
.. role:: mc-minecoin-gold
.. role:: mc-material-quartz
.. role:: mc-material-iron
.. role:: mc-material-netherite
.. role:: mc-material-redstone
.. role:: mc-material-copper
.. role:: mc-material-gold
.. role:: mc-material-emerald
.. role:: mc-material-diamond
.. role:: mc-material-lapis
.. role:: mc-material-amethyst

This module contains a variety of unicode characters and colors
to use inside Minecraft. They can be used everywhere where text is
used: chat, signs, titles etc. The appearance may be changed
by resource packs.


Useful Links & Reference
========================

- https://wiki.bedrock.dev/concepts/emojis.html
- https://github.com/Partymann2000/bedrock-edition-symbols
- https://minecraft.wiki/w/Formatting_codes#Color_codes


Example
=======

.. code-block:: python

    >>> from bedrock.ext import ui
    >>> f"{ui.red:Hello} {ui.blue:Player}! {ui.AGENT_ICON}"
"""

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
        str
            The text prefixed by the formatting code and suffixed with the reset code.
        """
        return f"§{self.code}{text}§r"

    def __format__(self, format_spec: str, /) -> str:
        return self(format_spec)


black = Style("0")
"""Black (:mc-black:`#000000`) colored text."""

dark_blue = Style("1")
"""Dark blue (:mc-dark-blue:`#0000AA`) colored text."""

dark_green = Style("2")
"""Dark green (:mc-dark-green:`#00AA00`) colored text."""

dark_aqua = Style("3")
"""Dark aqua (:mc-dark-aqua:`#00AAAA`) colored text."""

dark_red = Style("4")
"""Dark red (:mc-dark-red:`#AA0000`) colored text."""

dark_purple = Style("5")
"""Dark purple (:mc-dark-purple:`#AA00AA`) colored text."""

gold = Style("6")
"""Gold (:mc-gold:`#FFAA00`) colored text."""

gray = Style("7")
"""Gray (:mc-gray:`#AAAAAA`) colored text."""

dark_gray = Style("8")
"""Dark gray (:mc-dark-gray:`#555555`) colored text."""

blue = Style("9")
"""Blue (:mc-blue:`#5555FF`) colored text."""

green = Style("a")
"""Green (:mc-green:`#55FF55`) colored text."""

aqua = Style("b")
"""Aqua (:mc-aqua:`#55FFFF`) colored text."""

red = Style("c")
"""Red (:mc-red:`#FF5555`) colored text."""

light_purple = Style("d")
"""Light purple (:mc-light-purple:`#FF55FF`) colored text."""

yellow = Style("e")
"""Yellow (:mc-yellow:`#FFFF55`) colored text."""

white = Style("f")
"""White (:mc-white:`#FFFFFF`) colored text."""

minecoin_gold = Style("g")
"""Minecoin gold (:mc-minecoin-gold:`#DDD605`) colored text."""

material_quartz = Style("h")
"""Material quartz (:mc-material-quartz:`#E3D4D1`) colored text."""

meterial_iron = Style("i")
"""Material iron (:mc-material-iron:`#CECACA`) colored text."""

material_netherite = Style("j")
"""Material netherite (:mc-material-netherite:`#443A3B`) colored text."""

obfuscated = Style("k")
"""Obfuscated text."""

bold = Style("l")
"""Bold text."""

material_redstone = Style("m")
"""Material redstone (:mc-material-redstone:`#971607`) colored text."""

material_copper = Style("n")
"""Material copper (:mc-material-copper:`#B4684D`) colored text."""

italic = Style("o")
"""Italic text."""

material_gold = Style("p")
"""Material gold (:mc-material-gold:`#DEB12D`) colored text."""

material_emerald = Style("q")
"""Material emerald (:mc-material-emerald:`#47A036`) colored text."""

reset = Style("r")
"""Reset all styles."""

material_diamond = Style("s")
"""Material diamond (:mc-material-diamond:`#2CBAA8`) colored text."""

material_lapis = Style("t")
"""Material lapis (:mc-material-lapis:`#21497B`) colored text."""

material_amethyst = Style("u")
"""Material amethyst (:mc-material-amethyst:`#9A5CC6`) colored text."""


# The `#:` below are required to include the constants in the
# documentation.

XBOX_A = chr(0xE000)  #:
XBOX_B = chr(0xE001)  #:
XBOX_X = chr(0xE002)  #:
XBOX_Y = chr(0xE003)  #:
XBOX_LB = chr(0xE004)  #:
XBOX_RB = chr(0xE005)  #:
XBOX_LT = chr(0xE006)  #:
XBOX_RT = chr(0xE007)  #:
XBOX_SELECT = chr(0xE008)  #:
XBOX_START = chr(0xE009)  #:
XBOX_LEFT_STICK = chr(0xE00A)  #:
XBOX_RIGHT_STICK = chr(0xE00B)  #:
XBOX_D_PAD_UP = chr(0xE00C)  #:
XBOX_D_PAD_LEFT = chr(0xE00D)  #:
XBOX_D_PAD_DOWN = chr(0xE00E)  #:
XBOX_D_PAD_RIGHT = chr(0xE00F)  #:

MOBILE_JUMP = chr(0xE014)  #:
MOBILE_ATTACK = chr(0xE015)  #:
MOBILE_JOY_STICK = chr(0xE016)  #:
MOBILE_PLACE = chr(0xE018)  #:
MOBILE_SNEAK = chr(0xE019)  #:
MOBILE_SPRINT = chr(0xE01A)  #:
MOBILE_FLY_UP = chr(0xE01B)  #:
MOBILE_FLY_DOWN = chr(0xE01C)  #:
MOBILE_DISMOUNT = chr(0xE01D)  #:

MOBILE_LEGACY_JUMP = chr(0xE084)  #:
MOBILE_LEGACY_CROUCH = chr(0xE085)  #:
MOBILE_LEGACY_FLY_UP = chr(0xE086)  #:
MOBILE_LEGACY_FLY_DOWN = chr(0xE087)  #:
MOBILE_LEGACY_STOP_FLYING = chr(0xE088)  #:
MOBILE_LEGAY_LEFT_ARROW = chr(0xE081)  #:
MOBILE_LEGACY_RIGHT_ARROW = chr(0xE083)  #:
MOBILE_LEGACY_UP_AROOW = chr(0xE080)  #:
MOBILE_LEGACY_DOWN_ARROW = chr(0xE082)  #:

PLAYSTATION_CROSS = chr(0xE020)  #:
PLAYSTATION_CIRCLE = chr(0xE021)  #:
PLAYSTATION_SQUARE = chr(0xE022)  #:
PLAYSTATION_TRIANGLE = chr(0xE023)  #:
PLAYSTATION_L1 = chr(0xE024)  #:
PLAYSTATION_R1 = chr(0xE025)  #:
PLAYSTATION_L2 = chr(0xE026)  #:
PLAYSTATION_R2 = chr(0xE027)  #:
PLAYSTATION_SELECT = chr(0xE028)  #:
PLAYSTATION_START = chr(0xE029)  #:
PLAYSTATION_LEFT_STICK = chr(0xE02A)  #:
PLAYSTATION_RIGHT_STICK = chr(0xE02B)  #:
PLAYSTATION_D_PAD_UP = chr(0xE02C)  #:
PLAYSTATION_D_PAD_LEFT = chr(0xE02D)  #:
PLAYSTATION_D_PAD_DOWN = chr(0xE02E)  #:
PLAYSTATION_D_PAD_RIGHT = chr(0xE02F)  #:

SWITCH_A = chr(0xE040)  #:
SWITCH_B = chr(0xE041)  #:
SWITCH_X = chr(0xE042)  #:
SWITCH_Y = chr(0xE043)  #:
SWITCH_L = chr(0xE044)  #:
SWITCH_R = chr(0xE045)  #:
SWITCH_ZL = chr(0xE046)  #:
SWITCH_ZR = chr(0xE047)  #:
SWITCH_MINUS = chr(0xE048)  #:
SWITCH_PLUS = chr(0xE049)  #:
SWITCH_LEFT_STICK = chr(0xE04A)  #:
SWITCH_RIGHT_STICK = chr(0xE04B)  #:
SWITCH_D_PAD_UP = chr(0xE04C)  #:
SWITCH_D_PAD_LEFT = chr(0xE04D)  #:
SWITCH_D_PAD_DOWN = chr(0xE04E)  #:
SWITCH_D_PAD_RIGHT = chr(0xE04F)  #:

MOBILE_SMALL_JUMP = chr(0xE059)  #:
MOBILE_SMALL_CROUCH = chr(0xE05A)  #:
MOBILE_SMALL_FLY_UP = chr(0xE05C)  #:
MOBILE_SMALL_FLY_DOWN = chr(0xE05D)  #:
MOBILE_SMALL_LEFT_ARROW = chr(0xE056)  #:
MOBILE_SMALL_RIGHT_ARROW = chr(0xE058)  #:
MOBILE_SMALL_UP_ARROW = chr(0xE055)  #:
MOBILE_SMALL_DOWN_ARROW = chr(0xE057)  #:
MOBILE_SMALL_INVENTORY = chr(0xE05B)  #:

WINDOWS_LEFT_MOUSE = chr(0xE060)  #:
WINDOWS_RIGHT_MOUSE = chr(0xE061)  #:
WINDOWS_MIDDLE_MOUSE = chr(0xE062)  #:

MOBILE_FORWARD_ARROW = chr(0xE080)  #:
MOBILE_LEFT_ARROW = chr(0xE081)  #:
MOBILE_BACKWARDS_ARROW = chr(0xE082)  #:
MOBILE_RIGHT_ARROW = chr(0xE083)  #:
MOBILE_JUMP = chr(0xE084)  #:
MOBILE_CROUCH = chr(0xE085)  #:
MOBILE_FLY_UP = chr(0xE086)  #:
MOBILE_FLY_DOWN = chr(0xE087)  #:

CRAFTABLE_TOGGLE_ON = chr(0xE0A0)  #:
CRAFTABLE_TOGGLE_OFF = chr(0xE0A1)  #:
FOOD_ICON = chr(0xE100)  #:
ARMOR_ICON = chr(0xE101)  #:
HEART_ICON = chr(0xE10C)  #:
MINECOIN = chr(0xE102)  #:
AGENT_ICON = chr(0xE103)  #:
IMMERSE_READER = chr(0xE104)  #:
TOKEN = chr(0xE105)  #:
STAR_HOLLOW = chr(0xE106)  #:
STAR_SOLID = chr(0xE107)  #:
WOODEN_PICKAXE = chr(0xE108)  #:
WOODEN_SWORD = chr(0xE109)  #:
CRAFTING_TABLE = chr(0xE10A)  #:
FURNACE = chr(0xE10B)  #:

WINMR_LEFT_GRAB = chr(0xE0C0)  #:
WINMR_RIGHT_GRAB = chr(0xE0C1)  #:
WINMR_MENU = chr(0xE0C2)  #:
WINMR_LEFT_STICK = chr(0xE0C3)  #:
WINMR_RIGHT_STICK = chr(0xE0C4)  #:
WINMR_LEFT_TOUCHPAD = chr(0xE0C5)  #:
WINMR_LEFT_TOUCHPAD_HORIZONTAL = chr(0xE0C6)  #:
WINMR_LEFT_TOUCHPAD_VERTICAL = chr(0xE0C7)  #:
WINMR_RIGHT_TOUCHPAD = chr(0xE0C8)  #:
WINMR_RIGHT_TOUCHPAD_HORIZONTAL = chr(0xE0C9)  #:
WINMR_RIGHT_TOUCHPAD_VERTICAL = chr(0xE0CA)  #:
WINMR_LEFT_TRIGGER = chr(0xE0CB)  #:
WINMR_RIGHT_TRIGGER = chr(0xE0CC)  #:
WINMR_WINDOWS = chr(0xE0CD)  #:

RIFT_ZERO = chr(0xE0E0)  #:
RIFT_A = chr(0xE0E1)  #:
RIFT_B = chr(0xE0E2)  #:
RIFT_LEFT_GRAB = chr(0xE0E3)  #:
RIFT_RIGHT_GRAB = chr(0xE0E4)  #:
RIFT_LEFT_STICK = chr(0xE0E5)  #:
RIFT_RIGHT_STICK = chr(0xE0E6)  #:
RIFT_LEFT_TRIGGER = chr(0xE0E7)  #:
RIFT_RIGHT_TRIGGER = chr(0xE0E8)  #:
RIFT_X = chr(0xE0E9)  #:
RIFT_Y = chr(0xE0EA)  #:
