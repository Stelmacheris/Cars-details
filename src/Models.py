from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class AllCarData(Base):
    """Represents the 'all_car_data' table in the database.

    This model captures comprehensive information about cars including basic details,
    engine specifications, transmission details, and more.
    """
    __tablename__ = 'all_car_data'
    All_car_data_Id = Column(Integer, primary_key=True, autoincrement=True)
    Car_Name = Column(String)
    Make = Column(String)
    Model = Column(String)
    Make_Year = Column(Integer)
    Color = Column(String)
    Body_Type = Column(String)
    Mileage_Run = Column(Float)
    No_of_Owners = Column(String)
    Seating_Capacity = Column(Integer)
    Fuel_Type = Column(String)
    Fuel_Tank_Capacity_L = Column(Integer)
    Engine_Type = Column(String)
    CC_Displacement = Column(Integer)
    Transmission = Column(String)
    Transmission_Type = Column(String)
    Power_BHP = Column(Float)
    Torque_Nm = Column(Float)
    Mileage_kmpl = Column(String)
    Emission = Column(String)
    Price = Column(String)

class VehicleMake(Base):
    """Represents the 'vehicle_make' table for storing car makes and models in the database."""
    __tablename__ = 'vehicle_make'
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    Make = Column(String)
    Model = Column(String)

class Engine(Base):
    """Represents the 'engine' table for storing engine details."""
    __tablename__ = 'engine'
    engine_id = Column(Integer, primary_key=True, autoincrement=True)
    Engine_Type = Column(String)
    CC_Displacement = Column(Integer)
    Power_BHP = Column(Float)
    Torque_Nm = Column(Float)

class FuelMileage(Base):
    """Represents the 'fuel_mileage' table for storing fuel-related data."""
    __tablename__ = 'fuel_mileage'
    fuel_mileage_id = Column(Integer, primary_key=True, autoincrement=True)
    Fuel_Type = Column(String)
    Fuel_Tank_Capacity = Column(Integer)
    Mileage_kmpl = Column(String)

class Transmission(Base):
    """Represents the 'transmission' table for storing transmission types and details."""
    __tablename__ = 'transmission'
    transmission_id = Column(Integer, primary_key=True, autoincrement=True)
    Transmission = Column(String)
    Transmission_Type = Column(String)

class CarDetail(Base):
    """Represents the 'car_detail' table, linking detailed car information with other entity tables."""
    __tablename__ = 'car_detail'
    Car_ID = Column(Integer, primary_key=True, autoincrement=True)
    Make_Year = Column(Integer)
    Color = Column(String)
    Body_Type = Column(String)
    Mileage_Run = Column(Float)
    No_of_Owners = Column(String)
    Seating_Capacity = Column(Integer)
    Emission = Column(String)
    Price = Column(String)
    Vehicle_Make_ID = Column(Integer, ForeignKey('vehicle_make.vehicle_id'))
    Engine_ID = Column(Integer, ForeignKey('engine.engine_id'))
    Fuel_Mileage_ID = Column(Integer, ForeignKey('fuel_mileage.fuel_mileage_id'))
    Transmission_ID = Column(Integer, ForeignKey('transmission.transmission_id'))

    vehicle_make = relationship("VehicleMake")
    engine = relationship("Engine")
    fuel_mileage = relationship("FuelMileage")
    transmission = relationship("Transmission")
