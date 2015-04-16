import argparse
import unittest

#python -m unittest tests.test_module test_module2
#python -m unittest tests.test_module.TestStringMethods
#python -m unittest tests.test_module.TestStringMethods.test_isupper
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        print args.config
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    #unittest.main()
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('-config', '--config', default='config.json', help='Your config.json file')
    args = parser.parse_args()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
