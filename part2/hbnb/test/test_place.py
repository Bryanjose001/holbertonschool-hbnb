from part2.hbnb.app.models.place import Place
from part2.hbnb.app.models.user import User

def test_place_creation():
    user = User(first_name="Jose", last_name="Doe", email="bran@gmail.com",password="ahjjs",is_admin=True)
    place = Place(title="sentinel", description="Doe", price="5",latitude="ahjjs",longitude="3.000" , owner=user)
    assert place.title == "sentinel"
    assert place.description == "Doe"
    assert place.price == "5"
    assert place.latitude =="ahjjs" 
    assert place.longitude == "3.000"
    assert place.owner == user
    assert place.reviews == []  # Default empty list
    assert place.amenities == []  # Default empty list
    print("place creation test passed!")

test_place_creation()