import time
from web_app_with_celery import celery

@celery.task
def generate_file(num: int) -> None:
    with open('fizz_buzz_file.txt', 'w') as f:
        if num:
            for line in fizz_buzz(num):
                print(line)
                time.sleep(1)
                f.write(f"{line}\n")
        else:
            f.write("No number")

def fizz_buzz(limit: int) -> list[int]:
    return [
        "Fizz"*(num%3==0)+"Buzz"*(num%5==0) 
        or str(num) 
        for num in range(1, limit + 1)
    ]
