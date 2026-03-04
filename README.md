# Awesome RISC-V Resources

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated resources for the free and open RISC-V instruction set architecture - cores, toolchains, simulators, boards, courses, and research.

---

## Contents

- [Open Source Implementations](#open-source-implementations)
  - [Cores](#cores)
  - [SoCs](#socs)
  - [Uncategorized](#uncategorized)
- [Open Source Toolchains](#open-source-toolchains)
  - [Design Environment](#design-environment)
  - [HDLs](#hdls)
  - [Simulators/Emulators](#simulatorsemulators)
  - [Uncategorized](#uncategorized-1)
  - [Verification and Testing Environment](#verification-and-testing-environment)
- [Hardware](#hardware)
  - [Educational Boards](#educational-boards)
- [Technical Resources](#technical-resources)
  - [Articles](#articles)
  - [Books](#books)
  - [Courses](#courses)
  - [Research Papers and Publications](#research-papers-and-publications)
  - [Uncategorized](#uncategorized-2)
  - [Videos](#videos)
- [Social Media](#social-media)
  - [Forums](#forums)
  - [Google Groups](#google-groups)
  - [Reddit](#reddit)
  - [Telegram](#telegram)

## Open Source Implementations

A curated list of awesome RISC-V open source implementations which will inspire you to make yours.

### Cores

A curated list of RISC-V Cores, available as open source with proper documentations.

- [bigPULP](https://github.com/pulp-platform/bigpulp) - Big version of the PULP platform with large cluster configurations for HPC workloads.
- [biRISC-V](https://github.com/ultraembedded/biriscv) - 32-bit dual-issue in-order RISC-V CPU.
- [BOOM](https://github.com/riscv-boom/riscv-boom) - Berkeley Out-of-Order RISC-V Processor.
- [CV32E40P](https://github.com/openhwgroup/cv32e40p) - OpenHW Group CORE-V CV32E40P RISC-V IP.
- [CVA6](https://github.com/openhwgroup/cva6) - 6-stage, single-issue in-order RISC-V core maintained by the OpenHW Group.
- [DarkRISCV](https://github.com/darklife/darkriscv) - Experimental RISC-V implementation in Verilog, fitting in a small FPGA.
- [E203](https://github.com/SI-RISCV/e200_opensource) - Hummingbird E203 Opensource Processor Core.
- [FlexPRET](https://github.com/pretis/flexpret) - 5-stage, fine-grained multithreaded RISC-V processor.
- [Freedom](https://github.com/sifive/freedom) - By SiFive for its Freedom E300 and U500 platforms.
- [FWRISC](https://github.com/mballance/fwrisc) - Featherweight RISC-V implementation.
- [FWRISC-S](https://github.com/mballance/fwrisc-s) - Extended variant of the FWRISC featherweight RISC-V core with added CSR support.
- [Ibex](https://github.com/lowRISC/ibex) - Small, 32-bit RISC-V core from lowRISC, formally verified and production-proven.
- [KLESSYDRA-F03](https://github.com/klessydra/F03x) - Interleaved multithreaded RISC-V processor (F03 variant) with DSP extensions.
- [KLESSYDRA-T02](https://github.com/klessydra/T02x) - Interleaved multithreaded RISC-V processor (T02 variant).
- [KLESSYDRA-T03](https://github.com/klessydra/T03x) - Interleaved multithreaded RISC-V processor (T03 variant).
- [KLESSYDRA-T13](https://github.com/klessydra/T13x) - Interleaved multithreaded RISC-V processor (T13 variant).
- [Kronos](https://github.com/SonalPinto/kronos) - Lightweight, 3-stage in-order RV32I pipeline written in SystemVerilog.
- [Leros](https://github.com/leros-dev/leros) - Tiny accumulator-based processor core targeting FPGAs.
- [lipsi](https://github.com/schoeberl/lipsi) - Probably the smallest processor in the world, implemented in Chisel.
- [Lizard](https://github.com/cornell-brg/lizard) - Modular, out-of-order RISC-V processor built with PyMTL.
- [Maestro](https://github.com/Artoriuz/maestro) - RISC-V RV32I processor implemented in VHDL.
- [Minerva](https://github.com/lambdaconcept/minerva) - 32-bit RISC-V soft processor.
- [MR1](https://github.com/tomverbeure/mr1) - Minimal RISC-V RV32I core implemented in SpinalHDL.
- [mriscv](https://github.com/onchipuis/mriscv) - 32-bit pipelined RISC-V processor implemented in Verilog.
- [NEORV32](https://github.com/stnolting/neorv32) - Customizable, extensible MCU-class 32-bit soft-core CPU and SoC written in VHDL.
- [NutShell](https://github.com/OSCPU/NutShell) - RISC-V processor developed by the University of Chinese Academy of Sciences.
- [OpenPiton](https://github.com/PrincetonUniversity/openpiton) - World's first open source, general purpose, multithreaded manycore processor.
- [patmos](https://github.com/t-crest/patmos) - Time-predictable VLIW processor.
- [PicoRV32](https://github.com/cliffordwolf/picorv32) - Size-Optimized RISC-V CPU.
- [PULP](https://github.com/pulp-platform/pulp) - Parallel Ultra-Low-Power open-source multi-core computing platform.
- [Rattlesnake](https://github.com/PulseRain/Rattlesnake) - RISC-V RV32IMC Soft CPU, with a Security-Hardened Processor Core.
- [Reindeer](https://github.com/PulseRain/Reindeer) - PulseRain soft CPU supporting the RISC-V RV32IM instruction set.
- [ReonV](https://github.com/lcbcFoo/ReonV) - RISC-V implementation based on a modified version of the Leon3 SPARC processor.
- [RISCV-CLaSH](https://github.com/adamwalker/clash-riscv) - RiscV processor implementing the RV32I instruction set written in clash.
- [riscv-mini](https://github.com/ucb-bar/riscv-mini) - Simple three-stage RISC-V pipeline written in Chisel.
- [Riscy](https://github.com/csail-csg/riscy) - MIT CSAIL family of open-sourced, formally verified RISC-V processors.
- [RiscyOO](https://github.com/csail-csg/riscy-OOO) - MIT CSAIL out-of-order RISC-V processor with memory model support.
- [Rocket](https://github.com/chipsalliance/rocket-chip) - Parameterizable RISC-V SoC generator from UC Berkeley.
- [RPU](https://github.com/Domipheus/RPU) - Basic RISC-V CPU implementation in VHDL.
- [RSD](https://github.com/rsd-devel/rsd) - Out-of-order superscalar RISC-V processor written in SystemVerilog.
- [RV01](https://opencores.org/projects/rv01_riscv_core) - Pipelined RV32I implementation on OpenCores targeting FPGAs.
- [RV12](https://github.com/roalogic/RV12) - Single-issue, in-order RV32I/RV64I RISC-V core from RoaLogic.
- [Sail RISC-V](https://github.com/rems-project/sail-riscv) - RISCV Sail Model.
- [SCR1](https://github.com/syntacore/scr1) - Free and open-source MCU-class RISC-V core from Syntacore.
- [SERV](https://github.com/olofk/serv) - Award-winning ultra-compact bit-serial RISC-V core.
- [Shakti C-Class](https://gitlab.com/shaktiproject/cores/c-class) - Application-class 64-bit RISC-V core from IIT Madras.
- [Shakti E-Class](https://gitlab.com/shaktiproject/cores/e-class) - Embedded-class 32-bit RISC-V core from IIT Madras.
- [Sodor](https://github.com/ucb-bar/riscv-sodor) - Educational collection of simple RISC-V processors written in Chisel by UC Berkeley.
- [SSRV](https://github.com/risclite/SuperScalar-RISCV-CPU) - SuperScalar-RISCV-CPU.
- [Steel](https://github.com/rafaelcalcada/steel-core) - Simple, 32-bit RISC-V processor core designed to be easily embedded into SoCs.
- [SweRV](https://github.com/chipsalliance/Cores-SweRV) - EH1 SweRV RISC-V CoreTM 1.8 from Western Digital.
- [SweRV EH2](https://github.com/chipsalliance/Cores-SweRV-EH2) - EH2 SweRV RISC-V CoreTM 1.2 from Western Digital.
- [SweRV EL2](https://github.com/chipsalliance/Cores-SweRV-EL2) - EL2 SweRV RISC-V CoreTM 1.2 from Western Digital.
- [Taiga](https://gitlab.com/sfu-rcl/Taiga) - 32-bit RISC-V processor designed for Xilinx FPGAs, targeting high performance.
- [Tiny Risc-V](https://github.com/liangkangnan/tinyriscv) - Easy-to-understand, from-scratch RISC-V implementation written in Verilog.
- [VeeR EL2](https://github.com/chipsalliance/Cores-VeeR-EL2) - CHIPS Alliance VeeR EL2 RISC-V Core; the actively maintained successor to the Western Digital SweRV family.
- [VexRiscv](https://github.com/SpinalHDL/VexRiscv) - FPGA-friendly 32-bit RISC-V implementation written in SpinalHDL.
- [Wally (CVW)](https://github.com/openhwgroup/cvw) - CORE-V Wally: a configurable, 5-stage-pipeline RISC-V processor associated with the *RISC-V System-on-Chip Design* textbook by Harris et al.
- [WARP-V](https://github.com/stevehoover/warp-v) - Open-source RISC-V core IP you can shape to your needs.
- [XiangShan](https://github.com/OpenXiangShan/XiangShan) - Open-source high-performance out-of-order RISC-V processor developed at the Institute of Computing Technology, Chinese Academy of Sciences.

### SoCs

A curated list of RISC-V SoCs, available as open sources.

- [Icicle](https://github.com/grahamedgecombe/icicle) - 32-bit RISC-V system on chip for iCE40 HX8K, iCE40 UP5K and ECP5 FPGAs.
- [Iob-SoC](https://github.com/IObundle/iob-soc) - Template for building RISC-V-based SoCs using open-source tools.
- [PicoSoC](https://github.com/cliffordwolf/picorv32/tree/master/picosoc) - Simple example SoC using PicoRV32.
- [Raven](https://github.com/efabless/raven-picorv32) - ASIC implementation of the PicoSoC PicoRV32.
- [Riscy SoC](https://github.com/AleksandarKostovic/Riscy-SoC) - RISC-V SoC implementation targeting Xilinx FPGAs.
- [Shakti SoC](https://gitlab.com/shaktiproject/cores/shakti-soc) - Complete SoC built around the Shakti RISC-V processor family from IIT Madras.

### Uncategorized

- [CDL Hardware](https://github.com/atthecodeface/cdl_hardware) - Hardware designs in Cycle Description Language (CDL) targeting RISC-V.
- [DANA](https://github.com/bu-icsg/dana) - Dynamically Allocated Neural Network (DANA) Accelerator.
- [RISCV-FS](https://github.com/mrLSD/riscv-fs) - RISC-V formal ISA Specification.

## Open Source Toolchains

A curated list of open source toolchains which will help you make your own design.

### Design Environment

- [Chipyard](https://github.com/ucb-bar/chipyard) - Framework for agile development of Chisel-based systems-on-chip.
- [Firrtl](https://github.com/freechipsproject/firrtl) - Flexible Internal Representation for RTL.
- [LowRISC Chip](https://github.com/lowRISC/lowrisc-chip) - lowRISC SoC platform built on the Rocket RISC-V core.
- [nextpnr](https://github.com/YosysHQ/nextpnr) - Portable FPGA place and route tool.
- [PULPino](https://github.com/pulp-platform/pulpino) - Single-core microcontroller system, based on 32-bit RISC-V cores.
- [PULPissimo](https://github.com/pulp-platform/pulpissimo) - Microcontroller architecture of the more recent PULP chips.
- [RISC-V GNU Toolchain](https://github.com/riscv/riscv-gnu-toolchain) - RISC-V GNU Compiler Toolchain.
- [RISC-V Linux](https://github.com/westerndigitalcorporation/RISC-V-Linux/) - Build Fedora Gnome Desktop on RISC-V.
- [Treadle](https://github.com/freechipsproject/treadle) - Chisel/Firrtl Execution Engine.

### HDLs

- [CHISEL](https://github.com/freechipsproject/chisel3) - Hardware Design Language that facilitates advanced circuit generation and design reuse in Scala.

### Simulators/Emulators

A curated list of open source Emulators/Simulators to design and test your RISC-V related work.

- [Dromajo](https://github.com/chipsalliance/dromajo) - Esperanto Technology's RISC-V Reference Model.
- [FireSim](https://github.com/firesim/firesim) - Easy-to-use, Scalable, FPGA-accelerated Cycle-accurate Hardware Simulation.
- [FireSim-NVDLA](https://github.com/CSL-KU/firesim-nvdla) - Full-system simulator integrated with NVIDIA Deep Learning Accelerator (NVDLA).
- [FuseSoC](https://github.com/olofk/fusesoc) - Award-winning package manager and build tool set for HDL projects.
- [GAP8 SDK](https://github.com/GreenWaves-Technologies/gap_sdk) - SDK for the GAP8 RISC-V multi-core IoT application processor by GreenWaves Technologies.
- [gem5](https://github.com/gem5/gem5) - The gem5 computer-system architecture simulator; widely used in academia for RISC-V microarchitecture research.
- [QEMU](https://github.com/qemu/qemu) - The leading open-source machine emulator and virtualizer; supports both RV32 and RV64 system and user-mode emulation.
- [RARS](https://github.com/TheThirdOne/rars) - RISC-V Assembler and Runtime Simulator.
- [Renode](https://github.com/renode/renode) - Antmicro's open-source simulation framework with excellent RISC-V support; ideal for embedded and multi-core prototyping.
- [Ripes](https://github.com/mortbopet/Ripes) - Visual computer architecture simulator and assembly code editor.
- [riscv-VM](https://github.com/openhwgroup/riscv_vm) - OpenHW Group's RISC-V Virtual Machine.
- [Shakti SDK](https://gitlab.com/shaktiproject/software/shakti-sdk) - Software development kit for the Shakti RISC-V processor family from IIT Madras.
- [Spike](https://github.com/riscv/riscv-isa-sim/) - RISC-V ISA Simulator.
- [SweRV ISS](https://github.com/westerndigitalcorporation/swerv-ISS) - Instruction Set Simulator for the SweRV RISC-V core family.
- [TinyEMU](https://bellard.org/tinyemu/) - System emulator for the RISC-V and x86 architectures.
- [TLBSim](https://github.com/nbdd0121/TLBSim) - Fast TLB simulator for RISC-V systems.
- [Venus](https://venus.cs61c.org/) - Browser-based RV32 assembler and runtime simulator used in UC Berkeley's CS 61C course; ideal for beginners.
- [Verilator](https://github.com/verilator/verilator) - Fastest Verilog/SystemVerilog simulator.

### Uncategorized

- [BRSIC-V](https://ascslab.org/research/briscv/explorer/explorer.html) - Browser-based RISC-V architecture design space exploration tool from Boston University.
- [WebRISC-V](https://github.com/Mariotti94/WebRISC-V) - Web-based graphical pipelined datapath simulation environment built for the RISC-V.

### Verification and Testing Environment

- [Axe](https://github.com/CTSRD-CHERI/axe) - Automatic black box testing.
- [BOOM Attacks](https://github.com/riscv-boom/boom-attacks) - BOOM Speculative Attacks.
- [CHISEL Tester](https://github.com/freechipsproject/chisel-testers) - Testing utilities for circuits written in Chisel.
- [RISC-V DV](https://github.com/google/riscv-dv) - SV/UVM based open-source instruction generator for RISC-V processor verification.
- [RISC-V Formal](https://github.com/SymbioticEDA/riscv-formal) - Open-source formal verification framework for RISC-V processors.
- [RISC-V Tests](https://github.com/riscv/riscv-tests) - Unit tests for RISC-V processors.
- [RISC-V Torture](https://github.com/ucb-bar/riscv-torture) - Random torture test generator for RISC-V processors.

## Hardware

Physical boards and platforms for hands-on RISC-V experimentation.

### Educational Boards

Affordable and accessible RISC-V development boards recommended for students and researchers.

- [HiFive1 Rev B](https://www.sifive.com/boards/hifive1-rev-b) - SiFive's Arduino-compatible RISC-V microcontroller board; an accessible entry point for bare-metal embedded programming.
- [Milk-V Duo](https://milkv.io/duo) - Extremely low-cost ($5–$9) ultra-compact embedded Linux board based on a RISC-V + ARM dual-core SoC; great for IoT learning.
- [StarFive VisionFive 2](https://www.starfivetech.com/en/site/boards) - Affordable quad-core 64-bit RISC-V SBC (JH7110) with GPU, dual GbE, HDMI 2.0, and M.2 NVMe; runs Debian/Ubuntu; recommended for full Linux RISC-V experience.

## Technical Resources

Resources to help you make your own designs.

### Articles

- [2019 : A year of RISC-V and Open source silicon](https://www.linkedin.com/pulse/2019-year-risc-v-open-source-silicon-olof-kindgren/) - Year-in-review article covering the biggest RISC-V open-source silicon milestones of 2019.
- [Learn with Shakti](https://shakti.org.in/learn_with_shakti/intro.html) - Introductory learning resource for the Shakti RISC-V processor from IIT Madras.
- [Making a real processor step by step using RISC-V ISA](https://dl.acm.org/doi/10.1145/3210713.3210741) - ACM paper walking through a step-by-step processor implementation using the RISC-V ISA.
- [Research](https://www.ocf.berkeley.edu/~qmn/research.html) - Research page on RISC-V-related work from UC Berkeley.
- [RISC-V Bases and Extensions Explained](https://www.cnx-software.com/2019/08/27/risc-v-bases-and-extensions-explained/) - Accessible overview of the RISC-V base ISA and its standard extensions.
- [RISC-V RV32I assembly with Ripes simulator](https://dantalion.nl/en/risc-v-rv32i-assembly-with-ripes-simulator/) - Tutorial on writing and visualizing RV32I assembly using the Ripes simulator.
- [Sail](https://www.cl.cam.ac.uk/~pes20/sail/) - Research page for the Sail ISA specification language used to formally describe RISC-V.

### Books

- [Digital Design with Chisel](https://github.com/schoeberl/chisel-book) - Open-source textbook on hardware design using Chisel, with free PDF available.
- [RISC-V Assembly Language Programming](https://github.com/johnwinans/rvalp) - Free, open-source textbook (with PDF releases) covering RV32I assembly from first principles; actively maintained by John Winans.
- [RISC-V ISA Specification Manual](https://github.com/riscv/riscv-isa-manual) - The official, open-source RISC-V Instruction Set Manual (Volumes I & II); the definitive reference for the unprivileged and privileged ISA.
- [The RISC-V Reader: An Open Architecture Atlas](https://www.riscvbook.com/) - Concise introductory reference to the RISC-V ISA by Patterson & Waterman; free digital edition available.

### Courses

- [Building a RISC-V CPU Core (LFD111x)](https://www.edx.org/learn/computer-programming/the-linux-foundation-building-a-risc-v-cpu-core) - Free Linux Foundation course on edX covering hands-on CPU microarchitecture design using open-source tools (TL-Verilog / Makerchip).
- [Complex Digital Systems](https://csg.csail.mit.edu/6.375/6_375_2016_www/handouts.html) - By MIT.
- [Computer Architecture - Spring 2018](https://ascslab.org/courses/ec513/index.html) - By Boston University.
- [Computer Architecture, Summer 2017](https://passlab.github.io/CSE564/) - By Oakland University.
- [Computer Organization - Fall 2019](https://ascslab.org/courses/ec413/lectures.html) - By Boston University.
- [Computer Organization II](https://www.cs.fsu.edu/~zwang/cda3101.html) - By Florida State University.
- [Debugging & Verifying Programs](https://www.cs.utexas.edu/users/hunt/class/2019-spring/cs340d/cs340d.html) - By University of Texas.
- [Introduction to RISC-V (LFD110x)](https://www.edx.org/learn/computer-programming/the-linux-foundation-introduction-to-risc-v) - Free Linux Foundation course on edX; covers the RISC-V ISA, specifications, and ecosystem; ideal starting point for students.
- [Organization of Digital Computers Laboratory](https://canvas.eee.uci.edu/courses/7673/assignments/syllabus) - By UC Irvine.
- [RISC-V ISA using Chisel](https://pages.cs.wisc.edu/~karu/courses/cs752/fall2016/wiki/index.php?n=Main.Project) - By University of Wisconsin–Madison.

### Research Papers and Publications

- [A Case for OS-Friendly Hardware Accelerators](https://people.eecs.berkeley.edu/~krste/papers/osaccel-wivosca2013.pdf) - Paper arguing for OS-managed hardware accelerator interfaces.
- [A Hardware Accelerator for Tracing Garbage Collection](https://ieeexplore.ieee.org/document/8416824) - IEEE paper on custom hardware support for garbage collection in managed-runtime environments.
- [A Resource-Limited Hardware Accelerator for Convolutional Neural Networks in Embedded Vision Applications](https://ieeexplore.ieee.org/document/7891946) - IEEE paper on compact CNN acceleration for embedded vision.
- [A RISC-V Vector Processor With Simultaneous-Switching Switched-Capacitor DC–DC Converters in 28 nm FDSOI](https://ieeexplore.ieee.org/document/7422720) - IEEE paper on integrated power-management for RISC-V vector processors.
- [A RISC-V vector processor with tightly-integrated switched-capacitor DC-DC converters in 28nm FDSOI](https://ieeexplore.ieee.org/document/7231305) - IEEE paper on energy-efficient RISC-V vector cores with integrated DC-DC converters.
- [Accelerating Deep Convolutional Neural Networks Using Specialized Hardware](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/CNN20Whitepaper.pdf) - Microsoft Research whitepaper on dedicated CNN hardware acceleration.
- [AI Requires Many Approaches](https://www.linleygroup.com/uploads/intel-ai-white-paper-final.pdf) - Linley Group whitepaper on diverse hardware strategies for AI inference.
- [An Agile Approach to Building RISC-V Microprocessors](https://ieeexplore.ieee.org/document/7436635) - IEEE paper on agile hardware development methodology applied to RISC-V.
- [An Efficient Instruction Fetch Architecture for a RISC-V Soft Processor on an FPGA](https://dl.acm.org/doi/10.1145/3337801.3337803) - ACM paper on optimizing instruction fetch stages in FPGA-based RISC-V cores.
- [Ara: A 1 GHz+ Scalable and Energy-Efficient RISC-V Vector Processor with Multi-Precision Floating Point Support in 22 nm FD-SOI](https://arxiv.org/abs/1906.00478) - ArXiv paper on the high-performance Ara vector unit for RISC-V.
- [BOOM v2: an open-source out-of-order RISC-V core](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-157.pdf) - UC Berkeley technical report on the second-generation BOOM processor.
- [BRISC-V: An Open-Source Architecture Design Space Exploration Toolbox](https://arxiv.org/abs/1908.09992) - ArXiv paper describing the BRISC-V design-space exploration framework.
- [Cambricon: An Instruction Set Architecture for Neural Networks](https://ieeexplore.ieee.org/document/7551409) - IEEE paper introducing an ISA tailored to neural network operations.
- [Chipyard - An Integrated SoC Research and Implementation Environment](https://ieeexplore.ieee.org/document/9218756) - IEEE paper presenting the Chipyard SoC development framework.
- [Chipyard: Integrated Design, Simulation, and Implementation Framework for Custom SoCs](https://ieeexplore.ieee.org/document/9099108) - IEEE Micro article on agile SoC construction using Chipyard.
- [Design and Implementation of CNN Custom Processor Based on RISC-V Architecture](https://ieeexplore.ieee.org/document/8855445) - IEEE paper on a RISC-V custom processor extension for CNN inference.
- [Design and programming of a coprocessor for a RISC-V architecture](https://www.semanticscholar.org/paper/Design-and-programming-of-a-coprocessor-for-a-Panades/5734383c1b4e585d6c9df090875c715c66d0ad30) - Paper on designing and programming a RISC-V coprocessor for specialized computation.
- [Design of the RISC-V Instruction Set Architecture](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-1.pdf) - Andrew Waterman's PhD dissertation on the design philosophy of the RISC-V ISA.
- [DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning](https://users.cs.duke.edu/~lkw34/papers/diannao-asplos2014.pdf) - ASPLOS 2014 paper on the influential DianNao neural network accelerator.
- [FirePerf: FPGA-Accelerated Full-System Hardware/Software Performance Profiling and Co-Design](https://people.eecs.berkeley.edu/~alonamid/papers/asplos2020-fireperf.pdf) - ASPLOS 2020 paper on co-design profiling using FPGA simulation.
- [FireSim: FPGA-Accelerated Cycle-Exact Scale-Out System Simulation in the Public Cloud](https://people.eecs.berkeley.edu/~alonamid/papers/isca2018-firesim.pdf) - ISCA 2018 paper introducing the FireSim FPGA simulation platform.
- [FPGA-accelerated machine learning inference as a service for particle physics computing](https://arxiv.org/abs/1904.08986) - ArXiv paper on using FPGAs for ML inference in particle physics pipelines.
- [GAP-8: A RISC-V SoC for AI at the Edge of the IoT](https://ieeexplore.ieee.org/document/8445101) - IEEE paper on the GAP-8 multi-core RISC-V SoC for edge AI inference.
- [Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architectures](https://people.eecs.berkeley.edu/~alonamid/papers/gemmini-arxiv-1911.09925.pdf) - Paper on the Gemmini systolic array generator integrated with the Rocket/BOOM RISC-V ecosystem.
- [GhostRider: A Hardware-Software System for Memory Trace Oblivious Computation](https://dl.acm.org/doi/10.1145/2775054.2694385) - ASPLOS 2015 paper on oblivious RAM computation using custom hardware.
- [Hardware/Software Codesign for Mobile Speech Recognition](https://www.isca-speech.org/archive/archive_papers/interspeech_2013/i13_0627.pdf) - Interspeech 2013 paper on co-designed ASR acceleration for mobile devices.
- [Implementing a TLB Generator with Chisel for RISC-V Architecture](https://artemis.cslab.ece.ntua.gr:8080/jspui/bitstream/123456789/17459/3/NCPPD_Diploma_Thesis.pdf) - Diploma thesis on generating TLB microarchitectures in Chisel for RISC-V.
- [MALOC: A Fully Pipelined FPGA Accelerator for Convolutional Neural Networks With All Layers Mapped on Chip](https://ieeexplore.ieee.org/document/8412552) - IEEE paper on a fully pipelined FPGA CNN accelerator with on-chip mapping.
- [Minimizing Computation in Convolutional Neural Networks](https://link.springer.com/chapter/10.1007/978-3-319-11179-7_36) - Paper presenting techniques to reduce computation in CNN inference.
- [Nested-Parallelism PageRank on RISC-V Vector Multi-Processors](https://people.eecs.berkeley.edu/~alonamid/papers/carrv2019-nested_pagerank_hwacha.pdf) - CARRV 2019 paper on nested-parallel PageRank on the Hwacha RISC-V vector unit.
- [OSEK-V: Application-Specific RTOS Instantiation in Hardware](https://www4.cs.fau.de/Publications/2017/dietrich_17_lctes.pdf) - LCTES 2017 paper on hardware-level RTOS instantiation for RISC-V.
- [Out of order floating point coprocessor for RISC V ISA](https://ieeexplore.ieee.org/document/7208116) - IEEE paper on an out-of-order FPU coprocessor design for RISC-V.
- [PHANTOM: Practical Oblivious Computation in a Secure Processor](https://martinmaas.github.io/publications/maas-ccs13-phantom.pdf) - CCS 2013 paper on the PHANTOM oblivious computation system in secure processors.
- [Programmable Fine-Grained Power Management and System Analysis of RISC-V Vector Processors in 28-nm FD-SOI](https://ieeexplore.ieee.org/document/9144250) - IEEE paper on fine-grained power management for RISC-V vector workloads.
- [PULP-NN: Accelerating Quantized Neural Networks on Parallel Ultra-Low-Power RISC-V Processors](https://arxiv.org/abs/1908.11263) - ArXiv paper on quantized NN acceleration on the PULP RISC-V platform.
- [RISC-V out-of-order data conversion co-processor](https://ieeexplore.ieee.org/document/7208117) - IEEE paper on a data-format conversion coprocessor for RISC-V pipelines.
- [RV-CNN: Flexible and Efficient Instruction Set for CNNs Based on RISC-V Processors](https://link.springer.com/chapter/10.1007/978-3-030-29611-7_1) - Paper proposing a RISC-V ISA extension optimized for CNN workloads.
- [Scratchpad memory: a design alternative for cache on-chip memory in embedded systems](https://ieeexplore.ieee.org/document/1003604) - IEEE paper comparing scratchpad and cache memory for embedded RISC-V SoCs.
- [SHAKTI Processors: An Open-Source Hardware Initiative](https://ieeexplore.ieee.org/document/7434907) - IEEE paper introducing the Shakti family of open-source RISC-V processors from IIT Madras.
- [SHAKTI-F: A Fault Tolerant Microprocessor Architecture](https://ieeexplore.ieee.org/document/7422253) - IEEE paper on fault-tolerant extensions to the Shakti RISC-V architecture.
- [Simty: a Synthesizable General-Purpose SIMT Processor](https://hal.inria.fr/hal-01351689v2/document) - Inria paper presenting the Simty SIMT processor built on RISC-V.
- [Simty: generalized SIMT execution on RISC-V](https://hal.inria.fr/hal-01622208/document) - Workshop paper on generalizing SIMT execution semantics for RISC-V.
- [SonicBOOM: The 3rd Generation Berkeley Out-of-Order Machine](https://carrv.github.io/2020/papers/CARRV2020_paper_15_Zhao.pdf) - CARRV 2020 paper on the third-generation BOOM out-of-order RISC-V core.
- [Specification for the FIRRTL Language](https://aspire.eecs.berkeley.edu/wp/wp-content/uploads/2017/11/Specification-for-the-FIRRTL-Language-Izraelevitz.pdf) - Formal specification of the FIRRTL intermediate representation used in Chisel-based design flows.
- [The Berkeley Out-of-Order Machine (BOOM): An Industry-Competitive, Synthesizable, Parameterized RISC-V Processor](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-167.pdf) - UC Berkeley technical report introducing the first-generation BOOM processor.
- [The Case for RISC-V in Space](https://link.springer.com/chapter/10.1007/978-3-030-11973-7_37) - Paper presenting RISC-V as a viable ISA for space-grade processor designs.
- [The RISC-V Instruction Set Manual, Volume I: Base User-Level ISA](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2011/EECS-2011-62.pdf) - Original UC Berkeley technical report defining the RISC-V base ISA.
- [The Rocket Chip Generator](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-17.pdf) - UC Berkeley technical report on the parameterizable Rocket Chip SoC generator.
- [TIMBER-V: Tag-Isolated Memory Bringing Fine-grained Enclaves to RISC-V](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_10-3_Weiser_paper.pdf) - NDSS 2019 paper on tag-based memory isolation for RISC-V secure enclaves.
- [Towards a High-Performance RISC-V Emulator](https://www.researchgate.net/publication/328314631_Towards_a_High-Performance_RISC-V_Emulator) - Paper exploring micro-optimization techniques for RISC-V software emulation.
- [Towards Deep Learning using TensorFlow Lite on RISC-V](https://www.researchgate.net/publication/339298701_Towards_Deep_Learning_using_TensorFlow_Lite_on_RISC-V) - Paper on porting TensorFlow Lite to run on RISC-V embedded platforms.
- [Towards General-Purpose Neural Network Computing](https://ieeexplore.ieee.org/document/7429298) - IEEE paper on domain-specific neural network acceleration.
- [Tuning Algorithms and Generators for Efficient Edge Inference](https://arxiv.org/abs/1908.02239) - ArXiv paper on algorithm-level tuning for resource-efficient neural network inference.
- [Using FireSim to Enable Agile End-to-End RISC-V Computer Architecture Research](https://people.eecs.berkeley.edu/~alonamid/papers/carrv2019-firesim_agile.pdf) - CARRV 2019 paper on using FireSim for end-to-end RISC-V research workflows.
- [Variable Precision Floating-Point RISC-V Coprocessor Evaluation using Lightweight Software and Compiler Support](https://www.researchgate.net/publication/336778311_Variable_Precision_Floating-Point_RISC-V_Coprocessor_Evaluation_using_Lightweight_Software_and_Compiler_Support) - Paper evaluating variable-precision FP coprocessor designs for RISC-V with compiler integration.

### Uncategorized

- [Advanced Examples of Using Chisel](https://github.com/librecores/riscv-sodor/wiki/Advanced-Examples-of-Using-Chisel) - Wiki page with advanced Chisel hardware design examples using the Sodor RISC-V cores.
- [Chipyard Docs](https://chipyard.readthedocs.io/en/latest/) - Official documentation for the Chipyard SoC design framework.
- [CHISEL Bootcamp](https://github.com/freechipsproject/chisel-bootcamp) - Interactive Jupyter-notebook-based bootcamp for learning Chisel hardware design.
- [CHISEL Cheatsheet](https://github.com/freechipsproject/chisel-cheatsheet) - Quick-reference cheatsheet for the Chisel hardware design language.
- [Chisel/FIRRTL Hardware Compiler Framework](https://www.chisel-lang.org/) - Official website for the Chisel HDL and FIRRTL compiler framework.
- [Cookbook](https://github.com/freechipsproject/chisel3/wiki/Cookbook) - Community-contributed Chisel patterns and solutions wiki.
- [Embedded Linux on RISC-V](https://elinux.org/images/a/ad/Elce_2018_khem_raj_Embedded_Linux-Riscv.pdf) - ELCE 2018 slides on bringing embedded Linux to RISC-V platforms.
- [FTPVL](https://github.com/TypingKoala/FPGA-Tool-Performance-Visualization-Library) - FPGA Tool Performance Visualization Library.
- [How I built a RISC-V CPU Core in a span of 5 days](https://github.com/iamrk-vlsi/RISC-V-MYTH-Workshop) - Workshop repository documenting a hands-on RISC-V TL-Verilog CPU build in five days.
- [Intensivate's Learning Journey for Chisel](https://github.com/Intensivate/learning-journey/wiki) - Community wiki documenting a structured learning path for Chisel hardware design.
- [Notes for Rocket-Chip](https://github.com/cnrv/rocket-chip-read) - Annotated reading notes on the Rocket Chip generator source code.
- [Open SoC Fabric](https://www.opensocfabric.org/home.php) - Open-source on-chip network fabric for SoC interconnects.
- [Ripes Wiki](https://github.com/mortbopet/Ripes/wiki/Ripes-Introduction) - Official wiki and introduction for the Ripes RISC-V visual simulator.
- [RISC-V on Debian](https://wiki.debian.org/RISC-V) - Debian wiki page on RISC-V port status and build instructions.
- [RISC-V Notes](https://github.com/cnrv/riscv-notes) - Community-maintained collection of notes, links, and learning resources for RISC-V.
- [UVM](https://github.com/SymbiFlow/uvm) - Universal Verification Methodology (UVM) library for open-source EDA flows.

### Videos

- [Looking into Hello World on RISC-V by Dennis Clarke](https://www.twitch.tv/tsoding/video/498698691) - Live stream walkthrough of a Hello World program running on RISC-V hardware.
- [R32V2020 32-Bit RISC CPU Design](https://www.youtube.com/playlist?list=PLn__0BqzWEWPIsUE0TUdsspej2vHV-osY) - YouTube playlist on designing a custom 32-bit RISC CPU from scratch.
- [RISC-V ASM Tutorial Collection](https://www.youtube.com/watch?v=KLybwrpfQ3I&list=PL6noQ0vZDAdh_aGvqKvxd0brXImHXMuLY&ab_channel=WesternDigitalCorporation) - By Western Digital Corporation.
- [RISC-V Workshop Zurich](https://www.youtube.com/playlist?list=PL85jopFZCnbMcS3bdzdd7AdLop5DtEOWB) - Recordings from the RISC-V Workshop held in Zurich covering ISA development and ecosystem updates.

## Social Media

These social media profiles will update about recent RISC-V related news.

### Forums

- [OSDForum](https://www.osdforum.org/) - Open-source digital design forum covering RISC-V, FPGAs, and EDA topics.
- [RISC-V official forum](https://riscv.org/technical/technical-forums/) - Official RISC-V International technical forums for ISA and ecosystem discussions.

### Google Groups

- [Chisel Users](https://groups.google.com/g/chisel-users) - Community mailing list for users of the Chisel hardware design language.
- [RISC-V HW Dev](https://groups.google.com/a/groups.riscv.org/g/hw-dev?pli=1) - Official RISC-V hardware development mailing list.
- [RISC-V ISA Dev](https://groups.google.com/a/groups.riscv.org/g/isa-dev) - Official mailing list for RISC-V ISA specification development discussions.
- [RISC-V Teach](https://groups.google.com/a/groups.riscv.org/g/riscv-teach) - Mailing list for educators using RISC-V in courses and academic programs.

### Reddit

- [RISC-V](https://www.reddit.com/r/RISCV/) - Subreddit for RISC-V news, projects, and community discussion.

### Telegram

- [RISC-V](https://t.me/riscv) - Telegram group for real-time RISC-V community chat.

## Contribute

This list grows with the community. Whether you've found a new open-source core, a great course, or a tool that made your RISC-V workflow significantly better, your contribution is welcome here.

Please read the **[Contribution Guidelines](Contributing.md)** before opening a pull request. We follow the sindresorhus/awesome standard: every entry must have a description, a live `https://` link, and be actively maintained.

> Found a dead link or an outdated resource? Open an issue on GitHub — that's a contribution too! ✨
