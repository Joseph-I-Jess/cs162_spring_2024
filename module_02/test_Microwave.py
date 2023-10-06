import Microwave

def test_default_microwave():
    """Test default attributes of a Microwave."""
    m_wave = Microwave.Microwave()

    expected_name = "unnamed microwave"
    expected_volume = 1
    expected_volume_units = "cubic meters"
    expected_wattage = 1000
    expected_wattage_units = "watts"

    assert expected_name == m_wave.name
    assert expected_volume == m_wave.volume
    assert expected_volume_units == m_wave.volume_units
    assert expected_wattage == m_wave.wattage
    assert expected_wattage_units == m_wave.wattage_units

def test_upgrade():
    """Test that the upgrade method works properly on a defualt Microwave."""
    m_wave = Microwave.Microwave()
    m_wave.upgrade()

    expected_volume_minimum = 0
    expected_volume_maximum = 10

    expected_volume_matches_actual = False
    for current_volume in range(expected_volume_minimum, expected_volume_maximum + 1):
        if m_wave.volume == current_volume:
            expected_volume_matches_actual = True
            break

    expected_wattage_minimum = 0
    expected_wattage_maximum = 10_000
    expected_wattage_step = 1_000

    # debug
    # print(f"m_wave.wattage: {m_wave.wattage}")

    expected_wattage_matches_actual = False
    for current_wattage in range(expected_wattage_minimum, expected_wattage_maximum + 1, expected_wattage_step):
        # debug
        # print(f"current_wattage: {current_wattage}")
        if m_wave.wattage == current_wattage:
            expected_wattage_matches_actual = True
            break

    

    assert expected_volume_matches_actual == True
    assert expected_wattage_matches_actual == True
