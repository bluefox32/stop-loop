import threading
import time
import os

# レスポンスタイムを記録するための辞書
process_times = {}

def process_task(name, delay):
    start_time = time.time()
    
    # 遅延のシミュレーション
    time.sleep(delay)
    
    # プロセスが処理するデータ（ここでは例として固定のデータ）
    data = "sample_data"
    
    end_time = time.time()
    response_time = end_time - start_time
    
    # レスポンスタイムを記録
    process_times[name] = response_time
    
    print(f"{name} completed in {response_time:.2f} seconds")

    # 重複データの確認
    if check_duplicate_data(data, name):
        print(f"Process {name} stopped due to duplicate data.")
        stop_process(name)

def check_duplicate_data(data, current_process_name):
    # 他のプロセスが同じデータを処理しているか確認
    for process_name, response_time in process_times.items():
        if process_name != current_process_name and process_times.get(process_name) == response_time:
            return True
    return False

def stop_process(name):
    # ここでプロセスを終了する実際のコードを実装
    print(f"Stopping process: {name}")
    # threading.currentThread().do_run = False  # スレッドを終了させる例

# スレッドの作成と実行
threads = []
delays = [1, 3, 2]  # 各プロセスの遅延（レスポンスタイムに影響）

for i, delay in enumerate(delays):
    thread = threading.Thread(target=process_task, args=(f"Process_{i+1}", delay))
    threads.append(thread)
    thread.start()

# すべてのスレッドが完了するのを待つ
for thread in threads:
    thread.join()

# 最速のプロセスを優先
fastest_process = min(process_times, key=process_times.get)
print(f"The fastest process is: {fastest_process} (Priority)")

# 他のプロセスを停止
for process_name in process_times:
    if process_name != fastest_process:
        stop_process(process_name)