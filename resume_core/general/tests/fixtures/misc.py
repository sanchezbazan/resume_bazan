import pytest
from django.test import override_settings


@pytest.fixture(autouse=True)
def test_settings(settings):
    with override_settings(SECRET_KEY='38sgy2#abmgaqc&+f6cv@1gu%8t8at+b&pxv-s(g@@vg$wl&@9',):
        yield
