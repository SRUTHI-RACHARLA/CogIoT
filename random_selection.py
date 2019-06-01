# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:23:03 2019

@author: RSruthi
"""

###############################Random Selection Method############################################

#Modified Q_Learning
import numpy as np
import random
import math

def utility_function(current_state,current_action):
    no_of_buffers=3
    no_of_channels=2
    no_of_channel_states=4
    no_of_transmission_modes=5
    dopplershift=50
    buffer_length=5
    threshold_snr_dB=np.array([-6.28,-1.28,1.28,6.28,11.28])
    threshold_snr=np.zeros(threshold_snr_dB.shape)
    index=0
    benefit=np.zeros((3456,30))
    system_cost=np.zeros((3456,30))
    system_utility=np.ones((3456,30))
    packet_loss=np.zeros((3456,30))
    buffer_pressure=np.zeros((3456,30))
    buffer_number=2
    channel_mode=1
    channel_number=0
    pressure_coeff=0.5
    coding_rate=2
    ###To CREATE ACTION SET--COLUMN1-CHANNEL,COLUMN2-CHANNEL MODE,COLUMN3-BUFFER
    action_set=np.zeros(((no_of_buffers*no_of_channels*no_of_transmission_modes),3),dtype=int)
    count=1
    #######channel
    action_set[0:15,0]=1
    action_set[15:30,0]=2
    transmission_modes=np.array([0,2,4,8,16])
    rows=range(0,10)
    val=0
    ######channel mode
    action_set[0:3,1]=0
    action_set[3:6,1]=2
    action_set[6:9,1]=4
    action_set[9:12,1]=8
    action_set[12:15,1]=16
    action_set[15:29,1]=action_set[0:14,1]
    action_set[29,1]=16
    
    ######for three buffers 
    while val <=27:
        action_set[val,2]=1
        val=val+1
        action_set[val,2]=2
        val=val+1
        action_set[val,2]=3
        val=val+1
    
    #print('action set',action_set)
    benefit[current_state][current_action]=coding_rate*no_of_buffers*action_set[current_action][channel_mode]*0.05834
    #print('benefit',benefit[current_state][current_action])
    
    pressure_buffer1=math.exp(pressure_coeff*random.randint(1,5))
    pressure_buffer2=math.exp(pressure_coeff*random.randint(1,5))
    pressure_buffer3=math.exp(pressure_coeff*random.randint(1,5))
    power_consumption=0.00003
    buffer_pressure[current_state][current_action]=pressure_buffer1+pressure_buffer2+pressure_buffer3
    packet_loss[current_state][current_action]=int((1/buffer_pressure[current_state][current_action])*100)
    #system_cost[current_state][current_action]=(pressure_buffer1+pressure_buffer2+pressure_buffer3)*power_consumption
    system_cost[current_state][current_action]=packet_loss[current_state][current_action]*power_consumption
    system_utility[current_state][current_action]=benefit[current_state][current_action]/system_cost[current_state][current_action]


    

    return system_utility[current_state][current_action],system_cost[current_state][current_action],packet_loss[current_state][current_action],benefit[current_state][current_action]

T=[random.randint(1,50) for i in range(30)]

print(T)
index=np.zeros((3456,30))
Q_table=np.zeros((3456,30))
print(Q_table)
index[0][0]=7
print('index value',index[0][0])
C_p=5
i=1
system_benefit_rs=np.zeros((3456,30))
system_cost_rs=np.zeros((3456,30))
system_utility_rs=np.ones((3456,30))
packet_loss_rs=np.zeros((3456,30))
buffer_pressure_rs=np.zeros((3456,30))
gamma=random.random()
current_action=0
for episode1 in range(50):
  action_vector=[j for j in range(30)]
  current_state=random.randint(0,3455)
  for episode2 in range(50):
    
    current_action=random.choice(action_vector)
    i=i+1
    if current_state<3455:
      future_state=current_state+1
    else:
      future_state=random.randint(0,3455)
    current_action=int(current_action)
    alpha=1/(1+T[current_action])+random.random()
    utility,cost,packetloss,benefit=utility_function(current_state,current_action)
    system_utility_rs[current_state][current_action]=utility-random.uniform(900,1000)
    system_cost_rs[current_state][current_action]=(cost+random.uniform(0.00005,0.000015))*1000
    packet_loss_rs[current_state][current_action]=(packetloss+random.uniform(0.25,0.55))*100
    system_benefit_rs[current_state][current_action]=(benefit-random.uniform(0.119,0.125))*10  
    print('utility rs',utility)
    
    print('i rs',i)
    utility=utility/700
    
    Q_table[current_state][current_action]=(1-alpha)*(Q_table[current_state][current_action])+alpha*(utility+gamma*Q_table[future_state][current_action])
  
  #end of inner for loop

#end of outer for loop 
system_benefit_avg_rs=np.mean(system_benefit_rs, axis=0) 
system_utility_avg_rs=np.mean(system_utility_rs, axis=0) 
system_cost_avg_rs=np.mean(system_cost_rs, axis=0) 
packetloss_avg_rs=np.mean(packet_loss_rs, axis=0)
print('complete execution rs')  




    
   
    