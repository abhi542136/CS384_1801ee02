
import csv
import re
import os
import operator
import shutil
directory = os.getcwd()+"/analytics"


def std(x):
    if x == '01':
        return 'btech'
    elif x == '11':
        return "mtech"
    elif x == '12':
        return "msc"
    elif x == '21':
        return "phd"


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    pass


def course():
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            roll = re.split('[A-Z]+', row[0])
            branch = (re.split('[0-9]+', row[0]))
            try:
                var = str(std(roll[0][-2:len(roll[0])]))
                ri = roll[0][0]+roll[0][1]
                try:

                    os.makedirs(directory + "/course/" + var)
                    f = open(
                        directory + "/course/" + var + "/" + ri + "" +
                        str.lower(branch[1]) + "" + var + ".csv",
                        'a')
                    write = csv.writer(f)
                    write.writerow(
                        ['id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                except:
                    pass
                aa = directory+"/course/"+(var)
                f = open(directory+"/course/"+var+"/"+ri+"" +
                         str.lower(branch[1])+""+var+".csv", 'a')
                write = csv.writer(f)
                write.writerow(row)

            except:
                f = open(directory+"/course/"+"misc.csv", 'a')
                write = csv.writer(f)
                write.writerow(row)


def country():
    c = directory+"/country"
    try:
        os.makedirs(c)
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            country = str.lower(row[2])
            try:
                f = open(directory+"/"+"country/"+country+".csv", 'a')
                writer = csv.writer(f)
                writer.writerow(row)
            except:
                pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
