import pygame

pygame.init()

#Tạo kích thước màn hình cho game
SCREEN_SIZE=(540,540)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Welcome to Sudoku")

#Mã màu RGB cho các đối tượng
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (198, 0, 0)
BLUE = (0, 0, 255)

#Vẽ bảng cho game, khởi tạo các thông số dòng kẻ                           
def create_board(board):
    screen.fill(WHITE)
    for i in range(0, 10):            #Nếu i ứng với các dòng kẻ tại viền ngoài thì tô đậm
        linesize = 1
        if i % 3 == 0:
            linesize = 4
        pygame.draw.line(screen, RED, (50 + 50 * i, 50), (50 + 50 * i, 500), linesize)  
        pygame.draw.line(screen, RED, (50, 50 + 50 * i), (500, 50 + 50 * i), linesize)

# Khởi tạo cỡ chữ và tọa độ các số trên bảng              
    font = pygame.font.SysFont('Arial', 42, True, False)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = font.render(str(board[i][j]), True, BLACK)  
                x = j * 50 + 65
                y = i * 50 + 50
                screen.blit(num, (x, y))

def solve(board, row, col, num):
    # Kiểm tra giá trị bị trùng lặp trên các Dòng
    for i in range(9):
        if board[row][i] == num:       
            return False

    # # Kiểm tra giá trị bị trùng lặp trên các Cột
    for i in range(9):
        if board[i][col] == num:       
            return False

    # # Kiểm tra giá trị bị trùng lặp trong các ô vuông 3x3
    square_row = (row // 3) * 3                          
    square_col = (col // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False
    return True

def handle_input(board, click):
    # con trỏ chuột
    set_mouse = pygame.mouse.get_pos()

    #Kiểm tra xem người dùng đã click vào ô hay chưa?
    if 50 <= set_mouse[0] <= 500 and 50 <= set_mouse[1] <= 500:
        row = (set_mouse[1] - 50) // 50
        col = (set_mouse[0] - 50) // 50
        click = (row, col)

    # Kiểm tra xem người dùng đã nhập số hay chưa?
    keys = pygame.key.get_pressed()
    for i in range(1, 10):
        if keys[pygame.K_KP1 + i - 1] or keys[pygame.K_1 + i - 1]:
            if click is not None:
                row, col = click
                if solve(board, row, col, i):
                    board[row][col] = i

    return click

def start_game():
    board = [                            #Tạo bảng và nhập các số, các số 0 tương ứng với ô trống
        [9, 0, 2, 1, 0, 3, 0, 5, 7],     
        [0, 3, 0, 2, 0, 0, 9, 4, 1],
        [8, 0, 1, 0, 5, 0, 0, 3, 0],
        [0, 2, 7, 8, 0, 0, 4, 6, 5],
        [1, 0, 0, 0, 0, 6, 0, 0, 8],
        [6, 0, 8, 7, 0, 0, 1, 0, 3],
        [0, 6, 5, 4, 0, 1, 0, 8, 0],
        [7, 0, 9, 0, 3, 0, 5, 0, 4],
        [4, 0, 0, 5, 0, 8, 0, 7, 0]
    ]

    click = None
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        click = handle_input(board, click)

        create_board(board)

        if click is not None:
            row, col = click
            pygame.draw.rect(screen, BLUE, (50 + col * 50, 50 + row * 50, 50, 50), 3)

        pygame.display.update()
        clock.tick(40)

start_game()