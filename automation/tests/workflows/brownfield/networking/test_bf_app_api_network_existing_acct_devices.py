import logging
import allure
import pytest
from automation.conftest import ExistingUserAcctDevices

log = logging.getLogger(__name__)

@allure.parent_suite("activate-sm-workflows")
@allure.suite("Brownfield network devices")
@allure.sub_suite("Brownfield existing account existing network devices")
@pytest.mark.Plv
class TestDeviceClaimAppApi:
    @pytest.mark.order(1)
    @pytest.mark.testrail(id=1220654)
    @pytest.mark.Regression
    def test_brnf_sa_order_iap_devices(self, brnf_sa_order_iap_devices):
        """
        ===== Create IAP device on Activate order process ======
        1. Run AOP API manufacturing API to create IAP network device
        """
        assert brnf_sa_order_iap_devices

    @pytest.mark.order(2)
    @pytest.mark.testrail(id=1220654)
    @pytest.mark.Regression
    def test_brnf_app_api_iap_claim(self, brnf_sa_manual_claim_iap_device_app_api,
                                    brnf_app_api_session):
        """
        ===== Manually add IAP into account and verify claim ======
        1. Using the app api session
        2. Manually add IAP into account
        3. Verify the IAP is added/claimed to the account
        """
        test_rail_id = "C1220654"
        if brnf_app_api_session:
            assert brnf_sa_manual_claim_iap_device_app_api