# All decimal 3 places

# Function to compute mean
def mean(first_list):
    n = len(first_list)
    if(n == 0):
        return 0
    ans = 0
    for i in first_list:
        if(isinstance(i, int) or isinstance(i, float)):
            ans += i
        else:
            return 0
        #ans += i
    mean_value = ans/n
    mean_value = round(mean_value, 3)
    # mean Logic
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    median_value = 0
    # median Logic
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    standard_deviation_value = 0
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    variance_value = 0
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    rmse_value = 0
    # RMSE Logic
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    mse_value = 0
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    mae_value = 0
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    nse_value = 0
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    pcc_value = 0
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    skewness_value = []
    # Skewness Logic
    return skewness_value


def sorting(first_list):
    sorted_list = []
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    kurtosis_value = 0
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value = 0
    # sum Logic
    return summation_value
