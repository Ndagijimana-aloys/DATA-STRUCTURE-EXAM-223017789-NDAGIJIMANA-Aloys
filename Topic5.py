class AlertNode:
    def __init__(self, alert_name, danger_level, location):
        self.alert_name = alert_name
        self.danger_level = danger_level
        self.location = location
        self.next = None

class EmergencyAlertList:
    def __init__(self):
        self.head = None

    def add_alert(self, alert_name, danger_level, location):
        new_alert = AlertNode(alert_name, danger_level, location)
        if not self.head:
            self.head = new_alert
            print(f"First alert added: {alert_name}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_alert
            print(f"Added alert: {alert_name}")
            
    def show_all_alerts(self):
        if not self.head:
            print("No alerts in the system.")
            return

        print("\nCurrent Emergency Alerts:")
        print("-------------------------")
        current = self.head
        while current:
            print(f"Alert: {current.alert_name}")
            print(f"Danger Level: {current.danger_level}")
            print(f"Location: {current.location}")
            print("-------------------------")
            current = current.next

    def remove_alert(self, alert_name):
        if not self.head:
            print("No alerts in the system to remove.")
            return

        if self.head.alert_name == alert_name:
            print(f"Removed alert: {self.head.alert_name}")
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.alert_name != alert_name:
            current = current.next

        if current.next:
            print(f"Removed alert: {current.next.alert_name}")
            current.next = current.next.next
        else:
            print(f"Alert '{alert_name}' not found in the system.")

alert_list = EmergencyAlertList()

print("Adding emergency alerts...")
alert_list.add_alert("Flood", 3, "River Valley")
alert_list.add_alert("Fire", 5, "Forest Area")
alert_list.add_alert("Storm", 2, "Coast")
alert_list.add_alert("Earthquake", 4, "City Center")

alert_list.show_all_alerts()

print("\nRemoving an alert...")
alert_list.remove_alert("Storm")
alert_list.show_all_alerts()
