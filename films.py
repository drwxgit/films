import pymysql

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'mysql'
DATABASE = 'films'

'''QUERY'''
SELECT_ALL = 'SELECT * FROM film'


def doSelectAll(cur):
    rowCount = cur.execute(SELECT_ALL)
    
    if (rowCount > 0):
        print('%-5s\t%-20s\t%-20s\t%-20s\t%-4s\t%-6s' % ('IDX', 'TITOLO', 'ATTORI', 'REGISTA', 'ANNO', 'GENERE'))
        for r in cur.fetchall():
            print('%-5s\t%-20s\t%-20s\t%-20s\t%-4s\t%-6s' % (r[0],(r[1][:20]+'...') if len(r[1]) > 20 else r[1],r[2],r[3],r[4],r[5]))
    else:
        print('EMPTY')

def main():
	# initialize connection..
        conn = pymysql.connect(host=HOSTNAME, port=3306, user=USERNAME, passwd=PASSWORD, db=DATABASE)
        cur = conn.cursor()

        doSelectAll(cur)

        cur.close()
        conn.close()

if __name__ == "__main__":
	main()
