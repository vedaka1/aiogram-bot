import requests
from bs4 import BeautifulSoup


# login_url = 'https://sts.narfu.ru/adfs/ls?SAMLRequest=lZJBT%2BMwEIXv%2FIrI9yaOKQKsJlVVhITESqiUPXBZzdrjEim2sx6n25%2B%2FTtqKHFgEV2fem%2Fe%2ByWJ5sG22x0CNdxUrc84ydMrrxu0q9rK9n92wZX2xILBtJ1d9fHMb%2FNMjxWxFhCEm2do76i2GZwz7RuHL5rFibzF2JIvCQTD9DJIut15jT7kPu0J5a70bXll2l7waB3Hcf5ZRpHyU5qEvQBsqWmLZvQ8KxwwVM9ASsuzhrmK%2FUKM2urxVJb%2FmwoDg11eghTb899xc3po0Rk9A1OzxXUjU44OjCC5WTHBxOSvLmeDbci65kJzn5fzqlWU%2Fz2jEgCbBciRHGBXrg5MeqCHpwCLJqOTz6sejTJOyCz565VtWn9CN%2B8LXDeBMl9Wfsxy8RGExgoYIBXWnuZRAL4rp8mMU0cnTBVGPLNP5Ih5itva2g9DQUBYPoOK0rvheXzl1XrepzAbNxO7L3T8dU1IN1ul5uO5fH%2FRTioEqNdsGcNT5EI8IPsxTH7%2F9D0h9pjf96%2Bt%2F&RelayState=e9c9e572-226c-411f-b21a-381c86b8c73b&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=suxxmTgmNneTHwasCE9JpK5qwfKdIHhK1vWTHr5DmSiilBAfe2rTT5fXBWg4esLKCEby0iwdzJ0WbyvY75hWnkIUxeHWcqX%2Bd9MZCIJaCCJ%2FIos25Fp%2F2xIuueSC7snzoTJpBEKtCqm4lqWD%2FIYHPJsvLp6KZ3bMdBsBD1UMwkjg%2BZrF%2BPuM%2BHVV4jLzxzhnEI51IOcij6X8075SzowpH2sBcdRnUSV%2FY1Yr%2Fq%2FXsylZNm43pl9Qu9whyzBocq6AlcV5MWOfKuYYbyNBnLJlu5%2F205E1I31g7LpeoXzLVVTW153XDFPJP942R4CTM2jSc7PHGVtefuqKODDUYyZpIw%3D%3D'
url_new = 'https://narfu.modeus.org/schedule-calendar/my?timeZone=%22Europe%2FMoscow%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-20%22%7D'
# username = 'kuleshov.v@edu.narfu.ru'
# password = 'piZ@2$fAVE'


session = requests.Session()
# # response = session.get(url_new, auth=(username, password), allow_redirects=True)
# response = session.post("https://narfu-auth.modeus.org/commonauth", {"username": username, "password": password}, allow_redirects=True)
# print(response.text)
# # response = session.get("https://narfu-auth.modeus.org/oauth2/authorize")
# print(response.status_code)
# response = session.get(url_new, allow_redirects=True)

# # soup = BeautifulSoup(response.text, 'html.parser')


# cookies = {
#     '_ym_uid': '1690205781548726742',
#     '_ym_d': '1690205781',
# }

# headers = {
#     'authority': 'narfu-auth.modeus.org',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     'content-type': 'application/x-www-form-urlencoded',
#     # 'cookie': '_ym_uid=1690205781548726742; _ym_d=1690205781',
#     'origin': 'https://sts.narfu.ru',
#     'referer': 'https://sts.narfu.ru/',
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'cross-site',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
# }

