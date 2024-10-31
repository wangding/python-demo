import sys

# run python3 03-cmd-argv.py
# run python3 03-cmd-argv.py a b c

print(sys.argv)
print(sys.argv[1])

# 命令行参数解包
script, argv1, argv2, argv3 = sys.argv
print(script, argv1, argv2, argv3)