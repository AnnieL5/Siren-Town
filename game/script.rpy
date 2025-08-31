

define bl = Character('Bai Liu', color="#aaffcc")
define lucy = Character('Lucy', color="#ff99cc")
define andre = Character('Andre', color="#99aaff")
define jelf = Character('Jelf', color="#ccccff")
define driver = Character("Driver", color="#0000")
define fd = Character("Front desk")
define s = Character("Siren King", color="#ffcc99")
define board = Character("Board", color="#ffcc99")


label start:
    scene bg 1 12

    "You are Bai Liu. 白柳醒来，他发现自己坐在一个车的后座上，车内部狭隘窄小，破旧的椅背上泛着逼真的烟味，车窗上滑落不成股的水流，能从玻璃上模糊地看到窗外细雨淅淅沥沥，天色昏沉，分不清是黄昏还是夜晚，他的鼻腔里还萦绕着一丝淡淡的，让他不适的咸鱼腥味。"

    "他的面前有一个飘浮的面板，上面写着――【游戏须知】。"

    "白柳皱起眉来。"
    
    bl "这是哪里？他为什么在这里？这个面板又是什么东西？"

    "这个面板好像能感知他心中的疑问一般，依次在上面显现出答案。"

    board "【你在一场致命的游戏中，而你之所以在这里是因为我们检测到你在失业之后爆发出了巨大的对金钱的欲望，欲望强烈到，符合游戏开启条件】"

    board "【通关游戏你将获得积分，而积分可以兑换金钱和你想要的一切事物】"

    bl "这是什么游戏？我要怎么做才能通关获得你说的积分？"

    board "【这是一场恐怖逃生游戏，里面充斥着鬼怪，杀人狂魔，不可思议之物，而你要做的就是找出他们的弱点，完成通关整个游戏副本的剧情，并从他们手中顺利存活下来】"
    
    board "【游戏副本载入中…..载入完毕】"

    board "【游戏副本名称：《塞壬小镇》】\n【等级：一级（玩家死亡率小于百分之五十的游戏为一级游戏）】\n【模式：单人模式】\n【综合说明：这是一款刺激的动作向和解密向相结合的游戏，在玩家中大受欢迎，但似乎对新人不是很友好，新人死亡率非常高】"
    
    scene bg 1 1 // edit afterwards

    "白柳是侧睡在一辆面包车的最后一排里，很挤很狭窄，他翻身都很艰难，他一动就看到有个项链从自己的脖子从落了出去，但他现在身上的衣服都和进入游戏之前没有区别，白衬衫黑裤子，典型的上班族社畜的日常穿搭，只有这根项链是多出来的东西。"

    "项链的挂坠是一个被打了孔的一块钱硬币，白柳把手放上去之后果然就看到了游戏面板弹了出来，面板和之前一样，没有什么多出来的信息。"

    "白柳从车后座探头出来，这是一辆七人座的面包车，除了白柳躺在后排之外，前面还有四个人，他一探头出来就有人很惊喜地看向他："

    lucy "白柳，嘿，我的小甜心，你终于醒了！"

    "除了白柳，这六个人很明显都是一副外国人的长相，喊白柳小甜心的是个棕色卷发大~波浪的妹子，红唇棕色眸子，穿着热裤和吊带，白柳在看到这个人的一瞬间，心口上的硬币就弹出了面板，上面写着人物信息："

    board "【npc名称：露西】\n【人物简介：你的同班同学，很喜欢你这类型的男生，昨晚你们有过性尝试，但你面对比你高十公分还热情大胆的露西太羞涩了，没有成功（笑）】"
    
    "这个游戏似乎触发npc面板信息是需要玩家自己【看】到的，就和玩网游需要把鼠标放上去才会弹出信息是一样的，玩家的眼睛现在就相当于玩家的鼠标和游戏手柄。"

    "他若有所思，看来在这个游戏中至少不能失去视力。"
    
    lucy "露西对着白柳挤眉弄眼：“嘿，宝贝，是我把你累着了吗？你可是从上车就开始睡了一路。”"

    bl "他及时地岔开话题，白柳看了看窗外越来越偏僻冷涩的景色，开口问道：“我们这是要去什么地方？怎么看着这么偏僻？”"

    andre "“看来有胆小鬼又想临阵脱逃了。”"

    "一道讽刺浑厚的男声从前面传过来，一个穿着紧身牛仔裤和运动t的高大男人抱胸鄙夷地看着白柳，这人的身材过于健壮，上衣被撑得快要爆炸一样，看着很像一个橄榄球运动队员。"

    andre "他居高临下的抱胸打量白柳，嗤道，“晚了，白柳，就算是你个懦夫想要临阵脱逃，我们也已经在去塞壬镇的路上了。”"

    board "【npc名称：安德烈】\n【人物简介：你的情敌，喜欢露西但被露西拒绝了，对你很有敌意，之前你和他打赌要在世界上最危险的地方守护露西，来证明你对露西的爱，于是你们一行人驱车来到塞壬镇，但你因为胆小在上车之前大哭了一场，后悔不想上车，是被他强硬地拉上车的】"

    menu:
        "“塞壬镇，是个什么地方？”"
            bl "白柳已经连续看到塞壬镇这个地名两次了，他忽视安德烈对他的嘲讽，询问：“塞壬镇，是个什么地方？”"
            jump siren_info
        "..."

