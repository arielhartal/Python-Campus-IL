def mult_tuple(tuple1, tuple2):
	m_list = []
	for i in range(len(tuple1)):
		for j in range(len(tuple2)):
			m_tuple1 = tuple1[i] , tuple2[j]
			m_tuple2 = tuple2[j] , tuple1[i]
			m_list.append(m_tuple1)
			m_list.append(m_tuple2)
		
	return tuple(m_list)
	
print(mult_tuple((1, 2,3),(4, 5,6)))		