# data = {
#     'SAMLResponse': 'PHNhbWxwOlJlc3BvbnNlIElEPSJfN2ZjM2U1NjUtMzAzYi00NjIzLTg2ODItMzJiOTcxZGNiZDg5IiBWZXJzaW9uPSIyLjAiIElzc3VlSW5zdGFudD0iMjAyMy0xMS0yMVQxMzoxMzowNi4wMDdaIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly9uYXJmdS1hdXRoLm1vZGV1cy5vcmcvY29tbW9uYXV0aCIgQ29uc2VudD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmNvbnNlbnQ6dW5zcGVjaWZpZWQiIEluUmVzcG9uc2VUbz0iXzNhNjRjNWFlY2MxNzUwYTQyYWU2MzFkNTY1NDIyMmUyIiB4bWxuczpzYW1scD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOnByb3RvY29sIj48SXNzdWVyIHhtbG5zPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj5odHRwOi8vc3RzLm5hcmZ1LnJ1L2FkZnMvc2VydmljZXMvdHJ1c3Q8L0lzc3Vlcj48c2FtbHA6U3RhdHVzPjxzYW1scDpTdGF0dXNDb2RlIFZhbHVlPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6c3RhdHVzOlN1Y2Nlc3MiIC8+PC9zYW1scDpTdGF0dXM+PEFzc2VydGlvbiBJRD0iX2I1NmJkY2YyLTIwNjktNDQ5OC04M2NhLTFlNTI4ZTZlNzMwNyIgSXNzdWVJbnN0YW50PSIyMDIzLTExLTIxVDEzOjEzOjA2LjAwN1oiIFZlcnNpb249IjIuMCIgeG1sbnM9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iPjxJc3N1ZXI+aHR0cDovL3N0cy5uYXJmdS5ydS9hZGZzL3NlcnZpY2VzL3RydXN0PC9Jc3N1ZXI+PGRzOlNpZ25hdHVyZSB4bWxuczpkcz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PGRzOlNpZ25lZEluZm8+PGRzOkNhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiIC8+PGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZHNpZy1tb3JlI3JzYS1zaGEyNTYiIC8+PGRzOlJlZmVyZW5jZSBVUkk9IiNfYjU2YmRjZjItMjA2OS00NDk4LTgzY2EtMWU1MjhlNmU3MzA3Ij48ZHM6VHJhbnNmb3Jtcz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmUiIC8+PGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIgLz48L2RzOlRyYW5zZm9ybXM+PGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jI3NoYTI1NiIgLz48ZHM6RGlnZXN0VmFsdWU+REdxK2RoMzlmNEU4UkJYZlNzbEU3eVIyOEpad29qL1pCWEk3UUMvLzI1QT08L2RzOkRpZ2VzdFZhbHVlPjwvZHM6UmVmZXJlbmNlPjwvZHM6U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU+WUlCOUlrVnkvb2VXRVFaZVorcnJqbXNCRld4VWVlcXJ1QWlQRUlicFNPWXdjVUhZbG92YkZxTVo1K054blBEOVFuUTJNemVuV3U1NGV0OGordFJrV3hBb01HVXRFYnVnLytnUGo3TEZPNTZxd2loZGprWGlEWlRCOUdyYk5yOEY3azZnKy8wZkMrSGVNRWk5eUhiVVJ3MGl1M0p1SHBWa01XQ2luMGhsV1JrdkxvbE16YzdzV3J4R3h4WDBTV2VJVjA3Z0wrK1dMdWtGalEvak5pdmJVcXBhU2FGbzBCMXJKZGsvZ1hEallHNDJ6NjNJZUJiTXpnemhqeFdmUjR2dnVKSlA2bWFVMDJZbWx3bGxrb3BLTVBqb3Npc2xVLzFkM25JVURhazZMMHNZZXR3bnhlbTBQcmJaakdSYkJ3UU5KL1I3ZDhHNWhDaS9FU1dqdkp4NGhBPT08L2RzOlNpZ25hdHVyZVZhbHVlPjxLZXlJbmZvIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj48ZHM6WDUwOURhdGE+PGRzOlg1MDlDZXJ0aWZpY2F0ZT5NSUlDMURDQ0FieWdBd0lCQWdJUUkzTXBKNndDekw1TnVoSlpubEVmU3pBTkJna3Foa2lHOXcwQkFRc0ZBREFtTVNRd0lnWURWUVFERXh0QlJFWlRJRk5wWjI1cGJtY2dMU0J6ZEhNdWJtRnlablV1Y25Vd0hoY05Nak13TmpFeU1qQXlNek0zV2hjTk1qUXdOakV4TWpBeU16TTNXakFtTVNRd0lnWURWUVFERXh0QlJFWlRJRk5wWjI1cGJtY2dMU0J6ZEhNdWJtRnlablV1Y25Vd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUURBM2xwSmxHN2JQTEQvUzgxWHhnTHBLWXYxUXdhWWozdktSMU9kNXJ2VVdZK25OR2hCTXZXeXBETkloRmFRMC9OUHpFSWxlYWJic1FMR2xjTlErVDQ2NGJxcThlNFlWRGUrYnZPYUV6L0VtVVp6M2FmZUpDS3NYSGdlaE51a0p2d1VGWUxhamsrRmFHaHY3bEVSUE9GbjNVK3JkRWNoUzlLMXkvdllma2F0RzZPaGhDVzh0YXFDM0dWMU5iZ1plQnpicU4vUlVIeEZFNG8wdFNKMk4zRGRnazRCYlFZSFkvUDVCUnBqNHM4MHFCQW5aWWdPeHNwcUo3NWRPcWFna3RnamFxeFdjLzlrdGRnK21GYWxvYVM2cHNEY3ZXcEYxaHhPTEt0TXVTbVE5dWJaZ0QvOEZ2NktXOGtwTGpHNjhRZVNYZlM0VnRDZ1BsTjg5TTF3U295OUFnTUJBQUV3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQURvZEhOcXlWd0JDaVhTakg0andOeGw2a0hVeFQ4dDdINkdRWWI1NjFJY0NlV1k0TzJYeERpeVl1eThKWktCbzlGKzNKaEY2ZG8wL2FrZmY1YUZGL2M1OVZ1cFFUZmNwMGtjNmRFUWtBV205ZS9BbXZIWlFiMkg2ZkwxQktVdFhZRndlSFdhZmJUdWVaSTVzMzg4SThLY0FHYkl0L3puM0Yza21id1pkT3NScjIyQnlVd3dhanNDaTROR0c1QXBEUTkvQU5CYmhiQ1EvNzIwclJSYjVmejd1cUdZcHRZMG1OaGU5WTFIY21kdHVwVDJWcHY3Z21wNHVjRzRWdzdvSGl6NGNmRHV0R2pYd3pLL0h3SUYxMzNlbStZek1Cd0NiYnhzM09acGgzY0NPOVR3ZTRtbU1VMmZXNFdJWC9abityYXR3MHFxTHppRVJyVWtnY28rYkpVOD08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvS2V5SW5mbz48L2RzOlNpZ25hdHVyZT48U3ViamVjdD48TmFtZUlEIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6dHJhbnNpZW50Ij5lMzkyZTc3Zi03ZGYxLTQxYTEtOWI3ZS0wMjQ0NjE0ZGM5ZGM8L05hbWVJRD48U3ViamVjdENvbmZpcm1hdGlvbiBNZXRob2Q9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpiZWFyZXIiPjxTdWJqZWN0Q29uZmlybWF0aW9uRGF0YSBJblJlc3BvbnNlVG89Il8zYTY0YzVhZWNjMTc1MGE0MmFlNjMxZDU2NTQyMjJlMiIgTm90T25PckFmdGVyPSIyMDIzLTExLTIxVDEzOjE4OjA2LjAwN1oiIFJlY2lwaWVudD0iaHR0cHM6Ly9uYXJmdS1hdXRoLm1vZGV1cy5vcmcvY29tbW9uYXV0aCIgLz48L1N1YmplY3RDb25maXJtYXRpb24+PC9TdWJqZWN0PjxDb25kaXRpb25zIE5vdEJlZm9yZT0iMjAyMy0xMS0yMVQxMzoxMzowMy40NjlaIiBOb3RPbk9yQWZ0ZXI9IjIwMjMtMTEtMjFUMTQ6MTM6MDMuNDY5WiI+PEF1ZGllbmNlUmVzdHJpY3Rpb24+PEF1ZGllbmNlPmh0dHBzOi8vbmFyZnUtYXV0aC5tb2RldXMub3JnL3NhbWwyL21ldGFkYXRhL3NwL25hcmZ1LXByb2Q8L0F1ZGllbmNlPjwvQXVkaWVuY2VSZXN0cmljdGlvbj48L0NvbmRpdGlvbnM+PEF0dHJpYnV0ZVN0YXRlbWVudD48QXR0cmlidXRlIE5hbWU9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpuYW1laWQtZm9ybWF0OnBlcnNpc3RlbnQiPjxBdHRyaWJ1dGVWYWx1ZT5lMzkyZTc3Zi03ZGYxLTQxYTEtOWI3ZS0wMjQ0NjE0ZGM5ZGM8L0F0dHJpYnV0ZVZhbHVlPjwvQXR0cmlidXRlPjxBdHRyaWJ1dGUgTmFtZT0iTkFSRlUtdG8tTW9kZXVzLVVzZXJJRCI+PEF0dHJpYnV0ZVZhbHVlPmUzOTJlNzdmLTdkZjEtNDFhMS05YjdlLTAyNDQ2MTRkYzlkYzwvQXR0cmlidXRlVmFsdWU+PC9BdHRyaWJ1dGU+PEF0dHJpYnV0ZSBOYW1lPSJOQVJGVS10by1Nb2RldXMtUGVyc29uSUQiPjxBdHRyaWJ1dGVWYWx1ZT44NTMxMjhjNi01MzRjLTRiYTgtOGFkZC03YzkyMDYyZWQ5N2M8L0F0dHJpYnV0ZVZhbHVlPjwvQXR0cmlidXRlPjxBdHRyaWJ1dGUgTmFtZT0iTkFSRlUtdG8tTW9kZXVzLURpc3BsYXlOYW1lIj48QXR0cmlidXRlVmFsdWU+0JrRg9C70LXRiNC+0LIg0JLQu9Cw0LTQuNGB0LvQsNCyINCQ0LvQtdC60YHQtdC10LLQuNGHPC9BdHRyaWJ1dGVWYWx1ZT48L0F0dHJpYnV0ZT48QXR0cmlidXRlIE5hbWU9Ik5BUkZVLXRvLU1vZGV1cy1Hcm91cHMiPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELUxlYXJuaW5nUGF0aE1hbmFnZXI9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVBlcmlvZHBsYW5uaW5nUmVzcG9uc2libGVGb3JHcm91cHNEaXN0cmlidXRpb249ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELUVkdWNhdGlvbmFsUHJvY2Vzc0FkbWluaXN0cmF0b3JzPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1DdXJyZW50QWNhZGVtY2lQcm9ncmVzc1dlaWdodHNBZG1pbmlzdHJhdG9ycz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtUmVzcG9uc2libGVGb3JBYnNlbmNlUmVhc29ucz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtQWJzZW5jZVJlYXNvbnNBZG1pbmlzdHJhdG9ycz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtVGVhY2hpbmdQbGFuc0FkbWluaXN0cmF0b3JzPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1Db3Vyc2VDYXRhbG9nQ3JlYXRvcnM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELUNvdXJzZUNhdGFsb2dQdWJsaXNoZXJzPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1Db3Vyc2VDYXRhbG9nQWRtaW5pc3RyYXRvcnM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELUN1cnJpY3VsdW1zQWRtaW5pc3RyYXRvcnM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELUN1cnJpY3VsdW1zUHVibGlzaGVycz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtUGVyaW9kcGxhbm5pbmdBZG1pbmlzdHJhdG9ycz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtUGVyaW9kcGxhbm5pbmdSZXNwb25zaWJsZUZvclBhcnRpYWxQbGFucz1mYWxzZTwvQXR0cmlidXRlVmFsdWU+PEF0dHJpYnV0ZVZhbHVlPk5BUkZVLVBST0QtUGVyaW9kcGxhbm5pbmdSZXNwb25zaWJsZUZvclRlYWNoZXJzPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1QZXJpb2RwbGFubmluZ1Jlc3BvbnNpYmxlRm9yU3R1ZGVudHM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVNjaGVkdWxlQ29udHJvbGxlcnM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVNlbmlvclNjaGVkdWxlQ29udHJvbGxlcnM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVN0dWRlbnRzPXRydWU8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVN0YWZmPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1FbXBsb3llZXM9ZmFsc2U8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5OQVJGVS1QUk9ELVJlc3BvbnNpYmxlRm9yU3R1ZGVudFBlcmZvcm1hbmNlPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1SZXNwb25zaWJsZUZvclN0dWRlbnRzUmF0aW5nPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48QXR0cmlidXRlVmFsdWU+TkFSRlUtUFJPRC1SZXBvcnRzPWZhbHNlPC9BdHRyaWJ1dGVWYWx1ZT48L0F0dHJpYnV0ZT48L0F0dHJpYnV0ZVN0YXRlbWVudD48QXV0aG5TdGF0ZW1lbnQgQXV0aG5JbnN0YW50PSIyMDIzLTExLTIxVDEzOjEzOjAzLjM3NVoiIFNlc3Npb25JbmRleD0iX2I1NmJkY2YyLTIwNjktNDQ5OC04M2NhLTFlNTI4ZTZlNzMwNyI+PEF1dGhuQ29udGV4dD48QXV0aG5Db250ZXh0Q2xhc3NSZWY+dXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFjOmNsYXNzZXM6UGFzc3dvcmRQcm90ZWN0ZWRUcmFuc3BvcnQ8L0F1dGhuQ29udGV4dENsYXNzUmVmPjwvQXV0aG5Db250ZXh0PjwvQXV0aG5TdGF0ZW1lbnQ+PC9Bc3NlcnRpb24+PC9zYW1scDpSZXNwb25zZT4=',
#     'RelayState': 'd44078d3-9194-4ca7-aacd-4d158d35cdf1',
# }

