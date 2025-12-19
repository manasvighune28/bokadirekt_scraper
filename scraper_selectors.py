from selenium.webdriver.common.by import By

COOKIE_ACCEPT = [
    (By.XPATH, "//button[contains(text(), 'Tillåt alla cookies')]"),
    (By.XPATH, "//button[contains(text(), 'Godkänn')]"),
    (By.XPATH, "//button[contains(text(), 'Acceptera')]"),
]

SHOW_SERVICES = [
    (By.XPATH, "//button[contains(text(), 'Visa tjänster')]"),
]

TAB_ALL_SERVICES = [
    (By.XPATH, "//button[contains(text(), 'Alla tjänster')]"),
]

TAB_TRY_OFFERS = [
    (By.XPATH, "//button[contains(text(), 'Prova på')]"),
]

SERVICE_CARD = [(By.CSS_SELECTOR, "div[data-testid='service-card'], article.service-card")]
SERVICE_TITLE = [(By.CSS_SELECTOR, "h3[data-testid='service-title'], h3")]
SERVICE_DESCRIPTION = [(By.CSS_SELECTOR, "div[data-testid='service-description'], p")]
BOOK_BUTTON = [(By.CSS_SELECTOR, "a[data-testid='book-button'], a[href*='bokadirekt.se']")]

CONTRACTOR_NAME = [(By.CSS_SELECTOR, "h3, h4")]
