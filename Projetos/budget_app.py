class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""

        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            body += f"{description}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + body + total


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = [(w / total_spent) * 100 for w in withdrawals]
    percentages = [int(p // 10 * 10) for p in percentages]

    for i in range(100, -1, -10):
        result += str(i).rjust(3) + "|"
        for p in percentages:
            result += " o " if p >= i else "   "
        result += " \n"

    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        result += "     "
        for c in categories:
            result += (c.name[i] if i < len(c.name) else " ") + "  "
        if i != max_len - 1:
            result += "\n"

    return result
