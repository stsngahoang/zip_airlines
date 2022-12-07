import random

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import DefaultAirPlaneFactory


class TestAirplaneView(APITestCase):
    @pytest.mark.django_db
    def setUp(self) -> None:
        super().setUp()
        self.new_airplane = DefaultAirPlaneFactory()

    def test_can_get_list_airplane(self):
        """
        This test ensures that user can get list of airplane
        """
        url = reverse("airplanes-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert len(data["results"]) == 1

    def test_can_get_airplane_detail_by_id(self):
        """
        This test ensures that user can get detail of airplane by id
        """
        url = reverse("airplanes-detail", kwargs={"pk": self.new_airplane.id})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["passengers"] == self.new_airplane.passengers
        assert data["fuel_tanks_capacity"] == self.new_airplane.fuel_tanks_capacity
        assert (
            data["fuel_consumption_per_minutes"]
            == self.new_airplane.fuel_consumption_per_minutes
        )
        assert (
            data["maximum_minutes_able_to_fly"]
            == self.new_airplane.maximum_minutes_able_to_fly
        )

    def test_cant_update_airplane_detail_by_id_with_incorrect_body(self):
        """
        This test ensures that user can update detail of airplane by id
        """
        url = reverse("airplanes-detail", kwargs={"pk": self.new_airplane.id})
        incorrect_data_with_no_body = {}
        response = self.client.put(url, data=incorrect_data_with_no_body)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        incorrect_data_with_passengers_lte_0 = {"passengers": random.randint(-100, 0)}
        response = self.client.put(url, data=incorrect_data_with_passengers_lte_0)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["passengers"] == ["passengers should be greater than 0"]

    def test_can_update_airplane_detail_by_id_with_correct_body(self):
        url = reverse("airplanes-detail", kwargs={"pk": self.new_airplane.id})
        correct_data = {"passengers": random.randint(1, 1000)}
        response = self.client.put(url, data=correct_data)
        assert response.status_code == status.HTTP_200_OK
        self.new_airplane.refresh_from_db()
        data = response.json()
        assert data["id"] == self.new_airplane.id
        assert data["passengers"] == self.new_airplane.passengers
        assert data["fuel_tanks_capacity"] == self.new_airplane.fuel_tanks_capacity

    def test_cant_create_airplane_with_incorrect_body(self):
        url = reverse("airplanes-list")
        correct_data = {"passengers": random.randint(-1000, 0)}
        response = self.client.post(url, data=correct_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["passengers"] == ["passengers should be greater than 0"]

    def test_can_create_airplane_with_correct_body(self):
        url = reverse("airplanes-list")
        correct_data = {"passengers": random.randint(1, 1000)}
        response = self.client.post(url, data=correct_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_can_update_or_create_list_airplane_with_correct_body(self):
        url = reverse("airplanes-create-list-airplane")
        correct_data = {
            "airplanes": [
                {"id": self.new_airplane.id, "passengers": 2000},  # update
                {"passengers": 1000},  # create
            ]
        }
        response = self.client.post(url, data=correct_data, format="json")
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        self.new_airplane.refresh_from_db()
        assert self.new_airplane.passengers == 2000
        assert len(data["data"]) == 2
