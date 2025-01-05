# mypackage
このパッケージは2024年ロボットシステム学課題2で作成したROS2のパッケージです

## calendar_notifierノード
[![test](https://github.com/Asanomaru/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Asanomaru/mypkg/actions/workflows/test.yml)

## 概要
- 日時通知: 現在の日付、曜日、時刻を通知します
- 予定通知: 特定の日付にある予定を通知します
- リマインダー通知: 明日行われる予定を通知します

## テスト環境
- Ubuntu 22.04 LTS

## 実行方法
```
ros2 run mypkg calendar_notifier
```

## 実行結果
```
[INFO] [1736051966.148992569] [calendar_notifier]: Published calendar notification.
```

- パブリッシュするトピック
  - calendar_notifier
    - 型: String

## eventsについて
events.pyは特定の日付に対応する予定情報を格納するためのファイルです

## listenerについて
listener.pyはcalendar_notifierから通知を受け取れているかを確認するためのテスト用ノードです

- 実行結果
```
[INFO] [1736051197.424672914] [listener]: Received: Today is 2025-01-05 (Sunday), and the current time is 13:26:37.Special event today: Assignment Deadline!
```

## ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- © 2025 Yuuki Udagawa
