# -*- coding: utf-8 -*-
"""

Wandb用のユーティリティ

@author: mizuno-group
"""

class WandbLogger:
    def __init__(self, entity=None, project=None, group=None, name=None, config=None, **kwargs):
        """

        Parameters
        ----------
        entity : str
            wandb entity (team or user)
            各自ヒト単位で用意して招待
        
        project : str
            wandb project name
            研究・テーマ単位

        group : str
            wandb group name (e.g. experiment name)
            試験単位 (同じデータセットでの実験など)
            Filter機能でgroupを選択して比較することができる

        name : str
            wandb run name (e.g. trial name)
            試験の中の一つのtrial, 図示などの際の単位

        config : dict
            wandb config (e.g. hyperparameters)
            そのままconfigを渡してしまってGUI上で不要なものを隠してもいい (自動で提案してくれる)

        kwargs : dict
            wandb init kwargs (e.g. tags, notes, etc.)
            tags, notesが便利, tagsはlistで与えるとFilterに使える
        
        """
        self.run = None
        try:
            self.run = wandb.init(
                entity=entity, project=project, group=group, name=name, config=config, **kwargs
                )
            # note: wandb.init returns run instance
        except Exception as e:
            print(f"!! WandbLogger failed to initialize: {e} !!")
            self.run = None

    def __call__(self, **kwargs):
        if self.run:
            self.run.log(dict(kwargs)) # dict is needed to fix kwargs (by copy)

    def finish(self):
        if self.run:
            self.run.finish()


class CallbackHandler:
    def __init__(self):
        self.callbacks = []

    def set_callbacks(self, callbacks):
        if not isinstance(callbacks, list):
            callbacks = [callbacks]

        for callback in callbacks:
            if not callable(callback):
                raise ValueError("!! Callbacks must be callable instances. !!")
            else:
                self.callbacks.append(callback)

    def run_callbacks(self, **kwargs):
        for callback in self.callbacks:
            callback(**kwargs)


class DefaultLogger:
    def __init__(self):
        self.items = []

    def __call__(self, **kwargs):
        self.items.append(dict(kwargs))

    def get_items(self):
        """ get items as a dict """
        items = {}
        for item in self.items:
            for k, v in item.items():
                if k not in items:
                    items[k] = []
                items[k].append(v)
        return items
