import matplotlib.pyplot as plt
import numpy as np

filename = 'algorithm.s'


with open(filename, "r") as myfile:
    data = myfile.read().replace('\n', '')

    #подсчёт кол-ва повторений вызовов общих регистров

    freq_eax = data.count('%eax')
    freq_ebx = data.count('%ebx')#оперативная память
    freq_ecx = data.count('%ecx')
    freq_edx = data.count('%edx')

    freq_esp = data.count('%esp')
    freq_ebp = data.count('%ebp')#оперативная память
    freq_esi = data.count('%esi')#оперативная память
    freq_edi = data.count('%edi')#оперативная память

    #Общее число вызовов
    #       первая группа общих регистров                  вторая группа общих регистров
    total = freq_eax + freq_ebx + freq_ecx + freq_edx +    freq_esp + freq_ebp + freq_esi +freq_edi



data = {'EAX': freq_eax,
        'EBX': freq_ebx,
        'ECX': freq_ecx,
        'EDX': freq_edx,

        'ESP': freq_esp,
        'EBP': freq_ebp,
        'ESI': freq_esi,
        'EDI': freq_edi}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

objects = ('EAX \n%i' %freq_eax, 'EBX\n%i\nО.П.' %freq_ebx, 'ECX\n%i' %freq_ecx, 'EDX \n%i' %freq_edx,
           'ESP \n%i' %freq_esp, 'EBP\n%i\nО.П.' %freq_ebp, 'ESI\n%i\nО.П.' %freq_esi, 'EDI \n%i\nО.П.' %freq_edi)
y_pos = np.arange(len(objects))

performance = [freq_eax, freq_ebx, freq_ecx, freq_edx, freq_esp, freq_ebp, freq_esi, freq_edi]

plt.bar(y_pos, performance, align='center', alpha=0.5, color='rgbk')
plt.xticks(y_pos, objects)
plt.ylabel('Количество вызовов общих регистров')
plt.title('Количество вызовов всех общих регистров: %i' %total)

plt.show()