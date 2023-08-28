import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
SCREEN_SIZE = (400, 400)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Chess Game')

# Kích thước ô cờ và kích thước hình ảnh quân cờ
SQUARE_SIZE = 50
PIECE_SIZE = 45

# Tải hình ảnh quân cờ
pieces = {
    'R': pygame.image.load('rook.png'),
    'N': pygame.image.load('knight.png'),
    'B': pygame.image.load('bishop.png'),
    'Q': pygame.image.load('queen.png'),
    'K': pygame.image.load('king.png'),
    'P': pygame.image.load('pawn.png'),
    'r': pygame.image.load('rook.png'),
    'n': pygame.image.load('knight.png'),
    'b': pygame.image.load('bishop.png'),
    'q': pygame.image.load('queen.png'),
    'k': pygame.image.load('king.png'),
    'p': pygame.image.load('pawn.png')
}

# Đại diện cho trạng thái ban đầu của bàn cờ
chess_board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
]

# Vẽ bàn cờ
def draw_board():
    for row in range(8):
        for col in range(8):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Main loop
running = True
selected_piece = None
clock = pygame.time.Clock()

# Hàm kiểm tra xem nước đi có hợp lệ cho quân mã hay không
def is_valid_knight_move(board, start, end):
    dx = abs(end[1] - start[1])
    dy = abs(end[0] - start[0])
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

# Hàm kiểm tra xem nước đi có hợp lệ cho quân tượng hay không
def is_valid_bishop_move(board, start, end):
    dx = abs(end[1] - start[1])
    dy = abs(end[0] - start[0])
    return dx == dy

# Hàm kiểm tra xem nước đi có hợp lệ cho quân xe hay không
def is_valid_rook_move(board, start, end):
    return start[0] == end[0] or start[1] == end[1]

def is_valid_move(board, start, end):
    piece = board[start[0]][start[1]]
    target_piece = board[end[0]][end[1]]
    
    # Kiểm tra xem điểm đích có phải là ô trống hoặc có quân cờ của màu khác không
    if target_piece != ' ' and target_piece.isupper() == piece.isupper():
        return False
    
    # Kiểm tra nước đi cho từng quân cờ cơ bản
    if piece == 'P' or piece == 'p':  # Tốt
        if piece == 'P' and start[0] == 1 and end[0] == 3 and board[2][start[1]] == ' ':
            return True  # Nước đi xuất phát 2 ô cho tốt trắng
        elif piece == 'p' and start[0] == 6 and end[0] == 4 and board[5][start[1]] == ' ':
            return True  # Nước đi xuất phát 2 ô cho tốt đen
        elif abs(end[1] - start[1]) == 1 and abs(end[0] - start[0]) == 1:
            return target_piece != ' '  # Nước đi ăn chéo
        
        # Nước đi tiến thẳng
        return start[1] == end[1] and (end[0] - start[0] == 1 if piece == 'P' else start[0] - end[0] == 1) and target_piece == ' '
    
    elif piece == 'N' or piece == 'n':  # Mã
        return is_valid_knight_move(board, start, end)
    
    elif piece == 'B' or piece == 'b':  # Tượng
        return is_valid_bishop_move(board, start, end)
    
    elif piece == 'R' or piece == 'r':  # Xe
        return is_valid_rook_move(board, start, end)
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // SQUARE_SIZE
            row = event.pos[1] // SQUARE_SIZE
            
            if selected_piece is None:
                piece = chess_board[row][col]
                if piece != ' ':
                    selected_piece = (row, col)
            else:
                target_piece = chess_board[row][col]
                if (row, col) != selected_piece and is_valid_move(chess_board, selected_piece, (row, col)):
                    chess_board[row][col] = chess_board[selected_piece[0]][selected_piece[1]]
                    chess_board[selected_piece[0]][selected_piece[1]] = ' '
                    selected_piece = None

    screen.fill((0, 0, 0))  # Xóa màn hình
    draw_board()  # Vẽ bàn cờ

    if selected_piece is not None:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(selected_piece[1] * SQUARE_SIZE, selected_piece[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

    # Hiển thị hình ảnh quân cờ
    for row in range(8):
        for col in range(8):
            piece = chess_board[row][col]
            if piece != ' ':
                screen.blit(pieces[piece], (col * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) / 2, row * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) / 2))

    pygame.display.flip()  # Cập nhật màn hình
    clock.tick(30)  # Giới hạn tốc độ khung hình

pygame.quit()
