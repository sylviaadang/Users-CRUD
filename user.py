from mysqlconnection import connectToMySQL

# Blueprint
class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# CREATE
    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM users;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        if results:
            for user in results:
                users.append(cls(user))
        return users

# This will add the data into the query
    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
