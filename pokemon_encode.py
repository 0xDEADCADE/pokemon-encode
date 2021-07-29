#!/usr/bin/env python3
# Pokemon gen 1 character encoding/decoding by 0xDEADCADE
# Licensed under GPLv3 https://www.gnu.org/licenses/gpl-3.0.txt
# Quick thrown together script that should probably be optimized, or even completely rewritten
# Can be used as cli program or importable script
# To use as import:
# import pokemon_encode
# pokemon_encode.encodeString("Hello World!", pokemon_encode.patchTables.English)

# Control codes taken from bulbapedia
# https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_I)
# Look there to figure out what some control characters like @page@ mean
# @ symbols have been added to make them distinct from other sets of characters

# Standard English decoding table
decodeTable = [[None], [], [], [], ["", "", "", "", "", "", "", "", "", "@page@", "PKMN", "@_cont@", "@autocont@", "", "@next line@", "@bottom line@"], ["@end@", "@paragraph@", "@players name@", "@rivals name@", "Poké", "@cont@", "……", "@done@", "@prompt@", "@target@", "@user@", "PC", "TM", "TRAINER", "ROCKET", "@dex@"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "V", "S", "L", "M", ":", "ぃ", "ぅ"], ["‘", "’", "“", "”", "・", "⋯", "ぁ", "ぇ", "ぉ", "╔", "═", "╗", "║", "╚", "╝", " "], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"], ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ":", ";", "[", "]"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"], ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "é", "'d", "'l", "'s", "'t", "'v"], [], [], ["'", "PK", "MN", "-", "'r", "'m", "?", "!", ".", "ァ", "ゥ", "ェ", "▷", "▶", "▼", "♂"], ["₽", "×", ".", "/", ",", "♀", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

# Tables of changed content per ROM
# Allows for multi-language support.
class patchTables:
    English = []
    French = [[], [], [], [], [], [], [], [], [], [], [], ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "è", "é", "ù", "ß", "ç"], ["Ä", "Ö", "Ü", "ä", "ö", "ü", "ë", "ï", "â", "ô", "û", "ê", "î"], ["", "", "", "", "", "c'", "d'", "j'", "l'", "m'", "n'", "p'", "s'", "'s", "t'", "u'", "y'"], ["'", "PK", "MN", "-", "+", "", "?", "!", ".", "ァ", "ゥ", "ェ", "▷", "▶", "♂"], []]
    German = French
    Italian = [[], [], [], [], [], [], [], [], [], [], [], ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "è", "é", "ù", "À", "Á"], ["Ä", "Ö", "Ü", "ä", "ö", "ü", "È", "É", "Ì", "Í", "Ñ", "Ò", "Ó", "Ù", "Ú", "á"], ["ì", "í", "ñ", "ò", "ó", "ú", "º", "&", "'d", "'l", "'m", "'r", "'s", "'t", "'v"], ["'", "PK", "MN", "-", "¿", "¡", "?", "!", ".", "ァ", "ゥ", "ェ", "▷", "▶", "▼", "♂"], []]
    Spanish = Italian
    Japanese = [[None, "イ゙", "ヴ", "エ゙", "オ゙", "ガ", "ギ", "グ", "ゲ", "ゴ", "ザ", "ジ", "ズ", "ゼ", "ゾ", "ダ"], ["ヂ", "ヅ", "デ", "ド", "ナ゙", "ニ゙", "ヌ゙", "ネ゙", "ノ゙", "バ", "ビ", "ブ", "ボ", "マ゙", "ミ゙", "ム"], ["ィ゙", "あ゙", "い゙", "ゔ", "え゙", "お゙", "が", "ぎ", "ぐ", "げ", "ご", "ざ", "じ", "ず", "ぜ", "ぞ"], ["だ", "ぢ", "づ", "で", "ど", "な゙", "に゙", "ぬ゙", "ね゙", "の゙", "ば", "び", "ぶ", "べ", "ぼ", "ま゙"], ["パ", "ピ", "プ", "ポ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ", "ま゚", "が", "@_cont@", "@autocont@", "も゚", "@next line@", "@bottom line@"], ["@end@", "@paragraph@", "@players name@", "@rivals name@", "ポケモン", "@cont@", "……", "@done@", "@prompt@", "@target@", "@user@", "パソコン", "わざマシン", "トレーナー", "ロケットだん", "@dex@"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "V", "S", "L", "M", "：", "ぃ", "ぅ"], ["「", "」", "『", "』", "・", "…", "ぁ", "ぇ", "ぉ", "╔", "═", "╗", "║", "╚", "╝", " "], ["ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "サ", "シ", "ス", "セ", "ソ", "タ"], ["チ", "ツ", "テ", "ト", "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ホ", "マ", "ミ", "ム"], ["メ", "モ", "ヤ", "ユ", "ヨ", "ラ", "ル", "レ", "ロ", "ワ", "ヲ", "ン", "ッ", "ャ", "ュ", "ョ"], ["ィ", "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ"], ["た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま"], ["み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん", "っ"], ["ゃ", "ゅ", "ょ", "ー", "゜", "゛", "?", "!", "。", "ァ", "ゥ", "ェ", "▷", "▶", "▼", "♂"], ["円", "×", ".", "/", "ォ", "♀", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    List = {"English": English, "French": French, "German": German, "Italian": Italian, "Spanish": Spanish, "Japanese": Japanese}

# Since we only create tables to decode, create reverse encoding tables here.
encodeTables = {}
for patchTableName in patchTables.List.keys():
    loopDecodeTable = {}
    for i in range(16):
        for j in range(16):
            value = hex(i).split("x")[1] + hex(j).split("x")[1]
            value = int(value, 16)
            try:
                loopDecodeTable[patchTables.List[patchTableName][i][j]] = value
            except IndexError:
                try:
                    loopDecodeTable[decodeTable[i][j]] = value
                except IndexError:
                    pass
    encodeTables[patchTableName] = loopDecodeTable

def encodeString(string, patchTable=patchTables.English):
    encodeTableName = ""
    for patchTableName in patchTables.List.keys():
        if patchTables.List[patchTableName] == patchTable:
            encodeTableName = patchTableName
    encodedString = ""
    for character in string:
        encodedString = ''.join([encodedString, encodeCharacter(character, encodeTables[encodeTableName])])
    return encodedString

def encodeCharacter(character, encodeTable):
    if character in encodeTable.keys():
        return chr(encodeTable[character])
    else:
        return ""

def decodeString(string, patchTable=patchTables.English):
    decodedString = ""
    for character in string:
        decodedString = ''.join([decodedString, decodeCharacter(character, patchTable)])
    return decodedString

def decodeCharacter(character, patchTable):
    hexStr = hex(ord(character)).split("x")[1]
    # This ensures 0X for single character hex str
    hexStr = ("0" * (2 - len(hexStr))) + hexStr
    try:
        return patchTable[int(hexStr[0], 16)][int(hexStr[1], 16)]
    except IndexError:
        pass
    try:
        return decodeTable[int(hexStr[0], 16)][int(hexStr[1], 16)]
    except IndexError:
        return ""

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        if sys.argv[2] not in patchTables.List.keys():
            print("Not a valid patch table!")
            print("Valid patch tables:")
            print(', '.join(list(patchTables.List.keys())))
            exit()
        if sys.argv[1] == "encode":
            print(encodeString(" ".join(sys.argv[3:]), patchTables.List[sys.argv[2]]))
            exit()
        elif sys.argv[1] == "decode":
            print(decodeString(" ".join(sys.argv[3:]), patchTables.List[sys.argv[2]]))
            exit()
    print("Invalid usage!")
    print(sys.argv[0] + " [encode|decode] patchTable string")
    print("Example:")
    print(sys.argv[0] + " encode English \"Hello World!\"")
