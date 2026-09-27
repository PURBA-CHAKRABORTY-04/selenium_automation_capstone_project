from datetime import datetime
from pathlib import Path


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        screenshot_dir = Path(__file__).resolve().parents[1] / "screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        screenshot_path = screenshot_dir / f"{test_name}_{timestamp}.png"

        if not driver.save_screenshot(str(screenshot_path)):
            raise OSError(f"WebDriver could not save screenshot: {screenshot_path}")

        return str(screenshot_path)