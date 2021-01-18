from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
from utils.data import readcsv, normalize, get_stock, get_total_gdp
from correlations import get_corr_gdp_with_stock


def get_quarterly_data(data_all):
    return {
        '1': [data for index, data in enumerate(data_all) if index % 4 == 0],
        '2': [data for index, data in enumerate(data_all) if index % 4 == 1],
        '3': [data for index, data in enumerate(data_all) if index % 4 == 2],
        '4': [data for index, data in enumerate(data_all) if index % 4 == 3],
    }


def plot_quarterly_data(quarterly_data, label):
    years_wo_2020 = [i for i in range(2011, 2020)]
    years_w_2020 = [i for i in range(2011, 2021)]
    fig, ax = plt.subplots()
    ax.plot(years_w_2020, quarterly_data['1'], 'C1o-', label='Quarter 1')
    ax.plot(years_w_2020, quarterly_data['2'], 'C2o-', label='Quarter 2')
    ax.plot(years_wo_2020, quarterly_data['3'], 'C3o-', label='Quarter 3')
    ax.plot(years_wo_2020, quarterly_data['4'], 'C0o-', label='Quarter 4')
    plt.ylabel(label)
    plt.xlabel('Year')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_all_data(gdp1, gdp2, nifty, sensex):
    fig, ax = plt.subplots()
    years = get_x_axis_years()
    ax.plot(years, nifty, 'C1o-', label='Nifty')
    ax.plot(years, sensex, 'C2o-', label='Sensex')
    ax.plot(years, gdp1, 'C0o-', label='Total GDP at Constant Price')
    ax.plot(years, gdp2, 'C4o-', label='Total GDP at Current Price')
    plt.xlabel('Year')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_all_sectors_with_stock(gdp_data, stock_data, xlabel, ylabel):
    fig, ax = plt.subplots()
    years = get_x_axis_years()

    # GDP Sectors
    gdp_sectors = list(gdp_data.columns.values[1:9])

    for i, sector in enumerate(gdp_sectors):
        sector_data = gdp_data[sector]
        ax.plot(stock_data, sector_data, 'C' + str(i) + 'o--', label=sector)

    plt.xlabel(xlabel + ' Prices')
    plt.ylabel('GDP at ' + ylabel+' Price')
    plt.grid()
    plt.legend()
    plt.show()


def plot_vs(data1, data2, label1, label2):
    fig, ax = plt.subplots()
    ax.scatter(data1, data2, marker='o')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.grid(True)
    plt.show()


def plot_vs_gdp(gdp_constant, gdp_current, data,  label):
    fig, ax = plt.subplots()
    ax.plot(data, gdp_constant, marker='o',
            color='C1', label="GDP at Constant Price")
    ax.plot(data, gdp_current, marker='o',
            color='C2', label="GDP at Current Price")
    plt.xlabel(label)
    plt.ylabel('GDP')
    plt.title('GDP vs ' + label + ' with year quarterly')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_bar_graph(xdata, ydata1, ydata2, xlabel, ylabel1, ylabel2):
    fig, ax = plt.subplots()
    barWidth = 0.25
    br1 = np.arange(len(xdata))
    br2 = [x + barWidth for x in br1]
    ax.bar(br1, ydata1, color='C1', width=barWidth)
    ax.bar(br2, ydata2, color='C2', width=barWidth)
    ax.legend(labels=[ylabel1, ylabel2])
    plt.title('Correlation between GDP at Current Price and Nifty Prices')
    plt.xlabel(xlabel)
    plt.xticks([r + barWidth for r in range(len(ydata1))], xdata)
    plt.show()


def get_x_axis_years():
    # X-axis Years
    years = []
    for year in range(2011, 2020):
        for quarter in range(1, 5):
            years.append(str(year) + '\nQ' + str(quarter))
    years.append(str(2020) + '\nQ' + str(1))
    years.append(str(2020) + '\nQ' + str(2))
    return years


