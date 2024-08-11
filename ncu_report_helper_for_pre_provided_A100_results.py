#########################################################################################################################
###                                                                                                                   ###
###                                                Workload Analysis                                                  ###
###                                                                                                                   ###
#########################################################################################################################
verbose = 0

# User Defined Path Prefix: Using Pre-Provided A100 Results
Results_Path_Prefix = "/home/micro57/Pre-Provided-Results/Pre-Provided-A100-Results/"

# Since PPT-GPU and Accel-Sim do not have configurations for Amphere A100 GPUs, 
# we do not provide their simulation results here.

ncu_report_file_paths = [ \
        [Results_Path_Prefix + "./NsightCollection/b+tree.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/b+tree", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/b+tree", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/b+tree/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/backprop.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/backprop", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/backprop", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/backprop/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/bfs.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/bfs", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/bfs", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/bfs/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/cfd.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/cfd", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/cfd", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/cfd/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/dwt2d.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/dwt2d", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/dwt2d", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/dwt2d/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gaussian.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/gaussian", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/gaussian", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/gaussian/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/hotspot.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/hotspot", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/hotspot", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/hotspot/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/hotspot3D.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/hotspot3D", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/hotspot3D", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/hotspot3D/outputs"], \
        # [Results_Path_Prefix + "./NsightCollection/huffman.ncu-rep", \
        #     Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/huffman", \
        #         Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/huffman", \
        #             Results_Path_Prefix + "./HyFiSS-Results/Rodinia/huffman/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/lavaMD.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/lavaMD", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/lavaMD", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/lavaMD/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/lud.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/lud", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/lud", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/lud/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/nn.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/nn", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/nn", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/nn/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/nw.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/nw", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/nw", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/nw/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/pathfinder.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Rodinia/pathfinder", \
                Results_Path_Prefix + "./Accel-Sim-Results/Rodinia/pathfinder", \
                    Results_Path_Prefix + "./HyFiSS-Results/Rodinia/pathfinder/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/2DConvolution.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/2DCONV", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/2DCONV", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/2DCONV/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/3DConvolution.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/3DCONV", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/3DCONV", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/3DCONV/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/3mm.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/3MM", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/3MM", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/3MM/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/atax.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/ATAX", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/ATAX", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/ATAX/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/bicg.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/BICG", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/BICG", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/BICG/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gemm.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/GEMM", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/GEMM", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/GEMM/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gesummv.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/GESUMMV", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/GESUMMV", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/GESUMMV/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gramschmidt.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/GRAMSCHM", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/GRAMSCHM", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/GRAMSCHM/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/mvt.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PolyBench/MVT", \
                Results_Path_Prefix + "./Accel-Sim-Results/PolyBench/MVT", \
                    Results_Path_Prefix + "./HyFiSS-Results/PolyBench/MVT/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/cublas_GemmEx_HF_CC_example_2048x2048x2048.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/cublas_GemmEx_HF_CC/2048x2048x2048", \
                Results_Path_Prefix + "./Accel-Sim-Results/cublas_GemmEx_HF_CC/2048x2048x2048", \
                    Results_Path_Prefix + "./HyFiSS-Results/cublas_GemmEx_HF_CC/2048x2048x2048/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/AN_32.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Tango/AlexNet", \
                Results_Path_Prefix + "./Accel-Sim-Results/Tango/AlexNet", \
                    Results_Path_Prefix + "./HyFiSS-Results/Tango/AlexNet/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/GRU.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Tango/GRU", \
                Results_Path_Prefix + "./Accel-Sim-Results/Tango/GRU", \
                    Results_Path_Prefix + "./HyFiSS-Results/Tango/GRU/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/LSTM_32.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Tango/LSTM", \
                Results_Path_Prefix + "./Accel-Sim-Results/Tango/LSTM", \
                    Results_Path_Prefix + "./HyFiSS-Results/Tango/LSTM/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/SN_32.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/Tango/SqueezeNet", \
                Results_Path_Prefix + "./Accel-Sim-Results/Tango/SqueezeNet", \
                    Results_Path_Prefix + "./HyFiSS-Results/Tango/SqueezeNet/outputs"], \
        # [Results_Path_Prefix + "./NsightCollection/conv_bench_inference_halfx700x161x1x1x32x20x5x0x0x2x2.ncu-rep", \
        #     Results_Path_Prefix + "./PPT-GPU-Results/DeepBench/conv_bench_inference_halfx700x161x1x1x32x20x5x0x0x2x2", \
        #         Results_Path_Prefix + "./Accel-Sim-Results/DeepBench/conv_bench_inference_halfx700x161x1x1x32x20x5x0x0x2x2", \
        #             Results_Path_Prefix + "./HyFiSS-Results/DeepBench/conv_bench_inference_halfx700x161x1x1x32x20x5x0x0x2x2/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gemm_bench_inference_halfx1760x7000x1760x0x0.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/DeepBench/gemm_bench_inference_halfx1760x7000x1760x0x0", \
                Results_Path_Prefix + "./Accel-Sim-Results/DeepBench/gemm_bench_inference_halfx1760x7000x1760x0x0", \
                    Results_Path_Prefix + "./HyFiSS-Results/DeepBench/gemm_bench_inference_halfx1760x7000x1760x0x0/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/gemm_bench_train_halfx1760x7000x1760x0x0.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/DeepBench/gemm_bench_train_halfx1760x7000x1760x0x0", \
                Results_Path_Prefix + "./Accel-Sim-Results/DeepBench/gemm_bench_train_halfx1760x7000x1760x0x0", \
                    Results_Path_Prefix + "./HyFiSS-Results/DeepBench/gemm_bench_train_halfx1760x7000x1760x0x0/outputs"], \
        # [Results_Path_Prefix + "./NsightCollection/rnn_bench_inference_halfx1024x1x25xlstm.ncu-rep", \
        #     Results_Path_Prefix + "./PPT-GPU-Results/DeepBench/rnn_bench_inference_halfx1024x1x25xlstm", \
        #         Results_Path_Prefix + "./Accel-Sim-Results/DeepBench/rnn_bench_inference_halfx1024x1x25xlstm", \
        #             Results_Path_Prefix + "./HyFiSS-Results/DeepBench/rnn_bench_inference_halfx1024x1x25xlstm/outputs"], \
        # [Results_Path_Prefix + "./NsightCollection/rnn_bench_train_halfx1024x1x25xlstm.ncu-rep", \
        #     Results_Path_Prefix + "./PPT-GPU-Results/DeepBench/rnn_bench_train_halfx1024x1x25xlstm", \
        #         Results_Path_Prefix + "./Accel-Sim-Results/DeepBench/rnn_bench_train_halfx1024x1x25xlstm", \
        #             Results_Path_Prefix + "./HyFiSS-Results/DeepBench/rnn_bench_train_halfx1024x1x25xlstm/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/lulesh.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/LULESH/cuda", \
                Results_Path_Prefix + "./Accel-Sim-Results/LULESH/cuda", \
                    Results_Path_Prefix + "./HyFiSS-Results/LULESH/cuda/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/pennant.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/PENNANT", \
                Results_Path_Prefix + "./Accel-Sim-Results/PENNANT", \
                    Results_Path_Prefix + "./HyFiSS-Results/PENNANT/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/color_max.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/color_max", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/color_max", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/color_max/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/color_maxmin.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/color_maxmin", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/color_maxmin", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/color_maxmin/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/fw.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/fw", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/fw", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/fw/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/mis.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/mis", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/mis", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/mis/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/pagerank.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/pagerank", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/pagerank", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/pagerank/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/pagerank_spmv.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/pagerank_spmv", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/pagerank_spmv", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/pagerank_spmv/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/sssp.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/sssp", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/sssp", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/sssp/outputs"], \
        [Results_Path_Prefix + "./NsightCollection/sssp_ell.ncu-rep", \
            Results_Path_Prefix + "./PPT-GPU-Results/pannotia/sssp_ell", \
                Results_Path_Prefix + "./Accel-Sim-Results/pannotia/sssp_ell", \
                    Results_Path_Prefix + "./HyFiSS-Results/pannotia/sssp_ell/outputs"], \
    ]

