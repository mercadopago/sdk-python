"""Payment Additional Info resource for Mercado Pago SDK."""

from mercadopago.sdk import MPBase


class PaymentAdditionalInfo(MPBase):
    """
    Payment Additional Info resource.
    
    Used for providing additional information for fraud scoring and payment processing.
    Includes items, payer information, and shipment details.
    """

    def __init__(self, client):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            client: Mercado Pago client instance
        """
        super().__init__(client)
        self._resource_name = "payment_additional_info"

    @staticmethod
    def create_item(id=None, title=None, description=None, picture_url=None,
                   category_id=None, quantity=None, unit_price=None):
        """
        Create a payment item dictionary.
        
        Args:
            id (str, optional): Item identifier
            title (str, optional): Item title
            description (str, optional): Item description
            picture_url (str, optional): Item picture URL
            category_id (str, optional): Item category identifier
            quantity (int, optional): Item quantity
            unit_price (float, optional): Unit price of the item
            
        Returns:
            dict: Payment item data
        """
        item = {}
        
        if id is not None:
            item["id"] = id
        if title is not None:
            item["title"] = title
        if description is not None:
            item["description"] = description
        if picture_url is not None:
            item["picture_url"] = picture_url
        if category_id is not None:
            item["category_id"] = category_id
        if quantity is not None:
            item["quantity"] = quantity
        if unit_price is not None:
            item["unit_price"] = unit_price
            
        return item

    @staticmethod
    def create_payer_info(first_name=None, last_name=None, phone=None, 
                         address=None):
        """
        Create payer information dictionary.
        
        Args:
            first_name (str, optional): Payer's first name
            last_name (str, optional): Payer's last name
            phone (dict, optional): Phone information (area_code, number)
            address (dict, optional): Address information (zip_code, street_name, 
                                     street_number)
            
        Returns:
            dict: Payer information data
        """
        payer = {}
        
        if first_name is not None:
            payer["first_name"] = first_name
        if last_name is not None:
            payer["last_name"] = last_name
        if phone is not None:
            payer["phone"] = phone
        if address is not None:
            payer["address"] = address
            
        return payer

    @staticmethod
    def create_phone(area_code=None, number=None):
        """
        Create phone information dictionary.
        
        Args:
            area_code (str, optional): Phone area code
            number (str, optional): Phone number
            
        Returns:
            dict: Phone information data
        """
        phone = {}
        
        if area_code is not None:
            phone["area_code"] = area_code
        if number is not None:
            phone["number"] = number
            
        return phone

    @staticmethod
    def create_address(zip_code=None, street_name=None, street_number=None):
        """
        Create address information dictionary.
        
        Args:
            zip_code (str, optional): Address zip code
            street_name (str, optional): Street name
            street_number (str, optional): Street number
            
        Returns:
            dict: Address information data
        """
        address = {}
        
        if zip_code is not None:
            address["zip_code"] = zip_code
        if street_name is not None:
            address["street_name"] = street_name
        if street_number is not None:
            address["street_number"] = street_number
            
        return address

    @staticmethod
    def create_shipments(receiver_address=None):
        """
        Create shipments information dictionary.
        
        Args:
            receiver_address (dict, optional): Receiver address information 
                                              (zip_code, street_name, street_number,
                                              floor, apartment)
            
        Returns:
            dict: Shipments information data
        """
        shipments = {}
        
        if receiver_address is not None:
            shipments["receiver_address"] = receiver_address
            
        return shipments

    @staticmethod
    def create_receiver_address(zip_code=None, street_name=None, 
                               street_number=None, floor=None, apartment=None):
        """
        Create receiver address information dictionary.
        
        Args:
            zip_code (str, optional): Address zip code
            street_name (str, optional): Street name
            street_number (str, optional): Street number
            floor (str, optional): Floor number
            apartment (str, optional): Apartment number
            
        Returns:
            dict: Receiver address information data
        """
        address = {}
        
        if zip_code is not None:
            address["zip_code"] = zip_code
        if street_name is not None:
            address["street_name"] = street_name
        if street_number is not None:
            address["street_number"] = street_number
        if floor is not None:
            address["floor"] = floor
        if apartment is not None:
            address["apartment"] = apartment
            
        return address

    @staticmethod
    def create_additional_info(items=None, payer=None, shipments=None):
        """
        Create complete additional info dictionary for payment.
        
        Args:
            items (list, optional): List of payment items
            payer (dict, optional): Payer information
            shipments (dict, optional): Shipments information
            
        Returns:
            dict: Complete additional info data structure
        """
        additional_info = {}
        
        if items is not None:
            additional_info["items"] = items
        if payer is not None:
            additional_info["payer"] = payer
        if shipments is not None:
            additional_info["shipments"] = shipments
            
        return additional_info

    def validate_additional_info(self, additional_info):
        """
        Validate additional info structure.
        
        Args:
            additional_info (dict): Additional info to validate
            
        Returns:
            tuple: (is_valid, errors) where is_valid is bool and errors is list of str
        """
        errors = []
        
        if not isinstance(additional_info, dict):
            errors.append("additional_info must be a dictionary")
            return False, errors
        
        # Validate items
        if "items" in additional_info:
            if not isinstance(additional_info["items"], list):
                errors.append("items must be a list")
            else:
                for idx, item in enumerate(additional_info["items"]):
                    if not isinstance(item, dict):
                        errors.append(f"item at index {idx} must be a dictionary")
        
        # Validate payer
        if "payer" in additional_info:
            if not isinstance(additional_info["payer"], dict):
                errors.append("payer must be a dictionary")
            else:
                payer = additional_info["payer"]
                if "phone" in payer and not isinstance(payer["phone"], dict):
                    errors.append("payer.phone must be a dictionary")
                if "address" in payer and not isinstance(payer["address"], dict):
                    errors.append("payer.address must be a dictionary")
        
        # Validate shipments
        if "shipments" in additional_info:
            if not isinstance(additional_info["shipments"], dict):
                errors.append("shipments must be a dictionary")
            else:
                shipments = additional_info["shipments"]
                if "receiver_address" in shipments and not isinstance(shipments["receiver_address"], dict):
                    errors.append("shipments.receiver_address must be a dictionary")
        
        return len(errors) == 0, errors