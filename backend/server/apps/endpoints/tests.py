from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "level": 2.0,
            "credits_paid": 0.0,
            "blocked_due_credit_denial": 0.0,
            "credits_in_process": 0.0,
            "credits_active": 0.0,
            "credits_overdue": 1.0,
            "credits_rejected": 0.0,
            "special_client": 0.0,
            "client_status": 0.0,
            "number_fee": 1.0,
            "value_fee": 10.66,
            "capital": 35.0,
            "overdue_to_pay": 0.0,
            "overdue_paid": 0.0,
            "fee_status": 2.0,
        }
        classifier_url = "/api/v1/default_risk_model/predict?status=production&version=1.0"
        response = client.post(classifier_url, input_data, format='json')
        print('RESPONSE',response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)