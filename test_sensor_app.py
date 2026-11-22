import sensor_app

def test_get_hottest_reading():
    readings = sensor_app.load_readings()
    assert sensor_app.get_hottest_reading(readings)=={
      'sensor_id':'S05',
      'location':'Server_Room',  
      'temperature' : 33.5
    }
    assert sensor_app.get_hottest_reading([]) is None

def test_filter_by_location():
    readings = sensor_app.load_readings()
    assert sensor_app.filter_by_location(readings,'Lab_A')==[
        {'sensor_id':'S01','location':'Lab_A','temperature' :24.5},
          {'sensor_id':'S03','location':'Lab_A','temperature' :22.8}
    ]
    assert sensor_app.filter_by_location(readings,'Office')==[]
    assert sensor_app.filter_by_location([],'Lab_A')==[]

def test_calc_average_temp():
    readings=sensor_app.load_readings()
    assert sensor_app.calc_average_temp(readings)==28.2
    assert sensor_app.calc_average_temp([])==0