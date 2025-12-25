#codigo do bot, sem as chaves de api e do bot por motivos obvios :), estou terminando de codar isso no natal alias, boas festas e que ano que vem seja bom 
#projeto bem simples, só para aplicar oque estudei em python, api etc o readme ta completo
import discord #cansei de comentar tudo pprt
from discord.ext import commands
from datetime import datetime
import requests
from urllib.parse import quote

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)#ate aqui foi só configuraçoes para o brinquedo rodar

def wikipedia_resumo(termo): #função para a pesquisa ser melhor e entender mais termos
    url = "https://pt.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "DiscordBot/1.0 (https://github.com/seu-bot)"
    }

    params = { #parametros igual os outros (escrevi essa função depois de todas as outras)
        "action": "query",
        "generator": "search",
        "gsrsearch": termo,
        "gsrlimit": 1,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "format": "json",
        "utf8": 1
    }

    resposta = requests.get(url, params=params, headers=headers)

    # essa estrutura texta pra ver se alguma coisa dá erro, muita coisa deu erro
    if resposta.status_code != 200:
        print("Status:", resposta.status_code)
        print(resposta.text)
        return None, None

    try: 
        dados = resposta.json()
    except Exception as e:
        print("Erro JSON:", e)
        print(resposta.text)
        return None, None
#se passou daqui gg
    paginas = dados.get("query", {}).get("pages", {}) #"le" as paginas que encontrou

    if not paginas:
        return None, None #se ta em branco fd td

    pagina = next(iter(paginas.values()))

    titulo = pagina.get("title")#salva um titulo, bem podrinho, mas funcional
    resumo = pagina.get("extract")#faz um resumo, ou tenta

    if not resumo: #se der erro no resumo tambem (da pra perceber que da muito erro aqui)
        return None, None

    return titulo, resumo #feliz natal





@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}') #retorna se esta funcionando

@bot.command()
async def obrigado(ctx):
    await ctx.send('de nada :) se precisar de mais alguma coisa é só chamar S2')#função basica para entender como funciona

@bot.command()
async def obrigada(ctx):
    await ctx.send('de nada :) se precisar de mais alguma coisa é só chamar S2')#não sei se tem como mudar só uma letra mas foi só copia e cola

@bot.command()
async def ajuda(ctx):
    msg = (
        " **Comandos disponíveis**\n\n"
        " !conta <a> <operador> <b>\n"
        "→ Realiza um cálculo simples\n"
        "Exemplo: !conta 5 + 3\n\n"
        " !hora\n"
        "→ Mostra a hora atual\n\n"
        " !clima <cidade>\n"
        "→ Mostra o clima atual\n\n"
        " !noticias <tema>\n"
        "→ Exibe notícias sobre um tema, tente ser especifico sobre o tema\n\n"
        " !oque_e <termo>\n"
        "→ Explica o que é algo\n"
        "outros comandos\n"
        "!ola; !obrigado(a); !ping (use para saber se estou online)"#tive que fazer todos em port pq o server é br (n tem ngm) e dava erro dependendo da palavra pq já tinha na biblioteca
    )
    await ctx.send(msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')#outro comando pra pegar como é a estrutura base

@bot.command()
async def ola(ctx):
    await ctx.send(f'olá {ctx.author.mention}, como posso ajudar?') #tentei usar essa função de mencionar o autor, achei interessante



@bot.command()
async def hora(ctx):
    agora = datetime.now().strftime("%H:%M:%S")
    hr = int(datetime.now().strftime("%H")) #isso deu um problema q plmr

    if 5 <= hr <= 11:
        saudacao = 'bom dia'
    elif hr <= 18:
        saudacao = 'boa tarde'
    else:
        saudacao = 'boa noite'

    await ctx.send(f'olá, {saudacao}! Agora são {agora}') #isso nem ficou tão legal pro trabalho



@bot.command()
async def conta(ctx, a: int, b: str, c: int):#esse nome de função fpoi na preg
    if b == '+':
        resultado = a + c
    elif b == '-':#estrutura basica if elif else
        resultado = a - c
    elif b == '*':
        resultado = a * c
    elif b == '/':
        if c == 0:
            resultado = "erro: divisão por zero"
        else:
            resultado = a / c
    else:
        resultado = "operador inválido"

    await ctx.send(resultado)



@bot.command()
async def clima(ctx, *, cidade: str):
    API_KEY = "blablabla" #segredo ne

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = { #parametros de pesquisa na api
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code != 200:
        await ctx.send("Não consegui encontrar essa cidade.")
        return

    dados = resposta.json() #armazenar dados uteis ou quase

    temp = dados["main"]["temp"]
    umidade = dados["main"]["humidity"]
    descricao = dados["weather"][0]["description"]
    vento = dados["wind"]["speed"]

    msg = (
        f"**Clima em {cidade.title()}**\n"
        f" Temperatura: {temp}°C\n"
        f" Umidade: {umidade}%\n"
        f" Vento: {vento} m/s\n"
        f" Condição: {descricao}" #mensagem bem simples só pra mostrar mesmo
    )

    await ctx.send(msg)



@bot.command()
async def noticias(ctx, *, tema: str):#mesma coisa do clima
    API_KEY = "blablabla" #confidencial

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": tema,
        "language": "pt",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code != 200:
        await ctx.send("Erro ao acessar a API de notícias.")
        return

    dados = resposta.json()
    artigos = dados.get("articles", [])

    if not artigos:
        await ctx.send(f"Nenhuma notícia encontrada sobre **{tema}**.")
        return

    msg = f" **Notícias sobre {tema.title()}**\n\n"

    for i, artigo in enumerate(artigos, start=1):
        titulo = artigo.get("title", "Sem título")
        fonte = artigo.get("source", {}).get("name", "Fonte desconhecida")
        link = artigo.get("url", "")

        msg += f"{i}. **{titulo}**\n"
        msg += f"   🏷 {fonte}\n"
        msg += f"   🔗 {link}\n\n"

    await ctx.send(msg)#esse é bem limitado mas deu pra entender como funciona (ou quase)


@bot.command()
async def oque_e(ctx, *, termo): #demonio
    titulo, resumo = wikipedia_resumo(termo)#pra deixar essa função  pequena e facil de ajustar criei outra pra dor de cabeça

    if not resumo:
        await ctx.send("Não consegui encontrar esse termo.")
        return

    LIMITE = 1000  # para não ser uma biblia

    if len(resumo) > LIMITE:
        resumo = resumo[:LIMITE] + "..."

    await ctx.send(f" **{titulo}**\n\n{resumo} \n\n fonte: Wikipedia") #fonte ""confiavel"" muitas aspas, brincadeira




bot.run("blablabla")#roda obot obviamente ali n estava escrito blablabla pra ele funcionar mesmo
#gg
