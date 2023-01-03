from collections import Counter
import csv


def ordered_by_client(orders, client):
    orders_list = list()
    for order in orders:
        if order['cliente'] == client:
            orders_list.append(order['pedido'])
    orders_count = Counter(orders_list)

    return (orders_count.most_common(1)[0][0])


def consumed(orders, client, food):
    count_food = 0
    for order in orders:
        if order['cliente'] == client:
            if order['pedido'] == food:
                count_food += 1

    return str(count_food)


def food_not_consumed(orders, client):
    food = {'coxinha', 'hamburguer', 'misto-quente', 'pizza'}
    for order in orders:
        if order['cliente'] == client:
            if order['pedido'] in food:
                food.remove(order['pedido'])

    return food


def non_clients(orders, client):
    days = set()
    for order in orders:
        days.add(order['dia'])

    for order in orders:
        if order['cliente'] == client:
            if order['dia'] in days:
                days.remove(order['dia'])

    return days


def read_file(path_to_file):
    orders_list = list()
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            orders = csv.reader(file, delimiter=",", quotechar='"')

            for order in orders:
                header = ['cliente', 'pedido', 'dia']
                orders_list.append(dict(zip(header, order)))
        return (orders_list)

    except (FileNotFoundError):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    is_maria = ordered_by_client(orders, 'maria')
    is_arnaldo = consumed(orders, 'arnaldo', 'hamburguer')
    is_joao = food_not_consumed(orders, 'joao')
    is_non_client = non_clients(orders, 'joao')
    file = open("./data/mkt_campaign.txt", mode="w")
    lines = [f"{is_maria}\n", f"{is_arnaldo}\n", f"{is_joao}\n", f"{is_non_client}\n"]
    file.writelines(lines)
    file.close()
