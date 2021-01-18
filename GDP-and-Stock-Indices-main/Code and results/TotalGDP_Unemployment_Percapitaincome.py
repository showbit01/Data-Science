import xlrd
import numpy as np
import matplotlib.pyplot as plt
from numpy import cov
from numpy import mean
from numpy import std
from scipy.stats import pearsonr

loc_sensex_data_quarterly=("E:/Data_Science_GDP_STOCK/SENSEX_DATA/Quarterly/SENSEX_QUARTERING_INVESTING.xlsx")
loc_nifty_data_quarterly=("E:/Data_Science_GDP_STOCK/NIFTY_50/Quaterly/NIFTY_50_INVESTING_QUARTERLY_DATA.xlsx")
loc_gdp_data=("E:/Statement_12_1stDec2020 (2).xlsx")
loc_unemployment_percapitaincome=("E:/Data_Science_GDP_STOCK/unemployment_percapita.xlsx")

sensex_quarterly_wb=xlrd.open_workbook(loc_sensex_data_quarterly)
nifty_quarterly_wb=xlrd.open_workbook(loc_nifty_data_quarterly)
gdp_quarterly_data=xlrd.open_workbook(loc_gdp_data)
unemployment_percapita_data=xlrd.open_workbook(loc_unemployment_percapitaincome)

sen_sheet=sensex_quarterly_wb.sheet_by_index(0)
nifty_sheet=nifty_quarterly_wb.sheet_by_index(0)
gdp_sheet=gdp_quarterly_data.sheet_by_index(0)
percapita_sheet=unemployment_percapita_data.sheet_by_index(0)

annual_gdp=[0]*9
unemployment_data=[]
percapita_data=[]
agriculture_gdp=[0]*9
mining_gdp=[0]*9
manufacturing_gdp=[0]*9
elec_gdp=[0]*9
con_gdp=[0]*9
trade_gdp=[0]*9
real_estate_gdp=[0]*9
public_gdp=[0]*9

for k in range(0,9):
    annual_gdp[k] = gdp_sheet.cell_value(20, k+1) + annual_gdp[k]
    public_gdp[k] = gdp_sheet.cell_value(13, k+1) + public_gdp[k]
    real_estate_gdp[k] = gdp_sheet.cell_value(12, k+1) + real_estate_gdp[k]
    trade_gdp[k] = gdp_sheet.cell_value(11, k+1) + trade_gdp[k]
    con_gdp[k] = gdp_sheet.cell_value(10, k+1) + con_gdp[k]
    elec_gdp[k] = gdp_sheet.cell_value(9, k+1) + elec_gdp[k]
    manufacturing_gdp[k] = gdp_sheet.cell_value(8, k+1) + manufacturing_gdp[k]
    mining_gdp[k] = gdp_sheet.cell_value(7, k+1) + mining_gdp[k]
    agriculture_gdp[k] = gdp_sheet.cell_value(6, k+1) + agriculture_gdp[k]



for k in range(0,9):
    x=k+1
    percapita_data.append(percapita_sheet.cell_value(x,1))

#print(percapita_data)
for k in range(0,9):
    x=k+13
    unemployment_data.append(percapita_sheet.cell_value(x,1))
#print(unemployment_data)


l_total_1=np.poly1d(np.polyfit(unemployment_data,annual_gdp,1))
l_total_2=np.poly1d(np.polyfit(percapita_data,annual_gdp,1))

l_mining_1=np.poly1d(np.polyfit(unemployment_data,mining_gdp,1))
l_mining_2=np.poly1d(np.polyfit(percapita_data,mining_gdp,1))

l_public_1=np.poly1d(np.polyfit(unemployment_data,public_gdp,1))
l_public_2=np.poly1d(np.polyfit(percapita_data,public_gdp,1))

l_estate_1=np.poly1d(np.polyfit(unemployment_data,real_estate_gdp,1))
l_estate_2=np.poly1d(np.polyfit(percapita_data,real_estate_gdp,1))

l_trade_1=np.poly1d(np.polyfit(unemployment_data,trade_gdp,1))
l_trade_2=np.poly1d(np.polyfit(percapita_data,trade_gdp,1))

l_con_1=np.poly1d(np.polyfit(unemployment_data,con_gdp,1))
l_con_2=np.poly1d(np.polyfit(percapita_data,con_gdp,1))

