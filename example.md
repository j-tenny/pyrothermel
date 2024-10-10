```python
import pyrothermel
import pandas as pd
import seaborn as sns
```

## Setup Base Fuel Model and Moisture Scenario


```python
moisture = pyrothermel.MoistureScenario.from_existing(dead_fuel_moisture_class='low',live_fuel_moisture_class='moderate')
fuel = pyrothermel.FuelModel.from_existing(identifier='TL8')
canopy_base_height = 2.5 # default unit is m
canopy_bulk_density = .1 # default unit is kg/m^3

# Print some fuel loading values from fuel model TL8
print([fuel.fuel_load_one_hour, fuel.fuel_load_ten_hour, fuel.fuel_load_hundred_hour])
print(fuel.units.loading_units)

```

    [1.300187341185569, 0.31383832373444764, 0.2465872543627803]
    LoadingUnitsEnum.KilogramsPerSquareMeter
    

## Run Rothermel Models Across Range of Wind Speeds


```python
results_list = []
for wind_speed in range(0,60,2):
    run = pyrothermel.PyrothermelRun(fuel,moisture,wind_speed,wind_input_mode='ten_meter',canopy_base_height=canopy_base_height,canopy_bulk_density=canopy_bulk_density,canopy_cover=.5,canopy_height=20,canopy_ratio=.6)
    results_surface = run.run_surface_fire_in_direction_of_max_spread()
    results_final = run.run_crown_fire_scott_and_reinhardt()
    results_final['wind_speed'] = wind_speed
    results_final['treatment'] = 'untreated'
    results_list.append(results_final)
    
untreated_crowning_index = run.calculate_crowning_index()
untreated_torching_index = run.calculate_torching_index()
    
df = pd.DataFrame(results_list)
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>spread_rate</th>
      <th>flame_length</th>
      <th>fireline_intensity</th>
      <th>scorch_height</th>
      <th>transition_ratio</th>
      <th>active_ratio</th>
      <th>fire_type</th>
      <th>wind_speed</th>
      <th>treatment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.035297</td>
      <td>0.850504</td>
      <td>182.940784</td>
      <td>5.005403</td>
      <td>0.274758</td>
      <td>0.025974</td>
      <td>Surface</td>
      <td>0</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.036477</td>
      <td>0.863471</td>
      <td>189.058483</td>
      <td>5.150455</td>
      <td>0.283946</td>
      <td>0.033603</td>
      <td>Surface</td>
      <td>2</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.038485</td>
      <td>0.885015</td>
      <td>199.463628</td>
      <td>5.391881</td>
      <td>0.299574</td>
      <td>0.046541</td>
      <td>Surface</td>
      <td>4</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.040997</td>
      <td>0.911142</td>
      <td>212.486479</td>
      <td>5.685303</td>
      <td>0.319133</td>
      <td>0.062713</td>
      <td>Surface</td>
      <td>6</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.043907</td>
      <td>0.940336</td>
      <td>227.566123</td>
      <td>6.013981</td>
      <td>0.341781</td>
      <td>0.081423</td>
      <td>Surface</td>
      <td>8</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.047152</td>
      <td>0.971693</td>
      <td>244.386618</td>
      <td>6.367902</td>
      <td>0.367044</td>
      <td>0.102279</td>
      <td>Surface</td>
      <td>10</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.050693</td>
      <td>1.004603</td>
      <td>262.738585</td>
      <td>6.740268</td>
      <td>0.394606</td>
      <td>0.125023</td>
      <td>Surface</td>
      <td>12</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.054500</td>
      <td>1.038631</td>
      <td>282.470446</td>
      <td>7.126172</td>
      <td>0.424242</td>
      <td>0.149466</td>
      <td>Surface</td>
      <td>14</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.058551</td>
      <td>1.073456</td>
      <td>303.466091</td>
      <td>7.521935</td>
      <td>0.455775</td>
      <td>0.175465</td>
      <td>Surface</td>
      <td>16</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.062828</td>
      <td>1.108839</td>
      <td>325.633015</td>
      <td>7.924731</td>
      <td>0.489067</td>
      <td>0.202906</td>
      <td>Surface</td>
      <td>18</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.067316</td>
      <td>1.144599</td>
      <td>348.895334</td>
      <td>8.332347</td>
      <td>0.524005</td>
      <td>0.231694</td>
      <td>Surface</td>
      <td>20</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.072003</td>
      <td>1.180595</td>
      <td>373.189391</td>
      <td>8.743023</td>
      <td>0.560492</td>
      <td>0.261751</td>
      <td>Surface</td>
      <td>22</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.076879</td>
      <td>1.216721</td>
      <td>398.460819</td>
      <td>9.155342</td>
      <td>0.598447</td>
      <td>0.293011</td>
      <td>Surface</td>
      <td>24</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.081935</td>
      <td>1.252892</td>
      <td>424.662512</td>
      <td>9.568151</td>
      <td>0.637799</td>
      <td>0.325414</td>
      <td>Surface</td>
      <td>26</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.087161</td>
      <td>1.289045</td>
      <td>451.753155</td>
      <td>9.980508</td>
      <td>0.678487</td>
      <td>0.358909</td>
      <td>Surface</td>
      <td>28</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.092553</td>
      <td>1.325129</td>
      <td>479.696141</td>
      <td>10.391632</td>
      <td>0.720454</td>
      <td>0.393453</td>
      <td>Surface</td>
      <td>30</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.098102</td>
      <td>1.361104</td>
      <td>508.458756</td>
      <td>10.800878</td>
      <td>0.763653</td>
      <td>0.429003</td>
      <td>Surface</td>
      <td>32</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.103804</td>
      <td>1.396940</td>
      <td>538.011536</td>
      <td>11.207708</td>
      <td>0.808038</td>
      <td>0.465524</td>
      <td>Surface</td>
      <td>34</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.109653</td>
      <td>1.432613</td>
      <td>568.327776</td>
      <td>11.611672</td>
      <td>0.853570</td>
      <td>0.502983</td>
      <td>Surface</td>
      <td>36</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.115645</td>
      <td>1.468107</td>
      <td>599.383126</td>
      <td>12.012394</td>
      <td>0.900212</td>
      <td>0.541350</td>
      <td>Surface</td>
      <td>38</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.121775</td>
      <td>1.503406</td>
      <td>631.155270</td>
      <td>12.409561</td>
      <td>0.947930</td>
      <td>0.580597</td>
      <td>Surface</td>
      <td>40</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.128040</td>
      <td>1.538500</td>
      <td>663.623663</td>
      <td>12.802911</td>
      <td>0.996695</td>
      <td>0.620699</td>
      <td>Surface</td>
      <td>42</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.241603</td>
      <td>3.448728</td>
      <td>1474.064719</td>
      <td>13.192226</td>
      <td>1.046476</td>
      <td>0.661632</td>
      <td>Torching</td>
      <td>44</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.379762</td>
      <td>5.160256</td>
      <td>2697.956066</td>
      <td>13.577327</td>
      <td>1.097248</td>
      <td>0.703375</td>
      <td>Torching</td>
      <td>46</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.536191</td>
      <td>7.103385</td>
      <td>4357.386068</td>
      <td>13.958064</td>
      <td>1.148986</td>
      <td>0.745907</td>
      <td>Torching</td>
      <td>48</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.711691</td>
      <td>9.296938</td>
      <td>6524.360652</td>
      <td>14.334319</td>
      <td>1.201667</td>
      <td>0.789210</td>
      <td>Torching</td>
      <td>50</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.907056</td>
      <td>11.754955</td>
      <td>9275.974007</td>
      <td>14.705996</td>
      <td>1.255270</td>
      <td>0.833266</td>
      <td>Torching</td>
      <td>52</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1.123074</td>
      <td>14.489637</td>
      <td>12694.462206</td>
      <td>15.073021</td>
      <td>1.309773</td>
      <td>0.878058</td>
      <td>Torching</td>
      <td>54</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1.360525</td>
      <td>17.512343</td>
      <td>16867.255868</td>
      <td>15.435336</td>
      <td>1.365159</td>
      <td>0.923571</td>
      <td>Torching</td>
      <td>56</td>
      <td>untreated</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1.620185</td>
      <td>20.833995</td>
      <td>21887.031854</td>
      <td>15.792902</td>
      <td>1.421409</td>
      <td>0.969790</td>
      <td>Torching</td>
      <td>58</td>
      <td>untreated</td>
    </tr>
  </tbody>
</table>
</div>



## Modify Fuel Loading and Recalculate


```python
fuel.fuel_load_one_hour *= .5
fuel.fuel_load_ten_hour *= .5
fuel.fuel_load_hundred_hour *= .75
fuel.fuel_bed_depth *= .5

