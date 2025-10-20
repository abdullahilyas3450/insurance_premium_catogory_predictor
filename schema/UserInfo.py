from pydantic import BaseModel,Field, computed_field, field_validator
from typing import Annotated, Literal, Optional
from config.city_tiers import tier_1_cities, tier_2_cities


class UserInfo(BaseModel):
    age:Annotated[int, Field(...,gt=0, lt=120, description="Age must be between 1 and 119")]
    weight:Annotated[float, Field(...,gt=0, lt=635, description="Weight must be between 1 and 635 kg")]
    height:Annotated[float, Field(...,gt=0, lt=3, description="Height must be between 1 and 3 mtrs")]
    income_lpa:Annotated[float, Field(...,gt=0, description="Income")]
    smoker:Annotated[bool, Field(..., description="Is the user a smoker? Ture or false")]
    city:Annotated[str, Field(..., description="City name")]
    occupation:Annotated[Literal["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job"], Field(..., description="Occupation type")]

    @field_validator('city')
    @classmethod
    def city_name_to_title(cls, v):
        return v.strip().title()


    @computed_field
    @property       
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
        
    @computed_field
    @property   
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return 'senior'
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3