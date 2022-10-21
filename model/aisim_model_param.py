##### スペックパラメータ #####
MY_CPU_CLOCK    = 3.00  # 実験マシン
CLOUD_CPU_CLOCK = 2.50  # クラウドインスタンス(Xeon Platinum 8175M)
EDGE_CPU_CLOCK  = 0.12  # エッジ(Renesus RX671)

CLOUD_EDGE_BPS = 12500000   # 100Mbps -> 12.5MB/sec

##### 処理時間パラメータ #####

# 処理時間の分散に与える共通の乗数
TASK_SIGMA_GAIN = 0.2  # 20%

# 画像データ取得
TASK_AVG_1 = 0.8765
TASK_VAR_1 = TASK_AVG_1 * TASK_SIGMA_GAIN
# 画像オープン・前処理
TASK_AVG_2 = 0.0580
TASK_VAR_2 = TASK_AVG_2 * TASK_SIGMA_GAIN
# 画像保存
TASK_AVG_3 = 0.0608
TASK_VAR_3 = TASK_AVG_3 * TASK_SIGMA_GAIN
# 画像表示
TASK_AVG_4 = 0.0262
TASK_VAR_4 = TASK_AVG_4 * TASK_SIGMA_GAIN
# ファイル画像ロード
TASK_AVG_5 = 0.00562
TASK_VAR_5 = TASK_AVG_5 * TASK_SIGMA_GAIN
# 画像デコード
TASK_AVG_6 = 0.0189
TASK_VAR_6 = TASK_AVG_6 * TASK_SIGMA_GAIN
# データ型変換
TASK_AVG_7 = 0.0114
TASK_VAR_7 = TASK_AVG_7 * TASK_SIGMA_GAIN
# 推論
TASK_AVG_8 = 6.59
TASK_VAR_8 = TASK_AVG_8 * TASK_SIGMA_GAIN
# 矩形表示
TASK_AVG_9 = 0.0529
TASK_VAR_9 = TASK_AVG_9 * TASK_SIGMA_GAIN

##### 通信量パラメータ #####

# 画像データ取得ー画像・オープン前処理
COMM_AVG_1_2 = 779298
COMM_VAR_1_2 = COMM_AVG_1_2 * 0.05
# 画像・オープン前処理ー画像保存
COMM_AVG_2_3 = 32
COMM_VAR_2_3 = 0 # 固定
# 画像保存－画像表示
COMM_AVG_3_4 = 3287176
COMM_VAR_3_4 = COMM_AVG_3_4 * 0.05
# 画像表示ーファイル画像ロード
COMM_AVG_4_5 = 152
COMM_VAR_4_5 = 0 # 固定
# ファイル画像ロードー画像デコード
COMM_AVG_5_6 = 152
COMM_VAR_5_6 = 0 # 固定
# 画像デコードーデータ型変換
COMM_AVG_6_7 = 152
COMM_VAR_6_7 = 0 # 固定
# データ型変換ー推論
COMM_AVG_7_8 = 216
COMM_VAR_7_8 = COMM_AVG_7_8 * 0.3 # 検知数によって大きく変わる
# 推論ー矩形表示
COMM_AVG_8_9 = 3287176
COMM_VAR_8_9 = COMM_AVG_8_9 * 0.05

##### 通信時間パラメータ #####

# 通信時間の分散に与える共通の乗数
LT_SIGMA_GAIN = 0.3  # 30%
