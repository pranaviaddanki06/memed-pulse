"""Optional offline training path. The Vercel demo uses its deterministic TypeScript surrogate."""
from pathlib import Path
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import joblib,json
d=pd.read_csv(Path(__file__).parents[1]/'data/prototype_content.csv');cols=['emotion','novelty','cultural_relevance','alignment','brand_suitability'];xtr,xte,ytr,yte=train_test_split(d[cols],d.performance,test_size=.2,random_state=42);m=GradientBoostingRegressor(random_state=42).fit(xtr,ytr);p=m.predict(xte);Path(__file__).parents[1].joinpath('models').mkdir(exist_ok=True);joblib.dump(m,Path(__file__).parents[1]/'models/model.pkl');json.dump({'mae':mean_absolute_error(yte,p),'rmse':mean_squared_error(yte,p)**.5,'r2':r2_score(yte,p)},open(Path(__file__).parents[1]/'evaluation/metrics.json','w'))
