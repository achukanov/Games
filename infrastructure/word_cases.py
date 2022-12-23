"""Склонение падежей"""

"""склонение для слова комментарий"""
async def word_cases(number: str) -> str:
    last_number = int(number[-1])
    if last_number == 1:
        return 'комментарий'
    if 1 < last_number < 5:
        return 'комментария'
    else:
        return 'комментариев'
