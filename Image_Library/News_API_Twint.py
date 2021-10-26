import twint



# SEtup tor connection 
# 
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
# 

c = twint.Config()
c.Tor_control_port =9050;
c.Proxy_port =9050;
c.Proxy_type = "socks5";

c.Username = "noneprivacy"
c.Custom["tweet"] = ["id"]
c.Custom["user"] = ["bio"]
c.Limit = 10
c.Store_csv = True
c.Output = "none"
twint.run.Search(c)
