class Jar:
    def __init__(self):
        self.components = {}
    
    def add(self, juice_type, amount):
        if amount <= 0:
            raise ValueError("Количество сока должно быть положительным")
        
        if juice_type in self.components:
            self.components[juice_type] += amount
        else:
            self.components[juice_type] = amount
    
    def pour_out(self, amount):
        if amount <= 0:
            raise ValueError("Количество для выливания должно быть положительным")
        
        total_volume = self.get_total_volume()
        
        if amount > total_volume:
            amount = total_volume  # Фикс если введенное количество больше всего количества которе есть
        
        # копия словаря компонентов
        components_copy = self.components.copy()
        
        # Выливаем сок пропорционально каждому компоненту
        for juice_type, juice_amount in components_copy.items():
            proportion = juice_amount / total_volume
            amount_to_pour = proportion * amount
            self.components[juice_type] -= amount_to_pour
            
            # Удаляем компонент, если его количество стало нулевым
            if self.components[juice_type] <= 0.0001:  # Фикс погрешности вычислений
                del self.components[juice_type]
    
    def get_total_volume(self):
        return sum(self.components.values())
    
    def get_concentrations(self):
        # Получить концентрации всех компонентов в миксе
        total_volume = self.get_total_volume()
        if total_volume == 0:
            return {}
        
        concentrations = {}
        for juice_type, juice_amount in self.components.items():
            concentrations[juice_type] = juice_amount / total_volume
        
        return concentrations
    
    def __str__(self):
        # Вывод всего содержимого (сока)
        total = self.get_total_volume()
        concentrations = self.get_concentrations()
        
        result = f"Общее количество сока: {total:.2f} мл\n"
        result += "Компоненты:\n"
        
        for juice_type, juice_amount in self.components.items():
            concentration = concentrations.get(juice_type, 0) * 100
            result += f"  - {juice_type}: {juice_amount:.2f} мл ({concentration:.1f}%)\n"
        
        return result


# Пример использования
if __name__ == "__main__":
    jar = Jar()
    
    # Наливаем разные соки
    jar.add("апельсиновый ", 200)
    jar.add("яблочный", 300)
    jar.add("виноградный", 100)
    
    print("После добавления соков: ")
    print(jar)
    
    # Выливаем часть сока
    jar.pour_out(150)
    print("После выливания 150 мл: ")
    print(jar)
    
    # Добавляем еще сок
    jar.add("апельсиновый", 100)
    print("После добавления 100 мл апельсинового сока: ")
    print(jar)
    
    # Получаем концентрации отдельно
    concentrations = jar.get_concentrations()
    print("Концентрации компонентов:")
    for juice_type, concentration in concentrations.items():
        print(f"  {juice_type}: {concentration*100:.1f}%")

