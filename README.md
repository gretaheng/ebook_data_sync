# ebook_data_sync

Before proceeding, please review the LibGuide detailing the setup process for data synchronization collections between OCLC and Alma at the following link: https://libguides.sdsu.edu/ebook/sync/datareq. This resource offers valuable insights into the rationale behind validating

The Python script "data_sync_validator.py" uses the TXT file exported from MarcEdit as the input. Download the Python script into the folder as the TXT file, open terminal, type 'python data_sync_validator.py <filename of the TXT file>' (e.g. python data_sync_validator.py report.txt). If there's no problematic records in the TXT file, the script will print 'All records are valid!' in the terminal. If not, it will generate a report and a CSV file of all problematic records in the same folder.
