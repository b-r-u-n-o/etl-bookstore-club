
class Book:
    
    def __init__(self, name, category, stars, price, status) -> None:
        self.book_name:str = name
        self.book_category:str = category
        self.book_stars:str = stars
        self.book_price:float = price
        self.book_status:bool = status
    