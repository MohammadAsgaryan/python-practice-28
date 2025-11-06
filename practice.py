import time

def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = round(end_time - start_time, 6)

        log_text = (
            f"Function: {func.__name__}\n"
            f"Args: {args}, Kwargs: {kwargs}\n"
            f"Result: {result}\n"
            f"Execution Time: {duration} seconds\n"
            "-----------------------------\n"
        )

        # ذخیره لاگ داخل فایل
        with open("log.txt", "a") as file:
            file.write(log_text)

        return result

    return wrapper


@logger
def multiply(a, b):
    time.sleep(1)  # شبیه‌سازی عملیات سنگین
    return a * b


@logger
def hello(name):
    return f"Hello, {name}!"


print(multiply(5, 7))
print(hello("Mohammad"))