#########################################################################################################################
###                                                                                                                   ###
###                                                Read NCU-REP Helper                                                ###
###                                                                                                                   ###
#########################################################################################################################

def get_dram__bytes_sum_per_second(kernel):
    """ Get Memory Throughput.
        # of bytes accessed in DRAM (This counter metric represents the sum of the number of operations per second across 
        all sub-unit instances)
        
        dram: Device (main) memory, where the GPUs global and local memory resides.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['dram__bytes.sum.per_second'].value()
    """
    global verbose
    if verbose:
        print("Memory Throughput [Gbyte/second]: ", kernel['dram__bytes.sum.per_second'].value())
    return kernel['dram__bytes.sum.per_second'].value()

def get_gpu__compute_memory_access_throughput_avg_pct_of_peak_sustained_elapsed(kernel):
    """ Get Mem Busy.
        Compute Memory Pipeline : throughput of internal activity within caches and DRAM (This throughput metric represe-
        nts the percent of the peak sustained rate achieved during elapsed cycles across all sub-unit instances)

        gpu: The entire Graphics Processing Unit.

        DRAM: Device (main) memory, where the GPUs global and local memory resides.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['gpu__compute_memory_access_throughput.avg.pct_of_peak_sustained_elapsed'].value()
    """
    global verbose
    if verbose:
        print("Mem Busy [%]: ", 
              kernel['gpu__compute_memory_access_throughput.avg.pct_of_peak_sustained_elapsed'].value())
    return kernel['gpu__compute_memory_access_throughput.avg.pct_of_peak_sustained_elapsed'].value()

