

directions = {
    "north": ("direction", "north"),
    "south": ("direction", "south"),
    "east": ("direction", "east"),
    "west": ("direction", "west"),
    "up": ("direction", "up"),
    "down": ("direction", "down"),
    "left": ("direction", "left"),
    "right": ("direction", "right"),
    "back": ("direction", "back"),
}

nouns = {
    "door": ("noun", "door"),
    "bear": ("noun", "bear"),
    "princess": ("noun", "princess"),
    "cabinet": ("noun", "cabinet"),
}
stops = {
    "the": ("stop", "the"),
    "in": ("stop", "in"),
    "of": ("stop", "of"),
    "from": ("stop", "from"),
    "at": ("stop", "at"),
    "it": ("stop", "it"),
}

verbs = {
    "go": ("verb", "go"),
    "kill": ("verb", "kill"),
    "eat": ("verb", "eat"),
    "fight": ("verb", "fight"),
}


def scan(user_input):
    words = user_input.lower()
    words = words.split()
    sentence = []

    for word in words:

        if word in directions:
            for word in words:
                try:
                    sentence.append(directions[word])
                except KeyError:
                    try:
                        sentence.append(("number", int(word)))
                    except ValueError:
                        sentence.append(("error", word))
            return sentence

        elif word in verbs:
            for word in words:
                try:
                    sentence.append(verbs[word])
                except KeyError:
                    try:
                        sentence.append(("number", int(word)))
                    except ValueError:
                        sentence.append(("error", word))
            return sentence

        elif word in stops:
            for word in words:
                try:
                    sentence.append(stops[word])
                except KeyError:
                    try:
                        sentence.append(("number", int(word)))
                    except ValueError:
                        sentence.append(("error", word))
            return sentence

        elif word in nouns:
            for word in words:
                try:
                    sentence.append(nouns[word])
                except KeyError:
                    try:
                        sentence.append(("number", int(word)))
                    except ValueError:
                        sentence.append(("error", word))
            return sentence

        else:
            for word in words:
                try:
                    sentence.append(("number", int(word)))
                except ValueError:
                    sentence.append(("error", word))
            return sentence