label siren_info:
    "安德烈又是冷哼一声，刚想开口继续嘲讽白柳，一道絮絮叨叨连绵不绝的小声念叨就打断了安德烈的嘲讽："

    jelf "“塞壬镇，历史上唯一一个被发现过海妖残骸的海滨小镇，历史上有不少人称他们撑在这里见过海妖塞壬的身影，或者在海浪中听闻到了海妖人鱼美妙的歌声，也见过这些相貌妖异的人鱼海妖在漆黑的礁石上对着人类的尸体大快朵颐….”"

    andre "“杰尔夫！那些只是塞壬镇为了骗游客去观光编造出来的故事罢了！”"

    "安德烈不耐烦地打断对方的低声快速的话，但神色上却有畏惧一闪而过。"

    jelf "一个小个子带着厚厚啤酒瓶酒盖的男生抱着自己胸前的书瑟缩了一下，似乎有些怕安德烈，声音更低地反驳道："

    jelf "“那你怎么解释，那些来塞壬镇的游客神秘失踪的事情！上个月甚至有十二名游客来了塞壬镇之后就彻底消失不见了！警方到处搜寻，没有人见过他们离开塞壬镇….”"

    board "【npc名称：杰尔夫】\n【人物简介：人鱼海怪等非自然生物的强烈爱好者，在得知露西一行人要前往塞壬镇之后，主动要求一起前往，对塞壬镇的传说故事十分了解】"

    andre "安德烈怼道：“这些人多半就是自己落水淹死了，海边淹死多正常。”"

    jelf "杰尔夫却很不服：“警察已经组织打捞了一个月了，没有打捞到任何一具尸骸，就算他们真的落入海中，这也不正常..”"

    jelf "他说着说着语气低沉幽暗起来，还夹带着一丝兴奋，“除非是他们的尸体被塞壬吃了，这样警察打捞不到也是…”"

    andre "安德烈终于火了，他怒着狠狠打了一下杰尔夫的头：“住嘴！你这个该死的四眼仔！整天人鱼人鱼的！我看你长得像条人鱼！”"

    "安德烈下手很重，白柳都能清晰地看到杰尔夫的头在座椅边磕了一下，他晕头晕脑地又在安德烈身上撞了一下，这下又激怒了安德烈，他甩手给了杰尔夫几巴掌，打得杰尔夫一颗牙齿都飞出来了。"

    jelf "杰尔夫低着头捡起自己的牙齿不说话了，他用一种很隐晦的暗恨的目光看着安德烈，嘴里很轻地用口型说了一句话。"

    jelf "其他人都没有听到，但白柳听力一向不错，他听到杰尔夫说：【人鱼一定会把你撕碎吞咽下去的，安德烈】"

    "白柳微挑了一下眉，但是什么都没说，这npc的人物关系还有点复杂。"

    "看来安德烈对杰尔夫随意打骂不是一两天的事情了，并且这个杰尔夫似乎已经用“人鱼”谋划了一个复仇计划。"

    jump second
    
