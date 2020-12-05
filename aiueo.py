from random import choice
from termcolor import colored as Color

kana_dict = {
    'a': ['あ', 'ア', '(a)安(あ)全第一啊(ア)', '安全第一啊'],
    'i': ['い', 'イ', '以(い)为你(i)依(イ)然爱我', '以为你依然爱我'],
    'u': ['う', 'ウ', '宇(う)宙(ウ)(u)无极限', '宇宙无极限'],
    'e': ['え', 'エ', '(e)欸?! 元(え)旦也工(エ)作?', '欸?! 元旦也工作?'],
    'o': ['お', 'オ', '(o)我(お)果然是天才(オ)', '我果然是天才'],
    'ka': ['か', 'カ', '(ka)咖(カ)啡溢出来一点(か)', '咖啡溢出来一点'],
    'ki': ['き', 'キ', '(ki)key(钥匙串(き)(キ))', 'key(钥匙串)'],
    'ku': ['く', 'ク', '工资少于(く)别人, (ku)哭了很久(ク)', '工资少于别人, 哭了很久'],
    'ke': ['け', 'ケ', '十一(け)放(ケ)假很(ke)开心', '十一放假很开心'],
    'ko': ['こ', 'コ', '圆(こ)括号, 方(コ)括号, 都是(ku)括号', '圆括号, 方括号, 都是括号'],
    'sa': ['さ', 'サ', '草(サ)地上发生(sa)杀(さ)人案', '草地上发生杀人案'],
    'si': ['し', 'シ', '用(si)吸管(し)喝水(シ)', '用吸管喝水'],
    'su': ['す', 'ス', '不要上吊(す)(ス), 会(su)死人', '不要上吊, 会死人'],
    'se': ['せ', 'セ', '跟世(せ)(セ)界 Say(se) hi', '跟世界 Say hi'],
    'so': ['そ', 'ソ', '(so)嗖(ソ)的一下飞(そ)走了', '嗖的一下飞走了'],
    'ta': ['た', 'タ', '(ta)她在(タ)夕阳下(た)太美了', '她在夕阳下太美了'],
    'ti': ['ち', 'チ', '她是有(ti)七(ち)千(チ)万的土豪', '她是有七千万的土豪'],
    'tu': ['つ', 'ツ', '小(tu)刺(つ)(ツ)猬很可爱', '小刺猬很可爱'],
    'te': ['て', 'テ', '(te)te(て)nnis要两(テ)个人一起打', 'tennis要两个人一起打'],
    'to': ['と', 'ト', '小兔子(to)偷吃胡萝卜(ト)(と)', '小兔子偷吃胡萝卜'],
    'na': ['な', 'ナ', '(na)那可真是无(ナ)奈(な)啊', '那可真是无奈啊'],
    'ni': ['に', 'ニ', '有1(に)个人很二(ニ)(に), 是的就是(ni)你', '有1个人很二, 是的就是你'],
    'nu': ['ぬ', 'ヌ', '又(ヌ)一个分(nu)奴(ぬ)', '又一个分奴'],
    'ne': ['ね', 'ネ', '(ne)内人掌权(ね), 我很幸福(ネ)', '内人掌权, 我很幸福'],
    'no': ['の', 'ノ', '(no)no(の), 不(ノ)要吃我的蛋糕', 'no, 不要吃我的蛋糕'],
    'ha': ['は', 'ハ', '(ha)哈利波(は)特第八(ハ)部', '哈利波特第八部'],
    'hi': ['ひ', 'ヒ', '一个大鼻子(ひ)坏蛋拿着(ヒ)匕首(hi)hihi的笑', '一个大鼻子坏蛋拿着匕首hihi的笑'],
    'hu': ['ふ', 'フ', '小(ふ)猫耳朵一竖, 表示不(フ)(hu)服', '小猫耳朵一竖, 表示不服'],
    'he': ['へ', 'ヘ', '(he)嘿嘿 ^_^(へ)(ヘ)', '嘿嘿 ^_^'],
    'ho': ['ほ', 'ホ', '汪(ほ)先生(ho)好木(ホ)讷', '汪先生好木讷'],
    'ma': ['ま', 'マ', '(ma)妈呀, 期末(ま)全挂了(マ)', '妈呀, 期末全挂了'],
    'mi': ['み', 'ミ', '21(み)岁的我终于养了猫(ミ)(mi)咪', '21岁的我终于养了猫咪'],
    'mu': ['む', 'ム', '(mu)木有么(ム)么哒(む)吗', '木有么么哒吗'],
    'me': ['め', 'メ', '(me)美女(め)与玫(メ)瑰', '美女与玫瑰'],
    'mo': ['も', 'モ', '(mo)摸摸狗狗的毛(も)(モ)', '摸摸狗狗的毛'],
    'ra': ['ら', 'ラ', '在马桶(ra)拉...(你懂的)(ら)(ラ)', '在马桶拉...(你懂的)'],
    'ri': ['り', 'リ', '(ri)利(り)(リ)益主义', '利益主义'],
    'ru': ['る', 'ル', '(ru)鲁先生有一(る)百个(ル)儿子', '鲁先生有一百个儿子'],
    're': ['れ', 'レ', '总要送礼(れ)(レ), 心好(re)累', '总要送礼, 心好累'],
    'ro': ['ろ', 'ロ', '3(ろ)(ro)楼住了3口(ロ)人', '3楼住了3口人'],
    'ya': ['や', 'ヤ', '(ya)鸭肉也(や)(ヤ)挺好', '鸭肉也挺好'],
    'yu': ['ゆ', 'ユ', '中(ゆ)国人都很(yu)勇敢(ユ)', '中国人都很勇敢'],
    'yo': ['よ', 'ヨ', '上(よ)山(ヨ)去捉(yo)妖', '上山去捉妖'],
    'wa': ['わ', 'ワ', '13(わ)(一生)17(ワ)(一起)(wa)挖地瓜', '13(一生)17(一起)挖地瓜'],
    'wo': ['を', 'ヲ', '大(を)不溜C(ヲ)(を)哦(wo)', '大不溜C哦'],
    'n': ['ん', 'ン',  '(n)人(ん)总是需要一点提(ン)点', '人总是需要一点提点'],
}

