% 清除环境
clear; clc; close all;

% 1. 符号计算梯度 (您截图中的原始代码)
syms x y;
f = x^2 * y^3;
gradf = gradient(f); % 计算梯度 [df/dx; df/dy]
fprintf('函数 f 的梯度为:\n');
disp(gradf);

% 2. 为数值绘图创建网格
[x_vals, y_vals] = meshgrid(linspace(-2, 2, 30)); % 在[-2,2]区间创建30x30的网格

% 3. 将符号表达式转换为数值计算函数
%   使用 matlabFunction 将符号表达式 f 和 gradf 转换为快速的数值函数
f_numeric = matlabFunction(f, 'Vars', [x, y]);
df_dx_numeric = matlabFunction(gradf(1), 'Vars', [x, y]);
df_dy_numeric = matlabFunction(gradf(2), 'Vars', [x, y]);

% 4. 在网格点上计算函数值和梯度分量值
Z = f_numeric(x_vals, y_vals); % 计算曲面高度
U = df_dx_numeric(x_vals, y_vals); % 计算梯度向量的X分量
V = df_dy_numeric(x_vals, y_vals); % 计算梯度向量的Y分量

% 5. 绘制图形
figure('Position', [100, 100, 1200, 500]); % 设置一个宽幅图形窗口

% 子图1：绘制函数曲面
subplot(1, 2, 1);
surf(x_vals, y_vals, Z, 'EdgeColor', 'none'); % 绘制曲面，隐藏网格线
title('函数曲面: f(x, y) = x^2y^3', 'FontSize', 12);
xlabel('x');
ylabel('y');
zlabel('f(x,y)');
colormap(jet); % 设置颜色映射
colorbar; % 显示颜色条
axis tight;

% 子图2：绘制梯度向量场
subplot(1, 2, 2);
% 使用 quiver 绘制梯度向量场
% U 和 V 决定了箭头的方向和大小
quiver(x_vals, y_vals, U, V, 'LineWidth', 1.5);
title('梯度向量场: \nabla f = (2xy^3, 3x^2y^2)', 'FontSize', 12);
xlabel('x');
ylabel('y');
axis equal tight; % 保持坐标轴比例一致
grid on;

% 可选：在一个新图中叠加显示曲面和梯度场
figure;
surf(x_vals, y_vals, Z, 'EdgeColor', 'none', 'FaceAlpha', 0.7);
hold on;
quiver3(x_vals, y_vals, zeros(size(Z)), U, V, zeros(size(Z)), 'r', 'LineWidth', 1.5);
title('函数曲面与梯度向量场叠加图');
xlabel('x');
ylabel('y');
zlabel('f(x,y)');
colorbar;
hold off;