label second:
    "开车的司机是白柳花钱请的塞壬小镇的当地人，从露西言谈中，白柳发现自己还是个富二代，一行人的食宿都是他包了的，司机也是他花大价钱请的，还麻烦了司机帮忙找当地的旅馆。"

    driver "车一直开到了深夜才到达那个神秘的塞壬小镇，在司机的描述中，塞壬小镇是一个靠着捕鱼和帮忙打捞沉船度日的小镇，一直都偏僻又破败，直到新镇长另辟蹊径用人鱼的传闻来吸引游客，塞壬小镇才靠着旅游业发达起来。"

    driver "但上个月不断有游客出事，这些游客并不像安德烈所说是落水了，有些甚至还没来得及去海边，就神不知鬼不觉地就消失在塞壬小镇的各个角落，比如有一个游客就是当晚住进酒店，第二天一早人就不见了，房屋紧闭也没有看见他出去，屋内的床都还留有余温，但是人就是不见了。"

    driver "于是处于旅游旺季的塞壬镇却荒凉得不可思议，不少旅馆酒店都因为经营不善而关门了。"

    "塞壬镇的确很破败，到处都是飞卷的围栏和渔网，地面上都是晒干的贝壳和海藻，还有泥沙，只有一些酒店旅馆的装潢不错，白柳他们到的时候已经是深夜了，但路上还是有很多行人。"

    "这些行人原本步伐一致地往海边去的，但白柳他们开着车一进来，这些原本要去海边的镇民就不约而同地停下，头一偏，目光直勾勾地看向白柳的车。"

    bl "白柳转头问司机：“已经半夜了，这些人去海边干什么？”"

    driver "司机摇摇头：“最近没什么人来旅游，经济不景气，他们就只能重新捕鱼，你没捕鱼过你不知道，很多值钱的鱼都畏强光，只有夜里才会出来活动，所以他们才在夜间下海。”"

    "镇民们用很诡异的目光看着白柳，眼神在夜里泛出猫一样的绿光，脸上带着一种奇异的表情，好像是在笑，但他们的嘴角没有彻底上扬，反倒是僵直一般在嘴角抽~搐着。"

    "他们手中还拿着渔网和鱼钩，有些人手上提着灯光乳化的油灯，他们目不转睛地凝视装着白柳那辆车，眼神随着车移动，好似随时都会冲上来用手中的渔具来攻打这辆车一般。"

    driver "“你们要小心一点这些家伙。”司机提醒，“他们最近很缺钱，而你们很有钱。”"

    "因为白柳这个富二代出手阔绰的原因，司机给他们一行人找了当地最好的酒店。"

    "这酒店豪华得和整个小镇的画风格格不入，是那种非常现代时髦的五星级酒店画风，门口居然还有喷泉池子。"

    "喷泉池子里有一尊人鱼的石雕，这人鱼雕刻得栩栩如生，莹润的大理石皮肤在黯淡的月光下闪着近乎于人类皮肤的光泽，长发垂落下来遮住她的丰满的乳/房，鱼尾立在水池中，她垂着眼眸，表情悲天悯人，手上托举着一个水壶，水壶里散落一些假的云母珍珠，喷泉就从水壶里倾倒下来，落在水池中，发出好似海浪一般的潮水声。"

    "司机绕着酒店门口的喷泉池子，一路把车开到了酒店的正门口。"

    # scene
    jelf "杰尔夫忽然惊叫了一声，他指着酒店门口那条人鱼喷泉雕像说：“她刚刚在看我！她刚刚动了一下！”"
    
    bl "白柳顺着杰尔夫的视线看过去，那条人鱼雕像依旧垂眉敛目，看着水里，一动不动。"

    andre "安德烈被杰尔夫叫得吓了一跳，恶狠狠地揍了杰尔夫一拳：“操！哪里动了！根本就没动！你要是在这样一惊一乍我把你声带给你扯出来，这样我看你还叫不叫！”"

    jelf "杰尔夫捂着自己被打了一拳的头，有些害怕地看了安德烈一眼，把自己蜷缩成一团，低声自言自语：“她动了的，她真的动了的……”"

    lucy "露西也被杰尔夫弄得有些发毛，她勉强笑了一下：“杰尔夫，你怎么那么肯定不是你眼花，而是这个人鱼雕像确定动了一下？这个人鱼雕像并没有眼珠，你怎么知道她在看你？”"

    "这是一尊乳白色的大理石人鱼雕像，虽然雕刻了眼睛但是并没有黑色的眼珠，它整个眼睛都是纯白的，就好像什么有眼无珠的死寂生灵一般矗立在酒店门口。"

    jelf "“你们没发现吗？”杰尔夫声音越来越低，还有些颤，“无论我们的车开到什么地方，我们的车都是被这个雕像直视着的，她的眼睛肯定在动…”"

    lucy "“这个啊…我还以为什么呢..”露西明显松了一口气，终于舒心地笑出来，“就和那个《蒙拉丽莎的微笑》的画像是一样的吧？无论从什么角度都以为画像上的人在看自己。”"

    bl "“不是，这种无论什么角度画像上的人都在看自己的情况智能二维平面产生，三维是无法产生的，也就是雕像是不可能出现这种情况的。”白柳很冷静地反驳了露西，“杰尔夫说的是对的，这个雕像的确眼神就一直盯着我们动。”"

    "和那些镇民是一样的，一进来就开始不断盯着他们，就好像是在看什么进入他们狩猎范围的猎物一样。"

    "这东西应该是个什么怪物。"

    board "在他这个想法刚刚落下，白柳胸前的硬币突兀地震动了一下，弹出一个全新的面板，游戏面板变成一本厚重古旧好像是中世纪的书籍般，在白柳面前缓缓翻开。"

    board "【恭喜玩家发现第一个游戏怪物，解锁怪物书――《塞壬小镇》特辑（1/4）】"

    # 书页上出现一张照片，人鱼雕塑苍白的脸浸泡在幽深的海水中露出半张脸，没有雕刻眼珠的眼睛看着照片外，无声的注视着白柳，似乎要从照片中爬出来。

    board "【怪物名称：人鱼雕塑（蛹状态）】\n【攻击值：？？？（未知未解锁，战斗后解锁）】\n【攻击方式：？？（未探索）】\n【弱点：？？（未探索）】"

    "那些问号的地方都是像是被湿濡了的墨迹和污渍，看不清具体字迹，后面飘浮着荧光字体的解释。"

    board "弱点下面有一行说明文字：\n【注：探索补全完该怪物书页信息可以获得相应的积分奖励和特殊奖励，集齐一个游戏副本的所有怪物书页，可以带走该游戏副本中某种怪物的最珍贵的东西】"

    "《塞壬小镇》的怪物书有四页，后面的书页白柳就翻不动了，显示未解锁，应该是其他的游戏副本里的怪物。"

    "但是看这个探索条件，甚至还有战斗，这完全就是鼓励玩家去作死挑衅怪物啊….."

    lucy "露西有些慌张地抱住白柳的手：“…她真的在动吗？！”"

    andre "“怎么可能！”安德烈似乎也被白柳振振有词的说辞感染了，他的脸上出现一瞬恐惧的神情，但很快被压了下去，对着白柳嘲讽道，“白柳，你个胆小鬼要是不愿意证明对露西的爱，贪生怕死编造这些理由想要逃跑，你就跑吧！回去之后你就自动放弃露西，然后跪下舔~我皮鞋上的尿！”"

    driver "司机神色奇怪的动了一下，但最后状若平常地调笑道：“天色太晚了，你们看错了吧？哪有什么会动的雕像啊，要真有，我们镇子早就保护起来用来做观光景点了！那可是可以挣一大笔钱呢！人鱼雕像只是我们城镇的特色而已，到处都有的，没什么特别的。”"

    driver "“到了，你们下车吧，今晚好好休息一晚，明早起来好好游玩吧。”司机打开车门，送他们下车。"

    "白柳回头看了一眼那个喷泉中人鱼雕像，远远望去，那尊雕像依旧是正面对着他们的，头温顺地低着，看着水面里，似乎并没有注视他们。"

    "但白柳清晰地记得，他们的车刚刚开进来的时候，这尊人鱼雕像的正面不是朝向酒店门口的，而是朝向入口的。"

    "酒店门口也一左一右摆放了两尊人鱼雕像，手上拿着权杖，嘴角带着奇异扭曲的微笑，似乎是在扮做侍者欢迎他们的样子，但那神情仿佛被迫立在这里欢迎旅客一般。"

    "等他们走进酒店之后，更是发现里面更是到处都摆着大大小小的人鱼雕像，就连收银台背后都有一尊等身的人鱼雕像，手里还拿着钱，似乎在收银的样子。"

    "就像是司机说的一样，人鱼雕像似乎是塞壬镇的特色，随处可见，但这也太多了点，从落地灯的人鱼雕像装潢到前台手边的人鱼雕刻笔筒，这已经不是随处可见了，而是密不可分了。"

    "而这些人鱼雕像都有一个特点，白柳发现自己无论走到屋内的什么角落里，这些摆放在不同地方的人鱼雕像都会给他直视的感觉，但这些人鱼雕像都没有眼珠子，按理来说没有瞳仁的雕像很难给人它在凝视你的感觉，但白柳就是有这种感觉。"

    "如此数量繁多，摆放密集的人鱼大理石雕像盯着你，实在是让人感到不适，就算是一直吼着讥讽白柳是胆小鬼的安德烈进来之后都起了一身鸡皮疙瘩，搓了搓胳膊，杰尔夫更是瑟瑟发抖地躲在安德烈的后面，似乎都不怕安德烈打他了。"

    lucy "露西小鸟依…大鸟依人地挽着白柳的胳膊，一张娇艳如玫瑰的脸庞泛着惨白的颜色，似乎也被这诡异的酒店装饰吓到了。"

    # frontdesk

    bl "而白柳神色自若地和前台沟通：“你好，我姓白，我之前有预定酒店。”"

    fd "前台是个肤色惨白得像大理石一样的年轻人，下/身穿着及地的苏格兰长裙，走起来一顿一顿的，似乎有些行动不便，这个年轻人静立不动的时候，甚至让人分不清他是雕像还是真人。"

    lucy "白柳一行人靠过去，这人忽然动了起来的时候，甚至把露西吓了一跳，她以为是雕像动起来了，捂脸惊叫道：“哦我的上帝！你白得就像是一尊雕像！”"

    fd = "“抱歉。”前台看着他们抱歉道，“我有白化病，吓到你们了不好意思，白先生是吗？您一周前预定了四个房间，预定了一周的时间，费用以及付了，房卡在这里，祝您□□愉快。”"

    "白柳接过房卡，他看到四个房间的时候，其实是松了一口气的。"

    "他不太想和让自己【没有成功】的露西女士睡一间房，露西似乎也明白了这一点，这位刚刚还受到惊吓的女人很快就恢复了，她用一种【哦！宝贝！你可真是太害羞了！】的眼神调侃地看着白柳，被白柳面色不改地忽视过去了。"

    menu:
        "“我想问一下，你们这个酒店里，怎么这么多人鱼雕像？”"
            bl "“我想问一下，你们这个酒店里，怎么这么多人鱼雕像？”"

            fd "前台语调平缓地回答：“先生，人鱼给了我们一切，塞壬小镇本来一无所有，自从打捞上人鱼的尸骸，来这里的旅游人越来越多了，我们获得了金钱，拥有了一切，所以我们很感激人鱼，在这里，家家户户都有很多人鱼雕像，这对于我们来说就像是护身符一样的存在。”"

            bl "白柳指了指前台身后的人鱼雕像：“你们人鱼雕像的类型，也很丰富，各种各样的都有，你背后那个，就和你长得一模一样的，似乎和其他雕像的材质不太一样。”"

            "其实不怪露西分不清这人和雕像，这个前台背后那个人鱼雕像和前台的面貌如出一辙，甚至表情还更生动痛苦，甚至有些狰狞了。"

            "这个人鱼雕像的眼睛直直瞪视着站在它前面的前台，无论前台去什么地方都不移开视线，好似要从雕像里张牙舞爪地跑出来把这个长得和自己一模一样的前台撕碎吃掉一般，看得人不寒而栗，但是材质看起来却更脆薄，不像是其他人鱼雕像那么厚重，看着有些破旧了。"

            fd "“是的先生。”前台抬起眼眸直视白柳，“背后这个人鱼雕像是我的护身符，我们会把人鱼雕刻成和我们的样子，当灾难来临的时候，这些人鱼雕塑护身符就会被魔鬼错当成我们，先我们一步帮我们承担风险了。”"

            "白柳觉得有点意思，这个【护身符雕像】明显是个和其他人鱼雕像不同的东西。"

            board "【玩家获得新认知――《塞壬小镇怪物书》人鱼雕像面板刷新】\n【怪物名称：人鱼雕像（蛹状态），护身符雕像（茧状态）】"

            "蛹和茧？这个名为【人鱼雕像】的怪物还有两种不同的状态？"

            bl "白柳缓慢地思量，蛹是成虫还没破壳的状态，破茧成蝶，茧是成虫成功孵化之后的状态，也可以说是留下的壳子，保护自己的外壳，和这个前台说的，抵御攻击的外壳的说法不谋而合…."

            "估计这个人鱼雕像还有【虫】和【蝶】状态，这两种状态白柳感觉上应该比【蛹】和【茧】的攻击性要强，目前看来，【蛹】和【茧】状态的人鱼雕像没有主动攻击人的意向，不过也有可能是【攻击】的方式是白柳意识不到的那种，比如精神污染之类的，他觉得满大厅的人鱼雕像一直盯着玩家，就挺精神污染的。"

            jump third
        "分发了房卡"
            jump third

