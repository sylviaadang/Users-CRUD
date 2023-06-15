from flask_app.config.mysqlconnection import connectToMySQL

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

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT *
        FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)

        return cls(results[0])

# This will add the data into the query
    @classmethod
    def add_user(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

# update
    @classmethod
    def update_user(cls, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
        """

        return connectToMySQL(cls.DB).query_db(query, data)


# delete
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s;
        """

        return connectToMySQL(cls.DB).query_db(query, data)
