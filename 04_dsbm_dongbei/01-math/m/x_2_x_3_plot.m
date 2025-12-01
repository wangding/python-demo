% 定义x的取值范围和步长（例如从-5到5，步长0.1）
x = -5:0.1:5;

% 计算y值
y1 = x.^2;  % 注意使用点乘幂 (.^) 进行逐元素运算
y2 = x.^3;

% 创建一个占满整个屏幕的窗口
figure('units', 'normalized', 'outerposition', [0 0 1 1]);

subplot(1,2,1); % 将窗口分为1行2列，并激活第1个子图[2,8](@ref)
plot(x, y1, 'b-', 'LineWidth', 2);
grid on;
xlabel('x'); ylabel('y');
title('y = x^2');

subplot(1,2,2); % 激活第2个子图
plot(x, y2, 'r--', 'LineWidth', 2);
grid on;
xlabel('x'); ylabel('y');
title('y = x^3');