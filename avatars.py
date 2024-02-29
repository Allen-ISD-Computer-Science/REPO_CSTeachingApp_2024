
import python_avatars

# TODO: This 100% needs a makeover.

'''
    my_avatar = python_avatars.Avatar(
        style=python_avatars.AvatarStyle.CIRCLE,
        background_color=python_avatars.BackgroundColor.BLACK,
        # begin
        top=python_avatars.HairType.STRAIGHT_2,
        eyebrows=python_avatars.EyebrowType.DEFAULT_NATURAL,
        eyes=python_avatars.EyeType.WINK,
        nose=python_avatars.NoseType.SMALL,
        mouth=python_avatars.MouthType.BIG_SMILE,
        facial_hair=python_avatars.FacialHairType.NONE,
        # You can use hex colors on any color attribute...
        skin_color="#00FFFF",
        # Or you can use the colors provided by the library
        hair_color=python_avatars.HairColor.BROWN,
        accessory=python_avatars.AccessoryType.SUNGLASSES,
        clothing=python_avatars.ClothingType.SHIRT_V_NECK,
        clothing_color=python_avatars.ClothingColor.HEATHER
    )
'''

def HairTypeConverter(given):
    match given:
        case 0:  return python_avatars.HairType.NONE
        case 1:  return python_avatars.HairType.BIG_HAIR
        case 2:  return python_avatars.HairType.BOB
        case 3:  return python_avatars.HairType.BUN
        case 4:  return python_avatars.HairType.CAESAR_SIDE_PART
        case 5:  return python_avatars.HairType.CAESAR
        case 6:  return python_avatars.HairType.CURLY
        case 7:  return python_avatars.HairType.CURVY
        case 8:  return python_avatars.HairType.DREADS
        case 9:  return python_avatars.HairType.FRIDA
        case 10: return python_avatars.HairType.FRIZZLE
        case 11: return python_avatars.HairType.FRO_BAND
        case 12: return python_avatars.HairType.FRO
        case 13: return python_avatars.HairType.LONG_NOT_TOO_LONG
        case 14: return python_avatars.HairType.MIA_WALLACE
        case 15: return python_avatars.HairType.SHAGGY_MULLET
        case 16: return python_avatars.HairType.SHAGGY
        case 17: return python_avatars.HairType.SHAVED_SIDES
        case 18: return python_avatars.HairType.SHORT_CURLY
        case 19: return python_avatars.HairType.SHORT_DREADS_1
        case 20: return python_avatars.HairType.SHORT_DREADS_2
        case 21: return python_avatars.HairType.SHORT_FLAT
        case 22: return python_avatars.HairType.SHORT_ROUND
        case 23: return python_avatars.HairType.SHORT_WAVED
        case 24: return python_avatars.HairType.SIDES
        case 25: return python_avatars.HairType.STRAIGHT_1
        case 26: return python_avatars.HairType.STRAIGHT_2
        case 27: return python_avatars.HairType.STRAIGHT_STRAND
        case 28: return python_avatars.HairType.ASTRONAUT
        case 29: return python_avatars.HairType.BRAIDS
        case 30: return python_avatars.HairType.BRIDE
        case 31: return python_avatars.HairType.BUZZCUT
        case 32: return python_avatars.HairType.CORNROWS
        case 33: return python_avatars.HairType.CURLY_2
        case 34: return python_avatars.HairType.DREADLOCKS
        case 35: return python_avatars.HairType.EINSTEIN_HAIR
        case 36: return python_avatars.HairType.ELVIS
        case 37: return python_avatars.HairType.EVIL_SPIKE
        case 38: return python_avatars.HairType.HALF_SHAVED
        case 39: return python_avatars.HairType.HAT
        case 40: return python_avatars.HairType.LONG_HAIR_CURLY
        case 41: return python_avatars.HairType.LOOSE_HAIR
        case 42: return python_avatars.HairType.MOHAWK
        case 43: return python_avatars.HairType.MOWGLI
        case 44: return python_avatars.HairType.PIXIE
        case 45: return python_avatars.HairType.POMPADOUR
        case 46: return python_avatars.HairType.QUIFF
        case 47: return python_avatars.HairType.TWIST_LONG_HAIR
        case 48: return python_avatars.HairType.TWIST_LONG_HAIR_2
        case 49: return python_avatars.HairType.WICK
        case 50: return python_avatars.HairType.WILD
        case 51: return python_avatars.HatType.HAT
        case 52: return python_avatars.HatType.HIJAB
        case 53: return python_avatars.HatType.TURBAN
        case 54: return python_avatars.HatType.WINTER_HAT_1
        case 55: return python_avatars.HatType.WINTER_HAT_2
        case 56: return python_avatars.HatType.WINTER_HAT_3
        case 57: return python_avatars.HatType.WINTER_HAT_4
        case 58: return python_avatars.HatType.CHEF_CAP
        case 59: return python_avatars.HatType.JEDI
        case 60: return python_avatars.HatType.GLADIATOR_HELMET
        case _:  raise Exception ("Invalid Hair Type")