# Read files
gdp_data_constant = readcsv('data/gdp_constant.csv')
gdp_data_current = readcsv('data/gdp_current.csv')
sensex_data = readcsv('data/sensex.csv')
nifty_data = readcsv('data/nifty.csv')
gdp_annual_data_constant = readcsv('data/gdp_constant_annual.csv')
gdp_annual_data_current = readcsv('data/gdp_current_annual.csv')
sensex_annual_data = readcsv('data/sensex_annual.csv')
nifty_annual_data = readcsv('data/nifty_annual.csv')

gdp_normalized_constant = normalize(gdp_data_constant)
gdp_normalized_current = normalize(gdp_data_current)
sensex_normalized = normalize(sensex_data)
nifty_normalized = normalize(nifty_data)

gdp_constant_plot_data = get_total_gdp(gdp_data_constant)
gdp_current_plot_data = get_total_gdp(gdp_data_current)
sensex_plot_data = get_stock(sensex_data)
nifty_plot_data = get_stock(nifty_data)

gdp_constant_plot_normalized_data = get_total_gdp(gdp_normalized_constant)
gdp_current_plot_normalized_data = get_total_gdp(gdp_normalized_current)
sensex_plot_normalized_data = get_stock(sensex_normalized)
nifty_plot_normalized_data = get_stock(nifty_normalized)

nifty_data_quarterly = get_quarterly_data(nifty_plot_data)
sensex_data_quarterly = get_quarterly_data(sensex_plot_data)
gdp_constant_data_quarterly = get_quarterly_data(gdp_constant_plot_data)
gdp_current_data_quarterly = get_quarterly_data(gdp_current_plot_data)

# GDP Sectors
gdp_sectors = list(gdp_data_constant.columns.values[1:9])
gdp_sectors_wrapped = [label.replace(',', ',\n') for label in gdp_sectors]
gdp_sectors_wrapped = [label.replace('&', ' &\n')
                       for label in gdp_sectors_wrapped]
# Plot Quarterly data
# plot_quarterly_data(gdp_constant_data_quarterly, "GDP at Constant Price")
# plot_quarterly_data(gdp_current_data_quarterly, "GDP at Current Price")

# Plot GDP versus Stocks
# plot_vs(nifty_plot_data, gdp_constant_plot_data,
#         'Nifty Prices', 'GDP at Constant Price')
# plot_vs(nifty_plot_data, gdp_current_plot_data,
#         'Nifty Prices', 'GDP at Current Price')
# plot_vs(sensex_plot_data, gdp_constant_plot_data,
#         'Sensex Prices', 'GDP at Constant Price')
# plot_vs(sensex_plot_data, gdp_current_plot_data,
#         'Sensex Prices', 'GDP at Current Price')

# Plot both GDP versus Stocks
# plot_vs_gdp(gdp_constant_plot_data, gdp_current_plot_data, sensex_plot_data,
#             'Sensex Prices')
# plot_vs_gdp(gdp_constant_plot_data, gdp_current_plot_data, nifty_plot_data,
#             'Nifty Prices')

# Plot GDP and stock for all years
# plot_all_data(gdp_constant_plot_normalized_data, gdp_current_plot_normalized_data,
#               nifty_plot_normalized_data, sensex_plot_normalized_data)


# Plot correlations

sensex_corr_gdp_constant = get_corr_gdp_with_stock(
    gdp_data_constant, sensex_data)

sensex_corr_gdp_current = get_corr_gdp_with_stock(
    gdp_data_current, sensex_data)

nifty_corr_gdp_constant = get_corr_gdp_with_stock(
    gdp_data_constant, nifty_data)

nifty_corr_gdp_current = get_corr_gdp_with_stock(
    gdp_data_current, nifty_data)

# plot_bar_graph(
#     gdp_sectors_wrapped, sensex_corr_gdp_constant['pearson'], sensex_corr_gdp_constant['spearman'], "GDP Sectors", "Pearson Correlation", "Spearman Correlation")


# plot_bar_graph(
#     gdp_sectors_wrapped, sensex_corr_gdp_current['pearson'], sensex_corr_gdp_current['spearman'], "GDP Sectors", "Pearson Correlation", "Spearman Correlation")

