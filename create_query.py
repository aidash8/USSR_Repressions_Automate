from config import DBType

def create_query(n: int, db_type: DBType):
    sql = """
            SELECT *
            FROM formular
            WHERE "расстрел" IS NOT NULL AND
    """
    if db_type == DBType.POSTGRESQL:
        sql += "random() < 0.01"
    else:
        sql += "1 = 1"
    sql += f"\nLIMIT {n}"
    
    return sql