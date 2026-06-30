# 🚀 Automação de Checklist Diário — Sistema M2

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para automatizar o checklist diário realizado no sistema M2, utilizado internamente pela empresa onde atuo como Analista de Sistemas.

O processo manual levava aproximadamente **2 horas por dia**, exigindo verificações repetitivas em diversas funcionalidades do sistema, dashboards e relatórios exportados pelos clientes.

Com a automação em Python, o tempo de execução foi reduzido para cerca de **20 minutos**, aumentando significativamente a produtividade, confiabilidade e padronização das verificações.

---

<img width="1685" height="1089" alt="image" src="https://github.com/user-attachments/assets/cb615b4b-f5f5-4643-9ab0-943b3f1a6de1" />

---

## ⚙️ Funcionalidades Automatizadas

- ✅ Login automático no sistema
- ✅ Navegação entre módulos
- ✅ Verificação de funcionalidades críticas
- ✅ Checagem de dashboards
- ✅ Validação de relatórios exportados
- ✅ Interação automática com elementos da interface
- ✅ Simulação de ações do usuário
- ✅ Execução padronizada do checklist
- ✅ Redução de falhas humanas

---

## 🛠️ Pré-requisitos e Instalação

### Requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- pip (incluído na instalação do Python)
- Conexão com a internet

### Dependências

| Biblioteca | Versão mínima | Uso |
|---|---|---|
| `playwright` | 1.40+ | Automação do navegador Chromium |
| `openpyxl` | 3.1+ | Geração do relatório Excel |

As dependências estão declaradas no arquivo `requirements.txt` na raiz do projeto.

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/mobs2-checklist-auto.git
cd mobs2-checklist-auto
```

**2. (Opcional) Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instale as dependências Python**
```bash
pip install -r requirements.txt
```

**4. Instale o navegador Chromium do Playwright**
```bash
playwright install chromium
```

**5. Configure suas credenciais de acesso**

Abra o arquivo `checklist.py` e localize a função `iniciar_sessao`. Substitua os placeholders com seu e-mail e senha do sistema:

```python
page.get_by_role("textbox", name="Email").fill("SEU_EMAIL")
page.get_by_role("textbox", name="Senha Senha Atual Nova Senha").fill("SUA_SENHA")
```

> **Atenção:** as credenciais precisam ser configuradas apenas uma vez. Após o primeiro login bem-sucedido, o arquivo `session.json` é gerado e reutilizado nas execuções seguintes.

**6. Execute o checklist**
```bash
python checklist.py
```

---

## ▶️ O que acontece durante a execução

1. **Uma janela do Chrome abre** — o script roda em modo visual (`headless=False`) para simular interações humanas e evitar bloqueios anti-bot.
2. **O script percorre cada cliente** — para cada um, verifica a telemetria, localização e dashboards no sistema M2.
3. **Logs são exibidos no terminal** — incluindo capturas de rede, veículos com atraso detectados e eventuais erros por cliente.
4. **Ao final, o Playwright Inspector é aberto** — a execução pausa automaticamente para inspeção. Feche a janela do Inspector ou clique em "Resume" para encerrar.
5. **O relatório é gerado** — o arquivo `Relatorio_Checklist.xlsx` é criado (ou sobrescrito) na pasta raiz do projeto com o resumo de todos os clientes e veículos com atraso acima de 1h30m.

---

## 🧠 Tecnologias Utilizadas

- 🐍 Python
- 🎭 Playwright
- ⌨️ Automação de teclado e mouse
- 📂 Manipulação de arquivos
- 📊 Verificação de dashboards e relatórios
- 📝 Logs de execução

---

## 📈 Resultados Obtidos

| Processo | Tempo Médio |
|---|---|
| ⏱️ Checklist Manual | Aproximadamente 2 horas |
| ⚡ Checklist Automatizado | Aproximadamente 20 minutos |

### ✅ Benefícios alcançados

1. Maior produtividade
2. Redução de atividades repetitivas
3. Padronização das validações
4. Diminuição de erros humanos
5. Mais tempo disponível para atividades analíticas e estratégicas

---

## 🎯 Aprendizados

Durante o desenvolvimento deste projeto, aprofundei conhecimentos em:

- Automação web com Playwright
- Controle de fluxo automatizado
- Manipulação dinâmica de elementos
- Tratamento de exceções
- Simulação de interação humana
- Otimização de processos corporativos

---

## ⭐ Diferencial do Projeto

Este projeto nasceu de uma necessidade real do ambiente corporativo e gerou impacto direto na operação diária, reduzindo drasticamente o tempo gasto em processos repetitivos.

Além disso, demonstra minha capacidade de:

- Identificar gargalos operacionais
- Desenvolver soluções automatizadas
- Aplicar Python em cenários reais
- Otimizar processos corporativos
- Gerar ganho de produtividade através da tecnologia

---

## ⭐ Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou contribuir com o projeto.
