from datetime import datetime
import csv
class LogEntry:
    def __init__(self, event_time, internal_ip, port_number, protocol, action, rule_id, source_ip, country, country_name):
        self.event_time = datetime.strptime(event_time, "%Y-%m-%d %H:%M:%S %Z")
        self.internal_ip = internal_ip
        self.port_number = int(port_number)
        self.protocol = protocol
        self.action = action
        self.rule_id = rule_id
        self.source_ip = source_ip
        self.country = country
        self.country_name = country_name

    def __str__(self):
        return f"{self.event_time} | {self.internal_ip} | {self.port_number} | {self.protocol} | {self.action} | {self.rule_id} | {self.source_ip} | {self.country} | {self.country_name}"


    @property
    def ipv4_class(self):
        first_octet = int(self.source_ip.split('.')[0])
        if 1 <= first_octet <= 126:
            return "A"
        elif 128 <= first_octet <= 191:
            return "B"
        elif 192 <= first_octet <= 223:
            return "C"
        elif 224 <= first_octet <= 239:
            return "D"
        else:
            return "Unknown"

class LogAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def load_logs(self):
        logs = []
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                logs.append(LogEntry(
                    row["event_time"],
                    row["internal_ip"],
                    row["port_number"],
                    row["protocol"],
                    row["action"],
                    row["rule_id"],
                    row["source_ip"],
                    row["country"],
                    row["country_name"]
                ))
        return logs
