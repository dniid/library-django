from django.test import TestCase

class UrlTest(TestCase):

    def testAuthorPage(self):
        response = self.client.get('/author/')
        print(response)

        self.assertEqual(response.status_code, 200)