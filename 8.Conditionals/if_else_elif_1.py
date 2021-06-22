cals_consumed = 400 # cals you have taken already
cals_in_item = 100 # cals in your next eatable item

total_cals = cals_consumed + cals_in_item
print(f"Total calories today: {total_cals}")

if total_cals >= 1600:
    print("Don't eat it!")
    # pass
elif total_cals < 300:
    print("Eat a larger portion.")
else:
    print("Sure you can eat it!")