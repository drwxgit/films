import pymysql

#
# Dati di accesso al db
#
HOSTNAME = 'localhost'
USERNAME = 'drwx'
PASSWORD = ''
DATABASE = 'films'

#
# Queries
#
SELECT_ALL = 'SELECT * FROM film'
INSERT_NEW = 'INSERT INTO film (TITOLO, ATTORI, REGISTA, ANNO, GENERE) VALUES (%s, %s, %s, %d, %s)'
#
# Tronca la stringa iStr se la lunghezza e' maggiore di iMax
#
def truncateIfNecessary(iStr, iMax):
    return (iStr[:iMax]+'...') if len(iStr) > iMax else iStr

#
# Esegui la query SELECT_ALL
#
def doSelectAll(iCur):
    rowCount = iCur.execute(SELECT_ALL)
    
    if (rowCount > 0):
        print('%-5s\t%-20s\t%-20s\t%-20s\t%-4s\t%-6s' % ('IDX', 'TITOLO', 'ATTORI', 'REGISTA', 'ANNO', 'GENERE'))

        for r in iCur.fetchall():
            print('%-5s\t%-20s\t%-20s\t%-20s\t%-4s\t%-6s' % (r[0], truncateIfNecessary(r[1],20), truncateIfNecessary(r[2],20), truncateIfNecessary(r[3],20), r[4], r[5]))
    else:
        print('EMPTY')

#
# Esegui la query INSERT_NEW
#
def doInsertNew(iCur):
    # leggi i dati del nuovo film
    titolo = input("Titolo? ")
    attori = input("Attori? ");
    regista = input("Regista? ");
    anno = int(input("Anno? "));
    genere = input("Genere? ");
bla bla
    iCur.execute(INSERT_NEW, (titolo,attori,regista,anno,genere));
    for r in iCur.fetchall():
        print(r)

#
# MAIN
#
def main():
	# initialize connection..
        conn = pymysql.connect(host=HOSTNAME, port=3306, user=USERNAME, passwd=PASSWORD, db=DATABASE)
        cur = conn.cursor()

        doSelectAll(cur)
        doInsertNew(cur)

        cur.close()
        conn.close()

if __name__ == "__main__":
	main()
