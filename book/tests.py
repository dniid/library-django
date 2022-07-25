from django.test import TestCase

class UrlTest(TestCase):

    def testBookPage(self):
        response = self.client.get('/book/')
        print(response)

        self.assertEqual(response.status_code, 200)