import xml.etree.ElementTree as ET


class WeatherData:
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature

    def to_xml(self):
        root = ET.Element("root")
        temp_elem = ET.SubElement(root, "Temperature")
        temp_elem.text = str(self.temperature)
        city_elem = ET.SubElement(root, "City")
        city_elem.text = str(self.city)
        lat_elem = ET.SubElement(root, "Latitude")
        lat_elem.text = str(self.latitude)
        lon_elem = ET.SubElement(root, "Longitude")
        lon_elem.text = str(self.longitude)

        xml_data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        return xml_data.decode("utf-8")

    def to_json(self):
        weather_dict = {
            "Weather": str(self.temperature) + " C",
            "Latitude": str(self.latitude),
            "Longitude": str(self.longitude),
            "City": f"{self.city} {self.country}",
        }
        return weather_dict
