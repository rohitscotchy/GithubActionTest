from playwright.sync_api import expect


def test_run(page) -> None:
    # A more robust smoke test for Amazon: assert the search box is present and usable.
    page.goto("https://www.amazon.com/")

    search = page.locator("input#twotabsearchtextbox")
    expect(search).to_be_visible(timeout=10000)
    search.fill("playwright")
    page.locator("input#nav-search-submit-button").click()

    results = page.locator("div.s-main-slot")
    expect(results).to_be_visible(timeout=10000)

