from collections import defaultdict

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# as chaves são os anos, os valores são as listas dos salários para cada ano
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# as chaves são os anos, cada valor é a média salarial para aquele ano
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two years"
    elif tenure < 5:
        return "between two and five years"
    else:
        return "more than five years"


# as chaves são agrupamentos dos casos, os valores são as listas dos salários para aquele agrupamento
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# as chaves são agrupamentos dos casos, os valores são a média salarial para aquele agrupamento
average_salary_by_bucket = {
    tenure_bucket: round(sum(salaries) / len(salaries), 2)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print(average_salary_by_bucket)
