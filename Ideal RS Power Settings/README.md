# Ideal RS Power Settings

Simulation of ideal RS power settings for LTE based on bandwidth and Power per Antenna Port (RS Antenna Port). This simulation consider only the combination of Pa-Pb ratio parameters that allows 100% Tx Power utilization.

### Explanation
In LTE, DL power allocation is calculated based on ratio concept. The concept is derived from 3GPP 36.213 Sec 5.2.

<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain01.png" alt="DL PA Concept" title="DL PA Concept" width=100% height=100% />
<br />
<br />
Roughly, 3D representation of DL power ratio can be seen as below figure:
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain02.png" alt="3D PA" title="3D PA" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain03.png" alt="Example" title="Example" width=100% height=100% />
<br />

### Reference

Simple Math of the ratio concept can be calculated as follows:
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain04.png" alt="Calc" title="Calc" width=100% height=100% />
<br />
<br />
RS Power can be calculated using the formula below. Based on the combination of Pa (dB) and Pb, power utilization ratio in DL can be identified.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain05.png" alt="Formula" title="Formula" width=100% height=100% />
<br />
<br />
Sample Calculation for RS power by assumption of Bandwidth and Power per Antenna Port.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain06.png" alt="Sample Calc" title="Sample Calc" width=100% height=100% />
<br />
<br />

### 3GPP Specs

3GPP 36.213 Sec 5.2.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain07.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain08.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain09.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />

### Running The Program

Expected results based on given input. The program will calculate Ideal RS Power Settings based on BW and Power per Antenna Port for every 100% Power Utilization Pa-Pb combination.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result01.png" alt="Input" title="Input" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result5MHz_3.png" alt="5MHz" title="5MHz" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result10MHz_3.png" alt="10MHz" title="10MHz" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result20MHz_3.png" alt="20MHz" title="20MHz" width=100% height=100% />
<br />
<br />
