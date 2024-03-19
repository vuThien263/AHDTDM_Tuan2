from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Khởi tạo danh sách arr
        self.arr = []

    def bubble_sort(self):
      n = len(self.arr)
      for i in range(n):
          swapped = False
          for j in range(0, n - i - 1):
              if self.arr[j] > self.arr[j + 1]:
                  self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                  swapped = True
          if not swapped:
              break

  
    def button_1_click(self, **event_args):
        input_string = self.text_box_1.text
        string_list = input_string.split()
        # Chuyển đổi các phần tử của danh sách từ chuỗi sang số nguyên
        self.arr = [int(item) for item in string_list]
        self.bubble_sort()
        self.text_box_2.text = ' '.join(map(str, self.arr))
  # Hiển thị kết quả sắp xếp

    def text_box_1_change(self, **event_args):
        # Xóa sự kiện "change" trước khi gán lại để tránh việc gọi đệ quy vô hạn
        self.text_box_1.set_event_handler("change", self.text_box_1_change)

   

    def outlined_button_1_click(self, **event_args):
      self.text_box_1.text=""
      self.text_box_2.text=""
      pass
