from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestAboutUsCreateAPITestCase(APITestCase):
    def setUp(self):
        self.data = {
            'name': 'Мы компания Кодифай',
            'description': 'CODIFY - это уникальная площадка в IT, целью которой является объединить классных айтишников, влюбленных в свое дело, и всех людей, готовых учиться. Идея создания платформы пришла к людям, которые являются действующими профессионалами с многолетним опытом менторства и взращивания специалистов. Цель CodifyLab поддерживать учащихся на всех этапах, будь это изменение сферы деятельности, поиск продвижения по службе или поиск новых интересов, Codify предлагает курсы для любопытных умов по различным направлениям - от основ программирования и информатики до лидерства и коммуникаций.'
        }

        self.url = reverse('about-us-list-create')
#
    def test_create_about_us_success(self):
        response = self.client.post(
            path=self.url,
            data=self.data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_data = {'message': 'Успешно добавлено'}
        self.assertEqual(response.data, expected_data)

    # def test_create_dish_via_get_405(self):
    #     response = self.client.get(
    #         path=self.url,
    #         data=self.data
    #     )
    #
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #     expected_data = {"detail": "Method \"GET\" not allowed."}
    #     self.assertEqual(response.data, expected_data)
    #
    # def test_create_dish_without_data_400(self):
    #     response = self.client.post(
    #         path=self.url,
    #         data={"name": "Test"}
    #     )
    #
    #     expected_data = {
    #         "price": [
    #             "This field is required."
    #         ],
    #     }
    #
    #     self.assertEqual(response.data, expected_data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class AboutUsListViewAPITestCase(APITestCase):
#     def test_get_about_us_list_success(self):
#         url = reverse('about-us-list-create')
#         response = self.client.get(url)
#         self.assertEqual((response.status_code, 200))
#         self.assertIsInstance(response.data, list)