from livereload import Server, shell


def rebuild():
    print("site rebuild")

rebuild()

server = Server()
server.watch('*.html', rebuild)
server.serve(root='.')