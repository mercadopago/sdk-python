from mercadopago.http import HttpClient
from mercadopago.config import RequestOptions
from typing import Any, Dict, Optional


class PaymentItem:
    """
    PaymentItem model representing an item in a payment transaction.
    
    Attributes:
        id (str, optional): Item identifier
        title (str, optional): Item title
        description (str, optional): Item description
        category_id (str, optional): Category identifier
        quantity (int, optional): Item quantity
        unit_price (float, optional): Unit price of the item
    """

    def __init__(self, client: HttpClient):
        """
        Initialize PaymentItem resource.
        
        Args:
            client: HttpClient instance for making API requests
        """
        self.client = client

    def create(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None,
        request_options: Optional[RequestOptions] = None
    ) -> Dict[str, Any]:
        """
        Create a payment item.
        
        Args:
            id: Item identifier
            title: Item title
            description: Item description
            category_id: Category identifier
            quantity: Item quantity
            unit_price: Unit price of the item
            request_options: Optional request configuration
            
        Returns:
            Dict containing the created payment item data
        """
        data = {}
        
        if id is not None:
            data['id'] = id
        if title is not None:
            data['title'] = title
        if description is not None:
            data['description'] = description
        if category_id is not None:
            data['category_id'] = category_id
        if quantity is not None:
            data['quantity'] = quantity
        if unit_price is not None:
            data['unit_price'] = unit_price
        
        response = self.client.post('/v1/payment_items', data=data, request_options=request_options)
        return response

    def get(self, item_id: str, request_options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """
        Get a payment item by ID.
        
        Args:
            item_id: The payment item identifier
            request_options: Optional request configuration
            
        Returns:
            Dict containing the payment item data
        """
        response = self.client.get(f'/v1/payment_items/{item_id}', request_options=request_options)
        return response

    def update(
        self,
        item_id: str,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None,
        request_options: Optional[RequestOptions] = None
    ) -> Dict[str, Any]:
        """
        Update a payment item.
        
        Args:
            item_id: The payment item identifier to update
            id: Item identifier
            title: Item title
            description: Item description
            category_id: Category identifier
            quantity: Item quantity
            unit_price: Unit price of the item
            request_options: Optional request configuration
            
        Returns:
            Dict containing the updated payment item data
        """
        data = {}
        
        if id is not None:
            data['id'] = id
        if title is not None:
            data['title'] = title
        if description is not None:
            data['description'] = description
        if category_id is not None:
            data['category_id'] = category_id
        if quantity is not None:
            data['quantity'] = quantity
        if unit_price is not None:
            data['unit_price'] = unit_price
        
        response = self.client.put(f'/v1/payment_items/{item_id}', data=data, request_options=request_options)
        return response

    def delete(self, item_id: str, request_options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """
        Delete a payment item.
        
        Args:
            item_id: The payment item identifier to delete
            request_options: Optional request configuration
            
        Returns:
            Dict containing the deletion response
        """
        response = self.client.delete(f'/v1/payment_items/{item_id}', request_options=request_options)
        return response

    def list(self, request_options: Optional[RequestOptions] = None, **params) -> Dict[str, Any]:
        """
        List payment items with optional filters.
        
        Args:
            request_options: Optional request configuration
            **params: Additional query parameters for filtering
            
        Returns:
            Dict containing list of payment items
        """
        response = self.client.get('/v1/payment_items', params=params, request_options=request_options)
        return response