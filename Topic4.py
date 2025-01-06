# Node class for a Binary Tree
class OrderNode:
    def __init__(self, order_id, alert_name, priority_level):
        self.order_id = order_id        
        self.alert_name = alert_name    
        self.priority_level = priority_level
        self.left = None        
        self.right = None 

class EmergencyOrderTree:
    def __init__(self):
        self.root = None
        self.order_count = 0
        self.max_orders = 5

    def add_order(self, order_id, alert_name, priority_level):
        if self.order_count > self.max_orders:
            print("Order limit reached. Cannot add more orders.")
            return

        new_order = OrderNode(order_id, alert_name, priority_level)
        if not self.root:
            self.root = new_order
            print(f"Added first order: {alert_name} (ID: {order_id})")
        else:
            self._add_order_helper(self.root, new_order)

        self.order_count += 1

    def _add_order_helper(self, current, new_order):
        if current.left is None:
            current.left = new_order
        elif current.right is None:
            current.right = new_order
        else:
            self._add_order_helper(current.left, new_order)
    def show_all_orders(self):
        if not self.root:
            print("No orders in the system.")
        else:
            print("\nCurrent Emergency Orders:")
            print("-------------------------")
            self._show_orders_helper(self.root)

    def _show_orders_helper(self, node):
        if node:
            print(f"Order ID: {node.order_id}")
            print(f"Alert: {node.alert_name}")
            print(f"Priority Level: {node.priority_level}")
            print("-------------------------")
            self._show_orders_helper(node.left)
            self._show_orders_helper(node.right)


order_tree = EmergencyOrderTree()
print("Adding emergency orders...")
order_tree.add_order(101, "Flood Alert", 3)
order_tree.add_order(102, "Fire Alert", 5)
order_tree.add_order(103, "Storm Alert", 2)
order_tree.add_order(104, "Earthquake Alert", 4)
order_tree.add_order(105, "Tornado Alert", 1)
order_tree.show_all_orders()

