def connect_login(name,password):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select sum(valid) as valid from (select case when user_name = '{0}' and password = '{1}' then 1 else 0 end as valid from login)aa".format(name, password)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	result = result.iat[0,0]
	return result


def enteremail(email):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Chiron',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into Users_1 values(NULL,NULL,NULL,'{0}',NOW(),NULL,NULL)".format(email)
		cursor.execute(sql)
		connection.commit()
	connection.close()
######################################

def createusernameandpassword(email,username,passwords):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "UPDATE Chiron.Users_1 SET username='{1}', password='{2}' WHERE email='{0}'".format(email,username,passwords)
		cursor.execute(sql)
		connection.commit()
	connection.close()


def complete_profiles(email,location,job):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "UPDATE Chiron.Users_1 SET location='{1}', job='{2}' WHERE email='{0}'".format(email,location,job)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def retrieve_email(username):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "SELECT email FROM Chiron.Users_1 where username = '{0}'".format(username)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	result = result.iat[0,0]
	return result

def view_customers():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Chiron',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read all employee records
		sql = "select * from temp_employees"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
		print(result)
	connection.close()
	return result
