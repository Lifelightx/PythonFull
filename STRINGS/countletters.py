my_str = "hello jeeban"

m_d = {}

for i in my_str:
    if i not in m_d.keys():
        m_d[i] = 1
    else:
        m_d[i] +=1
        
print(m_d)