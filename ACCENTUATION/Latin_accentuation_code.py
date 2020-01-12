
# encoding=utf8
# Usage: python latin_accentuation_code.py <source csv filename>
# Result: a csv file with lines in format <word>, <accentuated word>.

import sys, csv
reload(sys)
sys.setdefaultencoding('utf8')

diacritics = {
    'á':'\xc3\xa1',
    'é':'\xc3\xa9',
    'í':'\xc3\xad',
    'ó':'\xc3\xb3',
    'ú':'\xc3\xba',
    'ǽ':'\xc7\xbd',
    'œ́':'\xc5\x93\xcc\x81',
    'ă':'\xc4\x83',
    'ā':'\xc4\x81',
    'ĕ':'\xc4\x95',
    'ē':'\xc4\x93',
    'ĭ':'\xc4\xad',
    'ī':'\xc4\xab',
    'ī̆':'\xc4\xab\xcc\x86',
    'ŏ':'\xc5\x8f',
    'ō':'\xc5\x8d',
    'ō̆':'\xc5\x8d\xcc\x86',
    'ŭ':'\xc5\xad',
    'ū':'\xc5\xab',
    'ū̆':'\xc5\xab\xcc\x86',
    'ў':'\xd1\x9e',
    'ȳ':'\xc8\xb3',
    'ý':'\xc3\xbd',
    'Á':'\xc3\x81',
    'É':'\xc3\x89',
    'Í':'\xc3\x8d',
    'Ó':'\xc3\x93',
    'Ú':'\xc3\x9a',
    'Ǽ':'\xc7\xbc',
    'Œ́':'\xc5\x92\xcc\x81',
    'Ă':'\xc4\x82',
    'Ā':'\xc4\x80',
    'Ĕ':'\xc4\x94',
    'Ē':'\xc4\x92',
    'Ĭ':'\xc4\xac',
    'Ī':'\xc4\xaa',
    'Ī̆':'\xc4\xaa\xcc\x86',
    'Ŏ':'\xc5\x8e',
    'Ō':'\xc5\x8c',
    'Ō̆':'\xc4\x8c\xcc\x86',
    'Ŭ':'\xc5\xac',
    'Ū':'\xc5\xaa',
    'Ū̆':'\xc5\xaa\xcc\x86',
    'Ў':'\xd0\x8e',
    'Ȳ':'\xc8\xb2',
    'Ý':'\xc3\x9d'
}

decapitalised = {
    '\xc3\x81':'\xc3\xa1', # 'Á'
    '\xc3\x89':'\xc3\xa9', # 'É'
    '\xc3\x8d':'\xc3\xad', # 'Í'
    '\xc3\x93':'\xc3\xb3', # 'Ó'
    '\xc3\x9a':'\xc3\xba', # 'Ú'
    '\xc7\xbc':'\xc7\xbd', # 'Ǽ'
    '\xc5\x92\xcc\x81':'\xc5\x93\xcc\x81', # 'Œ́'
    '\xc4\x82':'\xc4\x83', # 'Ă'
    '\xc4\x80':'\xc4\x81', # 'Ā'
    '\xc4\x94':'\xc4\x95', # 'Ĕ'
    '\xc4\x92':'\xc4\x93', # 'Ē'
    '\xc4\xac':'\xc4\xad', # 'Ĭ'
    '\xc4\xaa':'\xc4\xab', # 'Ī'
    '\xc4\xaa\xcc\x86':'\xc4\xab\xcc\x86', # Ī̆
    '\xc5\x8e':'\xc5\x8f', # 'Ŏ'
    '\xc5\x8c':'\xc5\x8d', # 'Ō'
    '\xc4\x8c\xcc\x86':'\xc5\x8d\xcc\x86', # 'Ō̆'
    '\xc5\xac':'\xc5\xad', # 'Ŭ'
    '\xc5\xaa':'\xc5\xab', # 'Ū'
    '\xc5\xaa\xcc\x86':'\xc5\xab\xcc\x86', # 'Ū̆'
    '\xd0\x8e':'\xd1\x9e', # 'Ў'
    '\xc8\xb2':'\xc8\xb3', # 'Ȳ'
    '\xc3\xbd':'\xc3\xbd' # 'Ý'
}

capitalised = {v: k for k, v in decapitalised.items()}

# Returns true if the first letter of the word is capital, false otherwise.
def isCapitalised(word):
    bytes = list(word)
    if bytes[0] == '\xc4':
        if bytes[1] == '\x82' or bytes[1] == '\x80' or bytes[1] == '\x94' or bytes[1] == '\x92' or bytes[1] == '\xac' or bytes[1] == '\xaa':
            return True
        else:
            return False
    elif bytes[0] == '\xc5':
        if bytes[1] == '\xaa' or bytes[1] == '\x8c' or bytes[1] == '\x8e' or bytes[1] == '\xac':
            return True
        else:
            return False
    else:
        return False

