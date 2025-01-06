class EmergencyAlert:
    def __init__(self, alert_id, disaster_type, location, priority, impact_radius):
        self.alert_id = alert_id
        self.disaster_type = disaster_type
        self.location = location
        self.priority = priority
        self.impact_radius = impact_radius

class EmergencyAlertSystem:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        self.alerts.append(alert)
        
    def counting_sort(self, exp):
        n = len(self.alerts)
        output = [0] * n
        count = [0] * 10
        
        for alert in self.alerts:
            index = alert.priority // exp
            count[index % 10] += 1
            
        for i in range(1, 10):
            count[i] += count[i - 1]
            
        i = n - 1
        while i >= 0:
            index = self.alerts[i].priority // exp
            output[count[index % 10] - 1] = self.alerts[i]
            count[index % 10] -= 1
            i -= 1
            
        for i in range(n):
            self.alerts[i] = output[i]

    def radix_sort(self):
        max_priority = max(alert.priority for alert in self.alerts)
        exp = 1
        while max_priority // exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def display_alerts(self):
        print("\nEmergency Alerts (Sorted by Priority):")
        print("-" * 50)
        for alert in reversed(self.alerts):
            print(f"ID: {alert.alert_id}")
            print(f"Type: {alert.disaster_type}")
            print(f"Location: {alert.location}")
            print(f"Priority Level: {alert.priority}")
            print(f"Impact Radius: {alert.impact_radius}km")
            print("-" * 50)


system = EmergencyAlertSystem()

alert1 = EmergencyAlert(101, "Tsunami", "Coastal Area", 856, 100)
system.add_alert(alert1)

alert2 = EmergencyAlert(102, "Forest Fire", "National Park", 745, 50)
system.add_alert(alert2)

alert3 = EmergencyAlert(103, "Earthquake", "City Center", 999, 75)
system.add_alert(alert3)

alert4 = EmergencyAlert(103, "flood", "City Center", 786, 78)
system.radix_sort()
system.display_alerts()