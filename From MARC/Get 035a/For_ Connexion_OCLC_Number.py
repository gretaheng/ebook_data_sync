from pymarc import MARCReader
import sys

def get_o35a_connexion(fn):
    list035 = []
    with open(fn, 'rb') as fh:
        reader = MARCReader(fh)
        for record in reader:
            try:
                oclc = record['035']['a']
                num = oclc.lstrip('(OCoLC)')
                list035.append(int(num))
            except:
                try:
                    print(record['001'])
                except:
                    pass
    with open('connexion_oclc035a.txt', 'w') as f:
        print("Generating the list of OCLC number.")
        for item in list035:
            f.write("%s\n" % item)
        print("Done! See connexion_oclc035a.txt.")
    return

if __name__ == "__main__":
    get_o35a_connexion(sys.argv[1])