# Takes a word written with an initial uppercase and converts it to lowercase.
def decapitalise(word):
    word.lower()
    bytes = list(word)
    bytes[1] = chr(ord(bytes[1]) + 1)
    newWord = ''
    for char in bytes:
        newWord += char
    return newWord

# Takes a lowercase word and capitalises the first letter.
def capitalise(sounds):
    if(sounds[0].islower()):
        sounds[0] = sounds[0].upper()
    else:
        sounds[0] = capitalised[sounds[0]]
    return sounds

stress = {
    'a':'\xc3\xa1',
    'e':'\xc3\xa9',
    'i':'\xc3\xad',
    'o':'\xc3\xb3',
    'u':'\xc3\xba',
    '\xc4\x81':'\xc3\xa1', # ā
    '\xc4\x93':'\xc3\xa9', # ē
    '\xc4\xab':'\xc3\xad', # ī
    '\xc5\x8d':'\xc3\xb3', # ō
    '\xc5\xab':'\xc3\xba', # ū
    '\xc4\x83':'\xc3\xa1', # ă
    '\xc4\x95':'\xc3\xa9', # ĕ
    '\xc4\xad':'\xc3\xad', # ĭ
    '\xc5\x8f':'\xc3\xb3', # ŏ
    '\xc5\xad':'\xc3\xba', # ŭ
    '\xc5\x8d\xcc\x86':'\xc3\xb3', # ō̆
    'ae':'\xc7\xbd',
    'oe':'\xc5\x93\xcc\x81',
    'au':'\xc3\xa1u',
    '\xc4\x81e':'\xc7\xbd', # āe
    'a\xc4\x93':'\xc7\xbd', # aē
    'a\xc4\x95':'\xc7\xbd', # aĕ
    '\xc4\x83\xc4\x93':'\xc7\xbd', # ăē
    '\xc4\x83u':'\xc3\xa1u', # ău
    '\xc4\x83\xc5\xab':'\xc3\xa1u', # ăū
    '\xc4\x81\xc4\x95': '\xc7\xbd', # āĕ
    '\xc4\x81u':'\xc3\xa1u', # āu
    '\xc5\x8de':'\xc5\x93\xcc\x81', # ōe
    '\xc5\x8d\xc4\x95':'\xc5\x93\xcc\x81', # ōĕ
    'o\xc4\x93':'\xc5\x93\xcc\x81', # oē
    'o\xc4\x95':'\xc5\x93\xcc\x81', # oĕ
    '\xc5\x8f\xc4\x93':'\xc5\x93\xcc\x81', # ŏē
    '\xc5\xab\xcc\x86':'\xc3\xba', # ū̆
    '\xd1\x9e':'\xc3\xbd', # ў
    'y':'\xc3\xbd',
    '\xc4\xab\xcc\x86':'\xc3\xad', # ī̆
    '\xc8\xb3':'\xc3\xbd' # ȳ
}

diacritics_removed = {
    'a':'a',
    'e':'e',
    'i':'i',
    'o':'o',
    'u':'u',
    'y':'y',
    '\xc4\x81':'a', # ā
    '\xc4\x93':'e', # ē
    '\xc4\xab':'i', # ī
    '\xc5\x8d':'o', # ō
    '\xc5\xab':'u', # ŭ
    'ae':'ae',
    'oe':'oe',
    'au':'au',
    '\xc4\x81e':'ae', # āe
    'a\xc4\x93':'ae', # aē
    'a\xc4\x95':'ae', # aĕ
    '\xc4\x83\xc4\x93':'ae', # ăē
    '\xc4\x83u':'au', # ău
    '\xc4\x83\xc5\xab':'au', # ăū
    '\xc4\x81\xc4\x95': 'ae', # āĕ
    '\xc4\x81u':'au', # āu
    '\xc5\x8de':'oe', # ōe
    '\xc5\x8d\xc4\x95':'oe', # ōĕ
    'o\xc4\x93':'oe', # oē
    'o\xc4\x95':'oe', # oĕ
    '\xc5\x8f\xc4\x93':'oe', # ŏē
    '\xc4\x83':'a',
    '\xc4\x95':'e',
    '\xc4\xad':'i',
    '\xc5\x8f':'o',
    '\xc5\x8d\xcc\x86':'o',
    '\xc5\xad':'u',
    '\xc5\xab\xcc\x86':'u', # ū̆
    '\xd1\x9e':'y', # ў
    '\xc4\xab\xcc\x86': 'i', # ī̆
    '\xc8\xb3':'y ' # ȳ
}

