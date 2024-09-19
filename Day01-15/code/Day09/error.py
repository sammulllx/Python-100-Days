def test_raise():
    print("Before raise")
    raise ValueError("An error occurred")
    print("After raise")  # 这行代码不会被执行


test_raise()

# try:
#     test_raise()
# except ValueError as e:
#     print(f"Caught an exception: {e}")

# 输出:
# Before raise
# Caught an exception: An error occurred
