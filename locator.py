from geopy.geocoders import Nominatim

def locator():
    geolocator = Nominatim(user_agent="my_custom_application")

    with open(r'C:\xampp\htdocs\location.txt', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        lat, lng = last_line.strip().split(",")

    latitude = lat
    longitude = lng
    location = latitude + ", " + longitude

    address = geolocator.reverse(location)

    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write("\nFull Address: {}\n".format(address.address))
    except KeyError:
        print("Full Address information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("Latitude: {}\n".format(address.latitude))
    except KeyError:
        print("Latitude information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("Longitude: {}\n".format(address.longitude))
    except KeyError:
        print("Longitude information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("Country: {}\n".format(address.raw['address']['country']))
    except KeyError:
        print("Country information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("State: {}\n".format(address.raw['address']['state']))
    except KeyError:
        print("State information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("City: {}\n".format(address.raw['address']['city']))
    except KeyError:
        print("City information not available.")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write("Postal Code: {}\n".format(address.raw['address']['postcode']))
    except KeyError:
        print("Postal Code information not available.")

if __name__ == "__main__":
    locator()