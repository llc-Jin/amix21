# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## このリポジトリについて

`amix21` は PR ワークフロー練習用の最小 Python パッケージ。公開 API は `greeting(name)` 関数ひとつ。
ビルドや Lint の仕組みは無く、テストは pytest のみ。

## コマンド

| 目的 | コマンド |
|------|----------|
| 全テスト | `pytest` |
| 単一テスト | `pytest tests/test_greeting.py::test_greeting_rejects_empty_name` |
| 開発インストール | `pip install -e .` |
| 動作確認 | `python -c "from amix21 import greeting; print(greeting('World'))"` |

- Lint・型チェック・ビルドスクリプトは未設定（探さなくてよい）。
- `pyproject.toml` の `[tool.pytest.ini_options] pythonpath = ["."]` によりリポジトリ直下が
  import パスに入るため、テスト実行に `pip install -e .` は不要。

## 構成と設計

- フラットレイアウト：パッケージは `amix21/` 直下（`src/` レイアウトは使わない）。
- `amix21/__init__.py` が公開 API の窓口。関数を追加したら **`import` 文と `__all__` の両方**に
  載せる — テストや利用側は常に `from amix21 import ...` で参照する。
- 実装本体は用途ごとのモジュールに分ける（現状 `greeting.py` のみ）。
- 入力の前処理・バリデーションは関数内で行い、不正値は `ValueError` を送出する。
  docstring は Google スタイル（Args / Returns / Raises）。

## 変更の進め方

- このリポジトリは PR 練習が目的。変更は feature ブランチ → PR 経由で `main` に入れる
  （初期セットアップを除き `main` へ直接 push しない）。
- ブランチ名は `種別/内容` 形式（例 `test/cover-empty-name-validation`,
  `feat/add-farewell`, `docs/add-claude-md`）。
- 入力バリデーションを追加・変更したら、正常系とエラー系の両方のテストを
  `tests/test_<module>.py` に追加する。
