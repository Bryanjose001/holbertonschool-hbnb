from hbnb.app.models.place import Place

def test_place_creation():
    place = Place(title="sentinel", description="Doe", price="5",latitude="ahjjs",longitude="3.000" , owner="Jose" , reviews="nice", amenities="3" )
    assert place.title == "sentinel"
    assert place.description == "doe"
    assert place.price == "5"
    assert place.latitude =="ahjjs" 
    assert place.longitude == "3.000"
    assert place.owner == "jose"
    assert place.reviews== "nice"
    assert place.amenities =="3"
    print("place creation test passed!")

test_place_creation()