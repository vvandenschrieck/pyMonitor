import unittest

from website.website import Website, Status


def test_mock_true(url):
    return True

def test_mock_false(url) :
    return False

class TestingWebsite(unittest.TestCase):
    def test_init(self):
        site = Website("Test", "www.test.com")
        self.assertEquals(site.status, "UNKNOWN")

    def test_probe_true(self):
        site = Website("Test", "www.test.com")
        site.add_probe(test_mock_true)
        site.test()
        self.assertEquals(site.status, "OK")

    def test_probe_false(self):
        site = Website("Test", "www.test.com")
        site.add_probe(test_mock_false)
        site.test()
        self.assertEquals(site.status, "KO")

    def test_multiple_probes(self):
        site = Website("Test", "www.test.com")
        site.add_probe(test_mock_true)
        site.add_probe(test_mock_true)
        site.test()
        self.assertEquals(site.status, "OK")
        site.add_probe(test_mock_false)
        site.test()
        self.assertEquals(site.status, "KO")


    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
