## lesson_package

Python 学習用のサンプルパッケージです。  
サブモジュールとして `talk` と `tools` を含み、関数の呼び出しやパッケージ構成の理解を目的としています。
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

---

### インストール方法
開発者向け（編集しながら試す場合）
- 前提: プロジェクト直下に setup.pyがあること
```bash
pip install -e .
```
利用者が GitHub から使う場合（GitHub 上のリポジトリを直接インストール）
```bash
pip install git+https://github.com/chie-works/lesson_package.git
```
または
```bash
git clone https://github.com/chie-works/lesson_package.git
cd lesson_package
pip install .
```
利用者が PyPI から使う場合
```bash
pip install lesson_package
```

### 使用例
実際に import して動かす例です
```bash
from lesson_package.talk import human, animal
from lesson_package.tools import utils

print(human.sing())          # "human sings"
print(animal.cry())          # "animal cries"
print(utils.say_twice("hi")) # "hi!hi!"
```

### ディレクトリ構成
パッケージ全体の構造は以下の通りです。
```bash
lesson_package/
 ├── __init__.py
 ├── talk/
 │    ├── __init__.py
 │    ├── animal.py
 │    └── human.py
 └── tools/
      ├── __init__.py
      └── utils.py
```

### ライセンス
MIT License

---
