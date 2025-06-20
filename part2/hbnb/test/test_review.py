from hbnb.app.models.review import Review

def test_review_creation():
    review = Review(rating="nice",text="nice house",place="salinas",user="Bryan")
    assert review.text == "nice house"
    assert review.place == "salinas" 
    assert review.rating == "nice"
    assert review.user == "Bryan"
    print("review creation test passed!")

test_review_creation()