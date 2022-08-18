def new_func():
    pip install OptionParser
    return __name__

__name__ = new_func()
pip install BeautifulSoup 
from optparse import OptionParser
from bs4 import BeautifulSoup as BS
import os


def get_info(file):

    with open(file, encoding='utf8') as fp:
        soup = BS(fp, 'html.parser')
        
    div = soup.find('div', {'class' : 'mvf-wrapper has-transit no-image'})
    print('\n=== Linha: ' + div.h1.text + ' ===\n') # nome da linha
    
    i = 1
    for stop in soup.find_all('li', {'class' : 'stop-container'}):
        print(str(i) + '-' + stop.h3.text) #nome da parada
        print(stop.span.text) # endereço da parada
        print()
        i += 1
    
    return


# main function
def main():

    # parse command line args
    parser = OptionParser()
    parser.add_option("-d", "--datadir", type="string", dest="datadir", default="data", help="directory to store data")
    #parser.add_option("-u", "--user", type="string", dest="username", help="sigaa username")
    #parser.add_option("-p", "--pass", type="string", dest="password", help="sigaa password")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="print debug messages")
    (opt, args) = parser.parse_args()

    dirpath = os.path.join(os.getcwd(), opt.datadir)
    if not os.path.exists(dirpath):
        print("Creating data dir.")
        os.mkdir(dirpath)

    for file in os.listdir('.'):
        #print (file)
        if file.startswith('transporte_público-line-'):
            if opt.verbose: print(file)
            get_info(file)
            
    return


if __name__ == "__main__":
    main()
