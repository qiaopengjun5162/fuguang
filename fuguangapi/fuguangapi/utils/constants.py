"""
@Project  : fuguangapi
@Author   : QiaoPengjun
@Time     : 2023/10/11 上午2:08
@Software : PyCharm
@File     : constants.py
"""
"""常量配置文件"""
# 导航位置->头部
NAV_HEADER = 0
# 导航位置->脚部
NAV_FOOTER = 1
# 头部导航的显示数量
NAV_HEADER_SIZE = 7
# 脚部导航的显示数量
NAV_FOOTER_SIZE = 7

# 轮播广告的显示数量
BANNER_SIZE = 10
# 通用列表的缓存时间，单位：秒
LIST_PAGE_CACHE_TIME = 60 * 60 * 24

# 默认头像
DEFAULT_USER_AVATAR = "avatar/2023/avatar.jpg"
# 手动在uploads下创建avatar/2023/并把客户端的头像保存到该目录下。
