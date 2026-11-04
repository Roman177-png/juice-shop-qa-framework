import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_juice_shop_landing_page_loads(page: Page, base_url: str) -> None:
    page.goto(base_url)

    expect(page).to_have_title(re.compile("OWASP Juice Shop"))
    expect(page.get_by_text("OWASP Juice Shop", exact=False).first).to_be_visible()
