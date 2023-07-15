from rest_framework import routers

from supplier_network import views

# Создаем роутер для модели Factory (Завод)
router_factory = routers.SimpleRouter()
router_factory.register(r"factories", views.FactoryViews)

# Создаем роутер для модели RetailsNetwork (Розничная сеть)
router_retail = routers.SimpleRouter()
router_retail.register(r"retails", views.RetailsNetworkViews)

# Создаем роутер для модели IndividualEntrepreneur (Индивидуальный предприниматель)
router_individual = routers.SimpleRouter()
router_individual.register(r"individuals", views.IndividualEntrepreneurViews)

# Объявляем пустой список urlpatterns
urlpatterns = []

# Добавляем URL-пути для каждого роутера в список urlpatterns
urlpatterns += router_factory.urls + router_individual.urls + router_retail.urls
