'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    starNum = ord(letter)+shift
    if letter == " ":
        return " "
    elif starNum > 64 and starNum <91:
        return chr(starNum)
    elif starNum > 90:
        newShift = (starNum-90)%26
        if newShift == 0:
            return "Z"
        else:
            return chr(64+newShift)
    elif starNum <65:
        newShift = (65-starNum)%26
        if newShift == 0:
            return "A"
        else:
            return chr(91-newShift)


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    NewMessage = list()
    for letter in message:
        heartNum = ord(letter) + shift
        if letter == " ":
            NewMessage.append(" ")
        elif heartNum > 64 and heartNum < 91:
            NewMessage.append(chr(heartNum))
        elif heartNum > 90:
            newShift = (heartNum - 90)%26
            if newShift == 0:
                NewMessage.append("Z")
            else:
                NewMessage.append(chr(64+newShift))
        elif heartNum < 65:
            newShift = (65 - heartNum)%26
            if newShift == 0:
                NewMessage.append("A")
            else:
                NewMessage.append(chr(91-newShift))
    NewMessage = "".join(NewMessage)
    return NewMessage


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    starNum = ord(letter_shift) - 65
    diaNum = ord(letter) +starNum
    if letter == " ":
        return " "
    elif diaNum > 64 and diaNum < 91:
        return chr(diaNum)
    elif diaNum > 90:
        newShift = (diaNum - 90)%26
        if newShift == 0:
            return ("Z")
        else:
            return chr(64+newShift)
    elif diaNum < 65:
        newShift = (65 - newShift)%26
        if newShift == 0:
            return ("A")
        else:
            return chr(91-newShift)


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(message)==len(key):
        relations = list(zip(list(message),list(key)))
    else:
        newKey = key
        if len(message)%len(key) == 0:
            while len(message) != len(newKey):
                newKey = newKey + key
            relations = list(zip(list(message),list(newKey)))
        else:
            while len(message)!=len(newKey) and len(message)>len(newKey):
                newKey=newKey+key
            if len(message)%len(newKey)==0:
                remoNum = len(newKey)-len(message)
                newKey = newKey[:-remoNum]
            relations = list(zip(list(message),list(newKey)))
    indiCount = 0
    FINmess = list()
    while indiCount < len(message):
        semiNum = ord(relations[indiCount][1]) - 65
        circNum = ord(relations[indiCount][0]) + semiNum
        if relations[indiCount][0] == " ":
            FINmess.append(" ")
        elif circNum > 64 and circNum < 91:
            FINmess.append(chr(circNum))
        elif circNum > 90:
            newShift = (circNum-90)%26
            if newShift == 0:
                FINmess.append("Z")
            else:
                FINmess.append(chr(64+newShift))
        elif circNum < 65:
            newShift = (65-circNum)%26
            if newShift == 0:
                FINmess.append("A")
            else:
                FINmess.append(chr(91-newShift))
        indiCount = indiCount+1
    FINmess = "".join(FINmess)
    return FINmess

    

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    while len(message)%shift != 0:
        message = message+"_"
    countER = 0
    startIn = 0
    charPerRow = int(len(message)/shift)
    roTraList = list()
    while countER < shift:
        startIn = startIn + charPerRow
        rowtracker = "r" + str(countER+1)
        rowtracker = list(message[startIn-charPerRow:startIn])
        roTraList.append(rowtracker)
        countER = countER + 1
    faiMess = list()
    indiCount = 0
    while indiCount < charPerRow:
        faiMessCounter = 0
        while faiMessCounter < shift:
            faiMess.append(roTraList[faiMessCounter][indiCount])
            faiMessCounter = faiMessCounter + 1
        indiCount = indiCount + 1
    faiMess = "".join(faiMess)
    return faiMess

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    OGmess = list()
    rowNum = list(range(shift))
    for num in rowNum:
        addNum = num
        while addNum <len(message):
            OGmess.append(message[addNum])
            addNum = addNum + shift
    OGmess = "".join(OGmess)
    return OGmess
