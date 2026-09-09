---
name: make-pr
description: amix21 の変更をコミット・PR にする手順。変更を main に入れる前に必ず読む。
---

# 変更を PR にする手順

このリポジトリは PR 練習が目的。変更は必ず feature ブランチ → PR 経由で `main` に入れる
（初期セットアップを除き `main` へ直接 push しない）。

## 手順

1. feature ブランチを切る。ブランチ名は `種別/内容` 形式。
   - 例：`test/cover-empty-name-validation`, `feat/add-farewell`, `docs/add-claude-md`
2. 変更する。コードの構成・設計ルールは [add-code](../add-code/SKILL.md) を読む。
3. `pytest` で全テストが通ることを確認する。
4. コミットする。
5. PR を作成し、`main` へのマージは PR 経由で行う。

## 注意

- `main` へ直接 push しない。
- バリデーションを変えたら、正常系とエラー系の両方のテストを追加してからコミットする。
