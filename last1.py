import random

count = int(input("Enter the number of dice rolls (between 100 and 1,000,000) : "))
if count < 100 or count > 1000000:
    print("Please enter a number within the specific range")
    count = int(input("Enter the number of dice rolls (between 100 and 1,000,000) : "))

dice_1 = []
dice_2 = []
dice_3 = []
dice_4 = []
dice_5 = []
dice_6 = []
for i in range(count):
    dice_roll = random.randint(1,6)
    if dice_roll == 1:
        dice_1.append(dice_roll)
    elif dice_roll == 2:
        dice_2.append(dice_roll)
    elif dice_roll == 3:
        dice_3.append(dice_roll)
    elif dice_roll == 4:
        dice_4.append(dice_roll)
    elif dice_roll == 5:
        dice_5.append(dice_roll)
    else:
        dice_6.append(dice_roll)

highest_num = [len(dice_1),len(dice_2),len(dice_3),len(dice_4),len(dice_5),len(dice_6)]
for i in range(6):
    if highest_num[0] < highest_num[i]:
        highest_num[0],highest_num[i] = highest_num[i],highest_num[0]

print(f'''
Dice Roll Frequency Histogram
1: {"*"*int((len(dice_1)/highest_num[0])*10)} ({len(dice_1)} times, {((len(dice_1)/count)*100):.2f}%)
2: {"*"*int((len(dice_2)/highest_num[0])*10)} ({len(dice_2)} times, {((len(dice_2)/count)*100):.2f}%)
3: {"*"*int((len(dice_3)/highest_num[0])*10)} ({len(dice_3)} times, {((len(dice_3)/count)*100):.2f}%)
4: {"*"*int((len(dice_4)/highest_num[0])*10)} ({len(dice_4)} times, {((len(dice_4)/count)*100):.2f}%)
5: {"*"*int((len(dice_5)/highest_num[0])*10)} ({len(dice_5)} times, {((len(dice_5)/count)*100):.2f}%)
6: {"*"*int((len(dice_6)/highest_num[0])*10)} ({len(dice_6)} times, {((len(dice_6)/count)*100):.2f}%)''')
