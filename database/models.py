from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Метаданные для модели
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Модель, соответствующая существующей таблице users
class Shingles(Base):
    __tablename__ = "shingles"

    id = Column(Integer, primary_key=True, index=True)
    document_name = Column(String, index=True)
    shingle = Column(String, index=True)