
def get_formatted_name_population(city, country, population = ''):
    if not population:
        formatted_name = city + "," + country
    else:
        formatted_name = city + "," + country + " - " + population
    return formatted_name.title()

