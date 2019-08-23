from rest_framework import status
from rest_framework.test import APITestCase

from movies.models import Comment, Movie, Ratings
from movies.utils.test_utils.base_test import BaseTest


class MoviesTests(APITestCase):
    def test_retrieve_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(Movie.objects.count(), 0)
        self.assertTrue(response.data == [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_movie(self):
        initial_movie_count = Movie.objects.count()
        body = {'title': 'Titanic'}
        response = self.client.post('/movies/', body)
        self.assertEqual(Movie.objects.count(), initial_movie_count + 1)
        self.assertEqual(Ratings.objects.count(), 3)
        self.assertEqual(response.data['Title'], 'Titanic')
        self.assertEqual(type(response.data['Ratings']), list)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentsTests(APITestCase, BaseTest):
    def test_retrieve_comments(self):
        BaseTest.__init__(self)
        response = self.client.get('/comments/')
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.data[0]['body'], 'base comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_comment(self):
        BaseTest.__init__(self)
        body = {
            "movie_id": 1,
            "body": "test comment"
        }
        initial_comments_count = Comment.objects.count()
        response = self.client.post('/comments/', body)
        self.assertEqual(Comment.objects.count(), initial_comments_count + 1)
        self.assertEqual(response.data['body'], 'test comment')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TopCommentsTests(APITestCase, BaseTest):
    def test_retrieve_statistics(self):
        BaseTest.__init__(self)
        response = self.client.get('/top/2019-08-20/2020-09-30/')
        self.assertEqual(response.data[0]['total_comments'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filtered_statistics(self):
        BaseTest.__init__(self)
        response = self.client.get('/top/')
        self.assertEqual(response.data[0]['total_comments'], 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
