
import database
import greatcircle

class Calculator(object):
    def distance(self, postcode1, postcode2):
        """ Return the distance (in kilometers) between two postcodes. """
        fr = database.latlon.get(postcode1)
        if not fr:
            return None
        to = database.latlon.get(postcode2)
        if not to:
            return None
        frlat, frlon = fr
        tolat, tolon = to
        return greatcircle.distance(frlat, frlon, tolat, tolon)

    def postcodesaround(self, postcode, radius):
        """ Determine which postcodes are in geographical distance of the given postcode.
        Radius is specified in kilometers.
        The list consists of tuples (postcode, distance to the postcode). """
        if not postcode in database.latlon:
            return []
        within = []
        for topostcode in database.latlon:
            d = self.distance(postcode, topostcode)
            if d <= radius:
                within.append((topostcode, d))
        return sorted(within)

