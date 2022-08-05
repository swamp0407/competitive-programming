from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


print(Decimal(str(input())).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
