engine=http://{{ .Env.ENGINE_IP }}:{{ .Env.ENGINE_PORT }}
clustering=http://{{ .Env.CLUSTERING_IP }}:{{ .Env.CLUSTERING_PORT }}
classification=http://{{ .Env.CLASSIFICATION_IP }}:{{ .Env.CLASSIFICATION_PORT }}