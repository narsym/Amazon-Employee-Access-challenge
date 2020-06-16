from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
resource = int(input('resource'))
mgr = int(input('MGR_ID'))
r1 = int(input('Role rollup 1'))
r2 = int(input('role rollup 2'))
rd = int(input('role deptname'))
rt = int(input('role title'))
rfd = int(input('role family desc'))
rf = int(input('role family'))
data = [resource, mgr, r1, r2, rd, rt, rfd, rf]
data = np.array(data)
data = data.reshape(1, -1)
result = loaded_model.predict(data)
print('The prediction for the given resource is:', result[0])