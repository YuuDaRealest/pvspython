import random
from .. import constants as c

class Map():
    def __init__(self, width, height):
        self.width = width       # Chiều rộng bản đồ (số lượng ô ngang)
        self.height = height     # Chiều cao bản đồ (số lượng ô dọc)
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]  
        # Tạo ma trận 2 chiều với kích thước height x width, khởi tạo toàn 0

    def isValid(self, map_x, map_y):
        if (map_x < 0 or map_x >= self.width or
            map_y < 0 or map_y >= self.height):
            return False          # Nếu vị trí vượt ngoài bản đồ => không hợp lệ
        return True               # Ngược lại => hợp lệ
    
    def isMovable(self, map_x, map_y):
        return (self.map[map_y][map_x] == c.MAP_EMPTY)  
        # Kiểm tra ô (map_x, map_y) có rỗng không (có thể trồng cây)
    
    def getMapIndex(self, x, y):
        x -= c.MAP_OFFSET_X  # Trừ đi khoảng lệch theo trục X
        y -= c.MAP_OFFSET_Y  # Trừ đi khoảng lệch theo trục Y
        return (x // c.GRID_X_SIZE, y // c.GRID_Y_SIZE)  
        # Tính chỉ số hàng/cột tương ứng với tọa độ pixel (x, y)
    
    def getMapGridPos(self, map_x, map_y):
        return (map_x * c.GRID_X_SIZE + c.GRID_X_SIZE//2 + c.MAP_OFFSET_X,
                map_y * c.GRID_Y_SIZE + c.GRID_Y_SIZE//5 * 3 + c.MAP_OFFSET_Y)
        # Trả về tọa độ trung tâm của ô (map_x, map_y) trong game (theo pixel)
        # giúp hiển thị cây ở đúng vị trí giữa ô
    
    def setMapGridType(self, map_x, map_y, type):
        self.map[map_y][map_x] = type  # Gán loại (type) cho ô bản đồ tại (x, y)

    def getRandomMapIndex(self):
        map_x = random.randint(0, self.width-1)   # Chọn ngẫu nhiên cột
        map_y = random.randint(0, self.height-1)  # Chọn ngẫu nhiên hàng
        return (map_x, map_y)                     # Trả về chỉ số ô ngẫu nhiên

    def showPlant(self, x, y):
        pos = None                              # Khởi tạo biến vị trí ban đầu là None
        map_x, map_y = self.getMapIndex(x, y)   # Lấy vị trí chỉ số bản đồ từ tọa độ pixel
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            pos = self.getMapGridPos(map_x, map_y)  # Nếu ô hợp lệ và trống thì lấy vị trí chính xác để trồng
        return pos                              # Trả về tọa độ hiển thị cây (hoặc None nếu không hợp lệ)
