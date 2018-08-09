

class CluckyRouter:
    """
    Router to use clucky db information
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('clusers', 'main'):
            return 'clucky'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ('clusers', 'main'):
            return 'clucky'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        pass
