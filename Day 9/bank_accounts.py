# ============================================================
# Fully Type-Annotated Banking System
# ============================================================
#
# Objective:
# Build a banking system using Python type hints and dataclasses.
#
# Concepts Covered:
# - Optional[str]  -> value can be str or None
# - List[Transaction] -> list of Transaction objects
# - Dict[str, BankAccount] -> account number mapped to account
# - @dataclass -> auto-generates constructor and repr
# - mypy -> catches type errors before runtime
#
# Features:
# - Deposit
# - Withdraw
# - Transfer
# - Check Balance
# - Mini Statement
# - Transaction Summary
#
# Goal:
# Ensure every variable, parameter, and return value has
# proper type annotations and passes mypy with zero errors.
# ============================================================


from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class Transaction:
    txn_type: str
    amount: float
    balance: float
    note: Optional[str] = None


class BankAccount:

    def __init__(
        self,
        holder: str,
        acc_num: str,
        balance: float = 0.0
    ) -> None:

        self.holder: str = holder
        self.acc_num: str = acc_num
        self.balance: float = balance

        self.transactions: List[Transaction] = []

    def _add_transaction(
        self,
        txn_type: str,
        amount: float,
        note: Optional[str] = None
    ) -> None:

        transaction = Transaction(
            txn_type=txn_type,
            amount=amount,
            balance=self.balance,
            note=note
        )

        self.transactions.append(transaction)

        if len(self.transactions) > 5:
            self.transactions.pop(0)

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        self._add_transaction(
            txn_type="CR",
            amount=amount
        )

        print(f"Deposited Rs.{amount:,.2f}")

    def withdraw(self, amount: float) -> bool:

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount

        self._add_transaction(
            txn_type="DR",
            amount=amount
        )

        print(f"Withdrawn Rs.{amount:,.2f}")

        return True

    def transfer(
        self,
        amount: float,
        target_account: BankAccount
    ) -> bool:

        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("Insufficient balance for transfer.")
            return False

        self.balance -= amount
        target_account.balance += amount

        self._add_transaction(
            txn_type="TRF-OUT",
            amount=amount,
            note=f"To {target_account.acc_num}"
        )

        target_account._add_transaction(
            txn_type="TRF-IN",
            amount=amount,
            note=f"From {self.acc_num}"
        )

        print(
            f"Transferred Rs.{amount:,.2f} "
            f"from {self.acc_num} "
            f"to {target_account.acc_num}"
        )

        return True

    def get_balance(self) -> float:
        return self.balance

    def mini_statement(self) -> List[str]:

        statement: List[str] = []

        for txn in self.transactions:

            sign: str = (
                "+"
                if txn.txn_type in ("CR", "TRF-IN")
                else "-"
            )

            line = (
                f"{txn.txn_type:<8}"
                f"{sign}Rs.{txn.amount:,.2f} "
                f"Balance: Rs.{txn.balance:,.2f}"
            )

            statement.append(line)

        return statement

    def transaction_summary(self) -> Dict[str, float]:

        summary: Dict[str, float] = {
            "credits": 0.0,
            "debits": 0.0
        }

        for txn in self.transactions:

            if txn.txn_type in ("CR", "TRF-IN"):
                summary["credits"] += txn.amount
            else:
                summary["debits"] += txn.amount

        return summary

    def bank_statement(self) -> None:

        print("\n----- BANK STATEMENT -----")

        if not self.transactions:
            print("No transactions found.")
            return

        for line in self.mini_statement():
            print(line)

        print(
            f"\nCurrent Balance: "
            f"Rs.{self.balance:,.2f}"
        )

    def __str__(self) -> str:

        return (
            f"Holder: {self.holder} | "
            f"Account: {self.acc_num} | "
            f"Balance: Rs.{self.balance:,.2f}"
        )


class Bank:

    def __init__(self) -> None:
        self.accounts: Dict[str, BankAccount] = {}

    def add_account(
        self,
        account: BankAccount
    ) -> None:

        self.accounts[account.acc_num] = account

    def find_account(
        self,
        acc_num: str
    ) -> Optional[BankAccount]:

        return self.accounts.get(acc_num)


def main() -> None:

    bank = Bank()

    acc1 = BankAccount(
        "Aravind",
        "HDFC001",
        5000.0
    )

    acc2 = BankAccount(
        "Arjun",
        "SBI001",
        3000.0
    )

    bank.add_account(acc1)
    bank.add_account(acc2)

    acc1.deposit(2000.0)

    acc1.withdraw(1500.0)

    acc1.transfer(
        1000.0,
        acc2
    )

    print("\nAccounts")
    print(acc1)
    print(acc2)

    print("\nAcc1 Statement")
    acc1.bank_statement()

    print("\nAcc2 Statement")
    acc2.bank_statement()

    print("\nSummary")
    print(acc1.transaction_summary())


if __name__ == "__main__":
    main()