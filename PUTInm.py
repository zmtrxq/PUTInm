import heapq
cities = ['Алматы', 'Нур-Султан', 'Шымкент', 'Астана', 'Караганда', 'Бишкек', 'Ош', 'Тараз', 'Талдыкорган', 'Усть-Каменогорск']
routes = {('Астана', 'Нур-Султан'): 20, ('Алматы', 'Бишкек'): 250, ('Алматы', 'Нур-Султан'): 1200, ('Алматы', 'Талдыкорган'): 300, ('Караганда', 'Шымкент'): 1000, ('Караганда', 'Талдыкорган'): 900, ('Нур-Султан', 'Караганда'): 200, ('Нур-Султан', 'Усть-Каменогорск'): 1100, ('Ош', 'Тараз'): 750, ('Шымкент', 'Алматы'): 800, ('Шымкент', 'Астана'): 700, ('Шымкент', 'Тараз'): 160, ('Талдыкорган', 'Усть-Каменогорск'): 800, ('Тараз', 'Бишкек'): 190, ('Бишкек', 'Ош'): 700}
def show_cities():
    for i, city in enumerate(cities, 1): print(f"{i}. {city}")
def get_city(x):
    while True:
        try:
            choice = int(input(x))
            if 1 <= choice <= len(cities): return cities[choice - 1]
            print("Неверный номер города. Попробуйте снова")
        except ValueError: print("Введите число")
def show_routes():
    print("\nГорода:")
    show_cities()
    print("\nМаршруты:")
    for (s, e), d in routes.items(): print(f"{s} ⇆  {e}: {d} км")
def deikstra(src, end=None):
    g = {c: [] for c in cities}
    for (a, b), d in routes.items(): g[a].append((b, d)); g[b].append((a, d))
    dist, q, prev = {c: float('inf') for c in cities}, [(0, src)], {c: None for c in cities}
    dist[src] = 0
    while q:
        cd, cc = heapq.heappop(q)
        if cd > dist[cc]: continue
        for n, w in g[cc]:
            if (nd := cd + w) < dist[n]: dist[n], prev[n] = nd, cc; heapq.heappush(q, (nd, n))
    if end:
        if dist[end] == float('inf'): print("\nМаршрут недоступен."); return
        p = []
        while end: p.append(end); end = prev[end]
        print("\nКратчайший маршрут:", " → ".join(p[::-1]), f"\nРасстояние: {dist[p[0]]} км")
    else:
        for c, d in sorted(dist.items(), key=lambda x: x[1]): print(f"{c}: {d} км")
def add():
    print("\n1. Добавить город\n2. Добавить маршрут")
    c = input("Выбор: ")
    if c == '1':
        nc = input("Город: ")
        if nc in cities: print("Город уже есть")
        else: cities.append(nc); print("Город добавлен")
    elif c == '2':
        print("\nВыберите города для маршрута:")
        show_cities()
        a, b = get_city("Откуда: "), get_city("Куда: ")
        while True:
            try:
                d = int(input("Расстояние: "))
                if d <= 0: raise ValueError()
                routes[(a, b)] = routes[(b, a)] = d
                print("Маршрут добавлен"); break
            except ValueError: print("Введите целое положительное число")
print('Приветвуем в приложении логистической компании PUTI')
while True:
    print("\n1. Показать пути и города\n2. Найти путь\n3. Добавить город или путь\n4. Кратчайшие пути от города\n5. Выход")
    c = input("Выбор: ")
    if c == '1': show_routes()
    elif c == '2':
        show_cities()
        start = get_city("Откуда: ")
        end = get_city("Куда: ")
        deikstra(start, end)
    elif c == '3': add()
    elif c == '4':
        show_cities()
        start = get_city("Откуда: ")
        deikstra(start)
    elif c == '5': print("До свидания"); break
    else: print("Неверный ввод")