def get_l1tex__t_sector_hit_rate_pct(kernel):
    """ Get L1/TEX Hit Rate. 
        # of sector hits per sector (This ratio metric represents the value expressed as a percentage across all sub-unit 
        instances)
       
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC.
        It can be used as directed-mapped shared memory and/or store global, local and texture data in its cache portion.
        l1tex__t refers to its Tag stage. l1tex__m refers to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory.
        An L1 or L2 cache line is four sectors, i.e. 128 bytes.
        Sector accesses are classified as hits if the tag is present and the sector-data is present within the cache line.
        Tag-misses and tag-hit-data-misses are all classified as misses.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_sector_hit_rate.pct'].value()
    """
    global verbose
    if verbose:
        print("L1/TEX Hit Rate [%]: ", kernel['l1tex__t_sector_hit_rate.pct'].value())
    return kernel['l1tex__t_sector_hit_rate.pct'].value()

def get_L1_Total_Requests(kernel):
    """ Get lts__t_requests_srcunit_tex.sum.
        l1tex__t_requests_pipe_lsu_mem_local_op_ld.sum
        + l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum
        + l1tex__t_requests_pipe_tex_mem_surface_op_ld.sum
        + l1tex__t_requests_pipe_tex_mem_texture.sum
        + l1tex__t_requests_pipe_lsu_mem_global_op_st.sum
        + l1tex__t_requests_pipe_lsu_mem_local_op_st.sum
        + l1tex__t_requests_pipe_tex_mem_surface_op_st.sum
        + l1tex__t_requests_pipe_lsu_mem_global_op_red.sum
        + l1tex__t_requests_pipe_tex_mem_surface_op_red.sum
        + l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum
        + l1tex__t_requests_pipe_tex_mem_surface_op_atom.sum
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC.
        It can be used as directed-mapped shared memory and/or store global, local and texture data in its cache portion.
        l1tex__t refers to its Tag stage. l1tex__m refers to its Miss stage. l1tex__d refers to its Data stage.

        requests: A command into a HW unit to perform some action, e.g. load data from some memory location.
        Each request accesses one or more sectors.

        lsu: Load Store Unit.
        The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for global, local, and shared memory.
        It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait barrier instructions to the L1TEX unit.

        local: Local memory is private storage for an executing thread and is not visible outside of that thread.
        It is intended for thread-local data like thread stacks and register spills.
        Local memory has the same latency as global memory.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned system memory, or peer memory.
        Global memory is visible to all threads in the GPU.
        Global memory is accessed through the SM L1 and GPU L2.

        tex: Texture Unit.
        The SM texture pipeline forwards texture and surface instructions to the L1TEX unit's TEXIN stage.
        On GPUs where FP64 or Tensor pipelines are decoupled, the texture pipeline forwards those types of instructions, too.

        surface: Surface memory

        texture: Texture memory

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['lts__t_requests_srcunit_tex.sum'].value()
    """
    global verbose
    
    value = \
        kernel['l1tex__t_requests_pipe_lsu_mem_local_op_ld.sum'].value() + \
        kernel['l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum'].value() + \
        kernel['l1tex__t_requests_pipe_tex_mem_surface_op_ld.sum'].value() + \
        kernel['l1tex__t_requests_pipe_tex_mem_texture.sum'].value() + \
        kernel['l1tex__t_requests_pipe_lsu_mem_global_op_st.sum'].value() + \
        kernel['l1tex__t_requests_pipe_lsu_mem_local_op_st.sum'].value() + \
        kernel['l1tex__t_requests_pipe_tex_mem_surface_op_st.sum'].value() + \
        kernel['l1tex__t_requests_pipe_lsu_mem_global_op_red.sum'].value() + \
        kernel['l1tex__t_requests_pipe_tex_mem_surface_op_red.sum'].value() + \
        kernel['l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum'].value() + \
        kernel['l1tex__t_requests_pipe_tex_mem_surface_op_atom.sum'].value()
    
    if verbose:
        print("L1 Total Requests: ", value)
    
    return value

