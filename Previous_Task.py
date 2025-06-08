import asyncio
import time

class AsyncTask:
    def __init__(self, name, delay, description):  # ✅ исправлено
        self.name = name
        self.delay = delay
        self.description = description

    async def run(self):
        start_time = time.time()
        print(f"[{time.strftime('%H:%M:%S', time.localtime(start_time))}] Начало {self.description}...")
        await asyncio.sleep(self.delay)
        end_time = time.time()
        print(f"[{time.strftime('%H:%M:%S', time.localtime(end_time))}] {self.description} завершена. Длительность: {end_time - start_time:.2f} секунд.")
        return f"Результат {self.name}"

class Program:
    def __init__(self):  # ✅ исправлено
        self.tasks = []

    def add_task(self, task: AsyncTask):
        self.tasks.append(task)

    async def run(self):
        program_start_time = time.time()
        print(f"[{time.strftime('%H:%M:%S', time.localtime(program_start_time))}] Программа запущена.")

        results = await asyncio.gather(*(task.run() for task in self.tasks))

        print()
        for result in results:
            print(result)

        program_end_time = time.time()
        print(f"[{time.strftime('%H:%M:%S', time.localtime(program_end_time))}] Программа завершена.")
        print(f"Общая продолжительность работы программы: {program_end_time - program_start_time:.2f} секунд.")

# ✅ исправлено имя точки входа
if __name__ == "__main__":
    program = Program()
    program.add_task(AsyncTask("загрузки", 3, "загрузки файла"))
    program.add_task(AsyncTask("обработки", 2, "обработки данных"))

    asyncio.run(program.run())