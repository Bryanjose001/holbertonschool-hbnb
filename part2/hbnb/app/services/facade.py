from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_amenity(self, amenity_data):
        amenity= Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        for key, value in amenity_data.items():
            setattr(amenity, key, value)
        self.amenity_repo.update(amenity_id, amenity)
        return amenity
    def create_place(self, data):
        owner_id = data.get('owner_id')

        if not owner_id:
            raise ValueError("owner_id is required")

        # Step 1: Lookup User by ID using user_repo
        owner = self.user_repo.get(owner_id)

        if not owner:
            raise ValueError(f"User with id '{owner_id}' not found")

            # Step 2: Create the Place object
        new_place = Place(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            owner=owner
        )

        # Step 3: Add to the place repository
        self.place_repo.add(new_place)

        return new_place
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            setattr(place, key, value)
        self.place_repo.update(place_id, place)
        return place

    def create_review(self, review_data):
        place_id = review_data.get('place_id')
        user_id = review_data.get('user_id')

        if not place_id or not user_id:
            raise ValueError("Both place_id and user_id are required")

        # Fetch actual User and Place instances
        place = self.place_repo.get(place_id)
        user = self.user_repo.get(user_id)

        if not place:
            raise ValueError(f"Place with id '{place_id}' not found")
        if not user:
            raise ValueError(f"User with id '{user_id}' not found")

        # Create Review using validated data
        review = Review(
            text=review_data.get('text'),
            rating=review_data.get('rating'),
            place=place,
            user=user
        )

        # Save to review repo
        self.review_repo.add(review)

        # Add review to place
        place.add_review(review)

        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        reviews = self.review_repo.get_all()
        return [review for review in reviews if review.place.id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            setattr(review, key, value)
        self.review_repo.update(review_id, review)
        return review
    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
        return True if self.review_repo.get(review_id) is None else False