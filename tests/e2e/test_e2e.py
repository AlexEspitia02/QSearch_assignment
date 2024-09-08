import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class E2ETestCase(unittest.TestCase):

    def setUp(self):
        # 使用 Chrome 瀏覽器
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:5000/login")  # 替換成你的伺服器 URL

    def test_login_and_generate_image(self):
        driver = self.driver
        
        # 測試登入
        username_input = driver.find_element(By.ID, 'username')
        password_input = driver.find_element(By.ID, 'password')
        username_input.send_keys("user1")
        password_input.send_keys("password1")
        password_input.send_keys(Keys.RETURN)

        # 驗證登入後是否成功跳轉到首頁
        self.assertIn("Welcome", driver.page_source)

        # 測試生成圖片
        width_input = driver.find_element(By.ID, 'width')
        height_input = driver.find_element(By.ID, 'height')
        width_input.clear()
        width_input.send_keys("150")
        height_input.clear()
        height_input.send_keys("150")
        
        submit_btn = driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_btn.click()

        # 驗證圖片生成成功
        self.assertTrue("/image" in driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
