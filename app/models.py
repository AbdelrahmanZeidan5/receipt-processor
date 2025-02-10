from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime
import re

class Item(BaseModel):
    """Represents an item on the receipt."""
    shortDescription: str = Field(..., min_length=1)
    price: str = Field(...)

    @validator('shortDescription')
    def description_not_empty(cls, v):
        """Ensures the short description is not empty or whitespace."""
        if not v.strip():
            raise ValueError('shortDescription cannot be empty or whitespace')
        return v
    
    @validator('price')
    def valid_price(cls, v):
        """Validates price is in XX.XX format."""
        if not re.fullmatch(r'^\d+\.\d{2}$', v):
            raise ValueError('Price must be in XX.XX format')
        return v

class Receipt(BaseModel):
    """Represents a receipt with multiple items."""
    retailer: str = Field(..., min_length=1)
    purchaseDate: str
    purchaseTime: str = Field(...)
    items: List[Item]
    total: str = Field(...)

    @validator('retailer')
    def retailer_not_empty(cls, v):
        """Ensures the retailer name is not empty or whitespace."""
        if not v.strip():
            raise ValueError('Retailer cannot be empty or whitespace')
        return v

    @validator('purchaseDate')
    def valid_date(cls, v):
        """Validates and formats the purchase date."""
        date_formats = ["%Y-%m-%d", "%Y/%m/%d"]
        for date_format in date_formats:
            try:
                parsed_date = datetime.strptime(v, date_format)
                return parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                continue
        raise ValueError('purchaseDate must be a valid date in YYYY-MM-DD or YYYY/MM/DD format')


    @validator('purchaseTime')
    def valid_time(cls, v):
        """Validates the purchase time: 24-hour format (HH:MM)"""
        try:
            datetime.strptime(v, "%H:%M") 
        except ValueError:
            raise ValueError('purchaseTime must be a valid time in HH:MM format')
        return v


    @validator('total')
    def valid_total(cls, v):
        """Validates total is in XX.XX format."""
        if not re.fullmatch(r'^\d+\.\d{2}$', v):
            raise ValueError('Total must be in XX.XX format')
        return v