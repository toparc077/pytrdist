# -*- coding: utf-8 -*-

SERVICE_CHOICES = (
    ('経営者向け', (
        ('manager01', '経営コンサルティング'),
        ('manager02', '資金調達'),
        ('manager03', '賃貸オフィス・レンタルオフィス'),
        ('manager04', '秘書代行'),
        ('manager05', 'Pマーク・ISO取得'),
        ('manager06', '海外進出'),
        ('manager07', '会社設立'),
        )
    ),
    ('営業向け', (
        ('sales01', 'CRM・SFA'),
        ('sales02', '営業代行'),
        ('sales03', 'コールセンター'),
        ('sales04', 'メールマーケティング'),
        ('sales05', 'ノベルティ制作'),
        ('sales06', '営業力強化'),
        ('sales07', 'FAXDM'),
        ('sales08', '名刺管理'),
        ('sales09', '企業リスト'),
        )
    ),
    ('総務向け', (
        ('general01', '貸し会議室'),
        ('general02', '通信・携帯'),
        ('general03', '賃貸オフィス・レンタルオフィス'),
        ('general04', '事務用品・事務機器'),
        ('general05', '社内イベント'),
        ('general06', 'データ入力'),
        )
    ),
    ('人事向け', (
        ('human01', '人材育成・社員研修'),
        ('human02', '採用支援'),
        ('human03', '適性検査'),
        ('human04', 'メンタルヘルス'),
        ('human05', '人事評価システム'),
        ('human06', '就業規則'),
        )
    ),
    ('広報・販促向け', (
        ('pr01', 'マーケティング支援'),
        ('pr02', 'HP制作・デザイン'),
        ('pr03', 'チラシ・パンフレット印刷'),
        ('pr04', 'プレスリリース'),
        ('pr05', 'リスティング広告'),
        ('pr06', 'SEO'),
        ('pr07', 'メール配信システム'),
        ('pr08', '商品企画'),
        ('pr09', 'ブランド戦略'),
        )
    ),
    ('WEB担当向け', (
        ('web01', 'HP制作・デザイン'),
        ('web02', 'WEBシステム開発'),
        ('web03', 'レンタルサーバー・ホスティング'),
        ('web04', 'セキュリティ対策'),
        ('web05', 'WEBマーケティング'),
        ('web06', 'SEO'),
        ('web07', 'リスティング広告'),
        ('web08', '決済代行'),
        )
    ),
    ('その他', (
        ('other01', 'その他'),
        )
    ),
)

TARGET_TYPE_CHOICE = (
    ('0',  '全企業'),
    ('1',  '小売・卸売・商社'),
    ('2',  '飲食・宿泊'),
    ('3',  'サービス  ＩＴ・広告・マスコミ'),
    ('4',  'コンサル・会計・法務関連'),
    ('5',  '人材'),
    ('6',  '病院・福祉・介護'),
    ('7',  '不動産'),
    ('8',  '金融・保険'),
    ('9',  '教育・学習'),
    ('10', '建設・建築'),
    ('11', '運輸'),
    ('12', '製造'),
    ('13', '電気・ガス・水道'),
    ('14', '農林水産'),
    ('15', '鉱業'),
    ('16', '官公庁'),
    ('17', '組合・団体・協会'),
    ('18', '主婦・学生（なし）'),
    ('19', 'その他'),
)

TARGET_SIZE_CHOICE = (
    ('all', '企業規模問わず'),
    ('1-9', '1～9名'),
    ('10-49', '10～49名'),
    ('50-99', '50～99名'),
    ('100-299', '100～299名'),
    ('300-499', '300～499名'),
    ('500-999', '500～999名'),
    ('1000-2999', '1000～2999名'),
    ('3000-4999', '3000～4999名'),
    ('5000-9999', '5000～9999名'),
    ('10000-', '10000名以上'),
)

STATUS_CHOICE = (
    (0, '下書き'),
    (1, '公開'),
    (2, '削除'),
)