results_list = []
for wind_speed in range(0,60,2):
    run = pyrothermel.PyrothermelRun(fuel,moisture,wind_speed,wind_input_mode='ten_meter',canopy_base_height=2.5,canopy_bulk_density=.1,canopy_cover=.5,canopy_height=20,canopy_ratio=.6)
    results_surface = run.run_surface_fire_in_direction_of_max_spread()
    results_final = run.run_crown_fire_scott_and_reinhardt()
    results_final['wind_speed'] = wind_speed
    results_final['treatment'] = 'treated'
    results_list.append(results_final)

treated_crowning_index = run.calculate_crowning_index()
treated_torching_index = run.calculate_torching_index()

df_treated = pd.DataFrame(results_list)
df = pd.concat([df,df_treated])
```

## Display Results


```python
sns.lineplot(df,x='wind_speed',y='flame_length',hue='treatment').set(xlabel='Wind Speed (km/hr)',ylabel='Flame Length (m)')
```




    [Text(0.5, 0, 'Wind Speed (km/hr)'), Text(0, 0.5, 'Flame Length (m)')]




    
![png](example_files/example_8_1.png)
    



```python
print('Wind Speed to initiate crown fire in untreated stand: ', untreated_torching_index, ' km/hr')
print('Wind Speed to initiate crown fire in treated stand: ', treated_torching_index, ' km/hr')
print('Wind Speed to propagate crown fire in untreated stand: ', untreated_crowning_index, ' km/hr')
print('Wind Speed to propagate crown fire in treated stand: ', treated_crowning_index, ' km/hr')
```

    Wind Speed to initiate crown fire in untreated stand:  43  km/hr
    Wind Speed to initiate crown fire in treated stand:  98  km/hr
    Wind Speed to propagate crown fire in untreated stand:  60  km/hr
    Wind Speed to propagate crown fire in treated stand:  60  km/hr
    