# plot_bar_graph(
#     gdp_sectors_wrapped, nifty_corr_gdp_constant['pearson'], nifty_corr_gdp_constant['spearman'], "GDP Sectors", "Pearson Correlation", "Spearman Correlation")


# plot_bar_graph(
#     gdp_sectors_wrapped, nifty_corr_gdp_current['pearson'], nifty_corr_gdp_current['spearman'], "GDP Sectors", "Pearson Correlation", "Spearman Correlation")


# plot_all_sectors_with_stock(
#     gdp_data_constant, sensex_plot_data,  "Sensex", "Constant")
# plot_all_sectors_with_stock(
#     gdp_data_current, sensex_plot_data,  "Sensex", "Current")
# plot_all_sectors_with_stock(
#     gdp_data_constant, nifty_plot_data,  "Nifty", "Constant")
# plot_all_sectors_with_stock(
#     gdp_data_current, nifty_plot_data,  "Nifty", "Current")


def plot_separate(gdp_constant_data, gdp_current_data, gdp_sectors, stock_data, pearson_data_constant, pearson_data_current, label):
    f3, a = plt.subplots(2, 4)

    i = 0
    j = 0

    for sector in gdp_sectors:
        sector_constant_data = gdp_constant_data[sector][:-1]
        sector_current_data = gdp_current_data[sector][:-1]
        regression_func_constant = np.poly1d(
            np.polyfit(stock_data, sector_constant_data, 1))
        regression_func_current = np.poly1d(
            np.polyfit(stock_data, sector_current_data, 1))
        a[i][j].plot(stock_data, sector_constant_data, 'C1o-',
                     label=sector[:20] + '... at Constant Price')
        a[i][j].plot(stock_data, sector_current_data, 'C2o-',
                     label=sector[:20] + '... at Current Price')
        a[i][j].set_xlabel(label+" Data($)")
        a[i][j].set_ylabel("GDP(Cr)")
        a[i][j].set_title(
            "Spearman Coeff. at \nConstant/Current Price\n {:.3f}/{:.3f}".format(pearson_data_constant[i*4+j], pearson_data_current[i*4+j]))
        a[i][j].plot(stock_data, regression_func_constant(stock_data), 'C3-')
        a[i][j].plot(stock_data, regression_func_current(stock_data), 'C4-')
        a[i][j].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
        a[i][j].ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        a[i][j].grid()
        a[i][j].legend()

        j += 1
        if j == 4:
            i += 1
            j = 0
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95,
                        top=0.9, wspace=0.4, hspace=0.4)
    plt.show()


# plot_separate(gdp_annual_data_constant, gdp_annual_data_current, gdp_sectors,
#               sensex_annual_data[sensex_annual_data.columns[1]][:-1], sensex_corr_gdp_constant['pearson'])

# plot_separate(gdp_annual_data_constant, gdp_annual_data_current, gdp_sectors,
#               sensex_annual_data[sensex_annual_data.columns[1]][:-1],
#               sensex_corr_gdp_constant['pearson'], sensex_corr_gdp_current['pearson'],
#               label='Sensex')

# plot_separate(gdp_annual_data_constant, gdp_annual_data_current, gdp_sectors,
#               nifty_annual_data[nifty_annual_data.columns[1]][:-1],
#               nifty_corr_gdp_constant['pearson'], nifty_corr_gdp_current['pearson'],
#               label='Nifty')

plot_separate(gdp_annual_data_constant, gdp_annual_data_current, gdp_sectors,
              sensex_annual_data[sensex_annual_data.columns[1]][:-1],
              sensex_corr_gdp_constant['spearman'], sensex_corr_gdp_current['spearman'],
              label='Sensex')


plot_separate(gdp_annual_data_constant, gdp_annual_data_current, gdp_sectors,
              nifty_annual_data[nifty_annual_data.columns[1]][:-1],
              nifty_corr_gdp_constant['spearman'], nifty_corr_gdp_current['spearman'],
              label='Nifty')
