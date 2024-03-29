EC2_COST_PER_HOUR = 0.0216  # EC2料金単価(USD/hour t4g.small)
EBS_STORAGE_SIZE = 30       # EBSストレージサイズ(GB)
EBS_COST_PER_GB = 0.096     # EBS料金単価(USD/GB gp3ストレージ)
LAMBDA_MEM_SIZE = 4.096     # LAMBDAメモリサイズ(GB 4096MB)
LAMBDA_COST_PER_MEMS = 0.000016667    # LAMBDA料金単価(USD/メモリGB・S)
LAMBDA_COST_PER_REQ  = 2 * (10 ** -7) # LAMBDA料金単価(USD/リクエスト)
LAMBDA_REQ_FREE_TIER = 1000000        # LAMBDA無料利用枠
LAMBDA_GBS_FREE_TIER = 400000         # LAMBDA無料利用枠(コンピューティング時間GB・s)
OUT_DATA_COST_PER_GB = 0.114          # インターネットへのデータ転送(USD/GB 最初の 10 TB/月)
OUT_DATA_COST_FREE_TIER = 100000000   # インターネットへのデータ転送無料利用枠(100GB)
