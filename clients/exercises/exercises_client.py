from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    UpdateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    GetExerciseResponseSchema,
)
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserSchema,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
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

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с данными для создания упражнения (см. `CreateExerciseRequestDict`).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с данными для обновления упражнения (см. `UpdateExerciseRequestDict`).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercises_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения упражнения с автоматической обработкой ответа.

        :param exercises_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде словаря с данными упражнения.
        """
        response = self.get_exercise_api(exercises_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self, query: GetExercisesQuerySchema
    ) -> GetExercisesResponseSchema:
        """
        Метод получения списка упражнений с автоматической обработкой ответа.

        :param query: Словарь с courseId для фильтрации упражнений.
        :return: Ответ от сервера в виде словаря со списком упражнений.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        """
        Метод создания упражнения с автоматической обработкой ответа.

        :param request: Словарь с данными для создания упражнения
            (title, courseId, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде словаря с созданным упражнением.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self, exercises_id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Метод обновления упражнения с автоматической обработкой ответа.

        :param exercises_id: Идентификатор упражнения для обновления.
        :param request: Словарь с обновляемыми полями упражнения
            (title, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде словаря с обновленным упражнением.
        """
        response = self.update_exercise_api(exercises_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
