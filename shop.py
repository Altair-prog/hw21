from base_storage import Storage


class Shop(Storage):
    quantity = 0
    items = dict({'печенька': 5, 'собачка': 4, 'ель': 2, 'сосна': 6, 'кот': 1})
    capacity = 20

    def add(self, title, quantity):
        """
            Добавление товара в юнит
        """
        if self.items.get(title):
            self.items[title] = self.items[title] + quantity
        else:
            self.items[title] = quantity

    def remove(self, title, quantity):
        """
            Удаление товара из юнита
        """
        if self.items.get(title):
            self.items[title] -= quantity

    def get_free_space(self):
        """
            Получение свободного места в юните
        """
        free_space = self.capacity - sum(self.items.values())
        return free_space

    def get_items(self):
        """
            Получение всех товаров и количества в юните. Словарь
        """
        return self.items

    def get_unique_items_count(self):
        """
            Проверка количества уникальных товаров юните
        """
        if len(self.items) < 5:
            return True