def get_gpu__compute_memory_request_throughput_avg_pct_of_peak_sustained_elapsed(kernel):
    """ Get Max Bandwidth.
        Compute Memory Pipeline : throughput of interconnects between SM<->Caches<->DRAM (This throughput metric represents 
        the percent of the peak sustained rate achieved during elapsed cycles across all sub-unit instances)
        
        gpu: The entire Graphics Processing Unit. 
        request: A command into a HW unit to perform some action, e.g. load data from some memory location. Each request acc-
        esses one or more sectors.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['gpu__compute_memory_request_throughput.avg.pct_of_peak_sustained_elapsed'].value()
    """
    global verbose
    if verbose:
        print("Max Bandwidth [%]: ", 
              kernel['gpu__compute_memory_request_throughput.avg.pct_of_peak_sustained_elapsed'].value())
    return kernel['gpu__compute_memory_request_throughput.avg.pct_of_peak_sustained_elapsed'].value()

def get_lts__t_sector_hit_rate_pct(kernel):
    """ Get L2 Hit Rate. 
        proportion of L2 sector lookups that hit (This ratio metric represents the value expressed as a percentage across 
        all sub-unit instances)
       
        lts: A Level 2 (L2) Cache Slice is a sub-partition of the Level 2 cache.
        lts__t refers to its Tag stage. lts__m refers to its Miss stage. lts__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory.
        An L1 or L2 cache line is four sectors, i.e. 128 bytes.
        Sector accesses are classified as hits if the tag is present and the sector-data is present within the cache line.
        Tag-misses and tag-hit-data-misses are all classified as misses.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['lts__t_sector_hit_rate.pct'].value()
    """
    global verbose
    if verbose:
        print("L2 Hit Rate [%]: ", kernel['lts__t_sector_hit_rate.pct'].value())
    return kernel['lts__t_sector_hit_rate.pct'].value()

def get_lts__t_requests_srcunit_tex_sum(kernel):
    """ Get lts__t_requests_srcunit_tex.sum.
        # of LTS requests from unit TEX (This counter metric represents the sum across all sub-unit instances)
        
        lts: A Level 2 (L2) Cache Slice is a sub-partition of the Level 2 cache.
        lts__t refers to its Tag stage. lts__m refers to its Miss stage. lts__d refers to its Data stage.

        requests: A command into a HW unit to perform some action, e.g. load data from some memory location.
        Each request accesses one or more sectors.

        tex: Texture Unit.
        The SM texture pipeline forwards texture and surface instructions to the L1TEX unit's TEXIN stage.
        On GPUs where FP64 or Tensor pipelines are decoupled, the texture pipeline forwards those types of instructions, too.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['lts__t_requests_srcunit_tex.sum'].value()
    """
    global verbose
    if verbose:
        print("L2 Total Requests: ", kernel['lts__t_requests_srcunit_tex.sum'].value())
    return kernel['lts__t_requests_srcunit_tex.sum'].value()

def get_sm__memory_throughput_avg_pct_of_peak_sustained_elapsed(kernel):
    """ Get Mem Pipes Busy. 
        SM memory instruction throughput assuming ideal load balancing across SMSPs (This throughput metric represents the 
        percent of the peak sustained rate achieved during elapsed cycles across all sub-unit instances)
        
        sm: The Streaming Multiprocessor handles execution of a kernel as groups of 32 threads, called warps. Warps are fu-
        rther grouped into cooperative thread arrays (CTA), called blocks in CUDA. All warps of a CTA execute on the same 
        SM. CTAs share various resources across their threads, e.g. the shared memory.

        instruction: An assembly (SASS) instruction. Each executed instruction may generate zero or more requests.

        SMSPs: Each SM is partitioned into four processing blocks, called SM sub partitions. The SM sub partitions are the 
        primary processing elements on the SM. A sub partition manages a fixed size pool of warps.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__memory_throughput.avg.pct_of_peak_sustained_elapsed'].value()
    """
    global verbose
    if verbose:
        print("Mem Pipes Busy [%]: ", kernel['sm__memory_throughput.avg.pct_of_peak_sustained_elapsed'].value())
    return kernel['sm__memory_throughput.avg.pct_of_peak_sustained_elapsed'].value()

