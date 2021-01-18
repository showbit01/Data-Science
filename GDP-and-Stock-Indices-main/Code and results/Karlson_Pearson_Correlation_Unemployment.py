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

f1=plt.figure(1)
plt.plot(percapita_data,annual_gdp)
plt.scatter(percapita_data,annual_gdp)
plt.xlabel("Per Capita Income($)")
plt.ylabel("Total GDP(Cr)")
plt.xticks(np.arange(1400,2200,100))
plt.title("Karl Pearson Coefficient = {:.3f}".format(pearsonr(percapita_data,annual_gdp)[0]))
plt.plot(percapita_data,l_total_2(percapita_data),color='red')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.grid()
plt.legend()

f2=plt.figure(2)
plt.plot(unemployment_data,annual_gdp)
plt.scatter(unemployment_data,annual_gdp)
plt.xlabel("Unemployment Rate(%)")
plt.ylabel("Total GDP(Cr)")
plt.xticks(np.arange(5.2,5.8,0.05))
plt.title("Karl Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,annual_gdp)[0]))
plt.plot(unemployment_data,l_total_1(unemployment_data),color='red')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.grid()
plt.legend()


f3,a=plt.subplots(2,4)
a[0][0].scatter(unemployment_data,public_gdp,label='Public GDP')
a[0][0].plot(unemployment_data,public_gdp)
a[0][0].set_xlabel("Unemployment Rate(%)")
a[0][0].set_ylabel("Public GDP(Cr)")
a[0][0].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[0][0].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,public_gdp)[0]))
a[0][0].plot(unemployment_data,l_public_1(unemployment_data),color='red')
a[0][0].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[0][0].grid()
a[0][0].legend()

#f4=plt.figure(4)
a[0][1].scatter(unemployment_data,real_estate_gdp,label="Real Estate GDP")
a[0][1].plot(unemployment_data,real_estate_gdp)
a[0][1].set_xlabel("Unemployment Rate(%)")
a[0][1].set_ylabel("Real Estate GDP(Cr)")
a[0][1].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[0][1].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,real_estate_gdp)[0]))
a[0][1].plot(unemployment_data,l_estate_1(unemployment_data),color='red')
a[0][1].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[0][1].grid()
a[0][1].legend()

#f5=plt.figure(5)
a[0][2].scatter(unemployment_data,trade_gdp,label="Trade GDP")
a[0][2].plot(unemployment_data,trade_gdp)
a[0][2].set_xlabel("Unemployment Rate(%)")
a[0][2].set_ylabel("Trade GDP(Cr)")
a[0][2].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[0][2].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,trade_gdp)[0]))
a[0][2].plot(unemployment_data,l_trade_1(unemployment_data),color='red')
a[0][2].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[0][2].grid()
a[0][2].legend()

#f6=plt.figure(6)
a[0][3].scatter(unemployment_data,con_gdp,label="Construction GDP")
a[0][3].plot(unemployment_data,con_gdp)
a[0][3].set_xlabel("Unemployment Rate(%)")
a[0][3].set_ylabel("Construction GDP(Cr)")
a[0][3].set_xticks(np.arange(5.2,5.8,0.1))
#plt.ticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[0][3].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,con_gdp)[0]))
a[0][3].plot(unemployment_data,l_con_1(unemployment_data),color='red')
a[0][3].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[0][3].grid()
a[0][3].legend()

#f7=plt.figure(7)
a[1][0].scatter(unemployment_data,elec_gdp,label="Electricity GDP")
a[1][0].plot(unemployment_data,elec_gdp)
a[1][0].set_xlabel("Unemployment Rate(%)")
a[1][0].set_ylabel("Electricity GDP(Cr)")
a[1][0].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[1][0].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,elec_gdp)[0]))
a[1][0].plot(unemployment_data,l_elec_1(unemployment_data),color='red')
a[1][0].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[1][0].grid()
a[1][0].legend()

