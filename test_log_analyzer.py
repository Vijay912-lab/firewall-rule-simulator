import unittest
from log_analyzer import LogEntry
from datetime import datetime

class TestLogEntry(unittest.TestCase):
    def test_event_time_conversion(self):
        log = LogEntry("2022-01-01 08:29:25 UTC", "192.168.1.1", 80, "TCP", "ALLOW", 1, "11.177.69.220", "US", "United States")
        self.assertEqual(log.event_time.month, 1) 
        self.assertEqual(log.event_time.hour, 8)   

    def test_ipv4_class(self):
        log_a = LogEntry("2022-01-01 08:29:25 UTC", "192.168.1.1", 80, "TCP", "ALLOW", 1, "11.177.69.220", "US", "United States")
        self.assertEqual(log_a.ipv4_class, "A")  

        log_b = LogEntry("2022-01-01 08:29:25 UTC", "192.168.1.1", 80, "TCP", "ALLOW", 1, "128.163.4.51", "US", "United States")
        self.assertEqual(log_b.ipv4_class, "B")  
        log_c = LogEntry("2022-01-01 08:29:25 UTC", "192.168.1.1", 80, "TCP", "ALLOW", 1, "192.168.1.1", "US", "United States")
        self.assertEqual(log_c.ipv4_class, "C")  

        log_d = LogEntry("2022-01-01 08:29:25 UTC", "192.168.1.1", 80, "TCP", "ALLOW", 1, "229.163.4.51", "US", "United States")
        self.assertEqual(log_d.ipv4_class, "D")  

if __name__ == "__main__":
    unittest.main()
