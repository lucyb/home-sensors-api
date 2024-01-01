import os

import psycopg2

from .models import Urban


CONNECTION = os.environ.get("DB_CONN", None)


def create_table():
    query_create_sensordata_table = """
        CREATE TABLE urban_data (
            time TIMESTAMPTZ NOT NULL,
            sensor_id INTEGER,
            location_id INTEGER,
            temperature DOUBLE PRECISION,
            pressure DOUBLE PRECISION,
            noise DOUBLE PRECISION,
            pm1 DOUBLE PRECISION,
            pm2_5 DOUBLE PRECISION,
            pm10 DOUBLE PRECISION,
            voltage DOUBLE PRECISION,
            FOREIGN KEY (location_id) REFERENCES locations (id),
            FOREIGN KEY (sensor_id) REFERENCES sensors (id)
        );
        """
    query_create_sensordata_hypertable = (
        "SELECT create_hypertable('urban_data', by_range('time'));"
    )
    query_create_location = "INSERT INTO locations(location) VALUES('Front garden');"
    query_add_sensor = """
        INSERT INTO sensors(sensor, sensor_alias, measurements)
            VALUES('urban', 'urban', ARRAY ['temperature','humidity','pressure','noise','pm1','pm2_5','pm10','voltage']
        );"""

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        cursor.execute(query_create_sensordata_table)
        cursor.execute(query_create_sensordata_hypertable)
        cursor.execute(query_create_location)
        cursor.execute(query_add_sensor)
        conn.commit()


def write(urban: Urban):
    sql = """
        INSERT INTO urban_data(time, sensor_id, location_id, temperature, pressure, noise, pm1, pm2_5, pm10)
        VALUES(
            %(time)s, %(sensor_id)s, %(location_id)s, %(temperature)s, %(pressure)s, %(noise)s, %(pm1)s, %(pm2_5)s, %(pm10)s
        );"""

    sensor_id = 8
    location_id = 6

    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "time": urban.timestamp,
                "sensor_id": sensor_id,
                "location_id": location_id,
                **urban.readings.model_dump()
            },
        )
        conn.commit()


if __name__ == "__main__":
    create_table()
