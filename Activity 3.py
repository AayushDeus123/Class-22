#Weather Prediction
weather = (1,0,0,1,0,1,1)
sunny = 0
rainy = 0

for i in range(0 , len(weather)):
    if weather[i] == 0:
        sunny += 1
    else:
        rainy += 1
        
if sunny > rainy:
    print('The weather is Sunny!')
else:
    print('The weather is Rainy')