def get_l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate_pct(kernel):
    """ Get l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate.pct. 
        # of sector hits for global loads per sector for global loads (This ratio metric represents the value expressed as 
        a percentage across all sub-unit instances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through 
        the SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate.pct'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate.pct [%]: ", 
              kernel['l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate.pct'].value())
    return kernel['l1tex__t_sector_pipe_lsu_mem_global_op_ld_hit_rate.pct'].value()

def get_l1tex__t_requests_pipe_lsu_mem_global_op_ld_sum(kernel):
    """ Get l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum. 
        # of requests sent to T-Stage for global loads (This counter metric represents the sum across all sub-unit instan-
        ces)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through 
        the SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum [request]: ", 
              kernel['l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum'].value())
    return kernel['l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum'].value()

def get_l1tex__t_requests_pipe_lsu_mem_global_op_st_sum(kernel):
    """ Get l1tex__t_requests_pipe_lsu_mem_global_op_st.sum. 
        # of requests sent to T-Stage for global stores (This counter metric represents the sum across all sub-unit instan-
        ces)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through 
        the SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_requests_pipe_lsu_mem_global_op_st.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_requests_pipe_lsu_mem_global_op_st.sum [request]: ", 
              kernel['l1tex__t_requests_pipe_lsu_mem_global_op_st.sum'].value())
    return kernel['l1tex__t_requests_pipe_lsu_mem_global_op_st.sum'].value()

def get_l1tex__t_sectors_pipe_lsu_mem_global_op_ld_sum(kernel):
    """ Get l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum. 
        # of sectors requested for global loads (This counter metric represents the sum across all sub-unit instances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through 
        the SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum [sector]: ", 
              kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum'].value())
    return kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum'].value()

def get_l1tex__t_sectors_pipe_lsu_mem_global_op_st_sum(kernel):
    """ Get l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum. 
        # of sectors requested for global stores (This counter metric represents the sum across all sub-unit instances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through 
        the SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum [sector]: ", 
              kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum'].value())
    return kernel['l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum'].value()

def get_l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld_sum(kernel):
    """ Get l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld.sum. 
        # of sectors read from L2 into L1TEX M-Stage for local/global loads (This counter metric represents the sum across 
        all sub-unit instances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lg: Local/Global memory.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld.sum [sector]: ", 
              kernel['l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld.sum'].value())
    return kernel['l1tex__m_xbar2l1tex_read_sectors_mem_lg_op_ld.sum'].value()


def get_l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st_sum(kernel):
    """ Get l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st.sum. 
        # of sectors written to L2 for local/global stores (This counter metric represents the sum across all sub-unit ins-
        tances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory a-
        nd/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refers 
        to its Miss stage. l1tex__d refers to its Data stage.

        sector: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

        lg: Local/Global memory.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st.sum [sector]: ", 
              kernel['l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st.sum'].value())
    return kernel['l1tex__m_l1tex2xbar_write_sectors_mem_lg_op_st.sum'].value()

def get_dram__sectors_read_sum(kernel):
    """ Get dram__sectors_read.sum. 
        # of sectors read from DRAM (This counter metric represents the sum across all sub-unit instances)
        
        dram: Device (main) memory, where the GPUs global and local memory resides.

        sectors: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['dram__sectors_read.sum'].value()
    """
    global verbose
    if verbose:
        print("dram__sectors_read.sum [sector]: ", kernel['dram__sectors_read.sum'].value())
    return kernel['dram__sectors_read.sum'].value()

def get_dram__sectors_write_sum(kernel):
    """ Get dram__sectors_write.sum. 
        # of sectors read from DRAM (This counter metric represents the sum across all sub-unit instances)
        
        dram: Device (main) memory, where the GPUs global and local memory resides.

        sectors: Aligned 32 byte-chunk of memory in a cache line or device memory. An L1 or L2 cache line is four sectors, 
        i.e. 128 bytes. Sector accesses are classified as hits if the tag is present and the sector-data is present within 
        the cache line. Tag-misses and tag-hit-data-misses are all classified as misses.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['dram__sectors_write.sum'].value()
    """
    global verbose
    if verbose:
        print("dram__sectors_write.sum [sector]: ", kernel['dram__sectors_write.sum'].value())
    return kernel['dram__sectors_write.sum'].value()

def get_l1tex__t_requests_pipe_lsu_mem_global_op_atom_sum(kernel):
    """ Get l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum. 
        # of requests sent to T-Stage for global atomics (This counter metric represents the sum across all sub-unit inst-
        ances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory 
        and/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refe-
        rs to its Miss stage. l1tex__d refers to its Data stage.

        requests: A command into a HW unit to perform some action, e.g. load data from some memory location. Each request 
        accesses one or more sectors.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through the 
        SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum [request]: ", 
              kernel['l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum'].value())
    return kernel['l1tex__t_requests_pipe_lsu_mem_global_op_atom.sum'].value()

