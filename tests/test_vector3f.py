from ctypes import c_float
import unittest

import xr


class TestVector3f(unittest.TestCase):
    def setUp(self):
        self.v = xr.Vector3f(1.34, -9.6, 17.44444444442)

    def tearDown(self):
        pass

    def test_vector3f(self):
        self.assertEqual(3, len(self.v))
        self.assertAlmostEqual(17.44444444442, self.v[2], 5)
        self.assertEqual("(1.340, -9.600, 17.444)", str(self.v))
        self.assertEqual(
            "xr.Vector3f(1.340000033378601, -9.600000381469727, 17.44444465637207)",
            repr(self.v))
        count = 0
        for f in self.v:
            count += 1
        self.assertEqual(3, count)
        self.assertTrue(self.v.y in self.v)
        self.assertTrue(c_float(1.340).value in self.v)


if __name__ == '__main__':
    unittest.main()
