"""
    待校验的JSON数据
        {
            "scuccess":true,
            "code",10000,
            "message":"操作成功"
        }
    校验规则描述
        整个 JSON 数据是一个对象
        包含 success, code, message 字段,并且 必须存在
        success 字段为布尔型
        code 为整数
        message 为字符串
        ...
    编写json语法代码的校验规则

    调用 jsonschema.validate(instance="json 数据", schema="jsonschema 规则")

校验方式
        在线工具校验
        https://www.jsonschemavalidator.net/

        python 代码使用 jsonschema 库校验
        校验通过, 返回 None
        校验失败, schema 规则错误: SchemaError  校验规则语法有误
                 json 数据错误:  ValidationError  数据与校验规则不符

    JSON Schema 语法
        type: 约束数据类型
            integer
            string
            object 对象
            array  --> python: list 列表
            number 整数 /小数
            null 空值  --> python: None
            boolean

            语法:
                {
                    "type":"数据类型"
                }

        properties: key-value对 中 对 value 的限制条件
            是 type 关键字的辅助,用于 type的值为 obejct 的场景
            作用: 指定对象中 每个字段的校验规则, 可以嵌套使用

            语法:
                {
                "type": "object",
                "properties": {
                    "字段名1": {
                        规则
                    },
                   "字段名2": {
                        规则
                    },
                    ...
                嵌套使用:
                  "data": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "age":{
                                "type": "integer"
                            },
                            "height":{
                                "type": "number"
                            }
                        }
                    },
        required: 校验JSON对象中必须存在的key (字段名), 且唯一
            语法:
            "required": ["字段名1", "字段名2",...]

        const: 校验JSON字段的值必须等于指定的内容 (固定值)
            语法:
            "字段名": {
                "const":具体的值
            }
        如果具体值都能确定就不需要 type 校验了,直接用 const 校验具体值

        pattern: 指定正则表达式,对字符串类型数据进行模糊匹配
            基础正则举例:
                包含字符串: hello
                以字符串开头 ^: ^hello
                以字符串结尾 $: hello$
                匹配[]内任意1一个字符[]: [0-9]匹配任意一个数字  [a-z]匹配任意一个小写字母 [cjfew21312] 匹配任意一个 都是匹配任意一个
                匹配指定次数{}: [0-9]{11} 匹配11位数字  匹配出11个数,在 0-9 之间 此处, 匹配多个
                匹配手机号: ^[0-9]{11}$ 简单例子

            语法:
            {
                "字段名":{"pattern":"正则表达式"}
            }

                "message": {
                    "type": "string",
                    # "const": "操作成功",
                    "pattern": "^操作成功" # 以操作成功开头
                },
                "mobile": {
                    "type": "number",
                    # "const": "操作成功",
                    "pattern": "^[0-9]{11}$"
                },



# json 数据对应 python 中 字典数据




"""


















