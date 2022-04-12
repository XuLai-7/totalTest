import jsonschema

# 创建校验规则
# json 数据对应 python 中 字典数据
schema = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean",
            "const": True
        },
        "code": {
            "type": "integer",
            "const": 10000

        },
        "message": {
            "type": "string",
            # "const": "操作成功",
            "pattern": "操作成功" # 以操作成功开头
        },
        "mobile": {
            "type": "number",
            # "const": "操作成功",
            "pattern": "^[0-9]{11}$"
        },
        "money": {
            "type": "number"
        },
        "address": {
            "type": "null"
        },
        "data": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "const": "tom"
                },
                "age": {
                    "type": "integer",
                    "const": 10
                },
                "height": {
                    "type": "number"
                }
            },
            "required": ["name", "age", "height"]
        },
        "luckynumber": {
            "type": "array"
        }
    },
    "required": ["success", "code", "message", "money", "address", "data", "luckynumber"]
}
# 准备待校验数据
data = {
    "success": True,
    "code": 10000,
    "message": "!!!操作成功@@@@",
    "mobile": 138000000213131222,
    "money": 6.66,
    "address": None,
    "data": {
        "name": "tom",
        "age": 10,
        "height": 1.78,
        "abc": 123
    },
    "luckynumber": [6, 8, 9]
}

# 调用 jsonschema.validate(instance="json 数据", schema="jsonschema 规则") 进行校验
res = jsonschema.validate(instance=data, schema=schema)
print(res)
