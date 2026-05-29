from playwright.sync_api import expect


def test_run(page) -> None:
    # A more robust smoke test for Amazon: assert the search box is present and usable.
    page.goto("https://www.amazon.com/")

    # Handle Amazon's popup ("Continue shopping" button) if it appears
    continue_btn = page.locator("button:has-text('Continue shopping')")
    if continue_btn.is_visible(timeout=5000):
        continue_btn.click()

    # Wait for search box to be visible
    search = page.locator("input#twotabsearchtextbox")
    expect(search).to_be_visible(timeout=10000)
    search.fill("playwright")
    page.locator("input#nav-search-submit-button").click()

    # Verify results page loaded
    results = page.locator("div.s-main-slot")
    expect(results).to_be_visible(timeout=10000)

