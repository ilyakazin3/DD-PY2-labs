class Automobile:
    """
    Базовый класс для автомобилей.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует объект класса Automobile.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
        """
        self._brand: str = brand       # Скрытый атрибут для инкапсуляции данных
        self._model: str = model       # Скрытый атрибут для инкапсуляции данных
        self._year: int = year         # Год выпуска автомобиля

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Год выпуска должен быть положительным целым числом.")
        self._year = value


    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        Возвращает:
            str: Строка с информацией об автомобиле.
        """
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление автомобиля.

        Возвращает:
            str: Детальное строковое представление объекта.
        """
        return f"Automobile(brand={self._brand!r}, model={self._model!r}, year={self._year!r})"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Возвращает:
            str: Сообщение о запуске двигателя.
        """
        return "Двигатель запущен"


class PassengerCar(Automobile):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
        passenger_capacity (int): Количество пассажиров, которое может перевозить автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int) -> None:
        """
        Инициализирует объект класса PassengerCar.

        Расширяет конструктор базового класса Automobile, добавляя атрибут passenger_capacity.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            passenger_capacity (int): Вместимость автомобиля по количеству пассажиров.
        """
        super().__init__(brand, model, year)
        self.passenger_capacity: int = passenger_capacity

    @property
    def passenger_capacity(self) -> int:
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество пассажиров должно быть положительным целым числом.")
        self._passenger_capacity = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        Расширяет функциональность базового метода __str__, добавляя информацию о пассажирской вместимости.

        Возвращает:
            str: Строка с информацией о легковом автомобиле.
        """
        base_str: str = super().__str__()
        return f"{base_str}, пассажиров: {self.passenger_capacity}"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление легкового автомобиля.

        Расширяет функциональность базового метода __repr__, добавляя информацию о пассажирской вместимости.

        Возвращает:
            str: Детальное строковое представление объекта.
        """
        base_repr: str = super().__repr__()
        return f"{base_repr[:-1]}, passenger_capacity={self.passenger_capacity!r})"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        Перегружен метод start_engine базового класса для учета специфики легкового автомобиля,
        например, проверки систем безопасности перед запуском двигателя.

        Возвращает:
            str: Сообщение о запуске двигателя легкового автомобиля.
        """
        safety_check: bool = True
        if safety_check:
            return f"Двигатель легкового автомобиля {self._brand} запущен с учетом систем безопасности"
        else:
            return f"Невозможно запустить двигатель легкового автомобиля {self._brand} из-за проблем с безопасностью"

    def open_trunk(self) -> str:
        """
        Открывает багажник автомобиля.

        Возвращает:
            str: Сообщение о том, что багажник открыт.
        """
        return "Багажник открыт"


class Truck(Automobile):
    """
    Дочерний класс для грузовых автомобилей.

    Атрибуты:
        cargo_capacity (float): Грузоподъемность автомобиля в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, cargo_capacity: float) -> None:
        """
        Инициализирует объект класса Truck.

        Расширяет конструктор базового класса Automobile, добавляя атрибут cargo_capacity.

        Аргументы:
            brand (str): Марка грузового автомобиля.
            model (str): Модель грузового автомобиля.
            year (int): Год выпуска автомобиля.
            cargo_capacity (float): Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(brand, model, year)
        self.cargo_capacity: float = cargo_capacity

    @property
    def cargo_capacity(self) -> float:
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, value) -> None:
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        self._cargo_capacity = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        Расширяет функциональность базового метода __str__, добавляя информацию о грузоподъемности.

        Возвращает:
            str: Строка с информацией о грузовом автомобиле.
        """
        base_str: str = super().__str__()
        return f"{base_str}, грузоподъемность: {self.cargo_capacity} тонн"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление грузового автомобиля.

        Расширяет функциональность базового метода __repr__, добавляя информацию о грузоподъемности.

        Возвращает:
            str: Детальное строковое представление объекта.
        """
        base_repr: str = super().__repr__()
        return f"{base_repr[:-1]}, cargo_capacity={self.cargo_capacity!r})"

    def start_engine(self) -> str:
        """
        Запускает двигатель грузового автомобиля.

        Перегружен метод start_engine базового класса для учета специфики грузового автомобиля,
        например, необходимости предварительной проверки системы охлаждения.

        Возвращает:
            str: Сообщение о запуске двигателя грузового автомобиля.
        """
        cooling_system_ok: bool = True
        if cooling_system_ok:
            return f"Двигатель грузового автомобиля {self._brand} запущен после проверки системы охлаждения"
        else:
            return f"Запуск двигателя грузового автомобиля {self._brand} невозможен из-за проблем с охлаждением"

    def load_cargo(self, weight: float) -> str:
        """
        Загружает груз в автомобиль.

        Аргументы:
            weight (float): Вес груза, который необходимо загрузить (в тоннах).

        Возвращает:
            str: Сообщение о результате загрузки.
        """
        if weight <= self.cargo_capacity:
            return f"Груз весом {weight} тонн успешно загружен."
        else:
            return f"Невозможно загрузить груз весом {weight} тонн. Превышена грузоподъемность в {self.cargo_capacity} тонн."