def get_l1tex__t_requests_pipe_lsu_mem_global_op_red_sum(kernel):
    """ Get l1tex__t_requests_pipe_lsu_mem_global_op_red.sum. 
        # of requests sent to T-Stage for global reductions (This counter metric represents the sum across all sub-unit in-
        stances)
        
        l1tex: The Level 1 (L1)/Texture Cache is located within the GPC. It can be used as directed-mapped shared memory 
        and/or store global, local and texture data in its cache portion. l1tex__t refers to its Tag stage. l1tex__m refe-
        rs to its Miss stage. l1tex__d refers to its Data stage.

        requests: A command into a HW unit to perform some action, e.g. load data from some memory location. Each request 
        accesses one or more sectors.

        lsu: Load Store Unit. The LSU pipeline issues load, store, atomic, and reduction instructions to the L1TEX unit for 
        global, local, and shared memory. It also issues special register reads (S2R), shuffles, and CTA-level arrive/wait 
        barrier instructions to the L1TEX unit.

        global: Global memory is a 49-bit virtual address space that is mapped to physical memory on the device, pinned sys-
        tem memory, or peer memory. Global memory is visible to all threads in the GPU. Global memory is accessed through the 
        SM L1 and GPU L2.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['l1tex__t_requests_pipe_lsu_mem_global_op_red.sum'].value()
    """
    global verbose
    if verbose:
        print("l1tex__t_requests_pipe_lsu_mem_global_op_red.sum [request]: ", 
              kernel['l1tex__t_requests_pipe_lsu_mem_global_op_red.sum'].value())
    return kernel['l1tex__t_requests_pipe_lsu_mem_global_op_red.sum'].value()

#########################################################################################################################
###                                                                                                                   ###
###                                           Compute Workload Analysis                                               ###
###                                                                                                                   ###
#########################################################################################################################

def get_gpu__time_duration_sum(kernel):
    """ Get Duration.
        equals to gpu__time_duration_measured_user if collectable, otherwise equals to gpu__time_duration_measured_wallclo-
        ck (This counter metric represents the sum across all sub-unit instances)

        gpu: The entire Graphics Processing Unit.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['gpu__time_duration.sum'].value()
    """
    global verbose
    if verbose:
        print("Duration [nsecond]: ", kernel['gpu__time_duration.sum'].value())
    return kernel['gpu__time_duration.sum'].value()


def get_gpc__cycles_elapsed_max(kernel):
    """ Get Elapsed Cycles.
        # of cycles elapsed on GPC (This counter metric represents the max across all sub-unit instances)

        gpc: The General Processing Cluster contains SM, Texture and L1 in the form of TPC(s). It is replicated several 
        times across a chip.
        
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['gpc__cycles_elapsed.max'].value()
    """
    global verbose
    if verbose:
        print("Elapsed Cycles [cycle]: ", kernel['gpc__cycles_elapsed.max'].value())
    return kernel['gpc__cycles_elapsed.max'].value()


