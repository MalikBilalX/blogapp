from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse
# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='test', password='test', email='test@gmail.com')

        cls.post =  Post.objects.create(
            title = 'A test title',
            author = cls.user,
            body = 'This is a test body'
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'A test title')
        self.assertEqual(self.post.body, 'This is a test body')
        self.assertEqual(self.post.author.username, 'test')
        self.assertEqual(str(self.post.title), 'A test title')
        self.assertEqual(self.post.get_absolute_url(), '/blog/1/')

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_blog_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test body')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_blog_detailview(self):
        response = self.client.get(reverse('blog_detail', kwargs={'pk': self.post.pk}))
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A test title')
        self.assertTemplateUsed(response, 'blog_detail.html')

    def test_post_createview(self):
        response = self.client.post(
        reverse("blog_new"),
        {
        "title": "New title",
        "body": "New text",
        "author": self.user.id,
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
        reverse("blog_edit", args="1"),
        {
        "title": "Updated title",
        "body": "Updated text",
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("blog_delete",
        args="1"))
        self.assertEqual(response.status_code, 302)