
import greatcircle

martinitoren = (53.219332, 6.568239) # the Martinitoren in Groningen
csamsterdam = (52.378230, 4.899997) # Amsterdam Central Station
km = greatcircle.distance(martinitoren[0], martinitoren[1], csamsterdam[0], csamsterdam[1])
assert int(km) == 146



import calculator

calc = calculator.Calculator()
assert calc.distance(9718, 99999) is None
assert calc.distance(99999, 1000) is None
assert int(calc.distance(9718, 1000)) == 146

within = [postcode for (postcode, km) in calc.postcodesaround(9718, 10)]

assert len(within) > 0
assert 9811 in within
assert 1200 not in within