l_elec_1=np.poly1d(np.polyfit(unemployment_data,elec_gdp,1))
l_elec_2=np.poly1d(np.polyfit(percapita_data,elec_gdp,1))

l_man_1=np.poly1d(np.polyfit(unemployment_data,manufacturing_gdp,1))
l_man_2=np.poly1d(np.polyfit(percapita_data,manufacturing_gdp,1))

l_agr_1=np.poly1d(np.polyfit(unemployment_data,agriculture_gdp,1))
l_agr_2=np.poly1d(np.polyfit(percapita_data,agriculture_gdp,1))


Years=np.arange(2011,2020)
f1=plt.figure(1,dpi=80,figsize=(8,6))
plt.scatter(percapita_data,agriculture_gdp)
plt.scatter(percapita_data,mining_gdp)
plt.scatter(percapita_data,manufacturing_gdp)
plt.scatter(percapita_data,elec_gdp)
plt.scatter(percapita_data,con_gdp)
plt.scatter(percapita_data,trade_gdp)
plt.scatter(percapita_data,real_estate_gdp)
plt.scatter(percapita_data,public_gdp)

plt.plot(percapita_data,agriculture_gdp,label="Agriculture GDP")
plt.plot(percapita_data,mining_gdp,label="Mining GDP")
plt.plot(percapita_data,manufacturing_gdp,label="Manufacturing GDP")
plt.plot(percapita_data,elec_gdp,label="Electricity GDP")
plt.plot(percapita_data,con_gdp,label="Construction")
plt.plot(percapita_data,trade_gdp,label="Trade GDP")
plt.plot(percapita_data,real_estate_gdp,label="Real Estate GDP")
plt.plot(percapita_data,public_gdp,label="Public GDP")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.xlabel("Per Capita Income($)")
plt.ylabel("Sector GDP(Cr)")
plt.grid()
plt.legend(loc="upper left")
plt.title('Sector GDP vs Per Capita Income($)',fontsize='15')

f2=plt.figure(2,dpi=80,figsize=(8,6))
plt.scatter(unemployment_data,agriculture_gdp)
plt.scatter(unemployment_data,mining_gdp)
plt.scatter(unemployment_data,manufacturing_gdp)
plt.scatter(unemployment_data,elec_gdp)
plt.scatter(unemployment_data,con_gdp)
plt.scatter(unemployment_data,trade_gdp)
plt.scatter(unemployment_data,real_estate_gdp)
plt.scatter(unemployment_data,public_gdp)

plt.plot(unemployment_data,agriculture_gdp,label="Agriculture GDP")
plt.plot(unemployment_data,mining_gdp,label="Mining GDP")
plt.plot(unemployment_data,manufacturing_gdp,label="Manufacturing GDP")
plt.plot(unemployment_data,elec_gdp,label="Electricity GDP")
plt.plot(unemployment_data,con_gdp,label="Construction")
plt.plot(unemployment_data,trade_gdp,label="Trade GDP")
plt.plot(unemployment_data,real_estate_gdp,label="Real Estate GDP")
plt.plot(unemployment_data,public_gdp,label="Public GDP")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.xlabel("Unemployment Rate(%)")
plt.ylabel("Sector GDP(Cr)")
plt.grid()
plt.legend(loc="upper right")
plt.title('Sector GDP vs Unemployment Rate',fontsize='15')

fig, ax1 = plt.subplots(1,1,figsize=(8,6))

ax1.plot(Years, annual_gdp,label='Total GDP')
ax1.set_xlabel('Years', fontsize=15)
ax1.scatter(Years, annual_gdp)
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Total GDP', color='r',fontsize=15)
plt.legend(loc='center right')

ax2 = ax1.twinx()
ax2.plot(Years,unemployment_data,color='red',label='Unemployment Rate(%)')
ax2.scatter(Years,unemployment_data,color='red')
ax2.set_ylabel('Unemployment Rate',fontsize=15,color='r')
plt.grid()
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.legend(loc='center left')
plt.title('Annual GDP vs Unemployment Rate with Time',fontsize='15')
'''
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.25)) # move the right axis light bit to the right by 25 % of the axes
ax3.plot(time_arr, norm(energy_arr), 'black', linestyle='--', label='E_tot (J)', linewidth=5)
ax3.set_ylabel('E_tot (J)', color='black',fontsize=25)
ax3.tick_params('y', colors='black', labelsize=20)


fig.tight_layout()
plt.show()
'''
figure, axes1 = plt.subplots(1,1,figsize=(8,6))

