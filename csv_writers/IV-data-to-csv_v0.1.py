""" Script to parse IV data file into multiple csvs """
import pandas as pd
#import datetime
import os
import numpy as np




def subfolder_all_file_list(link='C:/Users/labuser/Documents/NEA_Scripts/Final_Scripts/IV_data'):
    """This function will extract all the filenames from all the subfolders
    
    in the working directory and returns a list """
    flist = []
    for path, subdirs, files in os.walk(link):
        for filename in files:
            f = os.path.join(path,filename)
            flist.append(f[-23:])
    flist = [i for i in flist if '.lvm' in i]
    return flist

def IVdatareader(filename):
    """Data Import and Cleaning
    
    Returns a list of 8 dataframes for further processing"""
    df1 = pd.read_csv(filename,sep="\t",skiprows = 22, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df2 = pd.read_csv(filename,sep='\t',skiprows = 108, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df3 = pd.read_csv(filename,sep='\t',skiprows = 194, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df4 = pd.read_csv(filename,sep='\t',skiprows = 280, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df5 = pd.read_csv(filename,sep='\t',skiprows = 366, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df6 = pd.read_csv(filename,sep='\t',skiprows = 452, usecols = [1,2], names = ['Voltage','Current',],nrows=76)
    df7 = pd.read_csv(filename,sep='\t',skiprows = 538, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df8 = pd.read_csv(filename,sep='\t',skiprows = 624, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df9 = pd.read_csv(filename,sep="\t",skiprows = 710, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df10 = pd.read_csv(filename,sep='\t',skiprows = 796, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df11 = pd.read_csv(filename,sep='\t',skiprows = 882, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df12 = pd.read_csv(filename,sep='\t',skiprows = 968, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df13 = pd.read_csv(filename,sep='\t',skiprows = 1054, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df14 = pd.read_csv(filename,sep='\t',skiprows = 1140, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df15 = pd.read_csv(filename,sep='\t',skiprows = 1226, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df16 = pd.read_csv(filename,sep='\t',skiprows = 1312, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df17 = pd.read_csv(filename,sep="\t",skiprows = 1398, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df18 = pd.read_csv(filename,sep='\t',skiprows = 1484, usecols=[1,2], names = ['Voltage','Current'],nrows=76)
    df19 = pd.read_csv(filename,sep='\t',skiprows = 1570, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df20 = pd.read_csv(filename,sep='\t',skiprows = 1656, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df21 = pd.read_csv(filename,sep='\t',skiprows = 1742, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    df22 = pd.read_csv(filename,sep='\t',skiprows = 1828, usecols = [1,2], names = ['Voltage','Current'],nrows=76)
    
    return [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22]


def dateparser(filename):
    """ Extracts the date on which the data was recorded from the file. Returns a single date value. """
    
    #Open the file with read only mode
    f= open(filename,"r")
    
    #Read the file line by line
    for i in range(10):
        dat = f.readline()
    
    dat = dat[5:-1]
    #dat = datetime.strptime(dat, '%Y/%m/%d').date()
        
    return dat

def commentparser(filename):
    """ Extracts the sensorID and comment from the data """
    #Open the file with read only mode
    df1 = pd.read_csv(filename,sep="\t",skiprows = 22, usecols=[1,2,3], names = ['Voltage','Current','ChipID'],nrows=76)
    
    try:
        l = str(df1['ChipID'][0]).split(';')
        
        chipID = l[0]
        try:
            comment = l[1]
        except IndexError:
            comment = ''
    except IndexError:
        chipID = 'Unknown'
        comment = ''

    
    return chipID, comment

def write_string_to_text(filename,stringlist):
    """ Takes in a list of strings and writes them to a text file """
    
    file = open(filename[:-4]+'.txt','a')
    for string in stringlist:
        file.write(string+'\n')
    file.close()
    
def write_df_to_text(fil,dflist):
    """ Takes in a list of dataframes and writes them to a text file """
    i = 1
   
    for df in dflist:
        df.to_csv(fil+'_channel_'+str(i), sep=',', encoding='utf-8')
        i += 1
        
def write_df_to_json(fil,dflist):
    """ Takes in a list of dataframes and writes them to a json file """
    i = 1
    
    for df in dflist:
        df.to_json(fil+'_channel_'+str(i), orient='columns')
        i += 1
        
def move_file(oldpath, newpath, filename):
    """ Moves file to the archive folder """
    
    os.rename(oldpath+filename, newpath+filename)
    
        

def main():
    
    #list files
    filelist = subfolder_all_file_list()
    #PATHS
    temp = 'C:/Users/labuser/Documents/NEA_Scripts/Final_Scripts/IV_Temp/'
    datapath = 'C:/Users/labuser/Documents/NEA_Scripts/Final_Scripts/IV_data/'
    archivepath = 'C:/Users/labuser/Documents/NEA_Scripts/Final_Scripts/IV_Archive/'
    
    
    
    for fil in filelist:
        
        os.chdir(datapath)
        
        #extract date, chipID, comment
        date = dateparser(fil)
        chipID, comment = commentparser(fil)
        strings = [chipID, date, comment]
        
        #Extract the IV-data
        dflist = IVdatareader(fil)
        
        #Organize temp folder
        
        temppath = temp+fil+'/'
        if not os.path.exists(temppath):
            os.makedirs(temppath)
        
        os.chdir(temppath)
        
        #Write date, chipID, comment to text file
        write_string_to_text(fil,strings)
        
        #Write the I-V dataframes to json
        write_df_to_json(fil,dflist)
        
        #Move files to archive
        newpath = archivepath+date+'/'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            
        move_file(datapath,newpath,fil)
        
main()
