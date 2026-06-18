from playwright.sync_api import sync_playwright
import os
import json
from datetime import datetime 

# Salvamento de sessao login
SESSION_FILE = "session.json"

with sync_playwright() as pw:
    navegador = pw.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    if os.path.exists(SESSION_FILE):
        contexto = navegador.new_context(
            storage_state=SESSION_FILE,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        contexto.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            }); 
        """)
        page = contexto.new_page()
        page.goto("https://system.mobs2.com/")

    else:
        contexto = navegador.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        contexto.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        page = contexto.new_page()
        page.goto("https://system.mobs2.com/")

        page.get_by_role("textbox", name="Email").fill("SEU_EMAIL")
        page.get_by_role("textbox", name="Senha Senha Atual Nova Senha").fill("SUA_SENHA")
        page.get_by_role("button", name="Entrar").click()

        page.wait_for_load_state("networkidle")
        contexto.storage_state(path=SESSION_FILE)

# ASA BRANCA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("ASA BRANCA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="ASA BRANCA").click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="- PCH6E24 - MB 417 CDI - EURO 6").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(200)

    page.get_by_text("ASA BRANCA", exact=True).click()
    page.wait_for_timeout(200)

    page.get_by_text("- PCH6E24 - MB 417 CDI - EURO 6").click()
    page.wait_for_timeout(200)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# BR7 
    campo = page.get_by_role("combobox").first 
    campo.wait_for()
    campo.click()
    campo.type("BR7", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)
        
    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("SÃO BERNARDO DO CAMPO - SP").nth(1).click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="SÃO BERNARDO DO CAMPO - SP").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.locator("li:nth-child(8) > .listItemContent > label").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("BR7 MOBILIDADE", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="SÃO BERNARDO DO CAMPO - SP").click()
    page.wait_for_timeout(500)

    page.get_by_text("- FIN4E21 - MBZ OF 1519 - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("BR7 MOBILIDADE", exact=True).click()
    page.wait_for_timeout(200)

    page.get_by_text("SÃO BERNARDO DO CAMPO - SP").click()
    page.wait_for_timeout(200)

    page.get_by_text("- FIN4E21 - MBZ OF 1519 - EURO 5").click()
    page.wait_for_timeout(200)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# ITAMARACA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("ITA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="DISPONIVEL").first.click()
    page.get_by_role("gridcell", name="DISPONIVEL").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)
        
    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("listitem").filter(has_text="- SNT-3E47 - 17260 E6").click()
    # page.wait_for_timeout(5000)

    # page.locator("li:nth-child(6) > .listItemContent").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("listitem").filter(has_text="- SNT-3H27 - VW - 17260 - EURO 6").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("ITAMARACA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("ITAMARACA").nth(2).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="- SNT-3F57 - 17260 E6").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("ITAMARACA", exact=True).click()
    page.wait_for_timeout(200)

    page.get_by_text("ITAMARACA").nth(2).click()
    page.wait_for_timeout(200)

    page.get_by_text("- SNT-3G77 - 17260 E6").click()
    page.wait_for_timeout(200)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000) 
           
# RAYMUNDO DA FONTE
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("RAYMUNDO", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="DISPONIVEL").first.click()
    page.get_by_role("gridcell", name="DISPONIVEL").first.first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("KFO7181 - MB 1720 - ANALÓGICO").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("-PE KFO7181 - MB 1720 - ANALÓGICO 101-PE KFO7191 - MB 1720 - ANALÓGICO 101-PE").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("PADRAO").first.click()
    page.wait_for_timeout(500)

    page.get_by_text("-PE").click()
    page.wait_for_timeout(500)

    page.get_by_text("KFO7281 - MB 1720 - ANALÓGICO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("PADRAO").first.click()
    page.wait_for_timeout(200)

    page.get_by_text("-PE").click()
    page.wait_for_timeout(200)

    page.get_by_text("KFO7281 - MB 1720 - ANALÓGICO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
           
# ATALAIA       
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("ATALAIA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="DISPONIVEL").first.first.click()
    page.get_by_role("gridcell", name="DISPONIVEL").first.first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("6133 - MBZ OF 1721 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("6133 - MBZ OF 1721 - EURO").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("ATALAIA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("ATALAIA").nth(2).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="6200 - VW 17230 OD - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("ATALAIA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("ATALAIA").nth(2).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="6200 - VW 17230 OD - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# MB LIMPEZA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("MB LIMPEZA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("1497 - VCL263 - VW 18260 CRM").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("APB4234 - VW 23.220 - SGF").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("MB LIMPEZA URBANA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="PATOS - PTS").click()
    page.wait_for_timeout(500)

    page.get_by_text("- VAR0006 - ITALA 135 BT - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("MB LIMPEZA URBANA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_role("listitem").filter(has_text="PATOS - PTS").click()
    page.wait_for_timeout(500)

    page.get_by_text("- VAR0006 - ITALA 135 BT - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# BORBOREMA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("BORBO", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="DISPONIVEL").first.click()
    page.get_by_role("gridcell", name="DISPONIVEL").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("- QYH9J85 - VW 17230 OD - EURO 5").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("- QYH0E06 - VW 17230 OD - EURO 5").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("BV - Grupo 03 - HORTON").click()
    page.wait_for_timeout(500)

    page.get_by_text("Linha 011").click()
    page.wait_for_timeout(500)

    page.get_by_text("- PCT8620 - VW 17230 OD - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("BV - Grupo 03 - HORTON").click()
    page.wait_for_timeout(500)

    page.get_by_text("Linha 011").click()
    page.wait_for_timeout(500)

    page.get_by_text("- PCT8620 - VW 17230 OD - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# M DIAS BRANCO
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("M DIAS", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    page.wait_for_timeout(9999)

    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("441_MAD DFY5J92 - HR HDB -").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("441_MAD EXU7D41 - HR HDB -").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("REG BA").click()
    page.wait_for_timeout(500)

    page.get_by_text("432_SAL").click()
    page.wait_for_timeout(500)

    page.get_by_text("TDA2F21 - FIAT ARGO - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("REG BA").click()
    page.wait_for_timeout(500)

    page.get_by_text("432_SAL").click()
    page.wait_for_timeout(500)

    page.get_by_text("TDA2F21 - FIAT ARGO - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
        
# GRUPO SANTA ZITA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("GRUPO SANTA ZITA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("- SGL5H47 - SPRINTER 417 - EURO 6").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("2111 - SPRINTER 417 - EURO").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(500)

    page.get_by_text("CARIACICA-ES").click()
    page.wait_for_timeout(500)

    page.get_by_text("2106 - SPRINTER 417 - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(500)

    page.get_by_text("CARIACICA-ES").click()
    page.wait_for_timeout(500)

    page.get_by_text("2106 - SPRINTER 417 - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# DELLYS
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("DELLYS", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("13 - OQL2G70 - VW 9.160 DRC").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("17 - OQL1G23 - VW 9.160 DRC").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("REGIONAL SC").click()
    page.wait_for_timeout(500)

    page.get_by_text("JARAGUA DO SUL - SC").click()
    page.wait_for_timeout(500)

    page.get_by_text("HJA7D13 - VOLVO FH 440 6X2T - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("REGIONAL SC").click()
    page.wait_for_timeout(500)

    page.get_by_text("JARAGUA DO SUL - SC").click()
    page.wait_for_timeout(500)

    page.get_by_text("HJA7D13 - VOLVO FH 440 6X2T - EURO").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# SAMBAIBA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("SAMBAIBA TRANSPORTES", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("21011 - EOY0E11 - Mercedes").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("21014 - FJY0E14 - Mercedes").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(500)

    page.get_by_text("SAO PAULO/SP").click()
    page.wait_for_timeout(500)

    page.get_by_text("22279 - CUC2A79 - Mercedes").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("PADRÃO").click()
    page.wait_for_timeout(500)

    page.get_by_text("SAO PAULO/SP").click()
    page.wait_for_timeout(500)

    page.get_by_text("22279 - CUC2A79 - Mercedes").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# MONTE ALEGRE
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("AGENCIA DE TURISMO MONTE ALEGRE", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("- CUE4G30 - 17.230 EOD - EURO 3").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("- DBM3160 - K 310 - EURO 3").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("MONTE ALEGRE", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("MONTE ALEGRE").nth(2).click()
    page.wait_for_timeout(500)

    page.get_by_text("- CUE4725 - 17.230 EOD - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("MONTE ALEGRE", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("MONTE ALEGRE").nth(2).click()
    page.wait_for_timeout(500)

    page.get_by_text("- CUE4725 - 17.230 EOD - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
    
# VALINHOS
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("RAPIDO LUXO - VALINHOS", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("- CUB3E82 - O 500 RS - EURO 3").click()
    # page.wait_for_timeout(5000)

    # page.get_by_text("- EJY9356 - O 500 M - EURO 3").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("RÁPIDO LUXO - VALINHOS (GB)", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("FRETAMENTO EXECUTIVO -").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BFZ8372 - O 500 R - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("RÁPIDO LUXO - VALINHOS (GB)", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("FRETAMENTO EXECUTIVO -").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BFZ8372 - O 500 R - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# RAPIDO LUXO CAMPINAS
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("RAPIDO LUXO CAMPINAS", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("RÁPIDO LUXO CAMPINAS - SOROCABA").click()
    page.wait_for_timeout(500)

    page.get_by_text("*EMTU - SOROCABA").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BUD7682 - OF 1722 - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("RÁPIDO LUXO CAMPINAS - SOROCABA").click()
    page.wait_for_timeout(500)

    page.get_by_text("*EMTU - SOROCABA").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BUD7682 - OF 1722 - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# RS - PAULINIA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("RAPIDO SUMARE LTDA - PAULINIA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("PAULÍNIA").click()
    page.wait_for_timeout(500)

    page.get_by_text("URBANO", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("- GIW6F07 - OF 1724 - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("PAULÍNIA", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("URBANO", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("- GIW6F07 - OF 1724 - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

# RS - PIRACICABA
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("RAPIDO SUMARE LTDA - PIRACICABA", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("RÁPIDO SUMARÉ", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("RAPIDO SUMARÉ").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BPO9J45 - 17.230 OD - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("RÁPIDO SUMARÉ", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("RAPIDO SUMARÉ").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BPO9J45 - 17.230 OD - EURO 5").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# VB TRANSPORTE
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("VB TRANSPORTE", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("FRETAMENTO", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("PIRACICABA - FRETAMENTO").click()
    page.wait_for_timeout(500)

    page.get_by_text("- ETU1353 - OH 1518 - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("FRETAMENTO", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("PIRACICABA - FRETAMENTO").click()
    page.wait_for_timeout(500)

    page.get_by_text("- ETU1353 - OH 1518 - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
    
# CAMPO LIMPO
    campo = page.get_by_role("combobox").first
    campo.wait_for()
    campo.click()
    campo.type("CAMPO LIMPO", delay=100)
    page.keyboard.press("Enter")

    page.get_by_text("Cockpit").wait_for(state="visible")   
    page.get_by_text("Cockpit").click()
    page.get_by_role("link", name=" Telemetria ").click()

    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9999)
    page.get_by_label("*").click()

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    
    page.get_by_role("gridcell", name="Disponível").first.click()
    page.get_by_role("gridcell", name="Disponível").first.click()

    page.wait_for_timeout(1000)

    for _ in range(50):
        page.keyboard.press("PageDown")
        page.wait_for_timeout(200)

    # page.get_by_text("Operação Telemetria").click()
    # page.get_by_role("link", name=" Timeline de Eventos ").click()
    # page.evaluate("document.documentElement.style.zoom = '67%'")
    # page.wait_for_timeout(5000)
    
    # page.get_by_title("Buscar veículo").click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").first.click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Todos ").nth(1).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_text("VANS 100 - RZW2J88 - CDI416 - EURO").click()
    # page.wait_for_timeout(5000)

    # page.locator("label").filter(has_text="VANS").nth(2).click()
    # page.wait_for_timeout(5000)
    
    # page.get_by_role("link", name="Selecionar").click()
    # page.wait_for_timeout(5000)

    # page.get_by_role("link", name="Adicionar").click()
    # page.wait_for_timeout(5000)  
    
    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Localização ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)  
    
    page.get_by_role("link", name="Todos ").first.click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(1).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Todos ").nth(2).click()
    page.wait_for_timeout(5000)  

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Player ao vivo ").click()    
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(500)

    page.get_by_title("Buscar veículo").click()
    page.wait_for_timeout(500)

    page.get_by_text("CAMPO LIMPO (GB)", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("RLC Campo Limpo - Artesp").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BUD7H96 - MBZ O500 MA - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(500)
    
    for _ in range(4):
        page.get_by_role("link").nth(4).click()
        page.wait_for_timeout(200)

    page.get_by_role("menuitemradio", name="Mostrar imagens de satélite").click()
    page.wait_for_timeout(500)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Detalhes das Viagens ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_text("CAMPO LIMPO (GB)", exact=True).click()
    page.wait_for_timeout(500)

    page.get_by_text("RLC Campo Limpo - Artesp").click()
    page.wait_for_timeout(500)

    page.get_by_text("- BUD7H96 - MBZ O500 MA - EURO 3").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox").first.click()
    page.get_by_text("19", exact=True).first.click()
    page.get_by_text("19", exact=True).first.click()
    page.wait_for_timeout(200)

    page.get_by_role("link", name="Selecionar").click()
    page.wait_for_timeout(5000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard Geral").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)

    page.get_by_text("Operação Telemetria").click()
    page.get_by_role("link", name=" Relatórios ").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(5000)

    page.get_by_role("link", name=" Mobs2 - Dashboard Icon Dashboard de Mapeamento de Eventos").click()
    page.evaluate("document.documentElement.style.zoom = '67%'")
    page.wait_for_timeout(9000)
  
    page.pause()