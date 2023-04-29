import sqlalchemy

from data.db_session import SqlAlchemyBase


class Wards(SqlAlchemyBase):
    __tablename__ = 'wards'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name_of_map_piece = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    side = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    folder_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
