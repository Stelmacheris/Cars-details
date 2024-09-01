# Import the necessary module
from dotenv import load_dotenv
load_dotenv()
from PostgresConnection import PostgresConnection
from CsvDataHandler import CsvDataHandler
from DatabaseManager import DatabaseSchemaManager

Csv_Data_Handler = CsvDataHandler('FINAL_SPINNY_900.csv')
df = Csv_Data_Handler.read_and_process_csv()

postgres_connection = PostgresConnection()
engine_url = postgres_connection.db_url
engine = postgres_connection.engine

schema_manager = DatabaseSchemaManager(engine_url)
schema_manager.create_schema()
schema_manager.insert_csv_data(df)
schema_manager.insert_into_engine()
schema_manager.insert_into_fuel_mileage()
schema_manager.insert_into_transmission()
schema_manager.insert_into_vehicle_make()
schema_manager.insert_into_car_detail()