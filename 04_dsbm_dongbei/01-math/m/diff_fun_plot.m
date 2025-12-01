% 清除环境
clear; clc; close all;

% 1. 符号计算偏导数（原代码部分）
syms x y;
f = x^y - y^x;  % 定义函数 f(x,y) = x^y - y^x

% 计算偏导数
df_dx = diff(f, x);  % 对x的偏导数
df_dy = diff(f, y);  % 对y的偏导数

% 显示结果
fprintf('函数 f(x,y) = x^y - y^x\n');
fprintf('对x的偏导数: ');
disp(df_dx);
fprintf('对y的偏导数: ');
disp(df_dy);

% 2. 创建网格点用于绘图
[x_vals, y_vals] = meshgrid(0.1:0.1:3, 0.1:0.1:3);  % 避免0和负值，因为幂函数可能产生复数

% 3. 将符号表达式转换为数值函数
f_numeric = matlabFunction(f, 'Vars', [x, y]);
df_dx_numeric = matlabFunction(df_dx, 'Vars', [x, y]);
df_dy_numeric = matlabFunction(df_dy, 'Vars', [x, y]);

% 4. 计算函数值（处理可能的复数结果）
try
    Z_f = f_numeric(x_vals, y_vals);
    Z_dfdx = df_dx_numeric(x_vals, y_vals);
    Z_dfdy = df_dy_numeric(x_vals, y_vals);
    
    % 如果结果是复数，只取实部
    if ~isreal(Z_f)
        Z_f = real(Z_f);
        fprintf('注意: 函数值包含复数部分，已取实部绘图\n');
    end
    if ~isreal(Z_dfdx)
        Z_dfdx = real(Z_dfdx);
    end
    if ~isreal(Z_dfdy)
        Z_dfdy = real(Z_dfdy);
    end
    
    % 5. 绘制三维曲面图
    figure('Position', [100, 100, 1200, 900]);
    
    % 子图1: 原函数 f(x,y) = x^y - y^x
    subplot(2, 2, [1, 2]);
    surf(x_vals, y_vals, Z_f, 'EdgeColor', 'none');
    title('原函数: f(x,y) = x^y - y^x', 'FontSize', 14, 'FontWeight', 'bold');
    xlabel('x', 'FontSize', 12);
    ylabel('y', 'FontSize', 12);
    zlabel('f(x,y)', 'FontSize', 12);
    colorbar;
    colormap(jet);
    shading interp;
    
    % 子图2: 对x的偏导数
    subplot(2, 2, 3);
    surf(x_vals, y_vals, Z_dfdx, 'EdgeColor', 'none');
    title('偏导数: ∂f/∂x', 'FontSize', 14, 'FontWeight', 'bold');
    xlabel('x', 'FontSize', 12);
    ylabel('y', 'FontSize', 12);
    zlabel('∂f/∂x', 'FontSize', 12);
    colorbar;
    colormap(jet);
    shading interp;
    
    % 子图3: 对y的偏导数
    subplot(2, 2, 4);
    surf(x_vals, y_vals, Z_dfdy, 'EdgeColor', 'none');
    title('偏导数: ∂f/∂y', 'FontSize', 14, 'FontWeight', 'bold');
    xlabel('x', 'FontSize', 12);
    ylabel('y', 'FontSize', 12);
    zlabel('∂f/∂y', 'FontSize', 12);
    colorbar;
    colormap(jet);
    shading interp;
    
    % 6. 添加梯度向量场（可选）
    figure;
    % 创建更稀疏的网格用于显示梯度向量
    [x_grad, y_grad] = meshgrid(0.5:0.5:3, 0.5:0.5:3);
    U = df_dx_numeric(x_grad, y_grad);
    V = df_dy_numeric(x_grad, y_grad);
    
    % 只取实部
    if ~isreal(U), U = real(U); end
    if ~isreal(V), V = real(V); end
    
    % 绘制梯度场
    quiver(x_grad, y_grad, U, V, 2, 'LineWidth', 1.5, 'Color', 'r');
    title('梯度向量场: ∇f = (∂f/∂x, ∂f/∂y)', 'FontSize', 14, 'FontWeight', 'bold');
    xlabel('x', 'FontSize', 12);
    ylabel('y', 'FontSize', 12);
    axis([0.1, 3, 0.1, 3]);
    grid on;
    
catch ME
    fprintf('计算或绘图过程中出现错误: %s\n', ME.message);
    fprintf('尝试调整定义域范围...\n');
end

fprintf('\n绘图完成！\n');