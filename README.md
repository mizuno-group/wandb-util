# wandb-util
WandBを扱う上でのユーティリティ.  

# HowToUse
1. **インストール.**  
```pip install git+https://github.com/mizuno-group/wandb-util.git```

2. **初期化.**  
呼び出し時にwandb.init(...)がコンストラクタで走る.  
    ```
    logger = WandbLogger(
        entity="aaa", # 自身の共有用teams, ヒト単位 ★ここを共有する
        project="bbb", # Wandbのproject, 研究・テーマ単位
        group="ccc", # 研究の中のある試験回, 試験単位 (NASなど)
        name="xxx", # Wandbのrun, 一回の学習単位 (可視化時の一単位)
    )

    ```

3. **直接ループ内に書く or Trainerにcallbackとして引き渡す.**  
    ```
    def train_epoch(...):
        ...

    def evaluate(...):
        ...

    logger = WandbLogger()

    for i in range(epochs):
        train_loss = train_epoch(train_loader)
        test_loss = evaluate(test_loader)
        logger(
            epoch=i + 1,
            train_loss=train_loss,
            test_loss=test_loss,
        )
    ```
    or  
    ```
    dat = Trainer(config, model, ..., callback=[logger])
    ```

4. **終了操作.**  
``` logger.finish() ```  
  
***  
# Note
This repository is under construction and will be officially released by [Mizuno group](https://github.com/mizuno-group).  
Please contact tadahaya[at]gmail.com before publishing your paper using the contents of this repository.  

## Authors
- [自身の名前](自身のgithub repository)  
    - main contributor  
- [Tadahaya Mizuno](https://github.com/tadahayamiz)  
    - correspondence  

## Contact
If you have any questions or comments, please feel free to create an issue on github here, or email us:  
- [自身のアドレス]  
- tadahaya[at]gmail.com  
    - lead contact  