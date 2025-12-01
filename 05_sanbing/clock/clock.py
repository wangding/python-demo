import os
import re
import threading
import time
import winsound

import ctypes
from ctypes import wintypes

# 定义必要的 Windows API 函数
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
kernel32.SetConsoleTitleW.argtypes = [wintypes.LPCWSTR]
kernel32.SetConsoleTitleW.restype = wintypes.BOOL

# 设置控制台窗口标题
kernel32.SetConsoleTitleW("sb_clock")

class Timer:
  def __init__(self, name, duration_minutes, index):
    self.name   = name
    self.index  = index
    self.thread = None
    self.stop_event = threading.Event()
    self.duration_minutes = duration_minutes
    self.start_time = time.time()  # 记录定时器创建的时间

  def start(self, callback):
    self.thread = threading.Thread(target=self._timer_thread, args=(callback,))
    self.thread.daemon = True
    self.thread.start()

  def _timer_thread(self, callback):
    duration_seconds = self.duration_minutes * 60
    elapsed = 0

    while elapsed < duration_seconds:
      if self.stop_event.is_set(): return
      time.sleep(1)
      elapsed = time.time() - self.start_time

    if not self.stop_event.is_set():
      print(f"定时器时间到: {self.name}")
      # 循环播放声音2次
      for _ in range(2):
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
        time.sleep(0.5)  # 短暂暂停避免声音重叠
      callback(self.index)

  def stop(self):
    self.stop_event.set()
    if self.thread: self.thread.join(timeout=1)

class ClockProgram:
  def __init__(self):
    self.timers     = []
    self.next_index = 1

  def extract_duration(self, name):
    # 提取名字末尾的数字作为时长
    match = re.search(r'(\d+)$', name)
    if match: return int(match.group(1))
    return 0

  def add_timer(self, name):
    duration = self.extract_duration(name)
    timer    = Timer(name, duration, self.next_index)
    timer.start(self.on_timer_finish)
    self.timers.append(timer)
    self.next_index += 1
    print(f"已添加定时器: {name} (时长: {duration}分钟)")

  def list_timers(self):
    if not self.timers:
      print("没有活动的定时器")
      return
    
    # 按剩余时长升序排列
    current_time = time.time()
    # 计算每个定时器的剩余时长（秒）
    for timer in self.timers:
      elapsed = current_time - timer.start_time
      timer.remaining_seconds = max(0, timer.duration_minutes * 60 - elapsed)
    
    sorted_timers = sorted(self.timers, key=lambda t: t.remaining_seconds)
    for timer in sorted_timers:
      # 格式化剩余时间为分:秒
      minutes = int(timer.remaining_seconds // 60)
      seconds = int(timer.remaining_seconds % 60)
      print(f"{timer.index:02d} {timer.name} (剩余: {minutes:02d}:{seconds:02d})")

  def remove_timer(self, index):
    for i, timer in enumerate(self.timers):
      if timer.index == index:
        timer.stop()
        del self.timers[i]
        print(f"已删除定时器: {timer.name}")
        return
    print("错误: 找不到指定索引的定时器")

  def on_timer_finish(self, index):
    for i, timer in enumerate(self.timers):
      if timer.index == index:
        del self.timers[i]
        break

  def stop_all_timers(self):
    for timer in self.timers: timer.stop()
    self.timers.clear()

  def parse_command(self, command):
    parts = command.strip().split(' ', 1)
    cmd = parts[0].lower()
    
    if cmd == 'add' and len(parts) > 1: self.add_timer(parts[1])
    elif cmd == 'ls':  self.list_timers()
    elif cmd == 'exit': return False
    elif cmd == 'rm' and len(parts) > 1:
      try:
        index = int(parts[1])
        self.remove_timer(index)
      except ValueError:
        print("错误: 无效的索引")
    else: print("未知命令，请使用 add、ls、rm 或 exit")
    return True

  def run(self):
    print("命令行定时器程序启动")
    print("可用命令: add <name>, ls, rm <index>, exit")

    try:
      while True:
        command = input("请输入命令: ")
        if not self.parse_command(command): break
    except KeyboardInterrupt: print("\n程序被用户中断")
    finally:
      self.stop_all_timers()
      print("程序已退出")

if __name__ == "__main__":
  program = ClockProgram()
  program.run()