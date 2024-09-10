## blockchain_interface.py

class BlockchainInterface:
    """
    This class defines an interface for interacting with a blockchain. It provides methods to add
    transactions and retrieve the list of transactions.
    """
    
    def __init__(self):
        """
        Initializes the BlockchainInterface with an empty list of transactions.
        """
        self._transactions = []
    
    def add_transaction(self, transaction: dict):
        """
        Adds a transaction to the blockchain interface.
        
        :param transaction: A dictionary representing the transaction details.
        """
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dictionary")
        
        # Here we would have additional logic to validate the transaction
        # For example, checking if it has all the necessary fields
        
        self._transactions.append(transaction)
    
    def get_transactions(self) -> list:
        """
        Returns the list of transactions added to the blockchain interface.
        
        :return: A list of dictionaries where each dictionary represents a transaction.
        """
        return self._transactions
