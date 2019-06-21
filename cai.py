import random

def random_number(randomt = 3,number = None):
    print('___GAME RESULT')
    if number is None:
        number = []
    while randomt > 0:
        randoms = random.randrange(0,6)
        number.append(randoms)
        randomt = randomt - 1
    return number

def double_number(double):
    dadan = 9 <= double % 2 != 0 <= 18
    xiaodan = 0 <= double %2 != 0 <= 8
    dashuang = 9 <= double % 2 == 0 <= 18
    xiaoshuang = 0 <= double % 2 == 0 <= 8
    if dadan:
        return 'dadan'
    elif xiaodan:
        return 'xiaodan'
    elif dashuang:
        return 'dashaung'
    elif xiaoshuang:
        return 'xiaoshuang'

def dan_shaung(ds):
    dan = 9 <= ds % 2 != 0 <= 18
    shuang = 0 <= ds % 2 == 0 <= 8
    if dan:
        return 'dan'
    elif shuang:
        return 'shuang'

def big_small(dx):
    da = 9 <= dx <= 18
    xiao = 0 <= dx <= 8
    if da:
        return 'da'
    elif xiao:
        return 'xiao'

def game_start():
    youer_money = 0
    recharge = int(input('recharge money:'))
    youer_money = recharge
    while youer_money > 0:
            project = ['da','xiao','dan','shuang','dadan','dashuang']
            buy = input('purchcse item')
            if buy in project:
                bet_money = int(input('bet amonunt:'))
                if bet_money <= youer_money:
                    result = random_number()
                    results = sum(result)
                    daxiao = project == big_small(results)
                    dnshaung = project == dan_shaung(results)
                    dasxiaos = project == double_number(results)
                    if daxiao:
                        print('Lottery result {},you win'.format(result))
                        youer_money = youer_money + bet_money
                        print('This amount of bet in this council {},balance {}'.format(bet_money,youer_money))
                    elif dnshaung:
                        print('Lottery result {},you win'.format(result))
                        youer_money = youer_money + bet_money
                        print('This amount of bet in this council {},balance {}'.format(bet_money, youer_money))
                    elif dasxiaos:
                        print('Lottery result {},you win'.format(result))
                        youer_money = youer_money + bet_money
                        print('This amount of bet in this council {},balance {}'.format(bet_money, youer_money))
                    else:
                        print('Lottery result {},you lose'.format(result))
                        youer_money = youer_money - bet_money
                        print('This amount of bet in this council {},balance {}'.format(bet_money, youer_money))
                else:
                    print('bet error')
            else:
                print('purchcse error')
    else:
        print('GAME OVER')

game_start()