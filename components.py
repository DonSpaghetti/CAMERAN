import random


async def anconfus():
    """
    Randomly express your befuddlement
    """
    ion = [
        'https://i.kym-cdn.com/photos/images/original/000/012/974/cat_im_confus20110724-22047-q16ber.jpg',
        'https://media.giphy.com/media/l3q2K5jinAlChoCLS/200w.gif',
        'https://media1.tenor.com/images/5b034e96d84c6c6b57a9a04ca14aac02/tenor.gif',
        'https://media1.tenor.com/images/4cb306a83b1b41da055f47a8071a1934/tenor.gif',
    ]
    reply = (random.choice(ion))
    return reply

