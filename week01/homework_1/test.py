import requests


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
jar = requests.cookies.RequestsCookieJar()
jar.set('uuid_n_v', 'v1')
jar.set('uuid', '27C9CAD0B89711EAACB6BBD781D8993868D41D2C507D4823B251DFDC04E71EB1')
jar.set('_csrf', '1bc54f037cd1ba0ac59ebaf73dd3f44cb090401b1a3b1d596cdee1a9bca658eb')
jar.set('Hm_lvt_703e94591e87be68cc8da0da7cbd0be2', '1593276996')
jar.set('_lxsdk_cuid', '172f6b59976c8-09c0241ea13f8e-4353760-e1000-172f6b59976c8'),
jar.set('_lxsdk', '27C9CAD0B89711EAACB6BBD781D8993868D41D2C507D4823B251DFDC04E71EB1')
jar.set('mojo-uuid', '145308c1e429294f02d2090fffccab8e')
jar.set('mojo-session-id', '{"id":"a3605148292ca1146ff7e4cb00e20998","time":1593280873412}')
jar.set('mojo-trace-id', '2')
jar.set('Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2', '1593280888')
jar.set('__mta', '144137482.1593276996539.1593280875437.1593280888469.3')
jar.set('_lxsdk_s', '172f6f0c5d8-ba1-d7e-ec3%7C%7C4')
header = {'user-agent': user_agent}
url = 'https://maoyan.com/films?showType=3'
r = requests.get(url, headers=header, cookies=jar)

print(len(r.cookies))
print(r.text)

