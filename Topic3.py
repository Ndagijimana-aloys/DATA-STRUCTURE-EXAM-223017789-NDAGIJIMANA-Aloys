class Alert:
    def __init__(self, disaster_type, location, severity, timestamp):
        self.disaster_type = disaster_type
        self.location = location
        self.severity = severity
        self.timestamp = timestamp
        self.next = None

class EmergencyAlertSystem:
    def __init__(self):
        self.head = None
        self.alert_count = 0
    
    def add_alert(self, disaster_type, location, severity, timestamp):
        new_alert = Alert(disaster_type, location, severity, timestamp)
        self.alert_count += 1
        
        if not self.head or severity > self.head.severity:
            new_alert.next = self.head
            self.head = new_alert
            return
            
        current = self.head
        while current.next and current.next.severity >= severity:
            current = current.next
        
        new_alert.next = current.next
        current.next = new_alert
    
    def remove_resolved_alert(self, location):
        if not self.head:
            return False
            
        if self.head.location == location:
            self.head = self.head.next
            self.alert_count -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.location == location:
                current.next = current.next.next
                self.alert_count -= 1
                return True
            current = current.next
        return False
    
    def display_alerts(self):
        if not self.head:
            print("\nNo active alerts")
            return
            
        print("\nActive Emergency Alerts:")
        current = self.head
        while current:
            print(f"\nType: {current.disaster_type}")
            print(f"Location: {current.location}")
            print(f"Severity: {current.severity}")
            print(f"Time: {current.timestamp}")
            current = current.next
        print(f"\nTotal Alerts: {self.alert_count}")

system = EmergencyAlertSystem()
    
system.add_alert("Flood", "River Valley", 4, "2024-01-03 10:30")
system.add_alert("Wildfire", "Forest Zone", 5, "2024-01-03 11:15")
system.add_alert("Landslide", "Mountain Area", 3, "2024-01-03 12:00")
    
system.display_alerts()
    
print("\nRemoving resolved alert from River Valley")
system.remove_resolved_alert("River Valley")
system.display_alerts()
    
