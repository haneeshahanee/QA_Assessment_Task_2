"""
Dynamic Loading Test Automation
This script tests the dynamic loading functionality on The Internet website.
It verifies that content loads properly after clicking a start button.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os


def test_dynamic_loading():
    """
    Test Case: Dynamic Loading
    Steps:
    1. Navigate to the dynamic loading page
    2. Click the 'Start' button
    3. Wait for loading bar to disappear
    4. Verify 'Hello World!' text appears
    5. Capture screenshot of the result
    """
    # Setup Chrome options for headless mode (bonus requirement)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the Dynamic Loading page
        url = "https://the-internet.herokuapp.com/dynamic_loading/1"
        print(f"Navigating to: {url}")
        driver.get(url)
        
        # Give page a moment to fully load
        time.sleep(1)

        print("\n" + "="*60)
        print("TASK 2: Dynamic Loading Test")
        print("="*60)

        print("\nStep 1: Clicking the 'Start' button...")
        # Click the "Start" button
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("✓ Start button clicked successfully")

        print("\nStep 2: Waiting for loading bar to disappear and 'Hello World!' to appear...")
        # Wait for the loading bar to disappear
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
        print("✓ Loading bar has disappeared")

        # Wait for "Hello World!" text to appear
        hello_text_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        print("✓ 'Hello World!' text element is now visible")

        print("\nStep 3: Asserting the text is visible and matches exactly...")
        # Get the text and verify
        actual_text = hello_text_element.text
        expected_text = "Hello World!"

        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        print(f"✓ Text assertion passed! Text is: '{actual_text}'")

        # Verify the element is visible
        assert hello_text_element.is_displayed(), "Element is not visible!"
        print("✓ Element visibility verified!")

        # Bonus: Capture screenshot in headless mode
        print("\n" + "-"*60)
        print("BONUS STEP: Capturing screenshot in headless mode...")
        print("-"*60)
        
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        screenshot_path = "screenshots/dynamic_loading_result.png"
        driver.save_screenshot(screenshot_path)
        print(f"✓ Screenshot saved as '{screenshot_path}'")

        print("\n" + "="*60)
        print("✅ TEST PASSED - All assertions successful!")
        print("="*60)

    except Exception as e:
        print("\n" + "="*60)
        print("TEST FAILED")
        print("="*60)
        print(f"Error: {str(e)}")
        
        # Capture screenshot on failure
        error_screenshot = "error_screenshot.png"
        driver.save_screenshot(error_screenshot)
        print(f"\n📸 Error screenshot saved as '{error_screenshot}'")
        raise

    finally:
        # Close the browser
        print("\nClosing browser...")
        driver.quit()
        print("✓ Browser closed successfully")


if __name__ == "__main__":
    print("\n" + "🚀 Starting Dynamic Loading Test Automation" + "\n")
    test_dynamic_loading()
    print("\n" + "✅ Test execution completed!" + "\n")