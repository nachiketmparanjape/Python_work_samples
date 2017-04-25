## ETL process in completed in the following steps -

1. CSV writer scripts convert laboratory output files into separate text and json files which get stored in respective subfolders under IV_temp folder

2. At the same time, datafiles inside the live data folder are moved to archive (IV_archive) and are stored in subfolders wrt experiment date

3. Database writer scripts parse the temp files, dump the data into the database and then clear the temp folder

### To test the scripts and the whole ETL process -

1. Install MySQL on your computer and create a database called 'new_schema'

2. Edit the scripts to enter the connetion information in 'create_connetion' funtion

3. Run the script to create table, and then test rest of the scripts
