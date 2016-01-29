# -*- coding: cp936 -*-
pointStr=raw_input('请输入领先分数:') 

points=int(pointStr) 

points=points-3 

has_ball=raw_input('是否有球权') 

if has_ball=='Yes': 
    points=points+0.5 
else: 
    points=points-0.5 
if points<0: 
    points=0 
    points=points**2 
seconds=int(raw_input('请输入比赛剩余时间(秒数)：')) 
if points>seconds: 
    print '安全！'

else:
    print '不安全'
