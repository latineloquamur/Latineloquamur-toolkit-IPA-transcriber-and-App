
The aim of this program is to convert a list of latin words (with diacritic marks representing long and short vowels) into a dictionary with each word having its accentuated counterpart in the same line.
 
# Encoding=utf8
# Usage: python latin_accenter.py <source csv filename>
# Result: a csv file with lines in format <word>, <accentuated word>.


1. Encoding was set to UTF-8 to cater for non-ASCII (not a-z) characters. Before this setting was in place, Python had problems reading words.
2. Dictionaries were provided for conversion from diacritic signs to unicode representations [diacritics], from uppercase letters to lowercase letters [decapitalise] and unaccentuated to accentuated [stress].
3. Each word read is first parsed using parseWord function. What happens is that the word is broken into an array of unicode characters. Two new arrays are then created, one for sounds and one for vowels alone. The original array is processed by detecting diphthongs and diacritic marks written in non-ASCII characters and all characters forming one letter are put into a single cell of the new array. If a letter is recognised as a vowel or a diphthong it also lands in the vowel array.
4. To find where the accent lands in a word, method findStress and isLongVowel are created. It iterates across an array of vowels created as in part 3.
5. The method process is used to obtain an array of lowercase letters with accents put in, while diacritics removed. After finding where the accent lands, as in part 4., it can iterate backwards the array of sounds. Each sound is recognised as either a vowel (isVowel method), in which case it gets an accent if it is supposed to or gets its diacritic marks removed otherwise, or not a vowel, in which case it is just copied.
6. Finally, the method produce occupies with manipulating with upper- or lowercase first letter as the earlier mentioned methods are written for all words being lowercase. For now it deals with just the first letter of the word being capital or not, but there is a capability for extending it on all letters in a word through introducing a boolean (true/false) array in the beginning of produce method.
7. The source csv file is being read and simultaneously a destination csv file is created. As the source file was given as an Excel column it has a whitespace as a delimiter.