def EyebrowTypeConverter(given):
    match given:
        case 0:  return python_avatars.EyebrowType.NONE
        case 1:  return python_avatars.EyebrowType.ANGRY_NATURAL
        case 2:  return python_avatars.EyebrowType.ANGRY
        case 3:  return python_avatars.EyebrowType.DEFAULT_NATURAL
        case 4:  return python_avatars.EyebrowType.DEFAULT
        case 5:  return python_avatars.EyebrowType.FLAT_NATURAL
        case 6:  return python_avatars.EyebrowType.FROWN_NATURAL
        case 7:  return python_avatars.EyebrowType.RAISED_EXCITED_NATURAL
        case 8:  return python_avatars.EyebrowType.RAISED_EXCITED
        case 9:  return python_avatars.EyebrowType.SAD_CONCERNED_NATURAL
        case 10: return python_avatars.EyebrowType.SAD_CONCERNED
        case 11: return python_avatars.EyebrowType.UNIBROW_NATURAL
        case 12: return python_avatars.EyebrowType.UP_DOWN_NATURAL
        case 13: return python_avatars.EyebrowType.UP_DOWN
        case _:  raise Exception("Invalid Eyebrow Type")

def EyeTypeConverter(given):
    match given:
        case 0:  return python_avatars.EyeType.DEFAULT
        case 1:  return python_avatars.EyeType.CLOSED
        case 2:  return python_avatars.EyeType.CRY
        case 3:  return python_avatars.EyeType.X_DIZZY
        case 4:  return python_avatars.EyeType.EYE_ROLL
        case 5:  return python_avatars.EyeType.HAPPY
        case 6:  return python_avatars.EyeType.HEART
        case 7:  return python_avatars.EyeType.SIDE
        case 8:  return python_avatars.EyeType.SQUINT
        case 9:  return python_avatars.EyeType.SURPRISED
        case 10: return python_avatars.EyeType.WINK
        case 11: return python_avatars.EyeType.WINK_WACKY
        case _:  raise Exception("Invalid Eyebrow Type")

def NoseTypeConverter(given):
    match given:
        case 0:  return python_avatars.NoseType.DEFAULT
        case 1:  return python_avatars.NoseType.SMALL
        case 2:  return python_avatars.NoseType.WIDE
        case _:  raise Exception("Invalid Nose Type")

def MouthTypeConverter(given):
    match given:
        case 0:  return python_avatars.MouthType.CONCERNED
        case 1:  return python_avatars.MouthType.DEFAULT
        case 2:  return python_avatars.MouthType.DISBELIEF
        case 3:  return python_avatars.MouthType.EATING
        case 4:  return python_avatars.MouthType.GRIMACE
        case 5:  return python_avatars.MouthType.SAD
        case 6:  return python_avatars.MouthType.SCREAM_OPEN
        case 7:  return python_avatars.MouthType.SERIOUS
        case 8:  return python_avatars.MouthType.SMILE
        case 9:  return python_avatars.MouthType.TONGUE
        case 10: return python_avatars.MouthType.TWINKLE
        case 11: return python_avatars.MouthType.VOMIT
        case 12: return python_avatars.MouthType.BIG_SMILE
        case _:  raise Exception("Invalid Mouth Type")
    
def FacialHairTypeConverter(given):
    match given:
        case 0:  return python_avatars.FacialHairType.NONE
        case 1:  return python_avatars.FacialHairType.BEARD_LIGHT
        case 2:  return python_avatars.FacialHairType.BEARD_MAGESTIC
        case 3:  return python_avatars.FacialHairType.BEARD_MEDIUM
        case 4:  return python_avatars.FacialHairType.MOUSTACHE_FANCY
        case 5:  return python_avatars.FacialHairType.MOUSTACHE_MAGNUM
        case 6:  return python_avatars.FacialHairType.EINSTEIN_MOUSTACHE
        case 7:  return python_avatars.FacialHairType.WICK_BEARD
        case _:  raise Exception("Invalid Facial Hair Type")

