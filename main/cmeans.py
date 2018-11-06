import json
import random
import math
from pprint import pprint
import os

def clusterize(data, features, n_cluster=5, fuzziness=2, n_iteration=100):
    membership_matrix = {}
    for key, features in data.items():
        membership_matrix[key] = [random.uniform(0, 1) for _ in range(0, n_cluster)]

    centroids = {}
    for c in range(0, n_cluster):
        centroid = {}
        for feature in features:
            centroid[feature] = 0
        centroids[c] = centroid

    def compute_centroids():
        for cluster, centroid in centroids.items():
            for feature in features:
                num = 0
                den = 0
                for key, record in data.items():
                    num += (membership_matrix[key][cluster] ** fuzziness) * record[feature]
                    den += (membership_matrix[key][cluster] ** fuzziness)
                centroid[feature] = num / den

    def distance(vec_a, vec_b):
        total = 0
        for key, _ in vec_a.items():
            total += (vec_a[key] - vec_b[key]) ** 2

        return math.sqrt(total)

    def compute_memberships():
        for i, m_matrix_rec in membership_matrix.items():
            for j in range(0, n_cluster):
                total = 0
                for k in range(0, n_cluster):
                    total += (
                        distance(data[i], centroids[j]) /
                        distance(data[i], centroids[k])
                    ) ** (2 / (fuzziness - 1))
                membership_matrix[i][j] = 1 / total

    for i in range(0, n_iteration):
        compute_centroids()
        compute_memberships()

    result = {}
    for key, record in membership_matrix.items():
        result[key] = record.index(max(record)) 

    return result

if __name__ == "__main__":
    with open('data.json') as file:
        data = json.load(file)

    processed_data = {}

    for record in data:
        record_id = record['id']
        del record['id']
        del record['nama']
        del record['NIP']
        processed_data[record_id] = record

    features = [
        'nilai_1', 'nilai_2', 'nilai_3', 'nilai_4', 'nilai_5', 'nilai_6', 'nilai_7', 'nilai_8',
        'nilai_9', 'nilai_10', 'nilai_11', 'nilai_12', 'nilai_13', 'nilai_14', 'nilai_15', 'nilai_16',
        'nilai_17',
    ]

    clusterize(processed_data, features=features)