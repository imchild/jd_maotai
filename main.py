import sys
from maotai.jd_spider_requests import JdSeckill

if __name__ == '__main__':
    a = """
 ___               _         _
(  _`\            ( )       (_ )
| (_) ) _   _    _| |   _ _  | |    _ _
|  _ <'( ) ( ) /'_` | /'_` ) | |  /'_` )
| (_) )| (_) |( (_| |( (_| | | | ( (_| |
(____/'`\___/'`\__,_)`\__,_)(___)`\__,_)
功能列表：
 1.预约商品
 2.秒杀抢购商品
    """
    print(a)

    jd_seckill = JdSeckill()
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice == '1':
            print('选择为预约')
            jd_seckill.reserve()
        elif choice == '2':
            print('选择为抢购')
            jd_seckill.seckill_by_proc_pool()
        else:
            print('参数1为预约，参数2为抢购')
            sys.exit(1)
    choice_function = input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)
