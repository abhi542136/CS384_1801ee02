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
    n = len(first_list)
    if(n == 0):
        return 0
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    temp_list = first_list.copy()
    #new_list = first_list

    new_list = sorting(temp_list)

    if(n % 2 == 0):
        y = n//2
        sm = (new_list[y]+new_list[y-1])/2
        median_value = round(sm, 3)
    else:
        z = n//2
        sm = new_list[z]
        median_value = round(sm, 3)

    # median Logic
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    standard_deviation_value = 0
    temp_list = first_list.copy()

    for i in temp_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    ans = 0
    for x in temp_list:
        ans += x
    n = len(temp_list)
    if(n == 0):
        return 0
    mn = ans/n
    sm = 0
    for x in temp_list:
        y = abs(x-mn)
        t = y*y
        sm += t
    sm /= n
    z = sm ** 0.5
    standard_deviation_value = round(z, 3)
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
    n = len(first_list)
    m = len(second_list)

    if(n == 0 or m == 0):
        return 0
    if(n != m):
        return 0
    for x, y in zip(first_list, second_list):
        if((isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float))):
            t = abs(x-y)
            l = t*t
            mse_value += l
            #print(x, y)
        else:
            return 0
    # mse Logic
    ans = mse_value/n
    mse_value = round(ans, 3)
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
    skewness_value = 0
    # Skewness Logic
    return skewness_value


def sorting(first_list):
    sorted_list = []
    temp_list = first_list.copy()
    new_list = []
    n = len(first_list)
    i = 0
    while i < n:
        min = temp_list[0]
        if(isinstance(min, int) == 0 and isinstance(min, float) == 0):
            return new_list
        for x in temp_list:
            if x < min:
                min = x
        sorted_list.append(min)
        i += 1
        temp_list.remove(min)
    # Sorting Logic
    temp_list = first_list
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    kurtosis_value = 0
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    n = len(first_list)
    if(n == 0):
        return 0
    summation_value = 0
    for i in first_list:
        if(isinstance(i, int) or isinstance(i, float)):
            summation_value += i
        else:
            return 0
    # sum Logic
    summation_value = round(summation_value, 3)
    return summation_value
