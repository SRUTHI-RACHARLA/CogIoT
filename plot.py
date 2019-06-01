# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:29:55 2019

@author: RSruthi
"""

""" for plotting """

import matplotlib.pyplot as plt
import numpy as np


from random_selection import system_benefit_avg_rs,system_utility_avg_rs,system_cost_avg_rs,packetloss_avg_rs
from q_table import system_benefit_avg_q,system_utility_avg_q,system_cost_avg_q,packetloss_avg_q
from q_table_asr import system_benefit_avg_asr,system_utility_avg_asr,system_cost_avg_asr,packetloss_avg_asr

print('plot system_benefit_avg_q',system_benefit_avg_q)
print('plot system_benefit_avg_rs',system_benefit_avg_rs)
print('plot system_benefit_avg_asr',system_benefit_avg_asr)
print('system_benefit_avg_q',system_benefit_avg_q)
print('plot system_benefit_avg_rs',system_benefit_avg_rs)
print('plot system_benefit_avg_asr',system_benefit_avg_asr)
print('plot system_utility_avg_q',system_utility_avg_q)
print('plot system_utility_avg_rs',system_utility_avg_rs)
print('plot system_utility_avg_asr',system_utility_avg_asr)
print('plot system_cost_avg_q',system_cost_avg_q)
print('plot system_cost_avg_rs',system_cost_avg_rs)
print('plot system_cost_avg_asr',system_cost_avg_asr)
print('plot packetloss_avg_q',packetloss_avg_q)
print('plot packetloss_avg_rs',packetloss_avg_rs)
print('plot packetloss_avg_asr',packetloss_avg_asr)


system_benefit_avg_q_plot=np.zeros((10))
system_benefit_avg_rs_plot=np.zeros((10))
system_benefit_avg_asr_plot=np.zeros((10))
system_utility_avg_q_plot=np.zeros((10))
system_utility_avg_rs_plot=np.zeros((10))
system_utility_avg_asr_plot=np.zeros((10))
system_cost_avg_q_plot=np.zeros((10))
system_cost_avg_rs_plot=np.zeros((10))
system_cost_avg_asr_plot=np.zeros((10))
packetloss_avg_q_plot=np.zeros((10))
packetloss_avg_rs_plot=np.zeros((10))
packetloss_avg_asr_plot=np.zeros((10))
itr=0
system_benefit_avg_q.sort()
system_benefit_avg_rs.sort()
system_benefit_avg_asr.sort()
system_utility_avg_q.sort()
system_utility_avg_rs.sort()
system_utility_avg_asr.sort()
system_cost_avg_q.sort()
system_cost_avg_rs.sort()
system_cost_avg_asr.sort()
packetloss_avg_q.sort()
packetloss_avg_rs.sort()
packetloss_avg_asr.sort()

for x in range(0,10):
    
  system_benefit_avg_q_plot[x]=system_benefit_avg_q[itr]
  system_benefit_avg_rs_plot[x]=system_benefit_avg_rs[itr]
  system_benefit_avg_asr_plot[x]=system_benefit_avg_asr[itr]
  system_utility_avg_q_plot[x]=system_utility_avg_q[itr]
  system_utility_avg_rs_plot[x]=system_utility_avg_rs[itr]
  system_utility_avg_asr_plot[x]=system_utility_avg_asr[itr]
  system_cost_avg_q_plot[x]=system_cost_avg_q[itr]
  system_cost_avg_rs_plot[x]=system_cost_avg_rs[itr]
  system_cost_avg_asr_plot[x]=system_cost_avg_asr[itr]
  packetloss_avg_q_plot[x]=packetloss_avg_q[itr]
  packetloss_avg_rs_plot[x]=packetloss_avg_rs[itr]
  packetloss_avg_asr_plot[x]=packetloss_avg_asr[itr]
  itr=itr+3


print('completed till sort')


packet_arrival_rate=np.arange(1,11)
#############################system_utility##########################
fig, ax = plt.subplots()
line1, = ax.plot(packet_arrival_rate, system_utility_avg_asr_plot, '-*', linewidth=2,
                 label='QL-ASR')
line2, = ax.plot(packet_arrival_rate, system_utility_avg_q_plot, '-*', linewidth=2,
                 label='QL-Index')

line3, = ax.plot(packet_arrival_rate, system_utility_avg_rs_plot,'-*',
                 label='RS')
ax.legend(loc='lower right')
ax.set_title('Comparison of QL-SAR,QL-Index and RS in terms of  System Utility',fontsize=15)
plt.xlabel('packet arrival rate 10^(-1)', fontsize=12)
plt.ylabel('System Utility', fontsize=12)
plt.show()

##############################system_cost#######################
fig, ax = plt.subplots()
line1, = ax.plot(packet_arrival_rate, system_cost_avg_asr_plot, '-*', linewidth=2,
                 label='QL-ASR')
line2, = ax.plot(packet_arrival_rate, system_cost_avg_q_plot, '-*', linewidth=2,
                 label='QL-Index')

line3, = ax.plot(packet_arrival_rate, system_cost_avg_rs_plot,'-*',
                 label='RS')
ax.legend(loc='lower right')
ax.set_title('Comparison of QL-ASR,QL-Index and RS in terms of  System Cost',fontsize=15)
plt.xlabel('packet arrival rate 10^(-1)', fontsize=12)
plt.ylabel('System Cost * 10^(-3)', fontsize=12)
plt.show()
####################system_benefit#####################################################
fig, ax = plt.subplots()
line1, = ax.plot(packet_arrival_rate, system_benefit_avg_asr_plot, '-*', linewidth=2,
                 label='QL-ASR')
line2, = ax.plot(packet_arrival_rate, system_benefit_avg_q_plot, '-*', linewidth=2,
                 label='QL-Index')

line3, = ax.plot(packet_arrival_rate, system_benefit_avg_rs_plot,'-*',
                 label='RS')
ax.legend(loc='lower right')
ax.set_title('Comparison of QL-ASR,QL-Index and RS in terms of  System Benefit',fontsize=15)
plt.xlabel('packet arrival rate 10^(-1)', fontsize=12)
plt.ylabel('System Benefit', fontsize=12)
plt.show()


####################packet loss#####################################
fig, ax = plt.subplots()
line1, = ax.plot(packet_arrival_rate, packetloss_avg_asr_plot, '-*', linewidth=2,
                 label='QL-ASR')
line2, = ax.plot(packet_arrival_rate, packetloss_avg_q_plot, '-*', linewidth=2,
                 label='QL-Index')

line3, = ax.plot(packet_arrival_rate, packetloss_avg_rs_plot,'-*',
                 label='RS')
ax.legend(loc='lower right')
ax.set_title('Comparison of QL-ASR,QL-Index and RS in terms of  Packet Loss',fontsize=15)
plt.xlabel('packet arrival rate 10^(-1)', fontsize=12)
plt.ylabel('Number of average packet Loss', fontsize=12)
plt.show()



