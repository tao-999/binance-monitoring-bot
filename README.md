# 🧨 Binance 合约大单监听机器人（骚版）

本项目是一个基于 Python 编写的 **多币种大单监控终端**，支持监听 Binance 合约交易对，实时抓取大单交易，并输出到控制台和独立日志文件。

---

## 📦 功能特色

- ✅ 支持监听多个币种（如 `ETHUSDT`、`FARTCOINUSDT`、`BTCUSDT`）
- ✅ 每个币种设置独立阈值（如 ETH ≥ 20万，BTC ≥ 50万）
- ✅ 实时控制台输出骚气十足的大单信息
- ✅ 每个币种单独生成 `log` 文件，如 `logs/ethusdt_log.txt`
- ✅ 每条记录有骚气 emoji 和分隔线，美观易读
- ✅ 自动创建 `logs/` 目录，不污染项目根目录
- ✅ 控制台同时显示买一 / 卖一盘口数据（来自 `@depth5`）

---

## 🚀 使用方法

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

> 默认只需要 `websocket-client`

---

### 2. 编辑配置文件

打开 `config.py`，配置你要监听的币种及各自的大单阈值（单位：USDT）：

```python
# config.py
SYMBOLS = {
    "ethusdt": 200000,
    "fartcoinusdt": 50000,
    "btcusdt": 500000,
    "neiroethusdt": 50000
}
```

---

### 3. 运行监听器

```bash
python listener.py
```

运行后，你将在控制台看到骚气输出，同时 `logs/` 目录下生成对应日志文件：

```
logs/
├── ethusdt_log.txt
├── fartcoinusdt_log.txt
└── btcusdt_log.txt
```

---

## 📂 日志内容示例

```
💥 交易对：ETHUSDT
🕒 时间：2025-05-12 23:59:59
📉 方向：🟥 空单（主动卖出）
📦 数量：5.5500 ETH
💰 单价：2558.0 USDT
💸 成交金额：14196.90 USDT
--------------------------
```

---

## 🧠 项目结构

```
binance-monitoring-bot/
├── listener.py         # 主程序，运行它
├── config.py           # 配置币种 + 阈值
├── requirements.txt    # 所需依赖
├── README.md           # 本说明文件
└── logs/               # 自动生成，记录每个币种的骚交易
```

---

## 💡 Tips

- 项目基于 Binance 合约 WebSocket API：`@aggTrade` + `@depth5`
- 监听的是“主动吃单”交易，判断方向精准可靠
- 可随时添加更多币种，只需在 `config.py` 里加一行

---

## 📣 作者骚话

> 庄家动了，哥，你听到了吗？

用这个监听器，别说“鲸鱼吃了谁”，你连它打了几个饱嗝都知道。
