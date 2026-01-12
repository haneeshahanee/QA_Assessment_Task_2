from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)

# Step 1: Click Start button
print("Step 1: Clicking Start button")
driver.find_element(By.CSS_SELECTOR, "#start button").click()

# Step 2: Wait for loading bar to disappear
print("Step 2: Waiting for loading")
wait.until(EC.invisibility_of_element_located((By.ID, "loading")))

# Step 3: Wait for Hello World text to appear
hello_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))

# Step 4: Assert text matches
print("Step 3: Verifying text")
actual_text = hello_element.text
assert actual_text == "Hello World!", f"Expected 'Hello World!', got '{actual_text}'"
assert hello_element.is_displayed()
print(f"Text verified: '{actual_text}'")

# Bonus: Screenshot
print("Step 4: Capturing screenshot")
driver.save_screenshot("dynamic_loading_result.png")
print("Screenshot saved")

print("\n Test Passed!")

driver.quit()
