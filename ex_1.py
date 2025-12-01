
def test_distinct(liste) :
    liste_copy = []
    for terme in liste :
        if terme in liste_copy :
            return False
        liste_copy.append(terme)
    return True

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))