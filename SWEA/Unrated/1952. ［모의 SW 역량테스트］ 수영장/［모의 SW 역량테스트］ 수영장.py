T = int(input())
for tc in range(1, T+1):
    daily, monthly, quarterly, yearly = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    dp = [0] * 13

    # 1, 2월의 최소 비용
    dp[1] = min(plan[1] * daily, monthly)
    dp[2] = dp[1] + min(plan[2] * daily, monthly)

    for month in range(3, 13):
        # 점화식 -> N월의 최소 비용
        # 1. N-3월에 1분기권을 구입한 경우
        # 2. N-1월의 최소 비용 + 1일권 구매
        # 3. N-1월의 최소 비용 + 1달권 구매
        dp[month] = min(dp[month - 3] + quarterly,
                        dp[month - 1] + (plan[month] * daily),
                        dp[month - 1] + monthly)

    result = min(dp[12], yearly)
    print(f"#{tc} {result}")
