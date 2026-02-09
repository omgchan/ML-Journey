import random
import matplotlib.pyplot as plt
import seaborn as sns

def roll_dice():
    roll = random.randint(1, 100)
    if roll <=50:
        # print(f"{roll} Shit, you lose!")
        return False
    elif roll == 100:
        # print(f"{roll} You Lose, on the house")
        return False
    elif 100>roll>50:
        # print(f"{roll} You Win")
        return True
    


def double_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    current_wager = 0
    wX, wY = [], []

    while current_wager < wager_count and value > 0:
        if wager > value:
            break  # bankrupt

        if roll_dice():
            value += wager
            wager = initial_wager  # reset after win
        else:
            value -= wager
            wager *= 2

        wX.append(current_wager)
        wY.append(value)
        current_wager += 1

    plt.plot(wX, wY)
    return value



finals = []

for _ in range(5000):
    finals.append(double_bettor(10000, 100, 5000))

plt.figure(figsize=(12, 6))
sns.kdeplot(finals, fill=True)
plt.xlabel("Final Account Value")
plt.title("Martingale: Distribution of Outcomes")
plt.show()




# def simple_bettor(funds, initial_wager, wager_count):
#     value = funds
#     wager = initial_wager

#     current_wager = 0
#     wX = []
#     wY = []


#     while current_wager < wager_count:
#         if roll_dice():
#             value += wager
#             wX.append(current_wager)
#             wY.append(value)
#         else:
#             value -= wager
#             wX.append(current_wager)
#             wY.append(value)

#         current_wager += 1
    
#     plt.plot(wX, wY)

#     return value


# # results = []
# x=1
# while x <= 100:
#     # results.append(simple_bettor(10000, 100, 100000))
#     x += 1

# plt.xlabel('Wager Count')
# plt.ylabel('Account Value')
# plt.show()
