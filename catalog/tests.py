from django.test import TestCase

class UrlTest(TestCase):

    def testCatalogPage(self):
        response = self.client.get('/catalog/')
        print(response)

        self.assertEqual(response.status_code, 200)