#f8=plt.figure(8)
a[1][1].scatter(unemployment_data,manufacturing_gdp,label='Manufacturing GDP')
a[1][1].plot(unemployment_data,manufacturing_gdp)
a[1][1].set_xlabel("Unemployment Rate(%)")
a[1][1].set_ylabel("Manufacturing GDP(Cr)")
a[1][1].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[1][1].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,manufacturing_gdp)[0]))
a[1][1].plot(unemployment_data,l_man_1(unemployment_data),color='red')
a[1][1].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[1][1].grid()
a[1][1].legend()

#f9=plt.figure(9)
a[1][2].scatter(unemployment_data,mining_gdp,label="Mining GDP")
a[1][2].plot(unemployment_data,mining_gdp)
a[1][2].set_xlabel("Unemployment Rate(%)")
a[1][2].set_ylabel("Mining GDP(Cr)")
a[1][2].set_xticks(np.arange(5.2,5.8,0.1))
#plt.yticks(np.arange(0.8*(10**7),1.6*(10**7),0.05*(10**7)))
a[1][2].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,mining_gdp)[0]))
a[1][2].plot(unemployment_data,l_mining_1(unemployment_data),color='red')
a[1][2].ticklabel_format(useOffset=True)
a[1][2].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[1][2].grid()
a[1][2].legend()

#f10=plt.figure(10)
a[1][3].scatter(unemployment_data,agriculture_gdp,label="Agriculture GDP")
a[1][3].plot(unemployment_data,agriculture_gdp)
a[1][3].set_xlabel("Unemployment Rate(%)")
a[1][3].set_ylabel("Agriculture GDP(Cr)")
a[1][3].set_xticks(np.arange(5.2,5.8,0.1))
a[1][3].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
a[1][3].set_title("     Pearson Coefficient = {:.3f}".format(pearsonr(unemployment_data,agriculture_gdp)[0]))
a[1][3].plot(unemployment_data,l_agr_1(unemployment_data),color='red')
a[1][3].grid()
a[1][3].legend()

f3.tight_layout()
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.4, hspace=0.4)
plt.show()

print("The Pearson Correlation between Unemployment and GDP is {}".format(pearsonr(unemployment_data,annual_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and GDP is {}".format(pearsonr(percapita_data,annual_gdp)[0]))

print("The Pearson Correlation between Unemployment and Public GDP is {}".format(pearsonr(unemployment_data,public_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Public GDP is {}".format(pearsonr(percapita_data,public_gdp)[0]))

print("The Pearson Correlation between Unemployment and Real Estate GDP is {}".format(pearsonr(unemployment_data,real_estate_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Real Estate GDP is {}".format(pearsonr(percapita_data,real_estate_gdp)[0]))

print("The Pearson Correlation between Unemployment and Trade GDP is {}".format(pearsonr(unemployment_data,trade_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Trade GDP is {}".format(pearsonr(percapita_data,trade_gdp)[0]))

print("The Pearson Correlation between Unemployment and Construction GDP is {}".format(pearsonr(unemployment_data,con_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Construction GDP is {}".format(pearsonr(percapita_data,con_gdp)[0]))

print("The Pearson Correlation between Unemployment and Electricity GDP is {}".format(pearsonr(unemployment_data,elec_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Electricity GDP is {}".format(pearsonr(percapita_data,elec_gdp)[0]))

print("The Pearson Correlation between Unemployment and Manufacturing GDP is {}".format(pearsonr(unemployment_data,manufacturing_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Manufacturing GDP is {}".format(pearsonr(percapita_data,manufacturing_gdp)[0]))

print("The Pearson Correlation between Unemployment and Mining GDP is {}".format(pearsonr(unemployment_data,mining_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Mining GDP is {}".format(pearsonr(percapita_data,mining_gdp)[0]))

print("The Pearson Correlation between Unemployment and Agriculture GDP is {}".format(pearsonr(unemployment_data,agriculture_gdp)[0]))
print("The Pearson Correlation between Per Capita Income and Agriculture GDP is {}".format(pearsonr(percapita_data,agriculture_gdp)[0]))