from blockchain.block import Block
from wallet.transaction import Transaction
from wallet.wallet import Wallet
from config import MINING_REWARD_INPUT

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        print("adding block", data)
        last_block = self.chain[-1]

        block = Block.mine_block(last_block, data)
        self.chain.append(block)

    def __repr__(self):
        return f'Blockchain : {self.chain}'

    def replace_chain(self, chain):
        """
        Replace local chain with incoming chain
        - Incoming chain is longer than the local one
        - Incoming chain is formatted properly
        """
        if len(chain) <= len(self.chain):
            raise Exception('The incoming chain must be longer')
        
        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'The incoming chain is invalid {e}')

        self.chain = chain

    def to_json(self):
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        blockchain = Blockchain()
        blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json))
        return blockchain
        
            

    @staticmethod
    def is_valid_chain(chain):
        """
        - The chain must with genesis block
        - The blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)
        
        Blockchain.is_valid_transaction_chain(chain)

    @staticmethod
    def is_valid_transaction_chain(chain):
        """
        - Each transaction must only appear once in the chain.
        - There can only be one transaction reward per block.
        - Each transaction must be valid.
        """
        transaction_ids = set()
        for i in range(len(chain)):
            block = chain[i]
            has_mining_reward = False
            for transaction_json in block.data:
                transaction = Transaction.from_json(transaction_json)

                if transaction.id in transaction_ids:
                    raise Exception(f'Transaction {transaction.id} is not unique')

                transaction_ids.add(transaction.id)
                if transaction.input == MINING_REWARD_INPUT:
                    if has_mining_reward:
                        raise Exception(f'There can only be one minig reward per block. Check the blov=ck with hash : {block.hash}')
                    has_mining_reward = True
                else:
                    historic_blockchain = Blockchain()
                    historic_blockchain.chain = chain[0:i]
                    historic_balance = Wallet.calculate_balance(historic_blockchain, transaction.input['address'])

                    if historic_balance != transaction.input['amount']:
                        raise Exception(f'Transaction {transaction.id} has an invalid amount')

                Transaction.is_valid_transaction(transaction)



def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain)

if __name__ == '__main__':
    main()