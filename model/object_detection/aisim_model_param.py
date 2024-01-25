EDGE = 0
CLOUD = 1
GW = 2

##### スペックパラメータ #####
MY_CPU_CLOCK    = 3.00  # 実験マシン(Intel Core i7-1185G7)
CLOUD_CPU_CLOCK = 2.50  # クラウドインスタンス(Intel Xeon Processor E5-2680 v3)
EDGE_CPU_CLOCK  = 1.50  # エッジ(ARM Cortex-A72)
GW_CPU_CLOCK  = 1.90    # エッジ(ARM Cortex-A57W)

MY_CPU_CORES    = 2     # 実験マシンのコア割当て数
CLOUD_CPU_CORES = 3     # クラウドインスタンスのコア割当て数
EDGE_CPU_CORES  = 4     # エッジのコア割当て数
GW_CPU_CORES  = 4       # ゲートウェイのコア割当て数

MY_CPU_BENCHMARK    = 35743 / 4   # 実験マシンCPUのベンチマーク(1コア相当)
CLOUD_CPU_BENCHMARK = 62262 / 12  # クラウドCPUのベンチマーク(1コア相当)
EDGE_CPU_BENCHMARK  = 5676 /  4   # エッジCPUのベンチマーク(1コア相当)
GW_CPU_BENCHMARK    = 12249 / 4   # ゲートウェイCPUのベンチマーク(1コア相当)

MY_CPU_BENCHMARK_MULTI = MY_CPU_BENCHMARK * MY_CPU_CORES          # 実験マシンCPUのベンチマーク(マルチスレッド)
CLOUD_CPU_BENCHMARK_MULTI = CLOUD_CPU_BENCHMARK * CLOUD_CPU_CORES # クラウドCPUのベンチマーク(マルチスレッド)
EDGE_CPU_BENCHMARK_MULTI = EDGE_CPU_BENCHMARK * EDGE_CPU_CORES    # エッジCPUのベンチマーク(マルチスレッド)
GW_CPU_BENCHMARK_MULTI = GW_CPU_BENCHMARK * GW_CPU_CORES    # エッジCPUのベンチマーク(マルチスレッド)

CLOUD_EDGE_BPS = 12500000   # 100Mbps -> 12.5MB/sec
CLOUD_GW_BPS = 12500000   # 100Mbps -> 12.5MB/sec
GW_EDGE_BPS = 12500000   # 100Mbps -> 12.5MB/sec

##### 処理時間パラメータ #####

# 処理時間の分散に与える共通の乗数
TASK_SIGMA_GAIN = 0.2  # 20%

# 画像データ取得
TASK_AVG_1 = 1.089
TASK_VAR_1 = TASK_AVG_1 * TASK_SIGMA_GAIN
# 画像オープン・前処理
TASK_AVG_2 = 0.0742
TASK_VAR_2 = TASK_AVG_2 * TASK_SIGMA_GAIN
# 画像保存
TASK_AVG_3 = 0.00952
TASK_VAR_3 = TASK_AVG_3 * TASK_SIGMA_GAIN
# ファイル画像ロード
TASK_AVG_4 = 0.000794
TASK_VAR_4 = TASK_AVG_4 * TASK_SIGMA_GAIN
# 画像デコード
TASK_AVG_5 = 0.00986
TASK_VAR_5 = TASK_AVG_5 * TASK_SIGMA_GAIN
# データ型変換
TASK_AVG_6 = 0.000585
TASK_VAR_6 = TASK_AVG_6 * TASK_SIGMA_GAIN
# 推論
TASK_AVG_7 = 1.738
TASK_VAR_7 = TASK_AVG_7 * TASK_SIGMA_GAIN
# 矩形表示
TASK_AVG_8 = 0.0681
TASK_VAR_8 = TASK_AVG_8 * TASK_SIGMA_GAIN
# 画面表示
TASK_AVG_9 = 0.106
TASK_VAR_9 = TASK_AVG_9 * TASK_SIGMA_GAIN

##### 通信量パラメータ #####

# 画像データ取得ー画像・オープン前処理
COMM_AVG_1_2 = 779270
COMM_VAR_1_2 = COMM_AVG_1_2 * 0.05
# 画像・オープン前処理ー画像保存
COMM_AVG_2_3 = 3324785
COMM_VAR_2_3 = COMM_AVG_2_3 * 0.05
# 画像保存－ファイル画像ロード
COMM_AVG_3_4 = 424661
COMM_VAR_3_4 = COMM_AVG_3_4 * 0.05
# ファイル画像ロードー画像デコード
COMM_AVG_4_5 = 424763
COMM_VAR_4_5 = COMM_AVG_4_5 * 0.05
# 画像デコードーデータ型変換
COMM_AVG_5_6 = 3287294
COMM_VAR_5_6 = COMM_AVG_5_6 * 0.05
# データ型変換ー推論
COMM_AVG_6_7 = 3287297
COMM_VAR_6_7 = COMM_AVG_6_7 * 0.05
# 推論ー矩形表示
COMM_AVG_7_8 = 232305
COMM_VAR_7_8 = COMM_AVG_7_8 * 0.3 # 検知数によって大きく変わる
# 矩形表示ー画面表示
COMM_AVG_8_9 = 3287235
COMM_VAR_8_9 = COMM_AVG_8_9 * 0.05

##### 通信時間パラメータ #####

# 通信時間の分散に与える共通の乗数
LT_SIGMA_GAIN = 0.3  # 30%
