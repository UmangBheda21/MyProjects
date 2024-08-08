# एक सामान्य उदाहरण: डेटा सेट और उसके लेबल्स को लोड करना
import pandas as pd

# डेटा सेट लोड करें
data = pd.read_csv('dataset.csv')

# डेटा का अध्ययन करें
print(data.head())

# लेबल्स लोड करें
labels = pd.read_csv('labels.csv')

# लेबल्स का अध्ययन करें
print(labels.head())
