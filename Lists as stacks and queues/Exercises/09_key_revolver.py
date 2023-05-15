from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())

bullets_counter = 0
is_safe_opened = False

while True:
    if not locks:
        is_safe_opened = True
        print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_counter * bullet_price}")
        break

    if not bullets:
        break

    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    else:
        print("Bang!")

    bullets_counter += 1

    if bullets_counter % gun_barrel == 0 and bullets:
        print("Reloading!")

if not is_safe_opened:
    print(f"Couldn't get through. Locks left: {len(locks)}")
