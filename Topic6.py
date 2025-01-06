
class AlertNode:
    def __init__(self, category_name):
        self.category_name = category_name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class EmergencyAlertTree:
    def __init__(self):
        self.root = None

    def set_root(self, root_name):
        self.root = AlertNode(root_name)
        print(f"Root category set: {root_name}")

    def add_alert(self, parent_name, alert_name):
        if not self.root:
            print("No root category found. Please set the root first.")
            return

        parent_node = self._find_node(self.root, parent_name)
        if parent_node:
            parent_node.add_child(AlertNode(alert_name))
            print(f"Added '{alert_name}' under '{parent_name}'")
        else:
            print(f"Parent category '{parent_name}' not found.")

    def _find_node(self, current_node, target_name):
        if current_node.category_name == target_name:
            return current_node

        for child in current_node.children:
            found_node = self._find_node(child, target_name)
            if found_node:
                return found_node
        return None

    def display_hierarchy(self):
        if not self.root:
            print("No root category found. Please set the root first.")
            return

        print("\nEmergency Alert Hierarchy:")
        print("--------------------------")
        self._display_helper(self.root, level=0)

    def _display_helper(self, node, level):
        print(" " * (level * 2) + f"- {node.category_name}")
        for child in node.children:
            self._display_helper(child, level + 1)


alert_tree = EmergencyAlertTree()

alert_tree.set_root("Natural Disasters")

alert_tree.add_alert("Natural Disasters", "Weather Events")
alert_tree.add_alert("Natural Disasters", "Geological Events")
alert_tree.add_alert("Weather Events", "Floods")
alert_tree.add_alert("Weather Events", "Storms")
alert_tree.add_alert("Geological Events", "Earthquakes")
alert_tree.add_alert("Geological Events", "Volcanoes")
alert_tree.add_alert("Floods", "River Flood")
alert_tree.add_alert("Storms", "Hurricane")
alert_tree.add_alert("Earthquakes", "Tectonic Activity")

alert_tree.display_hierarchy()