# session.post('https://narfu-auth.modeus.org/commonauth', cookies=cookies, headers=headers, data=data)

# cookies = {
#     '_ym_uid': '1690205781548726742',
#     '_ym_d': '1690205781',
#     'opbs': '85da93ee-e91d-4ae6-94cd-926141400c29',
#     'JSESSIONID': 'B610F8F4F1E986FF4C3DAF1E605CB1EA',
#     'commonAuthId': 'd4bc2a76-1206-4956-9226-8e6a70737989',
#     'tc01': '4d7cf69eef1e74a0ecb0849d35f73378',
# }

# headers = {
#     'authority': 'narfu-auth.modeus.org',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_ym_uid=1690205781548726742; _ym_d=1690205781; opbs=85da93ee-e91d-4ae6-94cd-926141400c29; JSESSIONID=B610F8F4F1E986FF4C3DAF1E605CB1EA; commonAuthId=d4bc2a76-1206-4956-9226-8e6a70737989; tc01=4d7cf69eef1e74a0ecb0849d35f73378',
#     'referer': 'https://sts.narfu.ru/',
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'cross-site',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
# }

# params = {
#     'sessionDataKey': '282a53fc-dde7-4f2d-a0fd-3f9c8055c6ba',
# }

# response = session.get('https://narfu-auth.modeus.org/oauth2/authorize', params=params, cookies=cookies, headers=headers, allow_redirects=True)

