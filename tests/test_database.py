from src import database
from src.models import Urban, Reading

def test_write_successful():
    urban = Urban(
        nickname="test",
        model="urban",
        uid="123",
        timestamp="2022-09-04T10:40:24Z",
        readings=Reading(
            temperature=27.57,
            humidity=49.33,
            pressure=996.22,
            noise=0.87,
            pm1=9,
            pm2_5=4,
            pm10=2,
            voltage=4.035
            )
        )

    assert database.write(urban)