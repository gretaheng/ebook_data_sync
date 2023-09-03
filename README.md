# ebook_data_sync

Before proceeding, please review the LibGuide detailing the setup process for data synchronization collections between OCLC and Alma at the following link: https://libguides.sdsu.edu/ebook/sync/datareq. This resource offers valuable insights into the rationale behind validating

The Python script "data_sync_validator.py" uses the TXT file exported from MarcEdit as the input. Download the Python script into the folder as the TXT file, open terminal, type 'python data_sync_validator.py <filename of the TXT file>' (e.g. python data_sync_validator.py report.txt). If there's no problematic records in the TXT file, the script will print 'All records are valid!' in the terminal. If not, it will generate a report and a CSV file of all problematic records in the same folder.

The "From MARC/Get 035a" folder contains two Python scripts. Both of these scripts serve the purpose of processing a MARC file and producing a text file containing all the 035a OCLC numbers found within the MARC file. The script named "For_ Alma_OCLC_Number copy.py" generates an output file that includes an additional header. This header is particularly useful when creating an itemized set in Alma. On the other hand, the script "For_ Connexion_OCLC_Number.py" generates an output file that only contains the 035a OCLC numbers, without any additional headers or information. It can be used for batch holding processing in OCLC Connexion.






