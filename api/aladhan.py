import httpx


class AladhanAPI:
    URL = "https://api.aladhan.com/v1"

    @staticmethod
    async def get_prayer_times_by_city(
        date: str, city: str, country: str, method: int = 3, school: int = 1
    ):
        """
        Получает время намаза для определенного города.
        
        :param date: Дата в формате "DD.MM.YYYY" ("01.12.2024").
        :param city: Название города на латинице(например, "Moscow").
        :param country: Название страны по ISO 3166 A-2(например, "RU").
        :param method: Метод расчёта времени намаза (по умолчанию 3 — Всемирная исламская лига).
                    Возможные значения: [0-21, 99]
        :param school: Мазхаб (по умолчанию 1 — Ханафитский).
                    Возможные значения: [0, 1]
        :return: Словарь (dict) с результатом, содержащим информацию о времени намаза.
                Подробнее читайте в документации
        :raises httpx.RequestError: Если запрос к API не удался (например, сеть недоступна).
        :raises httpx.HTTPStatusError: Если сервер вернул HTTP-ошибку (например, 404, 500).
        """
        path = AladhanAPI.URL + f"/timingsByCity/{date}"
        params = {"city": city, "country": country, "method": method, "school": school}

        async with httpx.AsyncClient() as client:
            response = await client.get(path, params=params)
            response.raise_for_status()
            return response.json()
