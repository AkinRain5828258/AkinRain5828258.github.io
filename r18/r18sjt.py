<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>轻量随机图</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #e6f7ff;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            width: 100%;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 120, 180, 0.1);
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #0078b4;
            margin: 0 0 20px;
        }
        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }
        select, button {
            padding: 8px 12px;
            border: 2px solid #4db8ff;
            border-radius: 5px;
            background: white;
            color: #0078b4;
            font-weight: bold;
        }
        button {
            background: #4db8ff;
            color: white;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background: #0078b4;
        }
        button:disabled {
            background: #ccc;
            cursor: wait;
        }
        .image-container {
            margin: 15px 0;
            min-height: 300px;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #f0f9ff;
            border-radius: 5px;
        }
        #randomImage {
            max-width: 100%;
            max-height: 60vh;
            display: none;
            border-radius: 3px;
        }
        .loading {
            display: none;
            width: 30px;
            height: 30px;
            border: 3px solid #4db8ff;
            border-top-color: transparent;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        footer {
            margin-top: 20px;
            color: #7fbfff;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>轻量随机图</h1>
        
        <div class="controls">
            <select id="category">
                <option value="all">全部</option>
                <option value="pc">横屏</option>
                <option value="mp">竖屏</option>
                <option value="furry">兽耳</option>
            </select>
            
            <select id="size">
                <option value="large">大图</option>
                <option value="mw1024">1024px</option>
                <option value="small">小图</option>
            </select>
            
            <button id="refreshBtn">获取图片</button>
        </div>
        
        <div class="image-container">
            <div class="loading" id="loading"></div>
            <img id="randomImage" alt="随机图片">
        </div>
        
        <footer>
            使用 <a href="https://image.anosu.top/" target="_blank" style="color:#4db8ff">anosu.top API</a>
        </footer>
    </div>

    <script>
        const refreshBtn = document.getElementById('refreshBtn');
        const randomImage = document.getElementById('randomImage');
        const loading = document.getElementById('loading');
        
        // 获取图片函数
        function getRandomImage() {
            const category = document.getElementById('category').value;
            const size = document.getElementById('size').value;
            
            // 显示加载状态
            randomImage.style.display = 'none';
            loading.style.display = 'block';
            refreshBtn.disabled = true;
            
            // 构建API URL (使用302跳转)
            const apiUrl = `https://image.anosu.top/pixiv/direct?sort=${category}&size=${size}&t=${Date.now()}`;
            
            // 预加载图片
            const img = new Image();
            img.onload = function() {
                randomImage.src = this.src;
                randomImage.style.display = 'block';
                loading.style.display = 'none';
                refreshBtn.disabled = false;
            };
            img.onerror = function() {
                loading.style.display = 'none';
                alert('图片加载失败，请重试');
                refreshBtn.disabled = false;
            };
            img.src = apiUrl;
        }
        
        // 初始加载和按钮点击
        getRandomImage();
        refreshBtn.addEventListener('click', getRandomImage);
    </script>
</body>
</html>