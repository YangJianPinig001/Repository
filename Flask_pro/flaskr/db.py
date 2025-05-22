
# migrate
# ORM映射插件的使用
# 1. flask db init # 初始化迁移环境
# 2. flask db migrate # 生成迁移脚本
# 3. flask db upgrade # 执行迁移脚本



# with app.app_context():
#     with db.engine.connect() as conn:
#         from sqlalchemy import text
#         result = conn.execute(text("SELECT VERSION()"))
#         version = result.fetchone()
#         print(f"Database version: version{version}")


