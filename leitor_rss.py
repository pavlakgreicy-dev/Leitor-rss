import feedparser

FEEDS = {
    "1":("G1 - Tecnologia", "https://g1.globo.com/rss/g1/tecnologia/"),
    "2":("Hacker news", "https://news.ycombinator.com/rss"),
    "3":("Python Blog", "https://blog.python.org/feeds/posts/default"),  
    
}

def mostrar_menu():
    print("\nEscolha um feed:")
    for numero, (nome, _) in FEEDS.items():
        print(f"{numero} - {nome}")
    print("0 - Sair")

def ler_feed(url, limite=5):
    feed = feedparser.parse(url)
    for i, noticia in enumerate(feed.entries[:limite], start=1):
        print(f"\n{i}. {noticia.title}")

while True:
    mostrar_menu()
    opcao = input("Opção:")

    if opcao == "0" :
        break
    elif opcao in FEEDS:
         nome, url = FEEDS[opcao]
         print(f"\n=== {nome} ===")
         ler_feed(url)
    else:
        print("Opção inválida.")       