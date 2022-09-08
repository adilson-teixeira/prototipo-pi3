import pytest
from django.urls import resolve, reverse

from .factories import TreeFactory

pytestmark = pytest.mark.django_db



class TestTreeListView:
    def test_reverse_resolve(self):
        assert reverse("trees:list") == "/trees/"
        assert resolve("/trees/").view_name == "trees:list"

        url = reverse("trees:list_by_square", kwargs={"slug": "test-slug"})
        assert url == "/trees/square/test-slug/"

        view_name = resolve("/trees/square/test-slug/").view_name
        assert view_name == "trees:list_by_square"

    def test_status_code(self, client, square):
        response = client.get(reverse("trees:list"))
        assert response.status_code == 200

        response = client.get(
            reverse("trees:list_by_square", kwargs={"slug": square.slug})
        )
        assert response.status_code == 200


class TestTreeDetailView:
    def test_reverse_resolve(self, tree):
        url = reverse("trees:detail", kwargs={"slug": tree.slug})
        assert url == f"/trees/{tree.slug}/"

        view_name = resolve(f"/trees/{tree.slug}/").view_name
        assert view_name == "trees:detail"

    def test_status_code(self, client):
        trees = TreeFactory(is_display=True)
        url = reverse("trees:detail", kwargs={"slug": trees.slug})
        response = client.get(url)
        assert response.status_code == 200