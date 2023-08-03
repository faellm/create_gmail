from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from faker import Faker
from selenium.webdriver.support.ui import Select
import csv

# Criando Nome Fake
def generate_random_name():
    fake = Faker()
    return fake.name()

# Exemplo de uso
random_name = generate_random_name()

# Separar o primeiro nome e o último nome
first_name_random, last_name_random = random_name.split(' ')

print(f'Primeiro Nome: {first_name_random}')
print(f'Segundo Nome: {last_name_random}')

print(random_name)

# Definir o novo user-agent que você deseja utilizar
#new_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win34; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
new_user_agent = ""

# Definir as opções do navegador com o user-agent personalizado
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={new_user_agent}')

# Inicializar o navegador com as opções configuradas
driver = webdriver.Chrome(options=options)

# Fazer uma requisição para um site e verificar o user-agent
#driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXo7B7U_hveWBNXZoTw7X6i89scYFWEajobRDNT54S8iCsSV0kHDn03wkln1PqLMzD__uo8hp9l6&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S571445266%3A1691062973260323')

driver.get("https://accounts.google.com/signup/v2/createaccount?biz=false&cc=BR&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S571445266%3A1691062973260323&flowEntry=SignUp&flowName=GlifWebSignIn&ifkv=AXo7B7U2SvhR4X3-2VQwfAJ1XpBOF-N9P-aDd0FJA_5ZPSfOLyLNI2BGKymt3qyf4pJzJgEFQdcHag&rip=1&service=mail")

sleep(2)

print("________________________________________________")
print("User Agent Alterado no navegador selenium:")
print(driver.execute_script("return navigator.userAgent;"))
print("________________________________________________")

input_Primeironome_create = driver.find_element(By.CSS_SELECTOR, "#firstName")
input_Primeironome_create.send_keys(first_name_random)

input_Segundonome_create = driver.find_element(By.CSS_SELECTOR, "#lastName")
input_Segundonome_create.send_keys(last_name_random)

button_continuar = driver.find_element(By.CSS_SELECTOR, "#collectNameNext > div > button")
button_continuar.click()

sleep(2)

input_diaNascimento = driver.find_element(By.CSS_SELECTOR, "#day")
input_diaNascimento.send_keys('14')

drop_mesNascimento = driver.find_element(By.CSS_SELECTOR, "#month")

select = Select(drop_mesNascimento)
select.select_by_value('1')  # Seleciona "Janeiro"

input_anoNascimento = driver.find_element(By.CSS_SELECTOR, "#year")
input_anoNascimento.send_keys('2000')

drop_genero = driver.find_element(By.CSS_SELECTOR, "#gender")
select = Select(drop_genero)
select.select_by_value('1') # seleciona masculino
button_continuar = driver.find_element(By.CSS_SELECTOR, "#birthdaygenderNext > div > button > span")
button_continuar.click()

sleep(2)

#escolha_email = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]')

try:

    escolha_email_ = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]')
    escolha_email_.click()

    new_user = escolha_email_.text.strip()

    print(new_user)

except:

    # creando o novo email. Formado pelo primeiro nome e o segundo nome
    input_create_user = driver.find_element(By.CSS_SELECTOR, "#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > div.d2CFce.cDSmF > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    new_user = (f'user{first_name_random}{last_name_random}')
    input_create_user.send_keys(new_user)

button_continuar = driver.find_element(By.CSS_SELECTOR, "#next > div > button > span")
button_continuar.click()

sleep(2)

# Criando senha
senha = driver.find_element(By.CSS_SELECTOR, "#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
senha.send_keys('umdoistres')

confirmar_senha = driver.find_element(By.CSS_SELECTOR, "#passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
confirmar_senha.send_keys('umdoistres')

button_continuar = driver.find_element(By.CSS_SELECTOR, "#createpasswordNext > div > button > span")
button_continuar.click()

# Escrever as informações em um arquivo CSV
csv_file = 'usuarios.csv'
data = [(first_name_random, last_name_random, new_user)]
header = ['Primeiro Nome', 'Segundo Nome', 'Email']

for datas in data:

    print(datas)

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"As informações foram salvas no arquivo {csv_file}")

# Fechar o navegador após a execução
#driver.quit()
