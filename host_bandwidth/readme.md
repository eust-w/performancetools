####　云主机内部运行

```shell
fio --ioengine=libaio --direct=1 --size=50G --iodepth=64 --runtime=360 --time_based --group_reporting --name=1m-write --bs=1m --rw=write --filename=/dev/vdb --write_iops_log=1m-write.results  --log_avg_msec=100 --write_bw_log=1m-write.results --write_lat_log=1m-write.results # fio磁盘测试
```

```shell
rename 1.log log * #更改名称
```

```shell
fio_generate_plots 1m-write # 生成svg图像
```

#### 物理机运行

```shell
host_bandwidth.py #临时写的脚本 自己实际使用可以修改一下cli命令以及原始数据输出|py2.7.5
```

```shell
process.py #临时写的脚本处理原始数据生成图像 自己实际使用可以修改 |py2.7.5
```

