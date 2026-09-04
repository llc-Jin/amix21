# amix21

PR ワークフロー練習用の小さな Python パッケージ。

## コマンド

| 目的 | コマンド |
|------|----------|
| テスト実行 | `pytest` |
| 開発インストール | `pip install -e .` |
| 単体動作確認 | `python -c "from amix21 import greeting; print(greeting('World'))"` |

- Python 3.8 以上。依存パッケージは無し(テストに `pytest` のみ)。
- `pytest` は `pyproject.toml` の `[tool.pytest.ini_options] pythonpath = ["."]` によりリポジトリ直下を import パスに追加して動く。

## 構成

```
amix21/          パッケージ本体
  __init__.py    公開 API を re-export（__all__ に列挙）
  greeting.py    greeting(name) の実装
tests/           pytest テスト（__init__.py は置かない）
pyproject.toml   ビルド設定 + pytest 設定
```

- `src` レイアウトではなくフラットレイアウト（`amix21/` が直下）。
- 公開する関数は必ず `amix21/__init__.py` の `import` と `__all__` の両方に追加する。

## 規約

- 変更は小さく保ち、機能追加・修正は feature ブランチ → PR 経由で `main` に入れる。
- ブランチ名は `種別/内容` 形式（例: `test/cover-empty-name-validation`, `feat/add-farewell`）。
- 関数には Google スタイルの docstring（Args / Returns / Raises）を付ける。
- 入力バリデーションを追加したら、正常系とエラー系の両方のテストを書く。
- コミットメッセージは要点を1行目に、詳細は本文に。

## やらないこと

- 秘密情報（トークン・鍵）をこのファイルやリポジトリに置かない。
- `main` へ直接 push しない（初期セットアップを除く）。