class ElectricCar(Automobile):
    """
    Дочерний класс для электромобилей.

    Атрибуты:
        battery_capacity (float): Емкость батареи автомобиля в киловатт-часах (kWh).
        charge_level (float): Текущий уровень заряда батареи в процентах.
    """

    def __init__(self, brand: str, model: str, year: int, battery_capacity: float, charge_level: float = 100.0) -> None:
        """
        Инициализирует объект класса ElectricCar.

        Расширяет конструктор базового класса Automobile, добавляя атрибуты, специфичные для электромобилей.

        Аргументы:
            brand (str): Марка электромобиля.
            model (str): Модель электромобиля.
            year (int): Год выпуска автомобиля.
            battery_capacity (float): Емкость батареи в kWh.
            charge_level (float): Текущий уровень заряда батареи (по умолчанию 100.0%).
        """
        super().__init__(brand, model, year)
        self.battery_capacity: float = battery_capacity
        self.charge_level: float = charge_level

    @property
    def charge_level(self) -> float:
        return self._charge_level

    @charge_level.setter
    def charge_level(self, value) -> None:
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Уровень заряда батареии должна быть положительным числом.")
        self._charge_level = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление электромобиля.

        Расширяет функциональность базового метода __str__, добавляя информацию о заряде батареи.

        Возвращает:
            str: Строка с информацией об электромобиле.
        """
        base_str: str = super().__str__()
        return f"{base_str}, заряд батареи: {self.charge_level}%"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление электромобиля.

        Расширяет функциональность базового метода __repr__, добавляя информацию о батарее.

        Возвращает:
            str: Детальное строковое представление объекта.
        """
        base_repr: str = super().__repr__()
        return (f"{base_repr[:-1]}, battery_capacity={self.battery_capacity!r}, "
                f"charge_level={self.charge_level!r})")

    def start_engine(self) -> str:
        """
        Запускает двигатель электромобиля.

        Перегружен метод start_engine базового класса, так как электромобили не используют традиционный двигатель внутреннего сгорания.

        Возвращает:
            str: Сообщение о запуске электромобиля.
        """
        if self.charge_level > 20:
            return f"Электромобиль {self._brand} готов к поездке. Заряд батареи достаточен."
        else:
            return f"Электромобиль {self._brand} не готов к поездке. Низкий уровень заряда батареи."

    def recharge(self, amount: float) -> str:
        """
        Заряжает батарею электромобиля.

        Аргументы:
            amount (float): Процент заряда, который необходимо добавить.

        Возвращает:
            str: Сообщение о результате зарядки.
        """
        new_charge = self.charge_level + amount
        if new_charge > 100:
            self.charge_level = 100.0
        else:
            self.charge_level = new_charge
        return f"Электромобиль {self._brand} заряжен до {self.charge_level}%."


if __name__ == "__main__":
    # Базовый автомобиль
    auto = Automobile("Generic", "ModelX", 2020)
    print(auto)
    print(repr(auto))
    print(auto.start_engine())
    print()

    # Легковой автомобиль
    car = PassengerCar("Toyota", "Camry", 2021, 5)
    print(car)
    print(repr(car))
    print(car.start_engine())
    print(car.open_trunk())
    print()

    # Грузовой автомобиль
    truck = Truck("Volvo", "FH16", 2019, 25.0)
    print(truck)
    print(repr(truck))
    print(truck.start_engine())
    print(truck.load_cargo(20.0))
    print(truck.load_cargo(30.0))
    print()

    # Электромобиль
    e_car = ElectricCar("Tesla", "Model S", 2022, 100.0, 50.0)
    print(e_car)
    print(repr(e_car))
    print(e_car.start_engine())
    print(e_car.recharge(30.0))
    print(e_car.recharge(30.0))
