# Penerimaan kandidat programer sistem
coding_score = int(input('Enter coding test score: '))
interview_score = input('Enter interview test score (A or B): ')

# Evaluasi coding test score
if coding_score > 80:
    coding_result = 'LOLOS'
elif 60 <= coding_score <= 80:
    coding_result = 'DIPERTIMBANGKAN'
else:
    coding_result = 'GAGAL'

# Evaluate interview test score
if interview_score in ['A', 'B']:
    interview_result = 'LOLOS'
else:
    interview_result = 'GAGAL'

# Determine overall result
if coding_result == 'LOLOS' and interview_result == 'LOLOS':
    print("Congratulations! You've successfully become a Programmer candidate.")
else:
    print("Sorry, you haven't successfully become a Programmer candidate.")