from application import db
from application.core.db_models import DomainInfo
from sqlalchemy import or_
class DomainUtils:
    @staticmethod
    def get_search_domain(keyword):
        domain_response = DomainInfo.query.filter(DomainInfo.domain_name.like(f"%{keyword}%")).all()
        return domain_response

    @staticmethod
    def delete_selected_domains(selected_list):
        query = DomainInfo.query.filter(or_(*(DomainInfo.id == id_val for id_val in selected_list))).all()
        for domain_entity in query:
            domain_entity.is_active = False
        db.session.commit()
        return DomainInfo.query.all()


