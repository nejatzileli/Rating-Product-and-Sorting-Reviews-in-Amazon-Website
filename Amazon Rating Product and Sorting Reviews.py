import pandas as pd
import numpy
import matplotlib.pyplot as plt
import xlrd
!pip install openpyxl
from scipy.stats import shapiro
from scipy.stats import levene
from scipy.stats import ttest_ind
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' %x)



data = pd.ExcelFile("Datasets/ab_testing.xlsx")
control_df = pd.read_excel(data, 'Control Group')
control = control_df.copy()
test_df = pd.read_excel(data, 'Test Group')
test = test_df.copy()

control.dropna(axis=1,inplace = True)
test.dropna(axis=1,inplace = True)

control.describe().T
test.describe().T

control['group'] = 'control'
test['group'] = 'test'

new_df = pd.concat([control,test], ignore_index = True) #merge ortak elemana gore ekler, concat dirakt alta yada yana ekler.

new_df



#Niye outlier'lari cikartmiyoruz?
# ayirilari eleyecem mi? atacam mi?
# hatali islenise at
# eger ender gozlenen bisiyse sunu sor analizime katki saglanio mu?
#?????????????????????????????????????????????????????
# outlier demek her zaman mudahale edicemiz bisey anlamina gelmez
# iki durum arasinda anlamli bi fark lup olmadigina bakiom. Test veri var kontrol  veri var,
# salliyorum. kONTROL =550 TEST= 650 ANLAMLI BIR FARK VAR GIBI GOZUKUOR. EE SIMDI BEN TESTTEN OUTLIER
# OLANLARI CIKARTTIM. INSTA DA IKI ARAYUZ VAR. IKINCI ARAYUZ DE DAHA COK GIRDI. DAHA COK SATIS. NORMAL SATTIGIMIN
# USTUNDE SATTIM. BU DA NE OLDU? OUTLIER OLDU. NORMAL SATTIGIMN USTUNDE SATTIM ICIN OUTLIER GGERIYE CEKTIK.
# SIRF BEN BUNLARI BASKILADIGIM ICIN  TEST 580 OLDU. DEDIM KI ANLAMLI BIR FARK YOKTUR DEDIM.
# SONRA BI BAKIYOSUN SEN OUTLIERLARI CIKARTTIGIN ICIN VERIYE MUDAHALE ETTIN VE TEST FARK YOK VERICEK.
# OUTLIER DEDIGIN ZAMAN ASLINDA O OUTLIER IN NEDEN OLDUGUNA BAKMAN LAZIM.


test['Purchase'].mean()

control['Purchase'].mean()

# Fark Var gibi gozukuyor.

# Gorev2.1 Hipotezi Tanimla.
 # H0 = Average bidding in purchase ortalamasi
 # h1 = Maximum bidding in purchase ortalamasi
 # hipotezim ise h0 == h1 yani average bidding in purchase ortalamasi ile maximum bidding in purchase ortalamasi
 # arasinda anlamli bir fark yoktur. Ve h0 != h1 iki ortalama arasinda anlamli bir fark vardir.


# Gorev 2.2

# Normallik testi. H0: m1= m2 (normal dagilim varasayimi saglanmaktadir) h1: m1 != m2 normallik varsayimi saglanmamaktadir.

test_stat, pvalue = shapiro(test['Purchase'])
print('Test Stat: %.4f, p-value: %.4f' % (test_stat, pvalue)) # pvalue=0.15 >0.05. H0 reddedilmedi. Normallik varsayimi bu grup icin saglandi. Ya diger grup?

#test_stat, pvalue = shapiro(control['Purchase'])
#print('Test Stat: %.4f, p-value: %.4f' % (test_stat, pvalue)) # pvalue = 0.5891 >0.05. H0 reddedilmedi. Normallik varsayimi saglandi.

test_stat, pvalue = levene(test['Purchase'], control['Purchase'])
print('Test Stat: %.4f, p-value: %.4f' % (test_stat, pvalue))

test_stat, pvalue = ttest_ind(test['Purchase'], control['Purchase'])

pvalue #h0 failed to reject. Kontrol ve test Gruplarinin satin alma ortalamalari arasinda
# anlamli bir farklilik yoktur.

# Gorev 4

# Once kontrol ve test gruplari icin iki normallik testi yaptim shapiro fonksiyonunu kullanarak.
# Shapiro normallik testinden cikan p degerleri ikisindede 0.05'ten buyuk oldugu icin h0 hipotezini
# reddetmedim.
# Daha sonra iki grubunda varyanslarininin homojen dagilip dagilmadigina bakmak icin levene testi yaptim.
# P Degerleri iki gruptada 0.05'ten buyuk oldugu icin h0 failed to reject oldu. Iki grupta varyanslar homojen dagilmis.
# Normal dagilim saglanmis ve varyans homojenligide saglandigina gore parametrik bir test kullanacaktik.


# Iki grubun satin alma ortalamalari arasinda bir farklilik yok. Dolayisiyla, average bidding'in
# maximum bidding'den daha fazla musteri donusumu sagladigina dair bir isaret istatistiksel olarak bulunamadi.
# average bidding ozelligini sitemize eklemek bize bir avantaj getirmeyecek. Dolayisiyla average bidding projesini
# iptal edebiliriz.

# 40 gozlem var. Biraz daha veri toplayip daha saglikli gozlem yapabiliriz. yani daha fazla veriyle ayni testleri
# tekrar yapip bir fark cikmasini bekleyebiliriz.