def get_sm__cycles_active_avg(kernel):
    """ Get SM Active Cycles.
        # of cycles with at least one warp in flight (This counter metric represents the avg across all sub-unit instan-
        ces)
        
        sm: The Streaming Multiprocessor handles execution of a kernel as groups of 32 threads, called warps. Warps are 
        further grouped into cooperative thread arrays (CTA), called blocks in CUDA. All warps of a CTA execute on the 
        same SM. CTAs share various resources across their threads, e.g. the shared memory.

        warp: A a group of 32 threads within a CTA. A warp is allocated to a sub partition and resides on the sub parti-
        tion from launch to completion.
        
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__cycles_active.avg'].value()
    """
    global verbose
    if verbose:
        print("SM Active Cycles [cycle]: ", kernel['sm__cycles_active.avg'].value())
    return kernel['sm__cycles_active.avg'].value()

def get_gpc__cycles_elapsed_avg_per_second(kernel):
    """ Get SM Frequency.
        # of cycles elapsed on GPC (This counter metric represents the avg of the number of operations per second across 
        all sub-unit instances)
        
        gpc: The General Processing Cluster contains SM, Texture and L1 in the form of TPC(s). It is replicated several 
        times across a chip.
        
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['gpc__cycles_elapsed.avg.per_second'].value()
    """
    global verbose
    if verbose:
        print("SM Frequency [cycle/second]: ", kernel['gpc__cycles_elapsed.avg.per_second'].value())
    return kernel['gpc__cycles_elapsed.avg.per_second'].value()


def get_dram__cycles_elapsed_avg_per_second(kernel):
    """ Get DRAM Frequency.
        # of elapsed DRAM memory clock cycles (This counter metric represents the avg of the number of operations per se-
        cond across all sub-unit instances)
        
        dram: Device (main) memory, where the GPUs global and local memory resides.
        
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['dram__cycles_elapsed.avg.per_second'].value()
    """
    global verbose
    if verbose:
        print("DRAM Frequency [cycle/second]: ", kernel['dram__cycles_elapsed.avg.per_second'].value())
    return kernel['dram__cycles_elapsed.avg.per_second'].value()


def get_sm__inst_executed_avg_per_cycle_elapsed(kernel):
    """ Get Executed Ipc Elapsed.
        # of warp instructions executed (This counter metric represents the avg of the number of operations per elapsed cy-
        cle across all sub-unit instances)
        
        sm: The Streaming Multiprocessor handles execution of a kernel as groups of 32 threads, called warps. Warps are fur-
        ther grouped into cooperative thread arrays (CTA), called blocks in CUDA. All warps of a CTA execute on the same SM.
        CTAs share various resources across their threads, e.g. the shared memory.

        warp: A a group of 32 threads within a CTA. A warp is allocated to a sub partition and resides on the sub partition 
        from launch to completion.

        instructions: An assembly (SASS) instruction. Each executed instruction may generate zero or more requests.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__inst_executed.avg.per_cycle_elapsed'].value()
    """
    global verbose
    if verbose:
        print("Executed Ipc Elapsed [inst/cycle]: ", kernel['sm__inst_executed.avg.per_cycle_elapsed'].value())
    return kernel['sm__inst_executed.avg.per_cycle_elapsed'].value()

#########################################################################################################################
###                                                                                                                   ###
###                                                    Occupancy                                                      ###
###                                                                                                                   ###
#########################################################################################################################


def get_launch__occupancy_limit_blocks(kernel):
    """ Get Block Limit SM.
        Occupancy limit due to maximum number of blocks managable per SM.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['launch__occupancy_limit_blocks'].value()
    """
    global verbose
    if verbose:
        print("Block Limit SM [block]: ", kernel['launch__occupancy_limit_blocks'].value())
    return kernel['launch__occupancy_limit_blocks'].value()

def get_launch__occupancy_limit_registers(kernel):
    """ Get Block Limit Registers.
        Occupancy limit due to register usage.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['launch__occupancy_limit_registers'].value()
    """
    global verbose
    if verbose:
        print("Block Limit Registers [block]: ", kernel['launch__occupancy_limit_registers'].value())
    return kernel['launch__occupancy_limit_registers'].value()

def get_launch__occupancy_limit_shared_mem(kernel):
    """ Get Block Limit Shared Mem.
        Occupancy limit due to shared memory usage.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['launch__occupancy_limit_shared_mem'].value()
    """
    global verbose
    if verbose:
        print("Block Limit Shared Mem [block]: ", kernel['launch__occupancy_limit_shared_mem'].value())
    return kernel['launch__occupancy_limit_shared_mem'].value()

