# https://docs.telethon.dev/en/stable/basic/signing-in.html
from telethon import connection
import python_socks

api_id = 111111
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
use_proxy = False
proxy_type = connection.ConnectionTcpMTProxyRandomizedIntermediate
# proxy_type = None
proxy_settings = ('cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.com.now_sudo.rm_rf.ddns.net.we_are_here.again_to_fight.everyone.i_am.the_internet.special_wayoka.tavalodi.cfd.', 443, 'dd00000000000000000000000000000000')
# proxy_settings = (python_socks.ProxyType.SOCKS5, '1.1.1.1', 5555, True, 'foo', 'bar')
channel_id = ''
channel_name = 'Test Channel'
discord_webhook = ''
avatar_url = ''
username = 'new message'
