#Create Variables
BMI=0
wei=0
hei=0
o=0
run=0
#Get the Ture
E=True
#Apply True for While
while E:
#Inputs
    wei=float(input("Enter Your weight (kg) = "))
    hei=float(input("Enter your height (m) = "))
#Process
    BMI=wei/(hei*hei)
#Display the BMI values
    print("Your BMI is = ",BMI)
#Process
    #18.5>BMI,
    if (BMI<18.5):
        print("Your Underweight")
    #24.9>BMI>18.5,
    elif (18.5<BMI<24.9):
         print("Your Normal")
    #29.9>BMI>25,
    elif (25<BMI<29.9):
         print("Your Overweight")
    #BMI>=30,
    elif (30<=BMI):
         print("Your Obese")
#Need to check BMI values
    o=input("Do you want to check BMI VALUES ? (Yes/No) = ")
    if o=="Yes":
#Display the BMI values
            print("Underweight: less than 18.5")
            print("Normal: between 18.5 and 24.9")
            print("Overweight: between 25 and 29.9")
            print("Obese: 30 or greater")

#Need to run/stop program?
    run=input("Do you want to run this program again ? (Yes/No) = ")
#True While for run program
    if run=="Yes":
        E=True
#Fales While for stop program
    else:
        E=False
print("END")
    
            





