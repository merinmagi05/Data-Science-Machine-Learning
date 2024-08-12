import matplotlib.pyplot as plt
days=['Mon','Tues','Wed','Thurs','Fri']
drinks_sales=[300,450,150,400,650]
food_sales=[400,500,350,300,500]

fig, axs=plt.subplots(2,1,figsize=(8,8))
plt.title("MERIN MAGI TELSON \nMCA 2023-2024",loc="right")

axs[0].plot(days,drinks_sales,linestyle='--',color='cyan',marker='H',markersize=8,markerfacecolor='magenta',markeredgecolor='black')
axs[0].set_xlabel('Days of Week')
axs[0].set_ylabel('Sales of Drinks')

axs[0].set_title('Sales Data1',loc='right')
axs[0].grid(True,color='blue',linestyle='dotted')

axs[1].plot(days,food_sales,linestyle='-',color='yellow',marker='D',markersize=8,markerfacecolor='green',markeredgecolor='red')
axs[1].set_xlabel('\nDays of the week')
axs[1].set_ylabel('Sale of Food')
axs[1].set_title('Sales Data2',loc='center')
axs[1].grid(True, color='blue',linestyle='dotted')

plt.tight_layout()
plt.show()