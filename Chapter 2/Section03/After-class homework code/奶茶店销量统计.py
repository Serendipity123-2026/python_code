print("-------- 奶茶店销量统计 --------")
sales = [35, 42, 28, 56, 61, 88, 73]
total_sales = sum(sales)
daily_sales = total_sales / len(sales)
highest_daily_sales = max(sales)
lowest_daily_sales = min(sales)
print(f"奶茶店这周的总销售量为：{total_sales}")
print(f"奶茶店这周的日均销量为：{daily_sales:.1f}")
print(f"奶茶店这周的最高单日销量为：{highest_daily_sales}")
print(f"奶茶店这周的最低单日销量为：{lowest_daily_sales}")

























