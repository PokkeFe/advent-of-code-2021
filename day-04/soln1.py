#!env python
 
bingo_draws = None
bingo_cards = []

def is_card_winner(card, drawn_values):
    # check rows
    for i in range(len(card)):
        if (len([x for x in card[i] if x not in drawn_values]) == 0):
            return True
    # check cols
    for i in range(len(card[0])):
        col = [row[i] for row in card]
        if (len([x for x in col if x not in drawn_values]) == 0):
            return True    
    return False

def get_card_leftover_sum(card, drawn_values):
    sum = 0
    for i in range(len(card)):
        for val in [x for x in card[i] if x not in drawn_values]:
            sum += int(val)
    return sum

with open("input") as input:
    # read the bingo order
    line = input.readline()

    bingo_draws = line[:-1].split(",")

    # skip blank line
    line = input.readline()

    bingo_card = []

    # read cards
    line = input.readline()
    while line != "":
        if line != "\n":
            row = line[:-1].split(" ")
            row = list(filter(lambda x: x != '', row))
            bingo_card.append(row)
        else:
            bingo_cards.append(bingo_card)
            bingo_card = []
        line = input.readline()
    bingo_cards.append(bingo_card)

for i in range(1, len(bingo_draws)):
    for card in bingo_cards:
        if is_card_winner(card, bingo_draws[:i]):
            leftover_sum = get_card_leftover_sum(card, bingo_draws[:i])
            latest_draw = int(bingo_draws[i - 1])
            print(f"answer: {leftover_sum * latest_draw}")
            exit()
