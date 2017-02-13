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


def failed_counter_count(name):
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
		sql = "select count(*) from login_failed_temp where user_name = '{0}';".format(name)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	result = result.iat[0,0]
	return result
######################################

def failed_counter_adder(name):
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
		sql = "insert into login_failed_temp values('{0}')".format(name)
		cursor.execute(sql)
		connection.commit()
	connection.close()

######################################

def failed_counter_clearer(name):
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
		sql = "delete  from login_failed_temp where user_name = '{0}';".format(name)
		cursor.execute(sql)
		connection.commit()
	connection.close()

######################################

def Navbar_Search():
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
		sql = "select SearchType from Brannas.Navbar_Search"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result
######################################

def get_all_customers():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select * from customers"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

######################################

def get_all_province():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select distinct province from customers"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

######################################

def get_all_city():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select distinct city from customers"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result
######################################

def get_customer_view():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
								 user='Admin',
								 password='Nabu2016!CJKL',
								 db='Brannas',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select province,bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

def merch_orders():
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
								 user='Admin',
								 password='Nabu2016!CJKL',
								 db='Brannas',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select  distinct monthname(OrderPlacedAt) as Month," \
			  "MerchName," \
			  "count(distinct TransactionID) as number_orders," \
			  "sum(Qty) as total_items_ordered," \
			  "cast(sum(Transaction_Cost) as DECIMAL(18,2)) as total_cost," \
			  "'Delivered' as Status" \
			  "from tmp_Merch_Transactions" \
			  "where month(OrderPlacedAt) = month(now())" \
			  "and   OrderDeliverdAt is not null" \
			  "group by monthname(OrderPlacedAt), MerchName" \
			  "order by month(OrderPlacedAt) asc"
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result

######################################

def get_filtered_view(bar,prov,city2):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
								 user='Admin',
								 password='Nabu2016!CJKL',
								 db='Brannas',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		if prov == "All Provinces" and city2 == "All Cities" and bar == "All Customers":
			result = get_customer_view()
			return result
		if prov != "All Provinces" and city2 != "All Cities" and bar == "All Customers":
			sql = "select province, bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where province = '{0}' and city = '{1}'".format(prov,city2)
		if prov != "All Provinces" and city2 == "All Cities" and bar != "All Customers":
			sql = "select province, bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where province = '{0}' and bar_name = '{1}'".format(prov,bar)
		if prov == "All Provinces" and city2 != "All Cities" and bar != "All Customers":
			sql = "select province, bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where city = '{0}' and bar_name = '{1}'".format(city2,bar)

		if prov == "All Provinces" and city2 == "All Cities" and bar != "All Customers":
			sql = "select province, bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where bar_name = '{0}'".format(bar)
		if prov == "All Provinces" and city2 != "All Cities" and bar == "All Customers":	
			sql = "select province,bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where city = '{0}'".format(city2)
		if prov != "All Provinces" and city2 == "All Cities" and bar == "All Customers":	
			sql = "select province,bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where province = '{0}'".format(prov)
		#sql = "select bar_name, city, contact_person, contact_number, contact_email, last_called_at, last_visited_at, updated_at from customers where bar_name = '{0}'".format(bar)
		rows_count = cursor.execute(sql)
		if rows_count > 0:
			result = cursor.fetchall()
			result = pd.DataFrame(result)
		else:
			result = "fuckup"
			return result
	connection.close()
	return result

def get_glasses_ordered(x):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select date,glasses from glasses_ordered where name = '{0}'".format(x)
		cursor.execute(sql)
		temp = cursor.fetchall()
		result = pd.DataFrame(temp)
	connection.close()
	return result


def orders(x):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select * from orders where id = 1".format(x)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result



def get_customers(name):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "select * from customers where bar_name = '{0}'".format(name)
		cursor.execute(sql)
		result = pd.DataFrame(cursor.fetchall())
	connection.close()
	return result


def update_customer(arguments, col_lables):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	print(2)
	print(arguments)
	print(col_lables)
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
										 user='Admin',
										 password='Nabu2016!CJKL',
										 db='Brannas',
										 charset='utf8mb4',
										 cursorclass=pymysql.cursors.DictCursor)

	for i in range(0,len(arguments)):
		print(i)
		print(arguments[0])
		if arguments[i] != "" and arguments[i] != 0 and i != 1 and (i == 4 or i == 13 or i ==16):
			with connection.cursor() as cursor:
				# Read a single recor 
				sql = "UPDATE customers SET {0} = {1} WHERE bar_name = '{2}'".format(col_lables[i], arguments[i], arguments[2])
				print(sql)
				cursor.execute(sql)
				connection.commit()

		elif arguments[i] != "" and arguments[i] != 0:
			with connection.cursor() as cursor:
				# Read a single recor
				sql = "UPDATE customers SET {0} = '{1}' WHERE bar_name = '{2}'".format(col_lables[i], arguments[i], arguments[2])
				print(sql)
				cursor.execute(sql)
				connection.commit()
	connection.close()

def register_user(name,password):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = "insert into login values('{0}', '{1}')".format(name, password)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def add_customer2(province, city, customer, person, number, email, street_number, street_name, date_added, suburb, asking_price, building_name, postal_code):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
	user='Admin',
	password='Nabu2016!CJKL',
	db='Brannas',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
	
	with connection.cursor() as cursor:
		# Read a single recor
		sql = """insert into  customers (province, city, bar_name, contact_person, contact_number, contact_email, 
		street_number, street_name, added_at, suburb, asking_rand_per_unit, building_name, postal_code)
		values('{0}','{1}', '{2}', '{3}', '{4}', '{5}','{6}', '{7}',  '{8}', '{9}', '{10}', '{11}', '{12}')""".format(province, city, customer, person, number, email, street_number, street_name, date_added, suburb, asking_price, building_name, postal_code)
		cursor.execute(sql)
		connection.commit()
	connection.close()

def add_orders2(customer, ordered_at, due_date, unit_price, order_quantity):
	import pymysql
	import pymysql.cursors
	import pandas as pd
	# Connect to the database
	connection = pymysql.connect(host='nabuproject.ch1ktyvsreco.eu-west-1.rds.amazonaws.com',
								user='Admin',
								password='Nabu2016!CJKL',
								db='Brannas',
								charset='utf8mb4',
								cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		# Read a single recor
		sql = """insert into  orders (ordered_at, due_date, unit_price, order_quantity, updated_at, customer) 
		values ('{0}','{1}', {2} , {3}, now(),'{4}')""".format(ordered_at,due_date,unit_price, order_quantity, customer)
		cursor.execute(sql)
		connection.commit()
	connection.close()

		#def LoadStaging(test):
#	import pandas
#	import pymysql
#	import pymysql.cursors
#	
#	connection = pymysql.connect(host='karel-sandbox.conflmsz3tjg.eu-west-1.rds.amazonaws.com',
#	user='dba',
#	password='juLKY8xIefhO',
#	db='sandbox',
#	charset='utf8mb4',
#	cursorclass=pymysql.cursors.DictCursor)
#	
#	cur = connection.cursor()
#	
#	cur.execute("CREATE TABLE sandbox.stg_olx_genders (id INT,name VARCHAR(255),prob FLOAT);")
#	connection.commit()
#	
#	test.to_sql(name='stg_olx_genders', con=connection, if_exists='append',flavor='mysql', index = 0)
#	connection.commit()