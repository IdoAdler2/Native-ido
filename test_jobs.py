import pytest


@pytest.mark.usefixtures("create_driver_after_login")
class Test_job:

    def test_create_job(self):
        self.workiz_app.create_job_from_plus_button()
        assert 1 == 1
