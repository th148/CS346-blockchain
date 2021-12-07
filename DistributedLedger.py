import hashlib
import time
from .ProofOfWork import *

#
#  This Python code demonstrates the "Distributed Ledger" aspect of
#   the blockchain technology. This is how the blockchain is verified and
#   how people are able to "own" a part of the blockchain if it is being
#   used as digital currency..
#

#
#  Some of this code adapted from: https://github.com/davecan/easychain/blob/master/blockchain.py
#   and from: https://towardsdatascience.com/build-your-own-blockchain-protocol-for-a-distributed-ledger-54e0a92e1f10
#

#
#  In the context of a blockchain currency, "transaction" is typically abbreviated to TX.
#
#  Transactions accrue on the network, waiting for a new block to go through so that they can
#   be validated (they are attached to the block.) This is the distributed ledger. Everyone, even
#   people who do not own any Bitcoin, can see all the transactions that have ever been made, since
#   they are recorded into the blockchain itself.
#

#
# In this simplified version, we simply attach one transaction to one block.
#  However, we can see that the chain of transactions becomes longer and longer.
#
# If someone wanted to alter the chain, and what the transactions say, could they?
#
# The answer, at least in the case of Bitcoin, is probably not. The amount of computing
#  power they would need would be in excess of half of all miners computing power on the
#  network. However, if they could somehow acquire that much computing power, they could
#  temporarily control all new blocks being added to the chain, which would be very bad for
#  the validity of the currency.
#

class TX:

    # In the case of the sender and receiver, in a real blockchain network, we would
    #  use unique digital signatures instead of names. However in this example we will
    #  use simple names, Bob and Sue.

    def __init__(self, tx_amount, sender, receiver):
        self.tx_message = tx_amount
        self.timestamp = time.time()
        self.sender = sender
        self.receiver = receiver

class block:

    # In blockchain, the transactions will be stored in the next block.
    #  Invalid transactions are prevented by the protocol itself;
    #  there is no risk of double spending or unsigned transactions.

    # In this case, the nonce is not actually what proves the work has
    #  been done, necessarily. It is the HASH that resulted in that nonce,
    #  that is important and must be placed into the block.
    # This is called the "hashed block header" and is used to identify the
    #  different blocks.

    def __init__(self, prev_block, transaction):
        self.prev_block = prev_block
        self.transaction = transaction

        self.hashSize = self.__get_hashSize
        self.challengeLevel = self.__get_challengeLevel

        self.nonce = testAttempt()

    def __get_hashSize (self):
        return 30

    def __get_challengeLevel (self):
        return 4
    

class block_chain:

    def __init__(self):
        pass

    def addBlock (self):



def main ():
    pass

if __name__ == "__main__" :
    main()