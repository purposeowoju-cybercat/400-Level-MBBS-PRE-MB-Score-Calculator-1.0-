#Each Pharmacology posting carries 22.5%; Seminar presentations carry 10%
IntroA = 0.225
IntroB = 0.225
Block_I = 0.225
Block_II = 0.225
Seminar_mark = 0.10
#User Inputting Scores gotten for each posting
One = input("What was your Intro A score?\n")
Two = input("What was your intro B score?\n")
Three = input("What was your Block I score?\n")
Four = input("What was your Block II score\n")
Five = input("Since we don't know our seminar scores, input an expected overall score out of 100\n")
#Converting the scores into the "set" percentages
One1 = float(One)*IntroA
Two2 = float(Two)*IntroB
Three3 = float(Three)*Block_I
Four4 = float(Four)*Block_II
Five5 = float(Five)*Seminar_mark
#Sum total of Pre-MB scores
PRE_MB = One1 + Two2 + Three3 + Four4 + Five5
print("Your Pre-MB score is: " + str(PRE_MB))
if PRE_MB >= 50: print("Congratulations! You passed the Pre-MB")
elif PRE_MB >=45: print("You are in the borderline zone, but very close!")
else: print("Unfortunately, you are below the pass mark")
# MB Goal Setting: To help improve MB preparation
Real_premb = PRE_MB*0.50
needed_for_Distinction = (70-Real_premb)/0.50
needed_for_B_Grade = (50-Real_premb)/0.50
if needed_for_Distinction > 100: print("A distinction is mathematically impossible this year")
else: print(f"You need to get {needed_for_Distinction}% exactly in your MB to get a DISTINCTION in your overall Pharmacology!")
# if Real_premb <=20: print(f"You need to get {needed_for_B_Grade}% in your MB to get a B-GRADE or PASS (B-Grade = 50-69%")







