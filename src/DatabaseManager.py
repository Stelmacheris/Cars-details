from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from Models import Base, AllCarData, Engine, Transmission, FuelMileage, VehicleMake, CarDetail

class DatabaseSchemaManager:
    """Manages the database schema and handles data operations.

    This class provides functionality to create a database schema, and insert data into various
    tables from CSV files or other data sources using SQLAlchemy ORM.

    Attributes:
        engine_url (str): The database connection URL.
    """

    def __init__(self, engine_url):
        """Initialize the DatabaseSchemaManager with a connection engine.

        Args:
            engine_url (str): The database connection URL used to create the engine.
        """
        self.engine = create_engine(engine_url)

    def create_schema(self):
        """Creates the database schema based on the models imported from Models.py."""
        Base.metadata.create_all(self.engine)

    def insert_csv_data(self, df):
        """Inserts data from a pandas DataFrame into the AllCarData table.

        Args:
            df (pd.DataFrame): The DataFrame containing car data.
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            Base.metadata.create_all(self.engine)
            
            for _, row in df.iterrows():
                car_data = AllCarData(**row.to_dict())
                session.add(car_data)
            
            session.commit()
            print("Data successfully inserted into the database.")
        except SQLAlchemyError as e:
            print(f"An error occurred during insertion: {e}")
            session.rollback()
        finally:
            session.close()

    def insert_into_engine(self):
        """Inserts distinct engine data into the Engine table based on existing AllCarData entries."""
        session = sessionmaker(bind=self.engine)()
        try:
            data = session.query(
                AllCarData.Engine_Type,
                AllCarData.CC_Displacement,
                AllCarData.Power_BHP,
                AllCarData.Torque_Nm
            ).distinct().all()

            for entry in data:
                if not session.query(Engine).filter_by(
                        Engine_Type=entry.Engine_Type,
                        CC_Displacement=entry.CC_Displacement,
                        Power_BHP=entry.Power_BHP,
                        Torque_Nm=entry.Torque_Nm).first():
                    new_engine = Engine(
                        Engine_Type=entry.Engine_Type,
                        CC_Displacement=entry.CC_Displacement,
                        Power_BHP=entry.Power_BHP,
                        Torque_Nm=entry.Torque_Nm
                    )
                    session.add(new_engine)

            session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def insert_into_transmission(self):
        """Inserts distinct transmission data into the Transmission table based on existing AllCarData entries."""
        session = sessionmaker(bind=self.engine)()
        try:
            data = session.query(
                AllCarData.Transmission,
                AllCarData.Transmission_Type
            ).distinct().all()

            for entry in data:
                if not session.query(Transmission).filter_by(
                        Transmission=entry.Transmission,
                        Transmission_Type=entry.Transmission_Type).first():
                    new_transmission = Transmission(
                        Transmission=entry.Transmission,
                        Transmission_Type=entry.Transmission_Type
                    )
                    session.add(new_transmission)

            session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def insert_into_fuel_mileage(self):
        """Inserts distinct fuel mileage data into the FuelMileage table based on existing AllCarData entries."""
        session = sessionmaker(bind=self.engine)()
        try:
            data = session.query(
                AllCarData.Fuel_Type,
                AllCarData.Fuel_Tank_Capacity_L,
                AllCarData.Mileage_kmpl
            ).distinct().all()

            for entry in data:
                if not session.query(FuelMileage).filter_by(
                        Fuel_Type=entry.Fuel_Type,
                        Fuel_Tank_Capacity=entry.Fuel_Tank_Capacity_L,
                        Mileage_kmpl=entry.Mileage_kmpl).first():
                    new_fuel_mileage = FuelMileage(
                        Fuel_Type=entry.Fuel_Type,
                        Fuel_Tank_Capacity=entry.Fuel_Tank_Capacity_L,
                        Mileage_kmpl=entry.Mileage_kmpl
                    )
                    session.add(new_fuel_mileage)

            session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def insert_into_vehicle_make(self):
        """Inserts distinct vehicle make and model data into the VehicleMake table based on existing AllCarData entries."""
        session = sessionmaker(bind=self.engine)()
        try:
            data = session.query(
                AllCarData.Make,
                AllCarData.Model
            ).distinct().all()

            for entry in data:
                if not session.query(VehicleMake).filter_by(
                        Make=entry.Make,
                        Model=entry.Model).first():
                    new_vehicle_make = VehicleMake(
                        Make=entry.Make,
                        Model=entry.Model
                    )
                    session.add(new_vehicle_make)

            session.commit()
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    def insert_into_car_detail(self):
        """Inserts detailed car data into the CarDetail table, including relationships to other data tables."""
        session = sessionmaker(bind=self.engine)()
        try:
            all_car_data_entries = session.query(AllCarData).all()
            for entry in all_car_data_entries:
                vehicle_make = session.query(VehicleMake).filter_by(Make=entry.Make, Model=entry.Model).first()
                engine = session.query(Engine).filter_by(
                    Engine_Type=entry.Engine_Type,
                    CC_Displacement=entry.CC_Displacement,
                    Power_BHP=entry.Power_BHP,
                    Torque_Nm=entry.Torque_Nm
                ).first()
                fuel_mileage = session.query(FuelMileage).filter_by(
                    Fuel_Type=entry.Fuel_Type,
                    Fuel_Tank_Capacity=entry.Fuel_Tank_Capacity_L,
                    Mileage_kmpl=entry.Mileage_kmpl
                ).first()
                transmission = session.query(Transmission).filter_by(
                    Transmission=entry.Transmission,
                    Transmission_Type=entry.Transmission_Type
                ).first()

                car_detail = CarDetail(
                    Make_Year=entry.Make_Year,
                    Color=entry.Color,
                    Body_Type=entry.Body_Type,
                    Mileage_Run=entry.Mileage_Run,
                    No_of_Owners=entry.No_of_Owners,
                    Seating_Capacity=entry.Seating_Capacity,
                    Emission=entry.Emission,
                    Price=entry.Price,
                    Vehicle_Make_ID=vehicle_make.vehicle_id if vehicle_make else None,
                    Engine_ID=engine.engine_id if engine else None,
                    Fuel_Mileage_ID=fuel_mileage.fuel_mileage_id if fuel_mileage else None,
                    Transmission_ID=transmission.transmission_id if transmission else None
                )
                session.add(car_detail)

            session.commit()
            print("CarDetail data successfully inserted.")
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()
