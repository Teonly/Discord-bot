# Discord Bot

## Project Overview / Visão Geral (EN/PT)

### EN:
Discord Bot is a personal Python project developed to explore Discord bot development, asynchronous programming, and integration with external APIs.  
The bot provides a set of practical commands such as time display, simple calculations, weather information, news retrieval, and term explanations using Wikipedia.

The main goal of the project is learning-oriented: understanding how bots interact with Discord, how APIs are consumed in real scenarios, and how to structure a growing Python project in a clear and maintainable way.

### PT:
Discord Bot é um projeto pessoal em Python desenvolvido para explorar a criação de bots no Discord, programação assíncrona e integração com APIs externas.  
O bot oferece um conjunto de comandos práticos como exibição de horário, cálculos simples, informações de clima, notícias e explicações de termos usando a Wikipedia.

O objetivo principal do projeto é o aprendizado: entender como bots interagem com o Discord, como APIs são consumidas em cenários reais e como estruturar um projeto Python de forma clara e sustentável.

---

## Key Features / Recursos Principais (EN/PT)

### EN:
- Discord bot with command-based interaction
- Time-based greeting and current time display
- Simple arithmetic command
- Weather information using OpenWeather API
- News search by topic using NewsAPI
- Term explanation using Wikipedia API
- Error handling for invalid input and API failures
- Respect for Discord message length limits

### PT:
- Bot de Discord com interação baseada em comandos
- Saudação dinâmica baseada no horário atual
- Comando de cálculo aritmético simples
- Informações de clima usando a API OpenWeather
- Busca de notícias por tema usando a NewsAPI
- Explicação de termos utilizando a API da Wikipedia
- Tratamento de erros para entradas inválidas e falhas de API
- Respeito ao limite de caracteres das mensagens do Discord

---

## Bot Commands / Comandos do Bot (EN/PT)

### EN:
- `!ola` – Greets the user
- `!hora` – Shows current time with contextual greeting
- `!conta <a> <operator> <b>` – Performs a simple calculation
- `!clima <city>` – Displays current weather for a city
- `!noticias <topic>` – Shows recent news about a topic
- `!oque_e <term>` – Explains a term using Wikipedia
- `!ajuda` – Displays the list of available commands

### PT:
- `!ola` – Cumprimenta o usuário
- `!hora` – Mostra o horário atual com saudação contextual
- `!conta <a> <operador> <b>` – Realiza um cálculo simples
- `!clima <cidade>` – Mostra o clima atual de uma cidade
- `!noticias <tema>` – Exibe notícias recentes sobre um tema
- `!oque_e <termo>` – Explica um termo usando a Wikipedia
- `!ajuda` – Exibe a lista de comandos disponíveis

---

## Architecture / Arquitetura (EN/PT)

### EN:
- Python as the main programming language
- discord.py library for Discord integration
- Command-based structure using `discord.ext.commands`
- External API integration handled via `requests`
- API logic separated into helper functions
- Clear separation between command logic and service logic
- Focus on readability and incremental expansion

### PT:
- Python como linguagem principal
- Biblioteca discord.py para integração com o Discord
- Estrutura baseada em comandos usando `discord.ext.commands`
- Integração com APIs externas via `requests`
- Lógica de API separada em funções auxiliares
- Separação clara entre lógica de comandos e serviços
- Foco em legibilidade e expansão incremental

---

## APIs Used / APIs Utilizadas (EN/PT)

### EN:
- **OpenWeather API** – Weather data
- **NewsAPI** – News search by topic
- **Wikipedia API** – Term search and summary extraction

### PT:
- **OpenWeather API** – Dados meteorológicos
- **NewsAPI** – Busca de notícias por tema
- **Wikipedia API** – Busca de termos e extração de resumos

---

## Technologies / Tecnologias (EN/PT)

### EN:
- Python 3
- discord.py
- requests
- REST APIs
- Asynchronous programming (async/await)

### PT:
- Python 3
- discord.py
- requests
- APIs REST
- Programação assíncrona (async/await)

---

## Status / Status Atual (EN/PT)

### EN:
The project is functional and stable, covering all planned core features.  
Future improvements may include code modularization, additional commands, and deployment to a cloud or hosting service for continuous operation.

### PT:
O projeto está funcional e estável, cobrindo todas as funcionalidades principais planejadas.  
Melhorias futuras podem incluir modularização do código, novos comandos e implantação em nuvem ou serviço de hospedagem para funcionamento contínuo.

---

## Known Limitations / Limitações Conhecidas (EN/PT)

### EN:
- Bot runs only while the Python process is active
- No persistent storage (database) implemented
- Wikipedia summaries are truncated to respect Discord limits
- Focus is on learning and clarity rather than scalability

### PT:
- O bot funciona apenas enquanto o processo Python está ativo
- Não há armazenamento persistente (banco de dados)
- Resumos da Wikipedia são truncados para respeitar limites do Discord
- O foco está no aprendizado e clareza, não em escalabilidade
