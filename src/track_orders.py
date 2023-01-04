from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders_list = list()

    def __len__(self):
        return len(self.orders_list)

    def add_new_order(self, customer, order, day):
        order_titles = ['cliente', 'pedido', 'dia']
        order_data = [customer, order, day]
        self.orders_list.append(dict(zip(order_titles, order_data)))

        return self.orders_list

    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered = list()
        for order in self.orders_list:
            if order['cliente'] == customer:
                most_ordered.append(order['pedido'])
        occurence_count = Counter(most_ordered)

        return (occurence_count.most_common(1)[0][0])

    def get_never_ordered_per_customer(self, customer):
        food = {'coxinha', 'hamburguer', 'misto-quente', 'pizza'}
        for order in self.orders_list:
            if order['cliente'] == customer:
                if order['pedido'] in food:
                    food.remove(order['pedido'])

        return food

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        for order in self.orders_list:
            days.add(order['dia'])

        for order in self.orders_list:
            if order['cliente'] == customer:
                if order['dia'] in days:
                    days.remove(order['dia'])

        return days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
