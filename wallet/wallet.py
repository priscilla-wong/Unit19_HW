from constants import *

def derive_wallets:

    {'btc-test': [{'address': 'n1acehohqGtZ5uuvopxa2fYknmPrw5tb6J',
              'index': 0,
              'path': "m/44'/1'/0'/0/0",
              'privkey': 'cUu5Z52Hzs7qneHN7CKmknXjcCWrgQGJ2NqCJgnxkVBEEbhGpyhs',
              'pubkey': '0261d7b1f42ab05bd92aaac38369f887befc355904ca957e3696cf28f7e1a32c9a',
              'pubkeyhash': 'dc13c81507d7a5cb7b550c99fe2392ac5b794c8a'
              'xprv': 'tprv8iYPhyXgbih3dmM3YdyVskyozHmshfxoNaJ3FyP49RSjktDQoxg5yNH47FwuJRvWDhXtRNA8KXi9dmxzYK232ukMYJjhz1pTt3VgskAEydn',
              'xpub': 'tpubDFERrPZvk6NiXENqSHe6HAdvZKHos19hwstpYVRMZhF8bNUBSMVg9rtvHP6tqmDbUQfeU9139otmfpUovywSD4SYkrqRhrKTpDgP5JLP5r1'}],
    'btc': [{'address': '1Eo9kQwLdjVweUKqtmQXBYGftsXHDTMyda',
              'index': 0,
              'path': "m/44'/1'/0'/0/0",
              'privkey': 'L4NHWqN9HNgn27ZC5Wxoik3iLW8Pd5a6zqe8ruomAeoo2Y6LiphT',
              'pubkey': '03e913d1d151d74ef35f36addbbb56e1670ea3213ba9ed08f994f96ec288c58ee4',
              'pubkeyhash': '97541282b96b73fbaefbf076fae685e47df0946e'
              'xprv': 'xprv9zoTGUq1PPkvtQLuhGVL2GfAPH2AESyAYBpBYC6aPBVKB9VDgASFZLAr2AqN6yxMkC3oPq1p7CpFegzxVhqdts1TdGNFqCk8Zu8iLtMVvAK',
              'xpub': 'xpub6DnofzMuDmKE6tRNoJ2LPQbtwJreduh1uQjnLaWBwX2J3wpNDhkW78VKsSposaFV9U7fkebQKeaFf6A76geia6t9XUgPuV75kqLodDPWXYx'}],
    'eth': [{'address': '0x0151ABb68bd09a042B31771E25011a5e59F914B2',
              'index': 0,
              'path': "m/44'/1'/0'/0/0",
              'privkey': '0xede6c437db5fabb2deea9035c6affa8b6e387b4cc22e1187200d4ddc919e30a9',
              'pubkey': '0x0278e3eb9fcc19dfc1fbe64ebe1199b9341796468c09e2736f588b2369ee2ae6aa',
              'pubkeyhash': 'dc13c81507d7a5cb7b550c99fe2392ac5b794c8a'
              'xprv': 'xprvA2QeK4FHxcBfkKFJXwXdu8cVE4nyxtEkaZCrk5bw8DyeJoHv8Ei52yEsxmCi7ReMGRpv9XS4221k1aSkDsfYf6RhahvHdmgymHE17T3irnZ',
              'xpub': 'xpub6FPziZnBnyjxxoKmdy4eGGZDn6dUNLxbwn8TYU1YgZWdBbd4fn2KamZMp4KJZijznnLg6cpraNDWA4NXg7eFRPfqAp6TEUhK5dUoiXczoDK'}]}


def priv_key_to_account:
    
#for ETH, BTC, and BTCTEST, need to return the private key

def create_tx (account, recipient, amount):
    
     gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()