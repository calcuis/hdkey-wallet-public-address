from bitcoinlib.keys import HDKey

words = input("Enter your seed phrase in words: ")
wallet = HDKey.from_passphrase(words)

addr1 = wallet.address(script_type='p2pkh')
addr2 = wallet.address(script_type='p2sh')
addr3 = wallet.address(encoding='bech32',script_type='p2wpkh')
addr4 = wallet.address(encoding='bech32',script_type='p2wsh')
addr5 = wallet.address(encoding='bech32',script_type='p2tr')

print("p2pkh:  "+addr1)
print("p2sh:   "+addr2)
print("p2wpkh: "+addr3)
print("p2wsh:  "+addr4)
print("p2tr:   "+addr5)
