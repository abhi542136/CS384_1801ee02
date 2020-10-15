
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
    try:
        os.makedirs(directory+"/email_domain")
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            try:
                x = (row[3].split('@'))

                f = open(directory+"/email_domain/" +
                         (x[1].split('.')[0])+".csv", 'a')

                writer = csv.writer(f)
                writer.writerow(row)
            except:
                pass


def gender():
    try:
        os.makedirs(directory+'/gender')
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            f = open(directory+'/gender/'+row[-4]+".csv", 'a')
            writer = csv.writer(f)
            writer.writerow(row)


def dob():
    filename = directory+'/dob'
    try:
        os.makedirs(filename)
    except:
        pass
    f1 = open(filename+'/bday_1995_1999.csv', 'a')
    f2 = open(filename+'/bday_2000_2004.csv', 'a')
    f3 = open(filename + '/bday_2005_2009.csv', 'a')
    f4 = open(filename + '/bday_2010_2014.csv', 'a')
    f5 = open(filename + '/bday_2015_21995020.csv', 'a')
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x = row[-3]
            y = x.split('-')[-1]
            if y >= '2015':
                reader = csv.writer(f1)
                reader.writerow(row)
            elif y >= '2010':
                reader = csv.writer(f2)
                reader.writerow(row)
            elif y >= '2005':
                reader = csv.writer(f3)
                reader.writerow(row)
            elif y >= '2000':
                reader = csv.writer(f4)
                reader.writerow(row)
            elif y >= '1995':
                reader = csv.writer(f5)
                reader.writerow(row)


def state():
    try:
        os.makedirs(directory + '/state')
    except:
        pass
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            states = (row[-1])
            t = directory+'/state/'+states+".csv"
            f = open(t, 'a')
            writer = csv.writer(f)
            writer.writerow(row)


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
