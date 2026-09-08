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

## スキル

作業の種類ごとの手順は `.claude/skills/` に切り出してある。着手前に該当する SKILL.md を読む。

- コードを追加・変更する（構成・設計・テストのルール）→ `.claude/skills/add-code/SKILL.md`
- 変更をコミット・PR にする（ブランチ運用の手順）→ `.claude/skills/make-pr/SKILL.md`