axes1.plot(Years, annual_gdp,label='Total GDP')
axes1.set_xlabel('Years', fontsize=15)
axes1.scatter(Years, annual_gdp)
# Make the y-axis label, ticks and tick labels match the line color.
axes1.set_ylabel('Total GDP', color='r',fontsize=15)
plt.legend(loc='upper left')

axes2 = axes1.twinx()
axes2.plot(Years,percapita_data,color='red',label='Per Capita Income')
axes2.scatter(Years,percapita_data,color='red')
axes2.set_ylabel('Per Capita Income($)',fontsize=15,color='r')
plt.grid()
plt.legend(loc='lower right')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title('Annual GDP vs Per Capita Income with Time',fontsize='15')

figure1,axes=plt.subplots(1,1,figsize=(8,6))
axes.plot(Years, agriculture_gdp,label="Agriculture GDP")
axes.plot(Years, mining_gdp,label="Mining GDP")
axes.plot(Years, manufacturing_gdp,label="Manufacturing GDP")
axes.plot(Years, elec_gdp,label="Electricity GDP")
axes.plot(Years, con_gdp,label="Construction GDP")
axes.plot(Years, trade_gdp,label="Trade GDP")
axes.plot(Years, real_estate_gdp,label="Real Estate GDP")
axes.plot(Years, public_gdp,label="Public GDP")

axes.scatter(Years, agriculture_gdp)
axes.scatter(Years, mining_gdp)
axes.scatter(Years, manufacturing_gdp)
axes.scatter(Years, elec_gdp)
axes.scatter(Years, con_gdp)
axes.scatter(Years, trade_gdp)
axes.scatter(Years, real_estate_gdp)
axes.scatter(Years, public_gdp)


axes.set_xlabel('Years', fontsize=15)
# Make the y-axis label, ticks and tick labels match the line color.
axes.set_ylabel('Sector GDP', color='r',fontsize=15)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.grid()
plt.legend(loc='upper left')

axes_2 = axes.twinx()
axes_2.plot(Years,percapita_data,color='cyan',label="Per Capita Income")
axes_2.scatter(Years,percapita_data,color='cyan')
axes_2.set_ylabel('Per Capita Income($)',fontsize=15,color='r')
plt.grid()
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.legend(loc='lower right')
plt.title('Sector GDP vs Per Capita Income with Time',fontsize='15')

figure2,rohan=plt.subplots(1,1,figsize=(8,6))
rohan.plot(Years, agriculture_gdp,label="Agriculture GDP")
rohan.plot(Years, mining_gdp,label="Mining GDP")
rohan.plot(Years, manufacturing_gdp,label="Manufacturing GDP")
rohan.plot(Years, elec_gdp,label="Electricity GDP")
rohan.plot(Years, con_gdp,label="Construction GDP")
rohan.plot(Years, trade_gdp,label="Trade GDP")
rohan.plot(Years, real_estate_gdp,label="Real Estate GDP")
rohan.plot(Years, public_gdp,label="Public GDP")

rohan.scatter(Years, agriculture_gdp)
rohan.scatter(Years, mining_gdp)
rohan.scatter(Years, manufacturing_gdp)
rohan.scatter(Years, elec_gdp)
rohan.scatter(Years, con_gdp)
rohan.scatter(Years, trade_gdp)
rohan.scatter(Years, real_estate_gdp)
rohan.scatter(Years, public_gdp)

rohan.set_xlabel('Years', fontsize=15)
# Make the y-axis label, ticks and tick labels match the line color.
rohan.set_ylabel('Sector GDP', color='r',fontsize=15)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.grid()
plt.legend(loc='upper left')

rohan_2 = rohan.twinx()
rohan_2.plot(Years,unemployment_data,color='cyan',label="Unemployment Rate(%)")
rohan_2.scatter(Years,unemployment_data,color='cyan')
rohan_2.set_ylabel('Unemployment Rate(%)',fontsize=15,color='r')
plt.grid()
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.legend(loc='lower right')
plt.title('Sector GDP vs Unemployment Rate with Time',fontsize='15')
plt.show()