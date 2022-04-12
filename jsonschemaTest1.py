import jsonschema

# 创建校验规则
# json 数据对应 python 中 字典数据

schema = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": ["success", "code", "message"]
}
# 准备待校验数据
data = {
    "success": True,
    "code": 10000,
    "message": "操作成功"
}

# 调用 jsonschema.validate(instance="json 数据", schema="jsonschema 规则") 进行校验
res = jsonschema.validate(instance=data,schema=schema)
print(res)