def discount(price):
    if 100000 <= price < 300000:
        return int(price * .95)
    elif 300000 <= price < 500000:
        return int(price * .9)
    elif 500000 <= price:
        return int(price * .8)
    else:
        return price


def solution(price):
    return discount(price)
