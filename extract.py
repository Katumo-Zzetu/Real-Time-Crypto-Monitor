import asyncio
import websockets
import json
import psycopg2

# Coinbase WebSocket URL
COINBASE_WS_URL = "wss://ws-feed.exchange.coinbase.com"

# Subscribe message for BTC-USD & ETH-USD ticker updates
subscribe_msg = {
    "type": "subscribe",
    "channels": [{
        "name": "ticker",
        "product_ids": [
            "BTC-USD", "ETH-USD", "LTC-USD", "BCH-USD", "XRP-USD", 
            "ADA-USD", "DOT-USD", "LINK-USD", "SOL-USD", "DOGE-USD"
        ]
    }]
}

# PostgreSQL connection (Replace placeholders before running)
conn = psycopg2.connect(
    host="<HOST>",
    database="<DATABASE>",
    user="<USERNAME>",
    password="<PASSWORD>"
)
cursor = conn.cursor()

async def coinbase_client():
    async with websockets.connect(COINBASE_WS_URL) as websocket:
        await websocket.send(json.dumps(subscribe_msg))
        print("✅ Subscribed to Coinbase ticker...\n")

        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)

                if data.get("type") == "ticker":
                    cursor.execute(
                        "INSERT INTO crypto_prices (timestamp, symbol, price) VALUES (%s, %s, %s)",
                        (data.get("time"), data.get("product_id"), data.get("price"))
                    )
                    conn.commit()
                    print("📨 Stored in PostgreSQL:", data)

            except websockets.exceptions.ConnectionClosedError:
                print("❌ WebSocket connection closed. Reconnecting...")
                await asyncio.sleep(5)
                return await coinbase_client()
            except Exception as e:
                print(f"⚠️ Error: {e}")
                break

asyncio.run(coinbase_client())
