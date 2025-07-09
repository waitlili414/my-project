import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 贪吃蛇和食物的大小
BLOCK_SIZE = 20

# 初始化贪吃蛇
snake_pos = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
snake_direction = 'RIGHT'

# 初始化食物位置
food_pos = (random.randrange(1, (WINDOW_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (WINDOW_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE)

# 初始化时钟
clock = pygame.time.Clock()

# 初始化分数
score = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 处理按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
    
    # 移动贪吃蛇
    if snake_direction == 'UP':
        new_head = (snake_pos[0][0], snake_pos[0][1] - BLOCK_SIZE)
    if snake_direction == 'DOWN':
        new_head = (snake_pos[0][0], snake_pos[0][1] + BLOCK_SIZE)
    if snake_direction == 'LEFT':
        new_head = (snake_pos[0][0] - BLOCK_SIZE, snake_pos[0][1])
    if snake_direction == 'RIGHT':
        new_head = (snake_pos[0][0] + BLOCK_SIZE, snake_pos[0][1])
    
    # 检查是否吃到食物
    if new_head == food_pos:
        score += 1
        food_pos = (random.randrange(1, (WINDOW_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                    random.randrange(1, (WINDOW_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE)
    else:
        snake_pos.pop()
    
    # 在头部添加新位置
    snake_pos.insert(0, new_head)
    
    # 检查碰撞
    if (new_head[0] >= WINDOW_WIDTH or new_head[0] < 0 or
        new_head[1] >= WINDOW_HEIGHT or new_head[1] < 0 or
        new_head in snake_pos[1:]):
        pygame.quit()
        sys.exit()
    
    # 绘制游戏界面
    window.fill(BLACK)
    
    # 绘制贪吃蛇
    for pos in snake_pos:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # 绘制食物
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # 显示分数
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'分数: {score}', True, WHITE)
    window.blit(score_text, (10, 10))
    
    # 更新显示
    pygame.display.flip()
    
    # 控制游戏速度
    clock.tick(10)