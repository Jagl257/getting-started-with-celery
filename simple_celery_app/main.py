from simple_celery_app.tasks import add, multiply

TIMEOUT = 10
INTERVAL = 1

if __name__ == "__main__":
    
    # Sending the tasks to the queue

    print("sum_1 -> Adding 2 and 3")
    task1 = add.delay(2,3)
    print("sum_2 -> Adding 6 and 4")
    task2 = add.delay(6,4)

    # Retreving the results from result backend

    sum_1 = task1.wait(timeout=TIMEOUT, interval=INTERVAL)
    sum_2 = task2.wait(timeout=TIMEOUT, interval=INTERVAL)

    print(f"sum_1 = {sum_1}")
    print(f"sum_2 = {sum_2}")
