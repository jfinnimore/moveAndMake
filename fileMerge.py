# Re-order the columns of one file and combine it with another

import pandas as pd

# read the daily csv into a dataframe
patientVolume = pd.read_csv('V:\\Data\\Tableau\\DailyEmailedFile.csv')

# read daily excel file into a dataframe
oncology = pd.read_excel('V:\\Data\\Tableau\\oncologyFiles\\pastAppts.xlsx')

# delete the patient name column from the patientVOlume dataframe
patientVOlume.drop(['Person Name- Full'], axis=1)

# rename the oncology columns
oncology.columns = ['MRN-Community','AppointmentStatus','Appointment Start Date & Time','Appointment Type-Short','Resource Short Description','Scheduling Location']

# insert columns into oncology dataframe
oncology['Scheduling Appointment ID'] = ""
oncology['Scheduling Event Display'] = ""

# re-order the columns of both dataframes
patientVolume = patientVolume[['MRN-Community','AppointmentStatus','Appointment Start Date & Time','Appointment Type-Short','Resource Short Description','Scheduling Location','Scheduling Appointment ID','Scheduling Event Display']]
oncology = oncology[['MRN-Community','AppointmentStatus','Appointment Start Date & Time','Appointment Type-Short','Resource Short Description','Scheduling Location','Scheduling Appointment ID','Scheduling Event Display']]

# union the files with the concatenate function
bothFiles = [patientVolume,oncology]
unionDataFrame = pd.concat(bothFiles, sort=False)

# export the file
unionDataFrame.to_csv('V:\\Data\\Tableau\\AppointmentVolumeFile.csv, index=False')
