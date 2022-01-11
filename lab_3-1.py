# Author: CRS 01/11/22
def add_foods(lst):
    for x in lst:
        try:
            lst[5] = x
            print(x)
            print("This is your new word.")
        except:
            print("Try again.")
        finally:
            print("Have a good day!")



add_foods(["potatoes", "salsa", "cherries", "banana", "apple"])
add_foods(["naan", "celery", "buckwheat", 7, "clementine"])
add_foods(["cheeseburger", True, "chicken", "rice", "radish"])