# This method takes a lowercase word and return 2 arrays - one of sounds
# (diphtong letters are combined) and one of just vowels.
def parseWord(word):
    bytes = list(word)
    sounds = []
    vowels = []
    first_vowel_read = False
    skipOne = False
    skipTwo = False
    skipThree = False
    for i in range(len(bytes)):
        if skipThree:
            skipThree = False
            skipTwo = True
            continue
        if skipTwo:
            skipTwo = False
            skipOne = True
            continue
        if skipOne:
            skipOne = False
            continue
        byte = bytes[i]
        if (byte == 'a' or byte == 'e' or byte == 'i' or byte =='o' or byte == 'u' or byte == '\xc4' or byte == '\xc5' or byte == '\xd1' or byte == '\xc8'):
            if (not i == (len(bytes) - 1)):
                nbyte = bytes[i+1]
                if byte == 'a':
                    #           ae  or          au
                    if nbyte == 'e' or nbyte == 'u':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        skipOne = True
                    # Either aĕ or aē
                    elif nbyte == '\xc4':
                        nnbyte = bytes[i+2]
                        if nnbyte == '\x95' or nnbyte == '\x95':
                            sound = '' + byte + '\xc4' + bytes[i+2]
                            sounds.append(sound)
                            vowels.append(sounds)
                            skipTwo = True
                    else:
                        sounds.append('a')
                        vowels.append('a')
                elif byte == 'o':
                    # oe
                    if nbyte == 'e':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        vowels.append(sound)
                        skipOne = True
                    # oē or oĕ
                    if nbyte == '\xc4':
                        nnbyte = bytes[i+2]
                        if nnbyte == '\x95' or nnbyte == '\x95':
                            sound = '' + byte + '\xc4' + bytes[i+2]
                            sounds.append(sound)
                            vowels.append(sounds)
                            skipTwo = True
                    else:
                        sounds.append('o')
                        vowels.append('o')
                elif byte == '\xc4':
                    # ă
                    if nbyte == '\x83':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            # ău
                            if nnbyte == 'u':
                                sound = '' + byte + nbyte + nnbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipTwo = True
                            # ăū or ăē
                            elif ((nnbyte == '\xc5' and bytes[i+3] == '\xab') or  (nnbyte == '\xc4' and bytes[i+3] == '\x93')):
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True
                    # ā
                    elif nbyte == '\x81':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            # āu or āe
                            if nnbyte == 'u' or nnbyte == 'e':
                                sound = '' + byte + nbyte + nnbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipTwo = True
                            # āĕ
                            elif nnbyte == '\xc4' and bytes[i+3] == '\x93':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True
                    # Vowels that do not begin diphtongs:
                    #               ĕ   or             ē   or           ĭ
                    elif nbyte == '\x95' or nbyte == '\x93' or nbyte == '\xad':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        vowels.append(sound)
                        skipOne = True
                    # ī or ī̆
                    elif nbyte == '\xab':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            if nnbyte == '\xcc':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True
                elif byte == '\xc5':
                    nbyte = bytes[i+1]
                    #             ŭ
                    if nbyte == '\xad':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        vowels.append(sound)
                        skipOne = True
                    #       ū or ū̆
                    elif nbyte =='\xab':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            if nnbyte == '\xcc' and bytes[i+3] == '\x86':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True
                    # 'ō' = '\xc5\x8d' or 'ō̆' = '\xc5\x8d\xcc\x86'
                    elif nbyte == '\x8d':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            # 'ō̆'' = '\xc5\x8d\xcc\x86'
                            if nnbyte == '\xcc' and bytes[i+3] == '\x86':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            # ōe
                            elif nnbyte == 'e':
                                sound = '' + byte + nbyte + nnbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipTwo = True
                            # ōĕ
                            elif nnbyte == '\xc4' and bytes[i+3] == '\x95':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True

                    # ŏ
                    elif nbyte == '\x8f':
                        if (i < len(bytes) - 2):
                            nnbyte = bytes[i+2]
                            # ŏē
                            if nnbyte == '\xc4' and bytes[i+3] == '\x93':
                                sound = '' + byte + nbyte + nnbyte + bytes[i+3]
                                sounds.append(sound)
                                vowels.append(sound)
                                skipThree = True
                            else:
                                sound = '' + byte + nbyte
                                sounds.append(sound)
                                vowels.append(sound)
                                skipOne = True
                        else:
                            sound = '' + byte + nbyte
                            sounds.append(sound)
                            vowels.append(sound)
                            skipOne = True
                # ў
                elif byte == '\xd1':
                    nbyte = bytes[i+1]
                    if nbyte == '\x9e':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        vowels.append(sound)
                        skipOne = True
                # ȳ
                elif byte == '\xc8':
                    nbyte = bytes[i+1]
                    if nbyte == '\xb3':
                        sound = '' + byte + nbyte
                        sounds.append(sound)
                        vowels.append(sound)
                        skipOne = True
                else:
                    sounds.append(byte)
                    vowels.append(byte)
            else:
                sounds.append(byte)
                vowels.append(byte)
        else:
            sounds.append(byte)
    return[sounds, vowels]

