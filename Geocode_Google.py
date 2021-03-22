from pygeocoder import Geocoder

endereco = '2829, Abel Scuissiato, Paraná, PR'

print(Geocoder('AIzaSyCRJfO_KDfHLrWcnMKtT0jChsZnCeu8-Vk').geocode(endereco).coordinates)