def get_launch__occupancy_limit_warps(kernel):
    """ Get Block Limit Warps.
        Occupancy limit due to block size.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['launch__occupancy_limit_warps'].value()
    """
    global verbose
    if verbose:
        print("Block Limit Warps [block]: ", kernel['launch__occupancy_limit_warps'].value())
    return kernel['launch__occupancy_limit_warps'].value()

def get_sm__maximum_warps_avg_per_active_cycle(kernel):
    """ Get Theoretical Active Warps per SM.
        
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__maximum_warps_avg_per_active_cycle'].value()
    """
    global verbose
    if verbose:
        print("Theoretical Active Warps per SM [warp]: ", kernel['sm__maximum_warps_avg_per_active_cycle'].value())
    return kernel['sm__maximum_warps_avg_per_active_cycle'].value()

def get_sm__maximum_warps_per_active_cycle_pct(kernel):
    """ Get Theoretical Occupancy.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__maximum_warps_per_active_cycle_pct'].value()
    """
    global verbose
    if verbose:
        print("Theoretical Occupancy [%]: ", kernel['sm__maximum_warps_per_active_cycle_pct'].value())
    return kernel['sm__maximum_warps_per_active_cycle_pct'].value()

def get_sm__warps_active_avg_per_cycle_active(kernel):
    """ Get Achieved Active Warps Per SM.
        cumulative # of warps in flight (This counter metric represents the avg of the number of operations per unit act-
        ive cycle across all sub-unit instances)
        
        sm: The Streaming Multiprocessor handles execution of a kernel as groups of 32 threads, called warps. Warps are 
        further grouped into cooperative thread arrays (CTA), called blocks in CUDA. All warps of a CTA execute on the sa-
        me SM. CTAs share various resources across their threads, e.g. the shared memory.

        warps: A a group of 32 threads within a CTA. A warp is allocated to a sub partition and resides on the sub parti-
        tion from launch to completion.
    
    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__warps_active.avg.per_cycle_active'].value()
    """
    global verbose
    if verbose:
        print("Achieved Active Warps Per SM [warp]: ", kernel['sm__warps_active.avg.per_cycle_active'].value())
    return kernel['sm__warps_active.avg.per_cycle_active'].value()

def get_sm__warps_active_avg_pct_of_peak_sustained_active(kernel):
    """ Get Achieved Occupancy.
        cumulative # of warps in flight (This counter metric represents the avg percent of the peak sustained rate achie-
        ved during unit active cycles across all sub-unit instances)
        
        sm: The Streaming Multiprocessor handles execution of a kernel as groups of 32 threads, called warps. Warps are 
        further grouped into cooperative thread arrays (CTA), called blocks in CUDA. All warps of a CTA execute on the sa-
        me SM. CTAs share various resources across their threads, e.g. the shared memory.

        warps: A a group of 32 threads within a CTA. A warp is allocated to a sub partition and resides on the sub parti-
        tion from launch to completion.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['sm__warps_active.avg.pct_of_peak_sustained_active'].value()
    """
    global verbose
    if verbose:
        print("Achieved Occupancy [%]: ", kernel['sm__warps_active.avg.pct_of_peak_sustained_active'].value())
    return kernel['sm__warps_active.avg.pct_of_peak_sustained_active'].value()


#########################################################################################################################
###                                                                                                                   ###
###                                             Instruction Statistics                                                ###
###                                                                                                                   ###
#########################################################################################################################

def get_smsp__inst_executed_sum(kernel):
    """ Get Executed Instructions.
        # of warp instructions executed (This counter metric represents the sum across all sub-unit instances)
        
        smsp: Each SM is partitioned into four processing blocks, called SM sub partitions. The SM sub partitions are the 
        primary processing elements on the SM. A sub partition manages a fixed size pool of warps.

        warp: A a group of 32 threads within a CTA. A warp is allocated to a sub partition and resides on the sub partition 
        from launch to completion.

        instructions: An assembly (SASS) instruction. Each executed instruction may generate zero or more requests.

    Args:
        kernel (_type_): _description_

    Returns:
        float: kernel['smsp__inst_executed.sum'].value()
    """
    global verbose
    if verbose:
        print("Executed Instructions [inst]: ", kernel['smsp__inst_executed.sum'].value())
    return kernel['smsp__inst_executed.sum'].value()

