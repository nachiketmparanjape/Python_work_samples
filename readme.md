## ETL process in completed in the following steps -

1. CSV writer scripts convert laboratory output files into separate text and json files which get stored in respective subfolders under IV_temp folder

2. At the same time, datafiles inside the live data folder are moved to archive (IV_archive) and are stored in subfolders wrt experiment date

3. Database writer scripts parse the temp files, dump the data into the database and then clear the temp folder
