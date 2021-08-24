# import txt
import pandas as pd
import re
import sys

# check ldr
def check_header_re(s):
    # 17 elv code added 'IKM'
    matched = re. match(r'^[0-9]{5}[acdnp][acdefgijkmoprt][abcdims][ a][ a][2][2][0-9]{5}[ 12345678uzIKM][ acinu][ abc][4][5][0][0]$', s)
    is_match = bool(matched)
    return is_match

def go(fn):
    dt = pd.read_csv(fn, sep='\t', encoding='utf-8',dtype=str)
    dt = dt.astype(str)
    rtn = []
    report = []
    for index, row in dt.iterrows():
        # check header
        if not check_header_re(row['000']):
            rtn.append(index)
            re = 'Number '+ index + ' record: header is wrong.'
            report.append()
            continue
        # 008 15-17 not blank
        if row['008'][15:17] == '   ':
            rtn.append(index)
            re = 'Number '+ index + ' record: 008 15-17 is wrong.'
            report.append()
            continue
        # 008 35-37 lowercase
        if not row['008'][35:37].islower():
            rtn.append(index)
            re = 'Number '+ index + ' record: 008 35-37 is wrong.'
            report.append()
            continue
        # 035 oclc:
        if not row['035$a'].startswith('(OCoLC)'):
            rtn.append(index)
            re = 'Number '+ index + ' record: 035$a is wrong.'
            report.append()
            continue
        # 066+880
        if row['066'] != 'nan' and row['880'] == 'nan':
            rtn.append(index)
            re = 'Number '+ index + ' record: 066/880 is wrong.'
            report.append()
            continue
        if row['066'] == 'nan' and row['880'] != 'nan':
            rtn.append(index)
            re = 'Number '+ index + ' record: 066/880 is wrong.'
            report.append()
            continue
        # 245
        if row['245'] == 'nan':
            rtn.append(index)
            re = 'Number '+ index + ' record: no 245.'
            report.append()
            continue
    if len(rtn) == 0:
        print('All records are valid!')
    else:
        dtrtn = dt.iloc[rtn]
        dtrtn.to_csv('problematic_records.csv')
        textfile = open("validation_report.txt", "w")
        for element in report:
            textfile.write(element + "\n")
        textfile.close()

if __name__ == "__main__":
    go(sys.argv[1])