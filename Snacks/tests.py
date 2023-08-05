from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Snack
# Create your tests here.
class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_Snack = Snack.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_Snack.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_Snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.owner)
        actual_name = str(snack.name)
        actual_desc = str(snack.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_Snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Snacks = response.data
        self.assertEqual(len(Snacks), 1)
        self.assertEqual(Snacks[0]["name"], "rake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("snack_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_delete_Snack(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("detail_list",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)