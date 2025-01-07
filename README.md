# mypackage
このパッケージは2024年ロボットシステム学課題2で作成したROS2のパッケージです。

[![test](https://github.com/Asanomaru/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Asanomaru/mypkg/actions/workflows/test.yml)

## ノード

### calendar_notifier
日時や予定に関する通知を送信するノードです。

### 主な機能
- 現在の日付、曜日、時刻を通知します。
- 特定の日付に対応する予定を通知します。
- 明日行われる予定をリマインドします。

### パブリッシュするトピック
- トピック名: `/calendar_notification`
- 型: `std_msgs/String`

## 実行方法
```
ros2 run mypkg calendar_notifier
```

## 実行結果
```
[INFO] [1736051966.148992569] [calendar_notifier]: Published calendar notification.
```

## トピックの確認方法
### 実行方法
```
ros2 topic echo /calendar_notification
```

### 実行結果
```
data: Today is 2025-01-07 (Tuesday), and the current time is 19:22:41.
---
```

## テスト環境
- Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- © 2025 Yuuki Udagawa