msgs = {
    'a': '🎉 --- 欢迎~ 这是练习假名的Python🎈程序\n🐈 --- designed by Viki 2020/12/5\n',
    'b': Color('😁 请先选择一个', 'cyan') + Color('练习模式', 'cyan', attrs=['bold', 'underline']),
    'c': Color('- 1.平假名模式\n- 2.片假名模式\n- 3.混合模式\n- 4.查看假名表\n- 0.退出程序', 'blue'),
    'd': '>>> ',
    'e': Color('🎊 欢迎~ 开始你的%s练习叭', 'cyan'),
    'f': Color('💡 tip: 输入1跳过当前题目, 输入0退出当前模式, 输入kana查看假名表', 'cyan'),
    'g': Color('%s ', 'blue', attrs=['bold']) + Color('怎么读: ', 'yellow'),
    'h': Color('✅ 干得漂亮 ヽ(✿ﾟ▽ﾟ)ノ', 'green'),
    'i': Color('❌ 答chuo了 再想想 (⊙x⊙;)', 'red'),
    'j': Color('%s', 'blue', attrs=['bold']) + Color(' 读作 ', 'cyan') + Color('%s', 'green', attrs=['bold']),
    # 'k': Color(),
    'l': Color('😅 下次记住哦~ 已帮宁跳过这题', 'cyan'),
    'm': Color('🆗 已退出%s模式', 'cyan'),
    'n': Color('👋 拜拜ヾ(•ω•`)o 我不在的时候也要好好学习哦', 'cyan')
}


def main():
    wel_msg = '\n' + msgs['a'] + '\n' + msgs['b']
    print(wel_msg)
    while(True):
        menu_msg = msgs['c'] + '\n' + msgs['d']
        mode = input(menu_msg)
        if mode == '1' or mode == '2' or mode == '3':
            exer_kana(mode)
        elif mode == '4':
            show_kana()
        elif mode == '0':
            exit(msgs['n'])
        else:
            continue


def show_kana():
    kana_str = ''
    for index in range(46):
        is_n = '\t\n' if (index + 1) % 5 == 0 else '\t'
        pinyin = list(kana_dict.keys())[index]
        hiragana = list(kana_dict.values())[index][0]
        katakana = list(kana_dict.values())[index][1]
        kana = Color(f'{hiragana} / {katakana}', 'yellow')
        kana_str += kana + ' : ' + Color(f'{pinyin} {is_n}', 'green')
    print(kana_str)


def exer_kana(mode):
    maps = {'1': [0, '平假名'], '2': [1, '片假名'], '3': [2, '混合假名']}
    print(msgs['e'] % (maps[mode][1]), msgs['f'])
    while(True):
        pinyin = choice(list(kana_dict.keys()))
        if maps[mode][0] == 2:
            kana = choice(kana_dict[pinyin])
        else:
            kana = kana_dict[pinyin][maps[mode][0]]
        while(True):
            msg = Color(msgs['g'] % (kana), 'blue')
            user_input = input(msg)
            if user_input == pinyin:
                print(msgs['h'])
                break
            elif user_input == '1':
                print(msgs['j'] % (kana, pinyin), msgs['l'])
                break
            elif user_input == '0':
                print(msgs['m'] % (maps[mode][1]))
                return
            elif user_input == 'kana':
                show_kana()
                continue
            else:
                print(msgs['i'])
                continue


if __name__ == '__main__':
    main()
