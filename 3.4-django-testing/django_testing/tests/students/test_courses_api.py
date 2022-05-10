import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def api_url():
    return "/api/v1/courses/"


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_single_course(api_url, client, courses_factory):
    courses = courses_factory(_quantity=1)
    course = courses[0]
    response = client.get(api_url, data={"id": course.id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["id"] == course.id


@pytest.mark.django_db
def test_get_courses_list(api_url, client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.get(api_url)
    assert response.status_code == 200
    data = response.json()
    for index, item in enumerate(data):
        assert item["id"] == courses[index].id


@pytest.mark.django_db
def test_get_courses_filter_by_id(api_url, client, courses_factory):
    courses = courses_factory(_quantity=10)
    course = courses[5]
    response = client.get(api_url, data={"id": course.id})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == course.id


@pytest.mark.django_db
def test_get_courses_filter_by_name(api_url, client, courses_factory):
    courses = courses_factory(_quantity=10)
    course = courses[7]
    response = client.get(api_url, data={"name": course.name})
    assert response.status_code == 200
    data = response.json()
    for item in data:
        assert course.name in item["name"]


@pytest.mark.django_db
def test_course_create(api_url, client):
    count = Course.objects.count()
    response = client.post(api_url, data={"name": "test"})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_course_update(api_url, client, courses_factory):
    courses = courses_factory(_quantity=10)
    count = Course.objects.count()
    course = courses[7]
    test_name = "test"
    patch_api_url = api_url + f"{course.id}/"
    response = client.patch(patch_api_url, data={"name": test_name})
    assert response.status_code == 200
    assert Course.objects.count() == count

    response = client.get(api_url, data={"id": course.id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == test_name


@pytest.mark.django_db
def test_course_delete(api_url, client, courses_factory):
    courses = courses_factory(_quantity=10)
    count = Course.objects.count()
    course = courses[7]
    delete_api_url = api_url + f"{course.id}/"
    response = client.delete(delete_api_url)
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
