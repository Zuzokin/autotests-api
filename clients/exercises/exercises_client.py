from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """

    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка упражнений.
    """

    exercises: list[Exercise]


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """

    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание упражнения.
    """

    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения.
    """

    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление упражнения.
    """

    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercises_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercises_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с данными для создания упражнения (см. `CreateExerciseRequestDict`).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с данными для обновления упражнения (см. `UpdateExerciseRequestDict`).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercises_id: str) -> GetExerciseResponseDict:
        """
        Метод получения упражнения с автоматической обработкой ответа.

        :param exercises_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде словаря с данными упражнения.
        :raises: httpx.HTTPStatusError: В случае ошибки HTTP-запроса.
        """
        response = self.get_exercise_api(exercises_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения списка упражнений с автоматической обработкой ответа.

        :param query: Словарь с courseId для фильтрации упражнений.
        :return: Ответ от сервера в виде словаря со списком упражнений.
        :raises: httpx.HTTPStatusError: В случае ошибки HTTP-запроса.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(
        self, request: CreateExerciseRequestDict
    ) -> CreateExerciseResponseDict:
        """
        Метод создания упражнения с автоматической обработкой ответа.

        :param request: Словарь с данными для создания упражнения
            (title, courseId, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде словаря с созданным упражнением.
        :raises: httpx.HTTPStatusError: В случае ошибки HTTP-запроса.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
        self, exercises_id: str, request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Метод обновления упражнения с автоматической обработкой ответа.

        :param exercises_id: Идентификатор упражнения для обновления.
        :param request: Словарь с обновляемыми полями упражнения
            (title, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде словаря с обновленным упражнением.
        :raises: httpx.HTTPStatusError: В случае ошибки HTTP-запроса.
        """
        response = self.update_exercise_api(exercises_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