label third:
    lucy "白柳分发了房卡，露西缠缠~绵绵地想要和他睡一间屋子，被白柳以【我还没有为了你证明自己的勇敢，不配真的拥有你！】的理由打发了，露西感动不已地回去了，走之前还很火辣地准备和白柳接吻，被愤怒的安德烈阻止了。"

    bl "感谢安德烈！希望安德烈今晚不要出事！\n白柳发自内心地希望安德烈能多活一会儿，不然他还真不好招架露西。"

    # room

    bl "白柳用房卡刷开了自己的房间，他一打开之后就顿住了进去的脚步。"

    "白柳扮演的这个npc有钱，订的是比较好的房间，房间内的摆件精美细致，但屋内从台灯造型到床头柜上的雕塑，全是人鱼，白柳刷开一进去，这些白森森的人鱼雕塑的眼珠子好似微不可查地移动了一下，看向了白柳。"

    board "【激活主线任务：玩家白柳在屋内安全渡过今晚，存活到明天，并且不被孵化――任务完成奖励：20积分】"

    "系统给白柳发了第一个任务，但白柳的关注点反而不在任务上，他看着【避免被孵化】几个字陷入了沉思。"

    "……孵化？\n 啧，那群雕塑可以孵化他们吗？"

    "白柳默默记下，他一转身他就看到床的对面立着一个等人高的人鱼雕塑。"

    "这是白柳看到的，屋内最大的人鱼雕塑了，也是唯一一个没有正眼看他的雕塑。"

    b "Where are we going? This place looks so remote."
    l "Hey, sweetheart, you're finally awake!"
    a "Too late to back out now, Bai Liu. We're already on our way to Siren Town."
    menu:
        "Tell me more about Siren Town":
            b "What is Siren Town?"
            jump siren_info

        "Discover Andre's hostility towards you and the details of the bet":
            a "Are you scared? In tonight's bet, I'll let you know what real fear is."
            
            "He revealed that the bet would be held on the beach, and the loser would lose Lucy."
            
            menu:
                "Agree to the bet":
                    b "Fine, I accept the bet. But I won't lose."
                    a "Hahaha, we'll see about that."
                    jump continue_journey2
                "Tell me more about the bet":
                    jump continue_journey2
                "Try to avoid the bet":
                    b "I don't want to participate in this bet."
                    a "What? Fine, you can back out."
                    jump continue_journey1

        "Keep a low profile":
            b "..."
            jump continue_journey1

