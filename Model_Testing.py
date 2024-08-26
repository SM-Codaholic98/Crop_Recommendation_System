import pickle

with open('D:\\EDA\\Crop_Recommendation_System\\Crop_Recommendation_System.pkl', 'rb') as file:
    model = pickle.load(file)

ans = 'y'
while ans.lower() == 'y':
    print()
    print("Enter the details to predict the crop :-")
    temperature = float(input("Enter Temperatue : "))
    humidity = float(input("Enter Humidity : "))
    ph = float(input("Enter pH : "))
    rainfall = float(input("Enter Rainfall : "))
    n = float(input("Enter Nitrogen : "))
    p = float(input("Enter Phosphorus : "))
    k = float(input("Enter Potassium : "))
    
    prediction = model.predict([[temperature, humidity, ph, rainfall, n, p, k]])
    output = prediction[0]
    output = output[output.find('_') + 1 : ].upper()
    print(f"According to the above conditions {output} will grow.")
    
    print()
    ans = input("Press 'y/Y' to predict again : ")