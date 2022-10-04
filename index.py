from dataclasses import dataclass,field
from pydantic import BaseModel
import uuid
from typing import Any



class Person_w0():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"name {self.name} and age {self.age}"
    def hello(self):
        return (f"hello my name is {self.name} and I am {self.age} years old!")

def gen_id():
    return str(uuid.uuid4())
@dataclass(frozen=False)
class Person_w1():
    name:str
    age:int
    _search_string:str=''
    active: bool = True
    email_list: list[str] = field(default_factory=list)
    id:str = field(default_factory=gen_id,repr=False)
    def hello(self):
        return (f"hello my name is {self.name} and I am {self.age} years old!")
    def __post_init__(self)->None:
        self._search_string = self.name +"search222"
    

class Person_w2(BaseModel):
    name:str
    age:int
    search_string:str=''
    active: bool = True
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__.search_string = __pydantic_self__.name +"search"
    def hello(self):
        return (f"hello my name is {self.name} and I am {self.age} years old!")


if __name__=="__main__":
    person0 = Person_w0(
         name = "nghia",
         age = 10
    )
    print(person0)
    print(person0.hello())
    print('-----------')



    person1 = Person_w1(
         name = "nghia",
         age = 10,
         active=False,
         id = "123"
    )
    print(person1)
    person1.name= 'ly'
    print(person1.hello())
    print(person1.__dict__)
    print('-----------')


    person2 = Person_w2(
         name = "nghia",
         age = 10
    )
    print(person2)
    print(person2.hello())
    print('-----------')