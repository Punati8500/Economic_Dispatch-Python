# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# Economic load dispatch at 13:00 Uhr

Load=823.65              # Power demand (MWh) at 13:00 Uhr 
data=pd.read_excel('./input.xlsx')   # data about Gas turbines from the task sheet 

a=data['first']              # a (€) values from fuel cost curves of Gas turbines 
b=data['second']             # b (€/MWh) values from fuel cost curves of Gas turbines  
c=data['third']            # c (€/MWh^2)values from fuel cost curves of Gas turbines 
Minimum_Capacity=data['fourth']     #  Minimum capacitiy (MW) values of Gas turbines 
Maximum_Capacity=data['fifth']     #  Maximum capacitiy (MW) values of Gas turbines 
Power_Demand=Load
Lambda=max(b)                  # assumed lambda value to solve the problem 

P = []
#while abs(Power_Demand)>0.00001:   # Transmission losses are neglected 
while abs(Power_Demand)>500:
    multiplier = (Lambda-b)/2
    P =np.divide(multiplier,c)
    P=np.minimum(P,Maximum_Capacity)
    P=np.maximum(P,Minimum_Capacity)
    Power_Demand=Load-np.sum(P)
    Lambda=Lambda+((Power_Demand*2)/(np.sum(np.add(1,c))))
    print Power_Demand

squaredP = np.multiply(P,P)

Fuel_Cost= np.add(a,np.multiply(b,P)+np.multiply(c,squaredP))         # Fuel cost of the Gas turbines
print Fuel_Cost 
total_Fuel_Cost=np.sum(Fuel_Cost)     # Total fuel cost of the plant to meet the demand 
print(total_Fuel_Cost)
#table(data(:,1),P,Fuel_Cost,'V',{'Unit' 'Power_Produced' 'Fuel_Cost'})