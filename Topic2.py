#Implementation of Binary Search Tree (BST) and Binary Tree to manage data in the emergency alert system for natural disasters.
class AlertNode:
    def __init__(self, alert_name, danger_level, location):
        self.alert_name = alert_name
        self.danger_level = danger_level
        self.location = location
        self.left = None
        self.right = None


class EmergencyAlertSystem:
    def __init__(self):
        self.root = None  
    def add_alert(self, alert_name, danger_level, location):
        new_alert = AlertNode(alert_name, danger_level, location)
        
        if not self.root:
            self.root = new_alert
            print(f"First alert added: {alert_name}")
            return
        
        current = self.root
        while True:
            if danger_level < current.danger_level:
                if current.left is None:
                    current.left = new_alert
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_alert
                    break
                current = current.right
        
        print(f"Added new alert: {alert_name}")
    
    def show_all_alerts(self):
        if not self.root:
            print("No alerts in system")
            return
        
        print("\nCurrent Emergency Alerts:")
        print("-------------------------")
        self._show_alerts_helper(self.root)
    
    def _show_alerts_helper(self, node):
        if node:
            self._show_alerts_helper(node.left)
            print(f"Alert: {node.alert_name}")
            print(f"Danger Level: {node.danger_level}")
            print(f"Location: {node.location}")
            print("-------------------------")
            self._show_alerts_helper(node.right)

alert_system = EmergencyAlertSystem()
    
#execute codes
print("Adding emergency alerts...")
alert_system.add_alert("Flood", 3, "North")
alert_system.add_alert("Fire", 5, "South")
alert_system.add_alert("Storm", 2, "South")
alert_system.add_alert("Earthquake", 4, "West")
alert_system.show_all_alerts()