label siren_info:
    a "Siren Town is the only seaside town in history where the remains of a siren have been found. In history, many people claimed that they had seen the sirens here, or heard the beautiful singing of sirens and mermaids in the waves, and also saw these strange-looking mermaids feasting on human corpses on the dark reefs..."
    
    a "Those tourists who came to Siren Town mysteriously disappeared! Last month, twelve tourists disappeared completely in Siren Town! The police searched everywhere but to no avail, and no one has ever seen them leave Siren Town..."

    a "\"The police have been organizing a salvage operation for a month, but they haven't found any bodies. Even if they really fell into the sea, this is not normal...\" \"Unless their bodies were eaten by Sirens, in which case it is also possible that the police couldn't salvage them...\""

    "Siren Town is a town that relies on fishing and helping to salvage sunken ships. It has always been remote and dilapidated. It was not until the new mayor took a different approach and used the rumor of mermaids to attract tourists that Siren Town developed through tourism."

    "But since last month, tourists have been in trouble. These tourists did not fall into the water as Andre said. Some of them even disappeared in different corners of Siren Town without anyone noticing before they had time to go to the beach. For example, one tourist checked into the hotel that night and disappeared the next morning. The door was closed and no one saw him go out. The bed in the room was still warm, but the person was gone."

    jump continue_journey1

