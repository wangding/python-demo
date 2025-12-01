% 定义 x 的取值范围和步长（从 -10 到 10，步长 0.1）
x = -10:0.1:10;

% 计算y值
y = sin(x);

% 创建一个占满整个屏幕的窗口
figure('units', 'normalized', 'outerposition', [0 0 1 1]);

% 绘图
plot(x, y, 'b-', 'LineWidth', 2);
grid on;
axis equal;
axis tight;
xlabel('x');
ylabel('y');
title('y = sin(x)');