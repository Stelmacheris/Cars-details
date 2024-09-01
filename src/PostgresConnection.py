import os
from sqlalchemy import create_engine

class PostgresConnection:
    """Manages a PostgreSQL database connection using SQLAlchemy.

    This class is designed to encapsulate the database connection logic, including testing
    the connection and retrieving the SQLAlchemy engine.

    Attributes:
        db_url (str): The database connection URL constructed from environment variables.
        engine (Engine): SQLAlchemy engine object for connecting to the database.
    """

    def __init__(self):
        """Initialize the PostgresConnection instance.

        Constructs the database URL from environment variables and initializes the engine to None.
        """
        self.db_url = (
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )
        self.engine = None

    def test_connection(self):
        """Tests the database connection.

        Attempts to connect to the database using the constructed URL. If successful, it prints a
        success message. If it fails, it catches the exception and prints an error message.
        """
        try:
            self.engine = create_engine(self.db_url)
            with self.engine.connect() as conn:
                print("Database connection successful.")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def get_engine(self):
        """Retrieves the SQLAlchemy engine.

        If the engine is not already created, this method creates it with logging enabled. It returns
        the engine instance.

        Returns:
            Engine: The SQLAlchemy engine object for database operations.
        """
        if not self.engine:
            self.engine = create_engine(self.db_url, echo=True)
        return self.engine