# Returns true if a sound is a long vowel or a diphtong.
def isLongVowel(sound):
    # ā, ē, ī, ō, ū, ȳ
    if (sound == diacritics['ā'] or sound == diacritics['ē'] or sound == diacritics['ī'] or sound == diacritics['ō'] or sound == diacritics['ū'] or sound == diacritics['ȳ']):
        return True
    # ae, oe, au
    elif (sound == 'ae' or sound == 'oe' or sound == 'au'):
        return True
    # āe, aē, aĕ
    elif (sound == '\xc4\x81e' or sound == 'a\xc4\x93' or sound == 'a\xc4\x95'):
        return True
    # ăē, ău, ăū
    elif (sound == '\xc4\x83\xc4\x93' or sound == '\xc4\x83u' or sound == '\xc4\x83\xc5\xab'):
        return True
    # āĕ, āu
    elif (sound == '\xc4\x81\xc4\x95' or sound == '\xc4\x81u'):
        return True
    # ōe, ōĕ,
    elif (sound == '\xc5\x8de' or sound == '\xc5\x8d\xc4\x95'):
        return True
    # oē, oĕ,
    elif (sound == 'o\xc4\x93' or sound == 'o\xc4\x95'):
        return True
    # ŏē
    elif (sound == '\xc5\x8f\xc4\x93'):
        return True
    else:
        return False

# Returns true if a sound is a vowel, and false otherwise.
def isVowel(sound):
    if isLongVowel(sound):
        return True
    elif sound == 'a' or sound == 'e' or sound == 'i' or sound == 'o' or sound == 'u':
        return True
    elif sound == diacritics['ă'] or sound == diacritics['ĕ'] or sound == diacritics['ĭ'] or sound == diacritics['ŏ'] or sound == diacritics['ŭ']:
        return True
    elif sound == diacritics['ō̆'] or sound == diacritics['ū̆'] or sound == diacritics['ў'] or sound == diacritics['ī̆']:
        return True
    else:
        return False

# Return 2 if the accent falls on penultimate vowel.
# Return 3 if it falls on the third vowel from the end.
# Return 0 otherwise.
def findStress(vowels):
    if len(vowels) < 2:
        return 0
    elif isLongVowel(vowels[-2]):
        return 2
    else:
        return 3

# Takes a lowercase word and returns an array of lowercase letters
# with accent mark present and other diacritics removed.
def process(word):
    parsedWord = parseWord(word)
    sounds = parsedWord[0]
    reversed_sounds = list(reversed(sounds))
    new_reversed = []
    vowels = parsedWord[1]
    stressIndex = findStress(vowels)
    vowelIndex = 0
    for sound in reversed_sounds:
        if isVowel(sound):
            vowelIndex += 1
            if vowelIndex == stressIndex:
                new_reversed.append(stress[sound])
            else :
                new_reversed.append(diacritics_removed[sound])
        # Consonant
        else:
            new_reversed.append(sound)
    return list(reversed(new_reversed))

# This method takes a word, puts an accent mark in the correct spot and removes
# diacritics.
def produce(word):
    cap = isCapitalised(word)
    if cap:
        word = decapitalise(word)
    result = ''
    processed = process(word)
    if cap:
        processed = capitalise(processed)
    for sound in processed:
        result += sound
    return result

filename = sys.argv[1]
csv_filename = filename.split('.')[0] + '_proc.csv'
with open(filename, 'r') as source:
    with open(csv_filename, 'w') as dest:
        output = csv.writer(dest, delimiter=",")
        reader = csv.reader(source, delimiter=' ')
        for row in reader:
            source_word = ''
            for element in row:
                # Ignore whitespaces
                if element == ' ' or element == '' or element == None:
                    continue
                else:
                    source_word = element
            dest_word = produce(source_word)
            output.writerow([source_word.decode('utf8'), dest_word.decode('utf8')])
