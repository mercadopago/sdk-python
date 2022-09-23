"""
    Module: plan
"""
from mercadopago.core import MPBase


class Plan(MPBase):
    """
    This class provides the methods to access the API that will allow you to create, search, get and update Plans to be
    used as templates for Subscriptions.

    [Click here for more info](https://www.mercadopago.com.br/developers/en/docs/subscriptions/integration-configuration/subscriptions-associated-plan)  # pylint: disable=line-too-long
    """

    def search(self, filters=None, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_plan_search/get)  # pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Plans found
        """
        return self._get(
            uri="/preapproval_plan/search",
            filters=filters,
            request_options=request_options)

    def get(self, plan_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_plan_id/get)  # pylint: disable=line-too-long

        Args:
            plan_id (str): The plan ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Plan found
        """
        return self._get(
            uri="/preapproval_plan/" + str(plan_id),
            request_options=request_options)

    def create(self, plan_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_plan/post)  # pylint: disable=line-too-long

        Args:
            plan_object (dict): Plan to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param plan_object must be a Dictionary

        Returns:
            dict: Plan creation response
        """
        if not isinstance(plan_object, dict):
            raise ValueError("Param plan_object must be a Dictionary")

        return self._post(
            uri="/preapproval_plan",
            data=plan_object,
            request_options=request_options)

    def update(self, plan_id, plan_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_plan_id/put)  # pylint: disable=line-too-long

        Args:
            plan_id (str): The plan ID to be updated
            plan_object (dict): Plan information to be updated
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param plan_object must be a Dictionary

        Returns:
            dict: Plan modification response
        """
        if not isinstance(plan_object, dict):
            raise ValueError("Param plan_object must be a Dictionary")

        return self._put(
            uri="/preapproval_plan/" + str(plan_id),
            data=plan_object,
            request_options=request_options)