# cookies = {
#     '_ym_uid': '1690205781548726742',
#     '_ym_d': '1690205781',
#     'tc01': '4d7cf69eef1e74a0ecb0849d35f73378',
# }

# headers = {
#     'authority': 'narfu.modeus.org',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_ym_uid=1690205781548726742; _ym_d=1690205781; tc01=4d7cf69eef1e74a0ecb0849d35f73378',
#     'if-modified-since': 'Fri, 22 Sep 2023 14:35:57 GMT',
#     'if-none-match': 'W/"650da64d-400"',
#     'referer': 'https://sts.narfu.ru/',
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'cross-site',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
# }

# response = session.get(
#     'https://narfu.modeus.org/schedule-calendar/my?timeZone=%22Europe%2FMoscow%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-27%22%7D&grid=%22Grid.01%22',
#     cookies=cookies,
#     headers=headers,
#     allow_redirects=True
# )
# response.raise_for_status()
cookies = {
    '_ym_uid': '1690205781548726742',
    '_ym_d': '1690205781',
    'tc01': '4d7cf69eef1e74a0ecb0849d35f73378',
    '_ym_isad': '1',
}

headers = {
    'authority': 'narfu.modeus.org',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU',
    'authorization': 'Bearer eyJ4NXQiOiJOMkU0WXpBMVpHWmpZV1ZoTmpJNFl6Z3pNVEkxTTJZMU5HRXdaV1ZsWkRNM1pqVTNOV1l6T0EiLCJraWQiOiJkMGVjNTE0YTMyYjZmODhjMGFiZDEyYTI4NDA2OTliZGQzZGViYTlkIiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiOUw3allCTi1Pb2s4WTM3VVVsM0JTZyIsInN1YiI6ImUzOTJlNzdmLTdkZjEtNDFhMS05YjdlLTAyNDQ2MTRkYzlkYyIsImF1ZCI6WyJZRE5DZUNQc2YxekwyZXRHUWZsaWp5ZnpvODhhIl0sImF6cCI6IllETkNlQ1BzZjF6TDJldEdRZmxpanlmem84OGEiLCJFeHRlcm5hbFBlcnNvbklkIjoiODUzMTI4YzYtNTM0Yy00YmE4LThhZGQtN2M5MjA2MmVkOTdjIiwiaXNzIjoiaHR0cHM6XC9cL25hcmZ1LWF1dGgubW9kZXVzLm9yZzo0NDNcL29hdXRoMlwvdG9rZW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiLQmtGD0LvQtdGI0L7QsiDQktC70LDQtNC40YHQu9Cw0LIg0JDQu9C10LrRgdC10LXQstC40YciLCJleHAiOjE3MDA2NTg3ODgsIm5vbmNlIjoiTjJSMGIzTkVjVVJtY1dWS1JISlhkVU50WDFGT1VHWlFaMEZIZVZWcVpYcHVZM1Z6Wlg1aGRtdFFkRkJVIiwiaWF0IjoxNzAwNTcyMzg4LCJwZXJzb25faWQiOiIxYmE1MzI3ZC02NTYzLTQ5YTAtOTVkYy1kNzkwYTVlMzhjZDAifQ.tJZJitOHr7spWtMRR7dgOqWj3ppaxXN8YxAr1vz5WMOa0XOjZF9adbpxHCbQtren732bxPMIJYNgYhSjOhtR6gkc9C0Gd6NiHGYbxvWGnwbO5qfnKSuQGgD9_5K0YZTB8iDjswO7uw9FIcm1je815-I6vD1AvHKPX8BWwAsiO_oclj9mER95bV2aCwMBsZJdzRAksYMEH7NLLhU0piaducqOQuW3dcQ_COTjVT5cDenGQAzVPRiJzY3fw6znFFF9XSqfI9g8ZrTnrOj3w5j7_r0lCXJIaaw61PpHX3c3YwHXy9CT1UJRd0txAH7MlJNbHm8wvLka28P9j4SfIzyxfw',
    'content-type': 'application/json',
    # 'cookie': '_ym_uid=1690205781548726742; _ym_d=1690205781; tc01=4d7cf69eef1e74a0ecb0849d35f73378; _ym_isad=1',
    'origin': 'https://narfu.modeus.org',
    'referer': 'https://narfu.modeus.org/schedule-calendar/my?timeZone=%22Europe%2FMoscow%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-20%22%7D&grid=%22Grid.01%22',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

json_data = {
    'size': 500,
    'timeMin': '2023-11-19T21:00:00Z',
    'timeMax': '2023-11-26T21:00:00Z',
    'attendeePersonId': [
        '1ba5327d-6563-49a0-95dc-d790a5e38cd0',
    ],
}

response = requests.post(
    'https://narfu.modeus.org/schedule-calendar-v2/api/calendar/events/search?tz=Europe/Moscow&authAction=',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
# soup = BeautifulSoup(response.json)
with open('test.json', 'w') as f:
    f.write(response.text)
# print(f"{response.content}")