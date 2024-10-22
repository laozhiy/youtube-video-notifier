# 部署 YouTube 频道视频更新监控并发送通知到邮件
1、fork此仓库

2、设置 GitHub Secrets

1.在你的仓库页面，点击 Settings。

2.找到 Secrets and variables，选择 Actions。

3.添加以下 Secrets：

YOUTUBE_API_KEY: 你的 YouTube API 密钥。

CHANNEL_ID: 你要监控的频道 ID。

EMAIL_ADDRESS: 用于发送通知的电子邮件地址。

EMAIL_PASSWORD: 该邮箱的密码（如果使用 Gmail，可能需要生成一个应用专用密码）。
# GitHub Actions 会自动运行，按照你设置的计划检查视频更新。
