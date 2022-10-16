from db.mysql_db import pool

class NewsDao:
    # 查询待审批新闻列表
    def search_unreview_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                "JOIN t_user u ON n.editor_id=u.id " \
                "WHERE n.state=%s " \
                "ORDER BY n.create_time DESC " \
                "LIMIT %s,%s"  # 起始位置，每页显示多少
            cursor.execute(sql,("待审批",(page-1)*10,10))
            result = cursor.fetchall()   # 这里有多条记录，使用fetchall
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s"
            cursor.execute(sql,["待审批"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 更新审批信息   这里需要开启事务
    def update_unreview_news(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state=%s WHERE id=%s"
            cursor.execute(sql,("已审批",id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()

    # 查询新闻列表
    def search_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                "JOIN t_user u ON n.editor_id=u.id " \
                "ORDER BY n.create_time DESC " \
                "LIMIT %s,%s"  # 起始位置，每页显示多少
            cursor.execute(sql,((page-1)*10,10))
            result = cursor.fetchall()   # 这里有多条记录，使用fetchall
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()


    # 查询新闻总数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 根据新闻id删除新闻
    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id=%s"
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
        finally:
            if "con" in dir():
                con.close()

# service = NewsDao()
# result = service.search_unreview_list(1)
# print(result)