#     Simple Bank Account System

#     Features:
#     - Deposit money
#     - Withdraw money
#     - Transfer money
#     - Check balance
#     - Display last 5 transactions



class BankAccount:

    def __init__(self, holder: str, acc_num: str, balance: float = 0):
        self.holder = holder
        self.acc_num = acc_num
        self.balance = balance
        self.transactions = []

    def _add_transaction(self, txn_type: str, amount: float):
        transaction = {
            "type": txn_type,
            "amount": amount,
            "balance": self.balance
        }

        self.transactions.append(transaction)

        # Keep only last 5 transactions
        if len(self.transactions) > 5:
            self.transactions.pop(0)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount
        self._add_transaction("CR", amount)

        print(f"Deposited Rs.{amount:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self._add_transaction("DR", amount)

        print(f"Withdrawn Rs.{amount:,.2f}")

    def transfer(self, amount: float, target_account) -> None:
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance for transfer.")
            return

        self.balance -= amount
        target_account.balance += amount

        self._add_transaction("TRF-OUT", amount)
        target_account._add_transaction("TRF-IN", amount)

        print(
            f"Transferred Rs.{amount:,.2f} "
            f"from {self.acc_num} to {target_account.acc_num}"
        )

    def get_balance(self) -> float:
        return self.balance

    def bank_statement(self) -> None:
        print("\n----- BANK STATEMENT -----")

        if not self.transactions:
            print("No transactions found.")
            return

        for txn in self.transactions:
            sign = "+" if txn["type"] in ("CR", "TRF-IN") else "-"

            print(
                f"{txn['type']} "
                f"{sign}Rs.{txn['amount']:,.2f} "
                f"Balance: Rs.{txn['balance']:,.2f}"
            )

        print(f"\nCurrent Balance: Rs.{self.balance:,.2f}")

    def __str__(self) -> str:
        return (
            f"Account Holder: {self.holder} | "
            f"Account Number: {self.acc_num} | "
            f"Balance: Rs.{self.balance:,.2f}"
        )


def main():
    acc1 = BankAccount("Aravind", "HDFC001", 5000)
    acc2 = BankAccount("Arjun", "SBI001", 3000)

    acc1.deposit(2000)
    acc1.withdraw(1500)

    print()
    acc1.transfer(1000, acc2)

    print("\n", acc1)
    print(acc2)

    print()
    acc1.bank_statement()

    print()
    acc2.bank_statement()


if __name__ == "__main__":
    main()