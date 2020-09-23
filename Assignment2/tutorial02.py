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
    #mean_value = round(mean_value, 3)
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
        median_value = sm
    else:
        z = n//2
        sm = new_list[z]
        median_value = sm

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
    standard_deviation_value = z
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    variance_value = 0
    temp_list = first_list.copy()
    ans = standard_deviation(temp_list)
    sm = ans*ans
    variance_value = sm
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    rmse_value = 0
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    for i in second_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    n = len(first_list)
    m = len(second_list)
    if(n != m):
        return 0
    if(n == 0 or m == 0):
        return 0
    ans = mse(first_list, second_list)
    rmse_value = ans ** 0.5
    # RMSE Logic
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    mse_value = 0
    n = len(first_list)
    m = len(second_list)
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    for i in second_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

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
    mse_value = ans
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    mae_value = 0
    n = len(first_list)
    m = len(second_list)
    if(n != m):
        return 0
    if(n == 0):
        return 0
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    for i in second_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    ans = 0
    for x, y in zip(first_list, second_list):
        z = abs(x-y)
        ans += z
    mae_value = ans/n

    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    nse_value = 0

    n = len(first_list)
    m = len(second_list)
    if(n != m):
        return 0
    if(n == 0):
        return 0
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    for i in second_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    ans = 0
    sm = 0
    mn = mean(first_list)
    for x, y in zip(first_list, second_list):
        i = abs(x-y)
        z = i ** 2
        ans += z
        k = abs(x-mn)
        k = k ** 2
        sm += k
    t = ans/sm
    nse_value = 1-t
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    pcc_value = 0
    n = len(first_list)
    m = len(second_list)
    if(n != m):
        return 0
    if(n == 0):
        return 0
    for i in first_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    for i in second_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    ans = 0
    mn1 = mean(first_list)
    mn2 = mean(second_list)
    sm1 = 0
    sm2 = 0
    sm3 = 0
    ans1 = 0
    for x, y in zip(first_list, second_list):
        i = x - mn1
        j = y - mn2
        k = i ** 2
        l = j**2
        t = i*j
        sm1 += t
        sm2 += k
        sm3 += l
    sm2 = sm2 ** 0.5
    sm3 = sm3 ** 0.5
    ans1 = sm2*sm3
    ans = sm1/ans1
    pcc_value = ans
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    skewness_value = 0
    temp_list = first_list.copy()
    n = len(temp_list)
    if(n == 0):
        return 0
    for i in temp_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0
    mn = mean(temp_list)
    sd = standard_deviation(temp_list)
    ans = 0
    for i in temp_list:
        x = (i-mn)/sd
        y = x ** 3
        ans += y
    ans /= n
    skewness_value = ans
    # Skewness Logic
    return skewness_value


def sorting(first_list):
    sorted_list = []
    temp_list = first_list.copy()
    new_list = []
    n = len(first_list)
    if(n == 0):
        return new_list
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
    temp_list = first_list.copy()
    n = len(temp_list)
    if(n == 0):
        return 0
    for i in temp_list:
        if(isinstance(i, int) == 0 and isinstance(i, float) == 0):
            return 0

    mn = mean(temp_list)
    sd = standard_deviation(temp_list)
    ans = 0
    for i in temp_list:
        x = (i-mn)/sd
        y = x ** 4
        ans += y
    ans /= n
    kurtosis_value = ans
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
