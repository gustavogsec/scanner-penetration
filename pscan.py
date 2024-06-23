import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo Scanner Penetration")
print("<--------------------------------->")

ip = input("Digite o ip a ser mapeado: ")
print("O ip digitado foi: ", ip)
type(ip)
menu = input(""""\n Escolha o tipo de varredura a ser realizada
                1 -> Tipo SYN
                2 -> Tipo UDP
                3 -> Tipo Intensa
                Digite a opção escolhida: """)
print("A opção escolhida foi: ", menu)

if menu == "1":
    print("Versão nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versão nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())
elif menu == "3":
    print("Versão nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
else:
    print("Escolha uma opção válida")