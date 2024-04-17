
![DF](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/3b979e1c-ac6d-4010-aa71-502b65f3513f)



# DepthFM IN COMFYUI

Unofficial implementation of [DepthFM](https://github.com/CompVis/depth-fm) for ComfyUI


https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/4d4b1e53-130e-449a-a065-5c066355d7b4


## 项目介绍 | Info

- 对 [DepthFM](https://github.com/CompVis/depth-fm) 的非官方实现

- DepthFM：CompVis 推出的 高效 + 多功能 深度估计模型
  
- 版本：V1.0 同时支持图像和视频深度估计


![Dingtalk_20240322220914](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/6ceb051e-8eac-4cff-acfc-bfb9921a9686)


## 节点说明 | Features

- DepthFM 模型加载 | 🌆DepthFM ModelLoader
    - 手动下载 [depthfm-v1](https://ommer-lab.com/files/depthfm/depthfm-v1.ckpt) 放入 `/ComfyUI/models/depthfm` 中
    
- 单图深度估计 | 🌆DepthFM
    - steps：普通建议 2-4 步，精细建议 10 步
    - ensemble_size：越高越准确，高值对显存要求高，一般建议 2-4 左右
    - 注意：图像尺寸需为 64 倍数
    
- 多图/视频深度估计| 🌆DepthFM Literative
    - 同时支持 图像 和 视频
    - steps：普通建议 2-4 步，精细建议 10 步
    - ensemble_size：越高越准确，高值对显存要求高，一般建议 2-4 左右
    - - 注意：图像/视频尺寸需为 64 倍数

 
![Dingtalk_20240322221331](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/bff49c26-d55b-4a43-8962-0237d9dd2c0c)




## 安装 | Install

- 推荐使用管理器 ComfyUI Manager 安装（On The Way）

- 手动安装：
    1. `cd custom_nodes`
    2. `git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM`
    3. `cd custom_nodes/ComfyUI-DepthFM`
    4. `pip install -r requirements.txt`
    5. 重启 ComfyUI


## 工作流 | Workflows

V1.0（注：工作流中的着色节点来自于[ComfyUI-Marigold](https://github.com/kijai/ComfyUI-Marigold)，非必要）

  - [V1.0 DepthFM img](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/blob/main/DepthFM%20Workflows/%F0%9F%8C%86DepthFM%20Image%E3%80%90Zho%E3%80%91.json)

    ![Dingtalk_20240322212751](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/d465eee6-f9f5-45e7-bdb9-0d8851e53d8b)


  - [V1.0 DepthFM Literative Video](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/blob/main/DepthFM%20Workflows/%F0%9F%8C%86DepthFM%20Literative%20Video%E3%80%90Zho%E3%80%91.json)
    
    ![Dingtalk_20240322220239](https://github.com/ZHO-ZHO-ZHO/ComfyUI-DepthFM/assets/140084057/33ffe05f-26f7-4426-9dfa-ff9f7196cf69)



## 更新日志

- 20240322

  V1.0 同时支持 图像和视频 深度估计

  创建项目
  

## 声明

  演示视频未经允许请勿搬运！！！


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/ComfyUI-DepthFM&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/ComfyUI-DepthFM&Date)


## 关于我 | About me

📬 **联系我**：
- 邮箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒体**：
- 个人页：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主页](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小红书：[我的小红书主页](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充电](https://space.bilibili.com/484366804)
- 爱发电：[为我充电](https://afdian.net/a/ZHOZHO)


## Credits

[DepthFM](https://github.com/CompVis/depth-fm)

演示视频中芭蕾舞和东京场景原视频分别来自：https://www.youtube.com/watch?v=cU8-rheBciw 、https://openai.com/sora
