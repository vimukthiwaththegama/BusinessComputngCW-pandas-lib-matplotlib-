import sqlite3

connect = sqlite3.connect("db")
cursor = connect.cursor()
# create table ,locations
cursor.execute('''       
CREATE TABLE IF NOT EXISTS locations (
location_id INT(3), 
street_address VARCHAR(50) unique not null, 
postal_code VARCHAR(10) not null, 
city VARCHAR(50) not null, 
state_province VARCHAR(50) not null, country 
VARCHAR(50) not null, 
constraint l_lid_pk PRIMARY KEY (location_id) 
);
''')
# create table,departments
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
department_id INT(4),
department_name VARCHAR(20) unique not null,
location_id INT(3),
constraint d_did_pk PRIMARY KEY (department_id),
constraint d_lid_fk FOREIGN KEY (location_id) references locations(location_id)
);
''')
# enter data to locations
cursor.executemany(
    '''INSERT INTO 
locations (location_id, street_address, postal_code, city, state_province, country) 
VALUES(?,?,?,?,?,?)''', [
        (100, '2 Nice Road', 'N2 7TH', 'London', 'Greater London', 'UK'),
        (200, '23 Pretty Road', 'BS1 8FD', 'Bristol', 'Bristol County', 'UK'),
        (300, '26 Great Street', 'BN1 4BF', 'Brigthon', 'Sussex', 'UK'),
        (400, '143 Lovely Road', 'CB1 2NV', 'Cambridge', 'Cambridgeshire', 'UK')])
# enter data to departments
cursor.executemany(
    '''INSERT INTO departments (department_id, department_name, location_id) VALUES(?,?,?)''', [
        (10, 'IT', 100),
        (20, 'Operations', 200),
        (30, 'Sales', 300),
        (40, 'Marketing', 200),
        (50, 'Management', None)])
cursor.execute('''
SELECT d.department_id, d.department_name, l.location_id, l.city
FROM departments d
LEFT JOIN locations l ON d.location_id = l.location_id;
''')
print("All departments and their locations:")
for row in cursor.fetchall():
    print(row)


cursor.execute('''
SELECT l.location_id, l.city
FROM locations l
LEFT JOIN departments d ON l.location_id = d.location_id
WHERE d.department_id IS NULL;
''')

print("\nLocations with no departments:")
for row in cursor.fetchall():
    print(row)

connect.close()
