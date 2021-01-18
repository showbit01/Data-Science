import csv
from scipy.stats import pearsonr, spearmanr
from utils.data import readcsv, normalize, get_stock


def get_correlations(data1, data2):
    pearson_corr, _ = pearsonr(data1, data2)
    spearman_corr, _ = spearmanr(data1, data2)
    return {
        'pearson': pearson_corr,
        'spearman': spearman_corr
    }


def print_correlations(corrs):
    print(f"Pearsons Correlation: {corrs['pearson']}")
    print(f"Spearman Correlation: {corrs['spearman']}")


def get_corr_gdp_with_stock(gdp_data, stock_data):
    corrs = {
        'pearson': [],
        'spearman': []
    }

    # GDP Sectors
    gdp_sectors = list(gdp_data.columns.values[1:9])

    for sector in gdp_sectors:
        cur_corrs = get_correlations(get_stock(stock_data), gdp_data[sector])
        for corr, val in cur_corrs.items():
            corrs[corr].append(val)
    return corrs


def create_corr_csv_file(filename, corrs, gdp_sectors):
    with open(filename+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Correlations'] + gdp_sectors)
        for corr, val in corrs.items():
            writer.writerow([corr] + val)


if __name__ == "__main__":
    # Read files
    gdp_data_constant = readcsv('data/gdp_constant.csv')
    gdp_data_current = readcsv('data/gdp_current.csv')
    sensex_data = readcsv('data/sensex.csv')
    nifty_data = readcsv('data/nifty.csv')

    # GDP Sectors
    gdp_sectors = list(gdp_data_constant.columns.values[1:9])

    # Correlation of stock with GDP at Constant price
    sensex_corrs_gdp_constant = get_corr_gdp_with_stock(
        gdp_data_constant, sensex_data)
    nifty_corrs_gdp_constant = get_corr_gdp_with_stock(
        gdp_data_constant, nifty_data)

    # Correlation of stock with GDP at Current price
    sensex_corrs_gdp_current = get_corr_gdp_with_stock(
        gdp_data_current, sensex_data)
    nifty_corrs_gdp_current = get_corr_gdp_with_stock(
        gdp_data_current, nifty_data)

    print(sensex_corrs_gdp_constant)
    print(sensex_corrs_gdp_current)

    create_corr_csv_file("output/Sensex_Corrs_GDP_Constant",
                         sensex_corrs_gdp_constant, gdp_sectors)
    create_corr_csv_file("output/Sensex_Corrs_GDP_Current",
                         sensex_corrs_gdp_current, gdp_sectors)
    create_corr_csv_file("output/Nifty_Corrs_GDP_Constant",
                         nifty_corrs_gdp_constant, gdp_sectors)
    create_corr_csv_file("output/Nifty_Corrs_GDP_Current",
                         nifty_corrs_gdp_current, gdp_sectors)