label continue_journey1:

    scene bg siren 42
    "You arrive at the town and find wax figures of mermaids all over the town. You check into the hotel at night, and the wax figures seem to move at night. Andre touches the wax figure in the wax museum and begins to transform."

    menu:
        "Actively investigate the secrets of the wax figure":
            b "What is this wax figure? Why does it look so lifelike?"
            "You decide to investigate the secrets of the wax figure."

            jump investigate_wax_figure
        "Avoid the wax figure and go to bed":
            b "I don't want to deal with this wax figure. I'll just go to bed."

            "No way it doesn't work. The wax figure moves at night, and you can't sleep peacefully."
            jump interact_wax_figure
        "Try to interact with the wax figure":
            b "Maybe I can interact with this wax figure."
            jump interact_wax_figure
        
label investigate_wax_figure:

    scene bg siren 12
    "You discover that the wax figures of mermaids are afraid of bright light and being looked at directly. Shining a flashlight or looking directly at them can stop them from moving. You plan to exploit this weakness."

    menu:
        "Use a flashlight to stop the wax figure":
            b "I'll use a flashlight to stop the wax figure."
            "You successfully stop the wax figure from moving. Points +2"
            jump continue_journey2
        "Continue to observe and look for more clues":
            b "I'll keep observing the wax figure for more clues."
            "You find that the wax figures are actually made of a special material that can mimic human movement."
            jump interact_wax_figure
        "Gather your teammates to discuss countermeasures":
            b "I need to gather my teammates to discuss how to deal with the wax figure."
            jump continue_journey2

