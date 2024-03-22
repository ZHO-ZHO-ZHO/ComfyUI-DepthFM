import os
import torch
import folder_paths
import numpy as np
from PIL import Image
from .depthfm import DepthFM


device = "cuda" if torch.cuda.is_available() else "cpu"
folder_paths.folder_names_and_paths["depthfm"] = ([os.path.join(folder_paths.models_dir, "depthfm")], folder_paths.supported_pt_extensions)


class DepthFM_ModelLoader_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "depthfm_model": (folder_paths.get_filename_list("depthfm"), ),
            }
        }

    RETURN_TYPES = ("DepthFMMODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "🌆DepthFM"
  
    def load_model(self, depthfm_model):
        if not depthfm_model:
            raise ValueError("Please provide the depthfm_model parameter with the name of the model file.")

        depthfm_path = folder_paths.get_full_path("depthfm", depthfm_model)
      
        model = DepthFM(depthfm_path)
        model.cuda().eval()
      
        return [model]


class DepthFM_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DepthFMMODEL",),
                "image": ("IMAGE",),
                "steps": ("INT", {"default": 2, "min": 1, "max": 100, "step": 1}),
                "ensemble_size": ("INT", {"default": 2, "min": 1, "max": 10}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "df_image"
    CATEGORY = "🌆DepthFM"
                       
    def df_image(self, model, image, steps, ensemble_size):

        img_tensor = image.permute(0, 3, 1, 2).to(device=device, dtype=torch.float32)
        
        depth = model.predict_depth(img_tensor, num_steps=steps, ensemble_size=ensemble_size)
        print(f"{'Depth':<10}: {depth.shape}")

        depth_map = depth.squeeze(0)
        
        if depth_map.dim() == 3:
            depth_map = depth_map.squeeze(0)

        depth_map = depth_map.unsqueeze(-1).repeat(1, 1, 3)
        depth_map = depth_map.unsqueeze(0)
        depth_map = 1.0 - depth_map

        return (depth_map,)


class DepthFM_Literative_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DepthFMMODEL",),
                "image": ("IMAGE",),
                "steps": ("INT", {"default": 2, "min": 1, "max": 100, "step": 1}),
                "ensemble_size": ("INT", {"default": 2, "min": 1, "max": 10}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "df_image"
    CATEGORY = "🌆DepthFM"
                       
    def df_image(self, model, image, steps, ensemble_size):
        processed_images = []
        for img_tensor in image: 
            
            img_tensor = img_tensor.permute(2, 0, 1).unsqueeze(0).to(device=device, dtype=torch.float32)
        
            depth = model.predict_depth(img_tensor, num_steps=steps, ensemble_size=ensemble_size)
            print(f"{'Depth':<10}: {depth.shape}") 

            depth_map = depth.squeeze(0)
        
            if depth_map.dim() == 3:
                depth_map = depth_map.squeeze(0)

            depth_map = depth_map.unsqueeze(-1).repeat(1, 1, 3)
            depth_map = depth_map.unsqueeze(0)
            depth_map = 1.0 - depth_map
          
            processed_images.append(depth_map)

        processed_images_tensor = torch.cat(processed_images, dim=0)

        return (processed_images_tensor,)



NODE_CLASS_MAPPINGS = {
    "DepthFM_ModelLoader_Zho": DepthFM_ModelLoader_Zho,
    "DepthFM_Zho": DepthFM_Zho,
    "DepthFM_Literative_Zho": DepthFM_Literative_Zho,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DepthFM_ModelLoader_Zho": "🌆DepthFM ModelLoader",
    "DepthFM_Zho": "🌆DepthFM",
    "DepthFM_Literative_Zho": "🌆DepthFM Literative",
}
