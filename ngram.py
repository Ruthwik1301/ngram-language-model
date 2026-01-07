

from collections import defaultdict, Counter
import random
import re

poe_text = '''
TRUE! — nervous — very, very dreadfully nervous I had been and am; but why will you say that I am mad?
The disease had sharpened my senses — not destroyed — not dulled them. Above all was the sense of hearing acute.
I heard all things in the heaven and in the earth. I heard many things in hell.
How, then, am I mad? Hearken! and observe how healthily — how calmly I can tell you the whole story.

It is impossible to say how first the idea entered my brain; but once conceived, it haunted me day and night.
Object there was none. Passion there was none. I loved the old man. He had never wronged me.
He had never given me insult. For his gold I had no desire.
I think it was his eye! yes, it was this! He had the eye of a vulture — a pale blue eye, with a film over it.
Whenever it fell upon me, my blood ran cold; and so by degrees — very gradually — I made up my mind
to take the life of the old man, and thus rid myself of the eye forever.

Now this is the point. You fancy me mad. Madmen know nothing. But you should have seen me.
You should have seen how wisely I proceeded — with what caution — with what foresight — with what dissimulation I went to work!
I was never kinder to the old man than during the whole week before I killed him.
And every night, about midnight, I turned the latch of his door and opened it — oh so gently!
And then, when I had made an opening sufficient for my head, I put in a dark lantern, all closed, closed,
so that no light shone out, and then I thrust in my head.
Oh, you would have laughed to see how cunningly I thrust it in!
I moved it slowly — very, very slowly, so that I might not disturb the old man's sleep.
It took me an hour to place my whole head within the opening so far that I could see him as he lay upon his bed.
Ha! — would a madman have been so wise as this?

And then, when my head was well in the room, I undid the lantern cautiously — oh, so cautiously — cautiously
(for the hinges creaked) — I undid it just so much that a single thin ray fell upon the vulture eye.
And this I did for seven long nights — every night just at midnight — but I found the eye always closed;
and so it was impossible to do the work; for it was not the old man who vexed me, but his Evil Eye.
And every morning, when the day broke, I went boldly into the chamber, and spoke courageously to him,
calling him by name in a hearty tone, and inquiring how he had passed the night.
So you see he would have been a very profound old man, indeed, to suspect that every night, just at twelve,
I looked in upon him while he slept.
'''

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

tokens = tokenize(poe_text)
N = 5
model = defaultdict(Counter)

for i in range(len(tokens) - N):
    context = tuple(tokens[i:i+N-1])
    target = tokens[i+N-1]
    model[context][target] += 1

def generate_text(seed_text, max_words=50):
    seed_tokens = tokenize(seed_text)
    current = tuple(seed_tokens[-(N-1):])
    output = list(seed_tokens)
    for _ in range(max_words):
        if current not in model:
            break
        next_word = random.choice(list(model[current].elements()))
        output.append(next_word)
        current = tuple(output[-(N-1):])
    return " ".join(output)

if __name__ == "__main__":
    samples = [
        "the night was very dark",
        "i heard a strange sound",
        "he opened the door slowly"
    ]
    for s in samples:
        print("Input:", s)
        print("Output:", generate_text(s, 40))
        print("-"*60)
