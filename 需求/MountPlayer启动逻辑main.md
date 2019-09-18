* MountPlayer启动逻辑

  * ```main.cpp``` 入口

    * 1. ```CAppModule::InitInstance()```

         解析```GPPlayerRes.zip```资源：

         其中```GPPlayerRes.zip```只包括了字体的设置

      2. ```ParseCmdLine()```:配置命令行参数

      3. ```MountRemoteCfgIns.init()```:配置相关swf动画和cef设置

         (1)发送请求到```http://download.game.yy.com/goa/xml/mount.xml```获取配置信息，cef，资源等文件

         (2)请求成功后，解析xml文件：

         调用```CheckAllRes()```判断是否本地有该文件

         没有的话调用```DownloadAllRes()```进行下载

      4. ```theApp.Run()```:运行该实例

         资源本地路径存放在```appdata/roaming/duowan/yygame5/online_res/mountres```

      5. 当mountplayer接收到消息：```MSG_YYGAME_TO_PLAYER_PLAY_MOUNT```时候，将触发``` MountMgr::PlayMount( MountInfo& info )```消息，将其加进```m_MountList```队列，通过```OnTimerPlayMount()```进行播放

  * 通过```HornMountDataMgr```里面的```m_timerFetchRemindInfo```定时启动```OnTimerFetchRemindInfo```启动```g_pMountLogic->OnTimerPlayMount();```

    然后调用到```SendMsgToPlayer(MSG_YYGAME_TO_PLAYER_PLAY_MOUNT,BuildPlayMountMsg(*iter).c_str());```启动坐骑类触发

    

* 从```GPMainImpl.cpp``` 中的```RunWork()``` 的```m_spHornLogic->Init()```启动

  启动```m_timerFectchRemindInfo```定时任务： 启动```OnTimerFetchRemindInfo```

  用户登录后 运行```DoMountRemind()```方法

  发送请求到url 附上登录的cookie

  收到服务器传回的消息，如果是坐骑的返回的请求的话，执行```ParseMountRemindResp()```去解析数据

  如果```data[mountLogin]```有值的话，解析，然后添加到```AddMount```,

  添加坐骑实例，

  运行```OnTimerPlayMount()``` 打开```MountPlayer.exe```如果```m_MountList```有值则发送```MSG_YYGAME_TO_PLAYER_PLAY_MOUNT```消息

  执行```OnMsgYYGameToPlayerPlayMount```方法，打开坐骑

  