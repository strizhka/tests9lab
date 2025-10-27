class Calculator:
    def add(self, a, b):
        """Сумма"""
        return a + b

    def divide(self, a, b):
        """Деление"""
        if b == 0:
            raise ValueError("дырка от бублика")
        return a / b

    def is_prime_number(self, n):
        """Проверка простого числа"""
        if not isinstance(n, int):
            raise TypeError("нужно число целое")
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True