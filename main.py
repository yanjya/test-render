import requests
import json

def get_my_ip():
    """
    從 api.ipify.org 取得使用者的公共 IP 位址，並以 JSON 字串格式回傳。
    """
    try:
        result = requests.get("https://api.ipify.org?format=json")
        result.raise_for_status()  # 檢查是否有 HTTP 錯誤
        return json.dumps(result.json())
    except requests.exceptions.RequestException as e:
        return json.dumps({"error": str(e)})

# 範例用法
if __name__ == '__main__':
    ip_address_json = get_my_ip()
    print(ip_address_json)