label interact_wax_figure:
    "You try to touch the wax figure, your mental strength drops rapidly, and alienation begins. The wax figure starts to attack you."

    "No it doesn't work. The wax figure is not just a wax figure, it has a life of its own. It attacks you, and you barely manage to escape."

    jump bad_ending

label continue_journey2:

    scene bg siren 22
    "The next day, Andre challenges you to a bet on the beach. You can't swim, and the others gradually become fish."

    "You boarded a huge ship to join the mermaid fishing. The sailors and fishermen on board were different, and the ship was unusually heavy. At night, the ship sailed into the deep sea, full of dangers."

    "You are waiting for the dawn at sea and discover that Lucy and Jelf are having an affair. Andre is missing and blood is found on the boat. You speculate that Jelf and the driver are plotting something and Lucy is gradually turning into a wax figure."

    "You enter the wax museum to find more clues and find that the wax figures can move, and Jellal's conspiracy surfaces. You need to choose how to fight the monster and escape."

    menu:
        "Use the flashlight to stop the wax figure":
            b "I'll use the flashlight to stop the wax figure."
            jump continue_journey3
        "Found a secret passage in the wax museum, you escape through the secret passage.":
            jump normal_ending
        "Try to fight the wax figure directly":
            b "I'll fight the wax figure directly."
            "You try to fight the wax figure directly, but it is too powerful. You are defeated and turned into a wax figure."
            jump bad_ending

