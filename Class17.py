import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

def create_scatter_plot(age, gender, address):
    plt.bar(age, gender, address)
    plt.xlabel('주소')
    plt.ylabel('나이')
    plt.title('서초구 주민 인구 - 나이, 성별, 주소')

address = ['강남대로', '반포대로', '신반포로', '잠원로']
age = [20,25,30,35,40,45,50,55,60]
gender = ['남성', '여성']

create_scatter_plot(age, gender, address)
plt.show()

