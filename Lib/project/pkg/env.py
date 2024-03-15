from dotenv import load_dotenv
import os


load_dotenv()

PORT = os.getenv("PORT")
SUBCLASS_PATH = os.getenv("SUBCLASS_PATH")
FOOD_CLASS_TEST_PATH= os.getenv("FOOD_CLASS_TEST_PATH")