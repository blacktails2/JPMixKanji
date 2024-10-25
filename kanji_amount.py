import re

def count_kanji(text):
    kanji_pattern = re.compile(r'[\u4E00-\u9FFF]')
    kanji_matches = kanji_pattern.findall(text)
    return len(kanji_matches)

# テスト用の文章
text = "医療の起源　古代ローマにおける医術の起源は確かではない。医療の最初は疑いもなくテウルギア（神働：神の御業への祈願）的でありすべての原始的な人々に共通なものであった。神官と医師の任務は１人の人間に兼ね備われていて、魔術が知識の代わりをしていた。初期の人間が植物を藥品として使う努力をした道筋を追求する試みを想像できる。しばしば、その土地に固有な植物のあるものに治療効果のあることが偶然に発見され、次の場所で試み観察するようになる。アグリッパ（Cornelius Agrippa 1486-1535）はその神秘哲学の本で、人間は多くの治療法を動物から学んでいると述べている。浣腸の使用は長いくちばしの鳥がくちばしに水を吸い込んで腸管に注入していることを見て発見したのであろうとさえ言っている。幼稚で不完全な医療の実施は古代にゆっくりと進歩し、ローマで行われていたと同じように、エジプト人、ユダヤ人、カルデア（古代バビロニア南部）人、インド人、ペルシャ人、およびシナ人やダッタン人によって行われた。　エトルリア（古代イタリア中部）人は哲学および医学にかなり堪能であり、古代ローマ人は彼らおよびサビニ（古代ローマの北東）人から知識を得ていた。サビニ出身のヌマ王（Numa Pompilius：王政ローマ第２代の王、715BC-）は物理学を学び、リウィウス（Titus Livius：英語では Livy、ローマの歴史家、59BC-17AD）によると実験の結果として稲妻に打たれて死去したとのことである。従って実験は電気の研究と考えられる。ヌマ王の十二表法に歯科手術が述べられているのは驚くべきことである。初期においてローマ人は他の民族のもっと有用な知識よりも迷信を習うことが多かったようである。ローマ人は宗教におけると同じように医療においてもコスモポリタンであった。彼らはすべての未開人たちに知られている家庭医学、かなり粗雑な手術、シビュラの書による処方箋を知っており、魔術に頼っていた。ローマ人たちが医療の知識および一般に芸術と科学を得たのはまず第１にギリシャからであるが、何時になっても知能文化においてギリシャ人には及ばなかった。神殿　大プリニウス（英語 Pliny 23-79AD）は次のように述べた。「ローマ人たちは600年以上にわたって実際に医学を持たなかったわけではないが、医師たちを持たなかった。」ローマ人たちはこれまでと同じ家庭薬を使い、病気および治癒の神および女神を持っていた。フェブリスは発熱の神であり、メフィティスは悪臭の神であり、フェソニアは疲れた人たちを助け、「甘いクロアキナ」は下水道を統括する。疫病に罹った人たちはアンゲロニア女神に、女たちはフルオニアとウテリナに哀願する。オッシパガは子どもたちの骨の世話をし、カルナは腹部臓器を管理する。レクティステルニウム―アスクレピオス神殿　アスクレピオス（Aesculapius）の父親とみなされているアポロンを祀る神殿は紀元前467年にローマに建立され、紀元前460年にエピダウロス（Epidaurus）のアスクレピオスが祀られた。10年後にローマ市内に疫病が流行したときにサルス（Salus：ギリシャのヒュギエイアに相当するローマの女神）を祀る神殿が建立された。紀元前399年にはシビュラの書の命令によって疫病を防ぐためにローマ市で最初のレクティステルニウムの大祭（lectisternium）が行われた。これはギリシャ起源の祭りであり、祈りと捧げ物の時であった。カウチ（lectus）が広げられて（sternere）神々の像が横たえられ、その前に食物をのせたテーブルが置かれた。これらの祭りは必要とあれば繰り返され、「疫病が暗闇を歩かず」「昼間に起きる破壊が無駄になる」ようにジュピター（ローマの主神）の神殿に釘を打ち込む仕掛けは、紀元前360年に始まった。適当な外科の知識が不足していた証拠として、ストリウム（紀元前309年）の戦闘の後で兵隊は戦闘よりも傷によって死亡した事実をリウィウスは記録している。アスクレピオスの信仰はローマでは紀元前291年に始まり、エジプトのイシス（Isis）およびセラピス（Serapis）の治癒能力もまた祈祷された。　ローマの大疫病（紀元前291年）にさいして、シビュラの書により使節がエピダウロスに送られ、アスクレピオスに助けを求めた。使節はアスクレピオスの神像を持ち帰ったが、彼らの船がテヴェレ川（イ：Tevere、英：Tiber）を遡行しているときに、航海中に隠れていたヘビが船から滑り出て、アスクレピオス自身がローマ市民を助けに来たと信じていた人々が歓迎している土手に上陸した。この疫病の後紀元前291年にアスクレピオス神殿はテヴェレ川のこの島に建立された。タルクィニウス王（王政最後の王、在位536-509BC）が追い出されたときに彼らの収穫物は慣習によってこの川に投げ入れられ土がこれに蓄積されて、この島が作られた。ヘビが船から上がった不思議な出来事によって島の端にアスクレピオス神殿が立てられた。これは船首のような形に作られ、アスクレピオスのヘビはレリーフとして彫刻された。この島はアエミリア帝橋から遠くなく、壊れたアーチが一つ残っている。"
kanji_count = count_kanji(text)
print(f"文章中の漢字の数: {kanji_count}個")