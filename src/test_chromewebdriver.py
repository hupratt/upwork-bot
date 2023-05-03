import pytest
import sys
from time import sleep
from selenium.webdriver.common.by import By


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium

@pytest.mark.nondestructive
def test_nondestructive(selenium):
    selenium.get('http://www.example.com')

def test_lambdatest_todo_app(selenium):
    
    selenium.get('https://lambdatest.github.io/sample-todo-app/')
 
    selenium.find_element(By.NAME,"li1").click()
    selenium.find_element(By.NAME,"li2").click()
 
    title = "Sample page - lambdatest.com"
    assert title == selenium.title
 
    sample_text = "Happy Testing at LambdaTest"
    email_text_field = selenium.find_element(By.ID,"sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)
 
    selenium.find_element(By.ID,"addbutton").click()
    sleep(5)
 
    output_str = selenium.find_element(By.NAME,"li6").text
    sys.stderr.write(output_str)
    
    sleep(2)
    selenium.close()