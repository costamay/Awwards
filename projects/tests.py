from django.test import TestCase
from .models import Profile,Post,User

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user,profile_picture="image.jpeg",bio="just testing", contact='titusouko@gmail.com')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)   
class PostTestClass(TestCase):

    def setUp(self):
        
        self.new_user = User(username='Titus', email='titusouko@gmail.com', password='1234')
        self.new_user.save()
        self.new_post=Post(title="techs",image='image.png',description="test app stuff",user=self.new_user,link="https://w3resource.com",country="kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))    

    def test_save_post(self):
        self.new_post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.new_post.save_post()
        self.new_post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post)==0)