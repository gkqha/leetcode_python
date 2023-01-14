from decimal import Decimal


def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    if start_price_new <= start_price_old:
        return [0, start_price_old - start_price_new]
    m = 1
    tmp_old = start_price_old
    tmp_new = start_price_new
    while True:
        tmp_old = tmp_old * (100 - percent_loss_by_month - 0.5 * (m // 2)) / 100
        tmp_new = tmp_new * (100 - percent_loss_by_month - 0.5 * (m // 2)) / 100
        res = saving_per_month * m + tmp_old - tmp_new
        if res > 0:
            return [
                m,
                int(Decimal(res).quantize(Decimal("1"), rounding="ROUND_HALF_UP")),
            ]
        m = m + 1


print(nbMonths(2000, 8000, 1000, 1.5))
