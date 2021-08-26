from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from snacks.models import Snack

# Create your tests here.

class SnackTests(TestCase):
    
    def test_snack_page(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_templates(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_string_representation(self):
        snack = Snack.objects.create(
            name = "Dried Mango",
            purchaser = get_user_model().objects.create_user(
                username="tester",
                email="tester@email.com",
                password="pass"),
        description="Tastes like candy")
        self.assertEqual(str(snack), "Dried Mango")
