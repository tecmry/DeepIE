# schema的中文医学信息抽取数据集CMeIE（Chinese Medical Information Extraction）
CMeIE_CONFIG = {
    "预防": 0,
    "阶段": 1,
    "就诊科室": 2,
    "辅助治疗": 3,
    "化疗": 4,
    "放射治疗": 5,
    "手术治疗": 6,
    "实验室检查": 7,
    "影像学检查": 8,
    "辅助检查": 9,
    "组织学检查": 10,
    "内窥镜检查": 11,
    "筛查": 12,
    "多发群体": 13,
    "发病率": 14,
    "发病年龄": 15,
    "多发地区": 16,
    "发病性别倾向": 17,
    "死亡率": 18,
    "多发季节": 19,
    "传播途径": 20,
    "并发症": 21,
    "病理分型": 22,
    "相关（导致）": 23,
    "鉴别诊断": 24,
    "相关（转化）": 25,
    "相关（症状）": 26,
    "临床表现": 27,
    "治疗后症状": 28,
    "侵及周围组织转移的症状": 29,
    "病因": 30,
    "高危因素": 31,
    "风险评估因素": 32,
    "病史": 33,
    "遗传因素": 34,
    "发病机制": 35,
    "病理生理": 36,
    "药物治疗": 37,
    "发病部位": 38,
    "转移部位": 39,
    "外侵部位": 40,
    "预后状况": 41,
    "预后生存率": 42,
    "同义词": 43
}

CMeEnt_CONFIG = {
    'bod': 0,  # 身体
    'dis': 1,  # 疾病
    'sym': 2,  # 临床表现
    'pro': 3,  # 医疗程序
    'dru': 4,  # 药物
    'ite': 5,  # 医学检验项目
    'mic': 6,  # 微生物类
    'equ': 7,  # 医疗设备
    'dep': 8,  # 科室
}

CMeEnt_Query = {
    # query max len default is 50
    "default": {
        "bod": "身体:身体物质,身体部位",
        "dis": "疾病:疾病或综合症,中毒或受伤,器官或细胞受损",
        "sym": "临床表现:症状,体征",
        "pro": "医疗程序:检查程序,治疗或预防程序",
        "dru": "药物:药物",
        "ite": "医学检验项目:医学检验项目",
        "mic": "微生物类:微生物类",
        "equ": "医疗设备:检查设备,治疗设备",
        "dep": "科室:科室",
    }
}
