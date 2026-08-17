"""Reproducibly generate correlated prototype data. See README; never represents platform data."""
import csv, random
random.seed(42)
with open('prototype_content.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=['id','caption','category','emotion','novelty','cultural_relevance','alignment','brand_suitability','performance']);w.writeheader()
 for i in range(300):
  e,n,c,a,b=[random.randint(45,95) for _ in range(5)];p=max(0,min(100,round(.21*e+.17*n+.21*c+.16*a+.12*b+random.gauss(0,6))))
  w.writerow(dict(id=i,caption=f'Prototype content {i}',category=['relatable','cricket','bollywood'][i%3],emotion=e,novelty=n,cultural_relevance=c,alignment=a,brand_suitability=b,performance=p))