label continue_journey3:

    scene bg siren 32
    "You enter a new place. The central exhibition hall is a circular exhibition hall, with a glass cabinet like a crystal coffin standing in the middle. The glass cabinet has dazzling white LED lights that illuminate the mermaid skeleton inside at 360 degrees without blind spots. Bai Liu looked at the mermaid corpse called skeleton with a rare look of surprise."

    "The lines of the muscles are elegant and sharp, and the well-proportioned muscles wrap around the thin bones. Bubbles slowly rise in the deep dark blue liquid, entwining and floating in the mermaid's dark brown hair, and finally embedded in its slender light-colored eyelashes like a pearl. \n Its eyes are closed, and its face is incredibly delicate and exquisite. Some slightly curly long hair flutters across its thick and beautiful cheeks in the water, revealing a pair of ears that are very different from ordinary people. \n Its left ear is a fin made of shell mica, which shines with a colorful luster in the water, while the right ear is a bone-like fin, which appears from the wet long hair. \n The winding and curly fish tail is like a bright silver-blue ribbon washed in the sea water, hanging on the glass cabinet, and the inverted triangle scales sparkle under the light. There is a translucent flesh membrane between the fingers of the right hand, which is wrapped and overlapped with the bony left hand in front of the chest."

    menu:
        "Look at the mermaid skeleton":
            "!!You have triggered the wandering god-level NPC Siren King!!"
            "!!Warning! Warning! This NPC is extremely dangerous and currently has no clear weakness. Once the NPC wants to kill, the player cannot use the weakness to escape and will only die. Please speed up the game cracking progress and quickly escape from Siren Town before the NPC wakes up!!"
            jump continue_journey4
        "Leave the wax museum":
            "You decide to leave the wax museum and not look at the mermaid skeleton."
            jump normal_ending

label continue_journey4:

    scene bg siren 67 22
    "You drag the Siren King into the sea, ready to send him back to the bottom of the sea. There are a lot of mermaid larvae lurking in the sea, and the system prompts that the Siren King is about to wake up. \nYou push the Siren King to the seaside, and the mermaid sailor's scales grow rapidly in the rain, and the speed increases! The Siren King\'s eyelashes tremble, and the countdown to awakening is shortened to 3 hours."

    "The Siren King opened his eyes, \"You brought me back to the deep sea, what is your wish?\" \nSpirit value 0.1, panel attributes break through the limit! The fish tail smashes you into the magma crack, and all the bones in your body are broken."

    menu:
        "Wish to leave Siren Town":
            "You wish to leave Siren Town, and the Siren King agrees. You are teleported back to the real world, but you have lost all your memories of Siren Town. You are safe, but you will never know what happened in Siren Town."
            jump normal_ending
        "How about a kiss?":
            "You ask the Siren King for a kiss, and he agrees. You kiss him."
            jump true_ending

label normal_ending:
    "You successfully escape from Siren Town and return to the real world. You have learned a lot about the mysteries of Siren Town, but you will never forget the horrors you experienced there."

    "Congratulations! You have completed the game with a normal ending."

    return

label bad_ending:
    "You were defeated by the wax figure and turned into a wax figure yourself. You are now part of the wax museum, forever trapped in Siren Town."
    return

label true_ending:
    "The lips of the Siren King were soft and cold, with a very light smell of creeping grass, and they separated at the touch."

    scene bg siren 67 32
    s "The Siren King leaned on Bai Liu, his expression slightly strange and confused: \"You're temperature is warm'.\""
    
    b "\"Of course.\" Bai Liu was a little amused, \"I am a warm-blooded animal. See you next time, Siren King.\""
    
    s "The Siren King whispered in the light: \"See you next time, Bai Liu.\""

    "True ending"

    return