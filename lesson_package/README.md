# lesson_package

Python 学習用のサンプルパッケージです。  
サブモジュールとして `talk` と `tools` を含み、関数の呼び出しやパッケージ構成の理解を目的としています。

## インストール方法

開発モードでインストールする場合:

````bash
pip install -e .


---

### 3. 使用例（サンプルコード）
- 実際に import して動かす例を載せると分かりやすい

```markdown
## 使用例

```python
from lesson_package.talk import human, animal
from lesson_package.tools import utils

print(human.sing())          # "human sings"
print(animal.cry())          # "animal cries"
print(utils.say_twice("hi")) # "hi!hi!"


---

### 4. ディレクトリ構成
- フォルダ構成を載せるとパッケージの全体像が伝わりやすい

```markdown
## ディレクトリ構成

lesson_package/
 ├── __init__.py
 ├── talk/
 │    ├── __init__.py
 │    ├── animal.py
 │    └── human.py
 └── tools/
      ├── __init__.py
      └── utils.py

## ライセンス
MIT License
````
