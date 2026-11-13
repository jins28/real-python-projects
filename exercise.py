# create table in DB
# establish connection
# ip_address, domain_name,user_name,password, port_number


class DBConnection:
    database = 'mysql'
    password = 123
    ip_address = 45

    def __init__(self, ip_address, user_name, password, port_number):
        self.port_number = port_number
        self.ip_address = ip_address
        self.user_name = user_name
        self.password = password

    def connect(self):
        print(
            f"connecting to {self.ip_address} with {self.user_name} on {self.port_number} {DBConnection.database}")

    @staticmethod
    def localtime():
        print("The time is 12'O clock")

    @classmethod
    def change_db_name(test, db_name):
        test.database = db_name


connection = DBConnection('102.0.1.1', 'jins', 896, 443)
print(connection.port_number)
print(connection.password)
connection.connect()
connection.localtime()
# connection.change_db_name('postgres')
print(connection.database)
