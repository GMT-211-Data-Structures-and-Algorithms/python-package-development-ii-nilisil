import unittest
import math
from veri_odev import Point, Line 

class TestGeometry(unittest.TestCase):
    
    def test_point_creation(self):
        """Point objesinin doğru koordinatlarla oluştuğunu test eder."""
        p = Point(3, 4, "A Noktası")
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)
        self.assertEqual(p.name, "A Noktası")

    def test_line_length_calculation(self):
        """Çizgi uzunluğunun doğru (Pisagor) hesaplandığını test eder."""
        p1 = Point(0, 0)
        p2 = Point(3, 4) 
        
        test_line = Line("Test Güzergahı")
        test_line.add_point(p1)
        test_line.add_point(p2)
        
        
        self.assertEqual(test_line.calculate_length(), 5.0)

    def test_perpendicular_distance_to_point(self):
        """Noktanın çizgiye olan dik uzaklığının doğru hesaplandığını test eder."""
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        
        test_line = Line("Yatay Çizgi")
        test_line.add_point(p1)
        test_line.add_point(p2)
        
        test_point = Point(1.5, 4)
        perpendicular_dist = test_line.perpendicular_distance_to_point(test_point)
        self.assertEqual(perpendicular_dist, 4.0)
        
    def test_perpendicular_distance_diagonal_line(self):
        """Köşegen çizgiye olan dik uzaklık testini test eder."""
        p1 = Point(0, 0)
        p2 = Point(1, 1)
        
        test_line = Line("Köşegen Çizgi")
        test_line.add_point(p1)
        test_line.add_point(p2)
        
        test_point = Point(1, 0)
        perpendicular_dist = test_line.perpendicular_distance_to_point(test_point)
        self.assertAlmostEqual(perpendicular_dist, math.sqrt(2)/2, places=5)

if __name__ == '__main__':
    unittest.main()
