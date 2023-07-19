import numpy as np
import pandas as pd
import os


if __name__ == '__main__':
    path = '/root/autodl-tmp/data/D100/test'
    files_path = os.listdir(path)
    
    data = pd.DataFrame({
    'id': [],
    'target': [],
    'path': [],
    'pair_target': [],
    'pair_path': []
})
    
    class_count = 0
    global_count = 0

    for i in range(2000):
        # 随机选两个文件夹
        file1 = np.random.choice(files_path)
        file2 = np.random.choice(files_path)
        
        # 获取他们的索引
        file1_index = files_path.index(file1)
        file2_index = files_path.index(file2)
        
        files1 = os.listdir(os.path.join(path, file1))
        files2 = os.listdir(os.path.join(path, file2))
        
        # 随机选两个文件
        file1 = np.random.choice(files1)
        file2 = np.random.choice(files2)
        
        file_path1 = os.path.join(path, files_path[file1_index], file1)
        file_path2 = os.path.join(path, files_path[file2_index], file2)
        
        new_row = pd.DataFrame({'id': str(global_count), 'target': str(file1_index), 'path': file_path1,\
                    'pair_target': str(file2_index),'pair_path': file_path2}, index=[3])
        data = pd.concat([data, new_row]).reset_index(drop=True)

        global_count += 1
        print(global_count)
    for i in range(20):
        for file_path in files_path:
            files = os.listdir(os.path.join(path, file_path))
            # 随机选两个文件
            file1 = np.random.choice(files)
            file2 = np.random.choice(files)
            
            file1_path = os.path.join(path, file_path, file1)
            file2_path = os.path.join(path, file_path, file2)

            file1_index = files_path.index(file_path)
            file2_index = files_path.index(file_path)
            
            new_row = pd.DataFrame({'id': str(global_count), 'target': str(file1_index), 'path': file1_path,\
                    'pair_target': str(file2_index),'pair_path': file2_path}, index=[3])
            data = pd.concat([data, new_row]).reset_index(drop=True)
            
            global_count += 1
            print(global_count)
    data.to_csv('test.csv', index=False)