import pandas
import os

#extract content of dataset in an array
ds=pandas.read_csv('salaryData.csv')

#separate feature and target
x=ds['YearsExperience'].values.reshape(30,1)
y=ds['Salary']

from sklearn.linear_model import LinearRegression

#train the model
model=LinearRegression()
model.fit(x,y)

#menu driven

while True:

    user_data=input( "Enter your years of experience = \n" )

    #if(user_data=="exit"):
        #break

    exp=float(user_data)

    #exception handling
    if(exp==0):
        print("Better earn some experience first!!!")
    else:
        #predicting the value
        predicted_value=model.predict([[exp]])
        print("Predicted Salary of person with {} yrs of experience is".format(exp)+'\x1b[4;60;60m'+ " {}".format(predicted_value[0]) + " INR\n"+'\x1b[0m')
        print("Do you want to exit? or if you want to continue prediction then press enter .. ")
        term=input("Type exit to terminate and press enter to continue..")
        if(term=="exit"):
            break
        
