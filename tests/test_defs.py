import unittest
import json
import sys
sys.path.append("..")
from src import get_instance_data_readable

class test_defs(unittest.TestCase):

    def test_get_instance_data_readable(self):

        instance_data_sample = json.load(
            open("instance_data_sample.json")
        )
        instance_sample = instance_data_sample[0]

        expected = "id: i-asdkjfaksjdfh\n"
        expected += "\tsize: t2.nano"

        self.assertEqual(expected, get_instance_data_readable(instance_sample))


if __name__ == '__main__':
    unittest.main()
