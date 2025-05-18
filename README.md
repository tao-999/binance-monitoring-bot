# Binance Monitoring Bot / 币安大额交易监听机器人

A Python-based Binance real-time monitoring bot that listens to high-value trades  
一个基于 Python 的币安链上实时大额交易监控机器人

---

## 🚀 Features / 功能亮点

- 🟢 Real-time monitoring via WebSocket / WebSocket 实时监听  
- 🔥 Auto-detect large trades / 自动检测大额交易  
- 🧠 Configurable token list & threshold / 支持自定义币种和金额阈值  
- 🧾 Auto logs (latest 100 entries) / 自动记录日志（每币种保留 100 条）  

---

## ⚙️ Setup / 安装依赖

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuration / 配置文件修改

In `config.py`  
在 `config.py` 中修改：

```python
SYMBOLS = {
    "ethusdt": 1000000,
    "btcusdt": 1000000,
    "trumpusdt": 300000
}
```

---

## ▶️ Run the Bot / 启动监听程序

```bash
python listener.py
```

Example output / 输出示例：

```
🔥 BINANCE | ETHUSDT @ 2025-05-18 20:00:00
[💥 Big Trade! / 大单来了！]
Direction: 🟩 Buy / 多单（主动买入）
Amount: 1,250,000.00 USDT
Message: 币安也顶不住了，哥你还在观望？
```

---

## 📁 Log Output / 日志说明

- Logs stored in `logs/` directory  
  所有日志保存在 `logs/` 目录中  
- Each symbol has a file, max 100 entries  
  每个币种一个文件，最多记录 100 条新交易

---

## 📄 License / 开源协议

MIT License