def HairColorConverter(given):
    match given:
        case 0:  return python_avatars.HairColor.AUBURN
        case 1:  return python_avatars.HairColor.BLACK
        case 2:  return python_avatars.HairColor.BLONDE
        case 3:  return python_avatars.HairColor.BLONDE_GOLDEN
        case 4:  return python_avatars.HairColor.BROWN
        case 5:  return python_avatars.HairColor.BROWN_DARK
        case 6:  return python_avatars.HairColor.PASTEL_PINK
        case 7:  return python_avatars.HairColor.PLATINUM
        case 8:  return python_avatars.HairColor.RED
        case 9:  return python_avatars.HairColor.SILVER_GRAY
        case _:  raise Exception("Invalid Hair Color Type")

def AccessoryTypeConverter(given):
    match given:
        case 0:  return python_avatars.AccessoryType.NONE
        case 1:  return python_avatars.AccessoryType.EYEPATCH
        case 2:  return python_avatars.AccessoryType.KURT
        case 3:  return python_avatars.AccessoryType.PRESCRIPTION_1
        case 4:  return python_avatars.AccessoryType.PRESCRIPTION_2
        case 5:  return python_avatars.AccessoryType.ROUND
        case 6:  return python_avatars.AccessoryType.SUNGLASSES
        case 7:  return python_avatars.AccessoryType.WAYFARERS
        case 8:  return python_avatars.AccessoryType.SUNGLASSES_2
        case 9:  return python_avatars.AccessoryType.WAYFARERS_2
        case _:  raise Exception("Invalid Accessory Type")

def ClothingTypeConverter(given):
    match given:
        case 0:  return python_avatars.ClothingType.NONE
        case 1:  return python_avatars.ClothingType.BLAZER_SHIRT
        case 2:  return python_avatars.ClothingType.BLAZER_SWEATER
        case 3:  return python_avatars.ClothingType.COLLAR_SWEATER
        case 4:  return python_avatars.ClothingType.GRAPHIC_SHIRT
        case 5:  return python_avatars.ClothingType.HOODIE
        case 6:  return python_avatars.ClothingType.OVERALL
        case 7:  return python_avatars.ClothingType.SHIRT_CREW_NECK
        case 8:  return python_avatars.ClothingType.SHIRT_SCOOP_NECK
        case 9:  return python_avatars.ClothingType.SHIRT_V_NECK
        case 10: return python_avatars.ClothingType.ASTRONAUT_SUIT
        case 11: return python_avatars.ClothingType.BOND_SUIT
        case 12: return python_avatars.ClothingType.CHEF
        case 13: return python_avatars.ClothingType.GLADIATOR
        case 14: return python_avatars.ClothingType.JEDI_ROBE
        case 15: return python_avatars.ClothingType.SHIRT_WICK
        case _:  raise Exception("Invalid Clothing Type")

def ClothingColorConverter(given):
    match given:
        case 0:  return python_avatars.ClothingColor.BLACK
        case 1:  return python_avatars.ClothingColor.BLUE_01
        case 2:  return python_avatars.ClothingColor.BLUE_02
        case 3:  return python_avatars.ClothingColor.BLUE_03
        case 4:  return python_avatars.ClothingColor.GRAY_01
        case 5:  return python_avatars.ClothingColor.GRAY_02
        case 6:  return python_avatars.ClothingColor.HEATHER
        case 7:  return python_avatars.ClothingColor.PASTEL_BLUE
        case 8:  return python_avatars.ClothingColor.PASTEL_GREEN
        case 9:  return python_avatars.ClothingColor.PASTEL_ORANGE
        case 10: return python_avatars.ClothingColor.PASTEL_YELLOW
        case 11: return python_avatars.ClothingColor.PINK
        case 12: return python_avatars.ClothingColor.RED
        case 13: return python_avatars.ClothingColor.WHITE
        case _:  raise Exception("Invalid Clothing Color")
        
_HairTypeConverter = [HairTypeConverter(HT) for HT in range(61)]
_EyebrowTypeConverter = [EyebrowTypeConverter(ET) for ET in range(14)]
_EyeTypeConverter = [EyeTypeConverter(ET) for ET in range(12)]
_NoseTypeConverter = [NoseTypeConverter(NT) for NT in range(3)]
_MouthTypeConverter = [MouthTypeConverter(MT) for MT in range(13)]
_FacialHairTypeConverter = [FacialHairTypeConverter(FHT) for FHT in range(8)]
_HairColorConverter = [HairColorConverter(HC) for HC in range(10)]
_AccessoryTypeConverter = [AccessoryTypeConverter(AT) for AT in range(10)]
_ClothingTypeConverter = [ClothingTypeConverter(CT) for CT in range(16)]
_ClothingColorConverter = [ClothingColorConverter(CC) for CC in range(14)]

