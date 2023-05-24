# auto_change_clash_proxy
1、脚本介绍

Python语言实现Clash for windows自动切换国家节点

2、脚本目的

当使用Python语言爬取网站并开启clash for windows时，ip即节点被ban后，实现Clash for windows自动切换国家节点

3、官方文档

https://clash.gitbook.io/doc/restful-api

4、配置

(1)查看port和secret
进入Clash for windows常规页面-->打开目录
 ![image](https://user-images.githubusercontent.com/79882515/237053980-ed3d9dfa-37f9-4dc7-9a33-89cacb47fe1e.png)
 
5、查看selector
官方文档说明：切换 Selector 中选中的代理，当前接口只支持切换 Selector 中的代理 查看可以切换的Selector，进入Clash for windows常规页面，如下图

 ![image](https://user-images.githubusercontent.com/79882515/237054361-bbb07165-e96c-44b2-bd53-190ca92128a5.png)
![image](https://user-images.githubusercontent.com/79882515/237054408-ba66e580-07a0-4f5f-b805-47c1820f68ee.png)

6、实现结果

 ![image](https://user-images.githubusercontent.com/79882515/237054430-8702053b-a71b-4844-ad34-335a1745f5db.png)

7、更新日志

20230519

增加获取当前代理的状态，切换不超时的国家节点
![image](https://github.com/allen746/auto_change_clash_proxy/assets/79882515/4f6544a8-957e-46be-b438-988f5db4bc7d)
