from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity , get_jwt

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        review_data = api.payload

        try:
            current_user = get_jwt_identity()  # string
            print("Current User ID:", current_user)
            claims = get_jwt()
            is_admin = claims['is_admin']
            place = facade.get_place(review_data['place_id'])
            if place.owner == current_user:
                return {'error': 'You cannot review your own place'}, 400
            reviews = facade.get_reviews_by_place(review_data['place_id'])
            for review in reviews:
                if review.user.id == current_user:
                    return {'error': 'You have already reviewed this place'}, 400
            new_review = facade.create_review(review_data)
            return {'id': new_review.id, 'text': new_review.text, 'rating': new_review.rating, 'user_id': new_review.user.id}, 201
        except Exception as e:
            return {'error': str(e)}, 400
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [{'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user.id} for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user.id}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if current_user != review.user.id:
           #return {'error': 'Unauthorized action'}, 403
            updated_review = facade.update_review(review_id, review_data)
        if not updated_review:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review updated successfully'}, 200
    
    @api.expect(review_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'You cannot modify email or password.')
    @api.response(403, 'Unauthorized action.')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        """Update user profile information (excluding email and password)"""
        user_data = api.payload
        current_user_id = get_jwt_identity()
        #Check that user is modifying their own data
        if current_user_id != user_id:
            return {'error': 'Unauthorized action.'}, 403
        #Prevent email or password modification
        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email or password.'}, 400
        #Fetch and update user
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        updated_user = facade.update_user(user_id, user_data)
        return {'message': 'User updated successfully'}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if current_user != review.user.id:
            return {'error': 'Unauthorized action'}, 403
        deleted = facade.delete_review(review_id)
        if not deleted:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        reviews = facade.get_reviews_by_place(place_id)
        if not reviews:
            return {'error': 'Place not found or no reviews available'}, 404
        return [{'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user.id} for review in reviews], 200