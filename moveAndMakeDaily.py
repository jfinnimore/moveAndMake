# moveAndMakeDaily by Jason Finnimore
# used to move files to a folder based on the file date contained in the filename

# import the libraries
import glob, os, re

# get file name for target folder
source = glob.glob("V:\\Financial_Reports\\subfolder\\costdetail*.txt")

# get file name for subfolder
source = glob.glob("V:\\Financial_Reports\\subfolder\\costdetail*.txt")

# set destination folder
dest = "V:\\Data_Analytics\\Project\\Daily_Files\\MMYY - Month"

# get folder name from filename
for filename in source:
  day = filename[-6:-4]
  month = filename[-8:-6]
  newFolderName = month+day
  os.chdir(dest)
  os.mkdir(newFolderName)
  
for costDetailFile in costDetail:
  costDetailSrc = costDetailFile
  costDetailDest = re.sub('_\d{8}','',costDetailFile)
  os.rename(costDetailSrc, costDetailDest)
  CDfilename = os.path.basename(costDetailDest)
  newDailyFolder = os.path.join(dest, newFolderName)
  os.replace(costDetailDest, os.path.join(newDailyFolder, CDfilename))
