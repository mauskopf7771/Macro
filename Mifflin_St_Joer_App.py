# Python Mifflin St. Joer Equation - this will eventually become an app.
# Mifflin St. Joer calculates your Basal Metabolic Rate - BMR - This is the number of caloeis 
# and macronutrients you require in order to maintain your bodyweight by doing nothing. 
# We will need to figure out a way to involve other bits of data etc. but for now, just the following:
# Weight
# Age
# Height I believe

# Men { [10 x weight (kg)] + [6.25 x height (cm) ] – [5 x age (y)] + 5 }x PAL
# Women { [10 x weight (kg)] + [6.25 x height (cm)] – [5 x age (y)] – 161} x PAL
# Example:  10 x 56.8 + 6.25 x 165 – 5 x 37 x 1.75 = 2193


weightkg = input()
weightlbs = weightkg * input()
weightstone = weightlbs * input()

heightcm = 176
heightfeet = 'idk'

age = 25

PAL = 1.1
# PAL adjusts for levels of activity
# Sedetary = 1.1-1.39 - Spend all day sitting
# Low physical activity = 1.40 - 1.59 - Office worker, does some walking
# Active = 1.60 - 1.89 - Traiing 1 hour a day or active person who walks 6-8 miles a day
# Very Active = 1.90 - 2.50 - Several hours of vigarous activity per day

Mmifflinstjoer = (((10*weightkg) + (6.25 * heightcm) - (5-age) + 5) * PAL)
Fmifflinstjoer = (((10*weightkg) + (6.25 * heightcm) - (5-age) - 161) * PAL)

print('CALORIES: ' + str(Mmifflinstjoer))
#print('FEMALES: ' + str(Fmifflinstjoer))

### CALCULATION OF MACROS ###
### This doesn't take bodyfatpercentage as a factor so the protein will be really high
protein = weightlbs * 0.8
fat = weightlbs * 0.35
calsprotein = protein * 4
calsfat = fat * 9
calsPandF = calsprotein + calsfat 
Carbs = ((Mmifflinstjoer - (calsprotein + calsfat))/4)

print('PROTEIN: ' + str(protein))
print('FAT: ' + str(fat))
print('CARBS: ' + str(Carbs))


#168g protein - sliced roast chicken breast 
#52g fat - 