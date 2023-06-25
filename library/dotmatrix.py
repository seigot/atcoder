# HWxマスの"."を削除した矩形を返す
# ......
# ..##..
# ..##..
# ......
#
# ##
# ##
# _HW,y,x

def get_removedoxMatrix(_hw,_h,_w):
    minx = INF
    miny = INF
    maxx = -INF
    maxy = -INF
    for jj in range(_h):
        for ii in range(_w):
            if _hw[jj][ii] == "#":
                minx = min(ii,minx)
                miny = min(jj,miny)
                maxx = max(ii,maxx)
                maxy = max(jj,maxy)
    __hw = [[] for h in range(maxy-miny+1)]
    for jj in range(maxy-miny+1):
        __hw[jj] = _hw[miny+jj][minx:minx+(maxx-minx)+1]
    return __hw, maxy-miny+1, maxx-minx+1
_HWa, _Ha, _Wa = get_removedoxMatrix(HWa,Ha,Wa)
_HWb, _Hb, _Wb = get_removedoxMatrix(HWb,Hb,Wb)
_HWx, _Hx, _Wx = get_removedoxMatrix(HWx,Hx,Wx)