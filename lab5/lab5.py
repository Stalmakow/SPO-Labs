#!/usr/bin/python3
import numpy as np
from web3 import Web3 
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/077017ca7a9a4ac785e8dfcaa68d4316"))
web3.eth.blockNumber
Reward=2
N=8945502
web3.eth.getBlock(N)

used = open('gasUsed.txt', 'a')
price = open('gasPrice.txt', 'a')
contract = open('gasContracts.txt', 'a')


for i in range(657):
  GasUsed = []
  Price = []
  Contracts=[]
  for trans in web3.eth.getBlock(N+i)['transactions']:
    gettr=web3.eth.getTransaction(trans)
    gettrRes=web3.eth.getTransactionReceipt(trans)
    GasUsed.append(gettrRes['gasUsed'])
    Price.append(gettr['gasPrice'])
    if gettr['input'] != '0x':
      Contracts.append(1)
    else:
      Contracts.append(0)
  used.write(str(GasUsed))
  price.write(str(Price))
  contract.write(str(Contracts))
  used.write("\n")
  price.write("\n")
  contract.write("\n")
