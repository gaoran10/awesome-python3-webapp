import asyncio

import www.orm as orm
from www.models import User

@asyncio.coroutine
def save_test(loop):
    yield from orm.create_pool(loop=loop, host='123.206.178.243', user='admin', password='Admin123123', db='awesome')

    u = User(name='sanji', email='sanji@126.com', passwd='123123', image='about:blank')
    yield from u.save()

@asyncio.coroutine
def find_test(loop):
    yield from orm.create_pool(loop=loop, host='123.206.178.243', user='admin', password='Admin123123', db='awesome')

    u = yield from User().find('001502421565775576b9c8a80e847e3b6ca4f45e5573712000')
    print(u)

# print(u.__select__)
# print(u.__insert__)
# print(u.__update__)
# print(u.__delete__)

loop = asyncio.get_event_loop()
task = [find_test(loop)]
loop.run_until_complete(asyncio.wait(task))
loop.close()