def SkinColorConverter(given):
    if ((len(bin(given)) - 2) <= 24) == False: raise Exception("Invalid hexidecimal color.")
    _hex = hex(given)[2:]
    _hex = "0" * (6 - len(_hex)) + _hex
    return "#" + _hex.upper()

def _SkinColorConverter(given):
    try: return eval("0x" + str(given[1:]))
    except: return eval("0x" + str(given.value[1:])) 

def extract_bits(number):
    if number & 1:  # Check if the last bit is not 0
        raise ValueError("The last bit is not 0")

    ClothingColorValue      = (number >> 1) & 0xF
    ClothingTypeValue       = (number >> 5) & 0xF
    AccessoryTypeValue      = (number >> 9) & 0xF
    HairColorValue          = (number >> 13) & 0xF
    SkinColorValue          = (number >> 17) & 0xFFFFFF
    FacialHairTypeValue     = (number >> 41) & 0x7
    MouthTypeValue          = (number >> 44) & 0xF
    NoseType                = (number >> 48) & 0x3
    EyeTypeValue            = (number >> 50) & 0xF
    EyebrowTypeValue        = (number >> 54) & 0xF
    HairTypeValue           = (number >> 58) & 0x3F

    return python_avatars.Avatar(
        style=python_avatars.AvatarStyle.CIRCLE,
        background_color=python_avatars.BackgroundColor.BLACK,
        # begin
        top=HairTypeConverter(HairTypeValue),
        eyebrows=EyebrowTypeConverter(EyebrowTypeValue),
        eyes=EyeTypeConverter(EyeTypeValue),
        nose=NoseTypeConverter(NoseType),
        mouth=MouthTypeConverter(MouthTypeValue),
        facial_hair=FacialHairTypeConverter(FacialHairTypeValue),
        skin_color=SkinColorConverter(SkinColorValue),
        hair_color=HairColorConverter(HairColorValue),
        accessory=AccessoryTypeConverter(AccessoryTypeValue),
        clothing=ClothingTypeConverter(ClothingTypeValue),
        clothing_color=ClothingColorConverter(ClothingColorValue)
    )

def avatar_to_int(avatar: python_avatars.Avatar) -> int:
    print(avatar.skin_color)
    HairTypeValue = _HairTypeConverter.index(avatar.top) if avatar.top != None else 0
    EyebrowTypeValue = _EyebrowTypeConverter.index(avatar.eyebrows) if avatar.eyebrows != None else 0
    EyeTypeValue = _EyeTypeConverter.index(avatar.eyes) if avatar.eyes != None else 0
    NoseType = _NoseTypeConverter.index(avatar.nose) if avatar.nose != None else 0
    MouthTypeValue = _MouthTypeConverter.index(avatar.mouth) if avatar.mouth != None else 0
    FacialHairTypeValue = _FacialHairTypeConverter.index(avatar.facial_hair) if avatar.facial_hair != None else 0
    SkinColorValue = _SkinColorConverter(avatar.skin_color)
    HairColorValue = _HairColorConverter.index(avatar.hair_color) if avatar.hair_color != None else 0
    AccessoryTypeValue = _AccessoryTypeConverter.index(avatar.accessory) if avatar.accessory != None else 0
    ClothingTypeValue = _ClothingTypeConverter.index(avatar.clothing) if avatar.clothing != None else 0
    ClothingColorValue = _ClothingColorConverter.index(avatar.clothing_color) if avatar.clothing_color != None else 0

    number = 0
    number |= HairTypeValue
    number <<= 4
    number |= EyebrowTypeValue
    number <<= 4
    number |= EyeTypeValue
    number <<= 2
    number |= NoseType
    number <<= 4
    number |= MouthTypeValue
    number <<= 3
    number |= FacialHairTypeValue
    number <<= 24
    number |= SkinColorValue
    number <<= 4
    number |= HairColorValue
    number <<= 4
    number |= AccessoryTypeValue
    number <<= 4
    number |= ClothingTypeValue
    number <<= 4
    number |= ClothingColorValue
    number <<= 1  # The last bit is always 0

    return number