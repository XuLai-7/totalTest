"""综合案例"""
# 测试数据
import jsonschema

data = {
    "success": False,
    "code": 10000,
    "message": "xxx登录成功",
    "data": {
        "name": "lily",
        "age": 20,
    }

}
# 校验规则

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
            "pattern": "登录成功$"
        },
        "data": {
            "type": "object",
            "properties": {
                "name": {
                    "const": "lily"
                },
                "age": {
                    "const": 20
                }
            },
            "required": ["name", "age"]
        }
    },
    "required": ["success", "code", "message", "data"]
}

# 调用测试方法
res = jsonschema.validate(instance=data, schema=schema)
print(res)
