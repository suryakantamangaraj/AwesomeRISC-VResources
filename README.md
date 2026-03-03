<div align="center">

# Awesome RISC-V Resources

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/github/license/suryakantamangaraj/AwesomeRISC-VResources?color=brightgreen)](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/suryakantamangaraj/AwesomeRISC-VResources)](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/stargazers)
[![Contributors](https://img.shields.io/github/contributors/suryakantamangaraj/AwesomeRISC-VResources?color=2b9348)](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/suryakantamangaraj/AwesomeRISC-VResources)](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/pulls)
[![Issues](https://img.shields.io/github/issues/suryakantamangaraj/AwesomeRISC-VResources)](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/issues)

**A curated, community-maintained list of high-quality RISC-V resources — open-source cores, simulators, toolchains, development boards, textbooks, courses, and research papers — for engineers, students, and researchers building on the open RISC-V ISA.**

</div>

---

### Contents

- [Open Source Implementations](#open-source-implementations)
  - [Cores](#cores)
  - [SoCs](#socs)
  - [Uncategorized](#uncategorized)
  - [Deprecated](#deprecated)
- [Open Source Toolchains](#open-source-toolchains)
  - [HDLs](#hdls)
  - [Simulators/Emulators](#simulatorsemulators)
  - [Design Environment](#design-environment)
  - [Verification and Testing Environment](#verification-and-testing-environment)
  - [Uncategorized](#uncategorized-1)
- [Hardware](#hardware)
  - [Educational Boards](#educational-boards)
- [Technical Resources](#technical-resources)
  - [Books](#books)
  - [Videos](#videos)
  - [Courses](#courses)
  - [Articles](#articles)
  - [Research Papers and Publications](#research-papers-and-publications)
  - [Uncategorized](#uncategorized-2)
- [Social Media](#social-media)
  - [Forums](#forums)
  - [Google Groups](#google-groups)
  - [Reddit](#reddit)
  - [Telegram](#telegram)
- [Contribute](#contribute)
- [Support This Project](#support-this-project)
- [Credits](#credits)
- [License](#license)

## Open Source Implementations

A curated list of awesome RISC-V open source implementations which will inspire you to make yours.

### Cores

A curated list of RISC-V Cores, available as open source with proper documentations.

- [bigPULP](https://github.com/pulp-platform/bigpulp)
- [biRISC-V](https://github.com/ultraembedded/biriscv) - BiRISC-V - 32-bit dual issue RISC-V CPU.
- [BOOM](https://github.com/riscv-boom/riscv-boom) - Berkeley Out-of-Order RISC-V Processor.
- [CV32E40P](https://github.com/openhwgroup/cv32e40p) - OpenHW Group CORE-V CV32E40P RISC-V IP.
- [CVA6](https://github.com/openhwgroup/cva6) - CVA6 RISC-V CPU.
- [DarkRISCV](https://github.com/darklife/darkriscv)
- [E203](https://github.com/SI-RISCV/e200_opensource) - Hummingbird E203 Opensource Processor Core.
- [FlexPRET](https://github.com/pretis/flexpret) - 5-stage, fine-grained multithreaded RISC-V* processor.
- [Freedom](https://github.com/sifive/freedom) - By SiFive for its Freedom E300 and U500 platforms.
- [FWRISC](https://github.com/mballance/fwrisc) - Featherweight RISC-V implementation.
- [FWRISC-S](https://github.com/mballance/fwrisc-s)
- [Ibex](https://github.com/lowRISC/ibex) - Ibex RISC-V Core.
- [KLESSYDRA-F03](https://github.com/klessydra/F03x)
- [KLESSYDRA-T02](https://github.com/klessydra/T02x) - KLESSYDRA-T02 INTRELEAVED MULTITHREADED PROCESSOR.
- [KLESSYDRA-T03](https://github.com/klessydra/T03x) - KLESSYDRA-T03 INTRELEAVED MULTITHREADED PROCESSOR.
- [KLESSYDRA-T13](https://github.com/klessydra/T13x) - KLESSYDRA-T13 INTRELEAVED MULTITHREADED PROCESSOR.
- [Kronos](https://github.com/SonalPinto/kronos) - Kronos RISC-V.
- [Leros](https://github.com/leros-dev/leros) - Tiny Processor Core.
- [lipsi](https://github.com/schoeberl/lipsi) - Lipsi: Probably the Smallest Processor in the World.
- [Lizard](https://github.com/cornell-brg/lizard) - Lizard Core.
- [Maestro](https://github.com/Artoriuz/maestro)
- [Minerva](https://github.com/lambdaconcept/minerva) - 32-bit RISC-V soft processor.
- [MR1](https://github.com/tomverbeure/mr1)
- [mriscv](https://github.com/onchipuis/mriscv)
- [NEORV32](https://github.com/stnolting/neorv32) - NEORV32 Processor (RISC-V).
- [NutShell](https://github.com/OSCPU/NutShell)
- [OpenPiton](https://github.com/PrincetonUniversity/openpiton) - World's first open source, general purpose, multithreaded manycore processor.
- [patmos](https://github.com/t-crest/patmos) - Time-predictable VLIW processor.
- [PicoRV32](https://github.com/cliffordwolf/picorv32) - Size-Optimized RISC-V CPU.
- [PULP](https://github.com/pulp-platform/pulp) - PULP (Parallel Ultra-Low-Power) is an open-source multi-core computing platform.
- [Rattlesnake](https://github.com/PulseRain/Rattlesnake) - RISC-V RV32IMC Soft CPU, with a Security-Hardened Processor Core.
- [Reindeer](https://github.com/PulseRain/Reindeer) - PulseRain Reindeer - RISCV RV32I[M] Soft CPU.
- [ReonV](https://github.com/lcbcFoo/ReonV)
- [RISCV-CLaSH](https://github.com/adamwalker/clash-riscv) - RiscV processor implementing the RV32I instruction set written in clash.
- [riscv-mini](https://github.com/ucb-bar/riscv-mini)
- [Riscy](https://github.com/csail-csg/riscy) - Riscy Processors - Open-Sourced RISC-V Processors.
- [RiscyOO](https://github.com/csail-csg/riscy-OOO) - RiscyOO: RISC-V Out-of-Order Processors.
- [Rocket](https://github.com/chipsalliance/rocket-chip) - Rocket Chip Generator 🚀.
- [RPU](https://github.com/Domipheus/RPU) - Basic RISC-V CPU implementation in VHDL.
- [RSD](https://github.com/rsd-devel/rsd) - RSD RISC-V Out-of-Order Superscalar Processor.
- [RV01](https://opencores.org/projects/rv01_riscv_core)
- [RV12](https://github.com/roalogic/RV12)
- [Sail RISC-V](https://github.com/rems-project/sail-riscv) - RISCV Sail Model.
- [SCR1](https://github.com/syntacore/scr1) - SCR1 RISC-V Core.
- [SERV](https://github.com/olofk/serv) - SERV is an award-winning bit-serial RISC-V core.
- [Shakti C-Class](https://gitlab.com/shaktiproject/cores/c-class) - Shakti C-Class Core.
- [Shakti E-Class](https://gitlab.com/shaktiproject/cores/e-class) - Shakti E-Class Core.
- [Sodor](https://github.com/ucb-bar/riscv-sodor)
- [SSRV](https://github.com/risclite/SuperScalar-RISCV-CPU) - SuperScalar-RISCV-CPU.
- [Steel](https://github.com/rafaelcalcada/steel-core)
- [SweRV](https://github.com/chipsalliance/Cores-SweRV) - EH1 SweRV RISC-V CoreTM 1.8 from Western Digital.
- [SweRV EH2](https://github.com/chipsalliance/Cores-SweRV-EH2) - EH2 SweRV RISC-V CoreTM 1.2 from Western Digital.
- [SweRV EL2](https://github.com/chipsalliance/Cores-SweRV-EL2) - EL2 SweRV RISC-V CoreTM 1.2 from Western Digital.
- [Taiga](https://gitlab.com/sfu-rcl/Taiga) - Taiga is a 32-bit RISC-V processor.
- [Tiny Risc-V](https://github.com/liangkangnan/tinyriscv)
- [VeeR EL2](https://github.com/chipsalliance/Cores-VeeR-EL2) - CHIPS Alliance VeeR EL2 RISC-V Core; the actively maintained successor to the Western Digital SweRV family.
- [VexRiscv](https://github.com/SpinalHDL/VexRiscv)
- [Wally (CVW)](https://github.com/openhwgroup/cvw) - CORE-V Wally: a configurable, 5-stage-pipeline RISC-V processor associated with the *RISC-V System-on-Chip Design* textbook by Harris et al.
- [WARP-V](https://github.com/stevehoover/warp-v) - Open-source RISC-V core IP you can shape to your needs!.
- [XiangShan](https://github.com/OpenXiangShan/XiangShan) - Open-source high-performance out-of-order RISC-V processor developed at the Institute of Computing Technology, Chinese Academy of Sciences.

### Deprecated

- [Ariane](https://github.com/pulp-platform/ariane)
- [SweRV from WD](https://github.com/westerndigitalcorporation/swerv_eh1_fpga) - FPGA Reference Design for the SweRV RISC-V CoreTM from Western Digital.
- [zscale](https://github.com/ucb-bar/zscale)

### SoCs

A curated list of RISC-V SoCs, available as open sources.

- [Icicle](https://github.com/grahamedgecombe/icicle) - 32-bit RISC-V system on chip for iCE40 HX8K, iCE40 UP5K and ECP5 FPGAs.
- [Iob-SoC](https://github.com/IObundle/iob-soc)
- [PicoSoC](https://github.com/cliffordwolf/picorv32/tree/master/picosoc) - Simple example SoC using PicoRV32.
- [Raven](https://github.com/efabless/raven-picorv32) - ASIC implementation of the PicoSoC PicoRV32.
- [Riscy SoC](https://github.com/AleksandarKostovic/Riscy-SoC)
- [Shakti SoC](https://gitlab.com/shaktiproject/cores/shakti-soc)
- [VexRiscv](https://github.com/SpinalHDL/VexRiscv) - [Briey](https://github.com/SpinalHDL/VexRiscv#briey-soc), and [Murax](https://github.com/SpinalHDL/VexRiscv#murax-soc).

### Uncategorized

- [CDL Hardware](https://github.com/atthecodeface/cdl_hardware)
- [DANA](https://github.com/bu-icsg/dana) - Dynamically Allocated Neural Network (DANA) Accelerator.
- [RISCV-FS](https://github.com/mrLSD/riscv-fs) - RISC-V formal ISA Specification.

## Open Source Toolchains

A curated list of open source toolchains which will halp to make your own design.

### Design Environment

- [Chipyard](https://github.com/ucb-bar/chipyard) - Framework for agile development of Chisel-based systems-on-chip.
- [Firrtl](https://github.com/freechipsproject/firrtl) - Flexible Internal Representation for RTL.
- [LowRISC Chip](https://github.com/lowRISC/lowrisc-chip)
- [nextpnr](https://github.com/YosysHQ/nextpnr) - Portable FPGA place and route tool.
- [PULPino](https://github.com/pulp-platform/pulpino) - Single-core microcontroller system, based on 32-bit RISC-V cores.
- [PULPissimo](https://github.com/pulp-platform/pulpissimo) - Microcontroller architecture of the more recent PULP chips.
- [RISC-V GNU Toolchain](https://github.com/riscv/riscv-gnu-toolchain) - RISC-V GNU Compiler Toolchain.
- [RISC-V LINUX](https://github.com/westerndigitalcorporation/RISC-V-Linux/) - Build Fedora Gnome Desktop on RISC-V!!.
- [Treadle](https://github.com/freechipsproject/treadle) - Chisel/Firrtl Execution Engine.

### HDLs

- [CHISEL](https://github.com/freechipsproject/chisel3)

### Simulators/Emulators

A curated list of open source Emulators/Simulators to design and test your RISC-V related work.

- [Dromajo](https://github.com/chipsalliance/dromajo) - Esperanto Technology's RISC-V Reference Model.
- [FireSim](https://github.com/firesim/firesim) - Easy-to-use, Scalable, FPGA-accelerated Cycle-accurate Hardware Simulation.
- [FireSim-NVDLA](https://github.com/CSL-KU/firesim-nvdla) - Full-system simulator integrated with NVIDIA Deep Learning Accelerator (NVDLA).
- [FuseSoC](https://github.com/olofk/fusesoc) - FuseSoC is an award-winning package manager and a set of build tools for HDL.
- [GAP8 SDK](https://github.com/GreenWaves-Technologies/gap_sdk)
- [gem5](https://github.com/gem5/gem5) - The gem5 computer-system architecture simulator; widely used in academia for RISC-V microarchitecture research.
- [QEMU](https://github.com/qemu/qemu) - The leading open-source machine emulator and virtualizer; supports both RV32 and RV64 system and user-mode emulation.
- [RARS](https://github.com/TheThirdOne/rars) - RISC-V Assembler and Runtime Simulator.
- [Renode](https://github.com/renode/renode) - Antmicro's open-source simulation framework with excellent RISC-V support; ideal for embedded and multi-core prototyping.
- [Ripes](https://github.com/mortbopet/Ripes) - Visual computer architecture simulator and assembly code editor.
- [riscv-VM](https://github.com/openhwgroup/riscv_vm) - OpenHW Group's RISC-V Virtual Machine.
- [Shakti SDK](https://gitlab.com/shaktiproject/software/shakti-sdk)
- [Spike](https://github.com/riscv/riscv-isa-sim/) - RISC-V ISA Simulator.
- [SweRV ISS](https://github.com/westerndigitalcorporation/swerv-ISS)
- [TinyEMU](https://bellard.org/tinyemu/) - System emulator for the RISC-V and x86 architectures.
- [TLBSim](https://github.com/nbdd0121/TLBSim) - Fast TLB simulator for RISC-V systems.
- [Venus](https://venus.cs61c.org/) - Browser-based RV32 assembler and runtime simulator used in UC Berkeley's CS 61C course; ideal for beginners.
- [Verilator](https://github.com/verilator/verilator) - Fastest Verilog/SystemVerilog simulator.

### Uncategorized

- [BRSIC-V](https://ascslab.org/research/briscv/explorer/explorer.html)
- [WebRISC-V](https://github.com/Mariotti94/WebRISC-V) - Web-based graphical pipelined datapath simulation environment built for the RISC-V.

### Verification and Testing Environment

- [Axe](https://github.com/CTSRD-CHERI/axe) - Automatic black box testing.
- [BOOM Attacks](https://github.com/riscv-boom/boom-attacks) - BOOM Speculative Attacks.
- [CHISEL Tester](https://github.com/freechipsproject/chisel-testers)
- [RISC-V DV](https://github.com/google/riscv-dv) - SV/UVM based open-source instruction generator for RISC-V processor verification.
- [RISC-V Formal](https://github.com/SymbioticEDA/riscv-formal) - RISC-V Formal Verification Framework.
- [RISC-V Tests](https://github.com/riscv/riscv-tests) - Unit tests for RISC-V processors.
- [RISC-V Torture](https://github.com/ucb-bar/riscv-torture) - RISC-V Torture Test Generator.

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

- [2019 : A year of RISC-V and Open source silicon](https://www.linkedin.com/pulse/2019-year-risc-v-open-source-silicon-olof-kindgren/)
- [Learn with Shakti](http://shakti.org.in/learn_with_shakti/intro.html)
- [Making a real processor step by step using RISC-V ISA](https://dl.acm.org/doi/10.1145/3210713.3210741)
- [Research](https://www.ocf.berkeley.edu/~qmn/research.html)
- [RISC-V Bases and Extensions Explained](https://www.cnx-software.com/2019/08/27/risc-v-bases-and-extensions-explained/)
- [RISC-V RV32I assembly with Ripes simulator](https://dantalion.nl/en/risc-v-rv32i-assembly-with-ripes-simulator/)
- [Sail](https://www.cl.cam.ac.uk/~pes20/sail/)

### Books

- [Digital Design with Chisel](https://github.com/schoeberl/chisel-book) - Or, [PDF](https://raw.githubusercontent.com/wiki/schoeberl/chisel-book/chisel-book.pdf).
- [RISC-V Assembly Language Programming](https://github.com/johnwinans/rvalp) - Free, open-source textbook (with PDF releases) covering RV32I assembly from first principles; actively maintained by John Winans.
- [RISC-V ISA Specification Manual](https://github.com/riscv/riscv-isa-manual) - The official, open-source RISC-V Instruction Set Manual (Volumes I & II); the definitive reference for the unprivileged and privileged ISA.
- [The RISC-V Reader: An Open Architecture Atlas](http://www.riscvbook.com/) - Concise introductory reference to the RISC-V ISA by Patterson & Waterman; free digital edition available.

### Courses

- [Building a RISC-V CPU Core (LFD111x)](https://www.edx.org/learn/computer-programming/the-linux-foundation-building-a-risc-v-cpu-core) - Free Linux Foundation course on edX covering hands-on CPU microarchitecture design using open-source tools (TL-Verilog / Makerchip).
- [Complex Digital Systems](http://csg.csail.mit.edu/6.375/6_375_2016_www/handouts.html) - By MIT.
- [Computer Architecture - Spring 2018](https://ascslab.org/courses/ec513/index.html) - By Boston University.
- [Computer Architecture, Summer 2017](https://passlab.github.io/CSE564/) - By Oakland University.
- [Computer Organization - Fall 2019](https://ascslab.org/courses/ec413/lectures.html) - By Boston University.
- [Computer Organization II](https://www.cs.fsu.edu/~zwang/cda3101.html) - By Florida State University.
- [Debugging & Verifying Programs](https://www.cs.utexas.edu/users/hunt/class/2019-spring/cs340d/cs340d.html) - By University of Texas.
- [Introduction to RISC-V (LFD110x)](https://www.edx.org/learn/computer-programming/the-linux-foundation-introduction-to-risc-v) - Free Linux Foundation course on edX; covers the RISC-V ISA, specifications, and ecosystem; ideal starting point for students.
- [Organization of Digital Computers Laboratory](https://canvas.eee.uci.edu/courses/7673/assignments/syllabus) - By UC Irvine.
- [RISC-V ISA using Chisel](http://pages.cs.wisc.edu/~karu/courses/cs752/fall2016/wiki/index.php?n=Main.Project) - By University of Wisconsin–Madison.

### Research Papers and Publications

- [A Case for OS-Friendly Hardware Accelerators](https://people.eecs.berkeley.edu/~krste/papers/osaccel-wivosca2013.pdf)
- [A Hardware Accelerator for Tracing Garbage Collection](https://ieeexplore.ieee.org/document/8416824)
- [A Resource-Limited Hardware Accelerator for Convolutional Neural Networks in Embedded Vision Applications](https://ieeexplore.ieee.org/document/7891946)
- [A RISC-V Vector Processor With Simultaneous-Switching Switched-Capacitor DC–DC Converters in 28 nm FDSOI](https://ieeexplore.ieee.org/document/7422720?arnumber=7422720&newsearch=true&queryText=risc-v)
- [A RISC-V vector processor with tightly-integrated switched-capacitor DC-DC converters in 28nm FDSOI](https://ieeexplore.ieee.org/document/7231305?arnumber=7231305&newsearch=true&queryText=risc-v)
- [Accelerating Deep Convolutional Neural Networks Using Specialized Hardware](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/CNN20Whitepaper.pdf)
- [AI Requires Many Approaches](https://www.linleygroup.com/uploads/intel-ai-white-paper-final.pdf)
- [An Agile Approach to Building RISC-V Microprocessors](https://ieeexplore.ieee.org/document/7436635?arnumber=7436635&newsearch=true&queryText=risc-v)
- [An Efficient Instruction Fetch Architecture for a RISC-V Soft Processor on an FPGA](https://dl.acm.org/doi/10.1145/3337801.3337803)
- [Ara: A 1 GHz+ Scalable and Energy-Efficient RISC-V Vector Processor with Multi-Precision Floating Point Support in 22 nm FD-SOI](https://arxiv.org/abs/1906.00478?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+HackernewsTop3Feed+%28HackerNews+Top+3+Feed%29)
- [BOOM v2: an open-source out-of-order RISC-V core](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-157.pdf)
- [BRISC-V: An Open-Source Architecture Design Space Exploration Toolbox](https://arxiv.org/abs/1908.09992)
- [Cambricon: An Instruction Set Architecture for Neural Networks](https://ieeexplore.ieee.org/document/7551409)
- [Chipyard - An Integrated SoC Research and Implementation Environment](https://ieeexplore.ieee.org/document/9218756)
- [Chipyard: Integrated Design, Simulation, and Implementation Framework for Custom SoCs](https://ieeexplore.ieee.org/document/9099108)
- [Design and Implementation of CNN Custom Processor Based on RISC-V Architecture](https://ieeexplore.ieee.org/document/8855445)
- [Design and programming of a coprocessor for a RISC-V architecture](https://www.semanticscholar.org/paper/Design-and-programming-of-a-coprocessor-for-a-Panades/5734383c1b4e585d6c9df090875c715c66d0ad30)
- [Design of the RISC-V Instruction Set Architecture](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-1.pdf)
- [DianNao:  A  Small-Footprint  High-Throughput  Acceleratorfor  Ubiquitous  Machine-Learning](https://users.cs.duke.edu/~lkw34/papers/diannao-asplos2014.pdf)
- [FirePerf: FPGA-Accelerated Full-System Hardware/Software Performance Profiling and Co-Design](https://people.eecs.berkeley.edu/~alonamid/papers/asplos2020-fireperf.pdf)
- [FireSim: FPGA-Accelerated Cycle-Exact Scale-OutSystem Simulation in the Public Cloud](https://people.eecs.berkeley.edu/~alonamid/papers/isca2018-firesim.pdf)
- [FPGA-accelerated machine learning inference as a service for particle physics computing](https://arxiv.org/abs/1904.08986)
- [GAP-8: A RISC-V SoC for AI at the Edge of the IoT](https://ieeexplore.ieee.org/document/8445101)
- [Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architectures](https://people.eecs.berkeley.edu/~alonamid/papers/gemmini-arxiv-1911.09925.pdf)
- [GhostRider: A Hardware-Software System for Memory Trace Oblivious Computation](https://dl.acm.org/doi/10.1145/2775054.2694385)
- [Hardware/Software Codesign for Mobile Speech Recognition](https://www.isca-speech.org/archive/archive_papers/interspeech_2013/i13_0627.pdf)
- [Implementing a TLB Generator with Chisel for RISC-V Architecture](http://artemis.cslab.ece.ntua.gr:8080/jspui/bitstream/123456789/17459/3/NCPPD_Diploma_Thesis.pdf)
- [MALOC: A Fully Pipelined FPGA Accelerator for Convolutional Neural Networks With All Layers Mapped on Chip](https://ieeexplore.ieee.org/document/8412552)
- [Minimizing Computation in Convolutional Neural Networks](https://link.springer.com/chapter/10.1007/978-3-319-11179-7_36)
- [Nested-Parallelism PageRank on RISC-V Vector Multi-Processors](https://people.eecs.berkeley.edu/~alonamid/papers/carrv2019-nested_pagerank_hwacha.pdf)
- [OSEK-V: Application-Specific RTOS Instantiation in Hardware](https://www4.cs.fau.de/Publications/2017/dietrich_17_lctes.pdf)
- [Out of order floating point coprocessor for RISC V ISA](https://ieeexplore.ieee.org/document/7208116?arnumber=7208116&newsearch=true&queryText=risc-v)
- [PHANTOM: Practical Oblivious Computationin a Secure Processor](https://martinmaas.github.io/publications/maas-ccs13-phantom.pdf)
- [Programmable Fine-Grained Power Management and System Analysis of RISC-V Vector Processors in 28-nm FD-SOI](https://ieeexplore.ieee.org/document/9144250)
- [PULP-NN: Accelerating Quantized Neural Networks on Parallel Ultra-Low-Power RISC-V Processors](https://arxiv.org/abs/1908.11263)
- [RISC-V out-of-order data conversion co-processor](https://ieeexplore.ieee.org/document/7208117?arnumber=7208117&newsearch=true&queryText=risc-v)
- [RV-CNN: Flexible and Efficient Instruction Set for CNNs Based on RISC-V Processors](https://link.springer.com/chapter/10.1007/978-3-030-29611-7_1)
- [Scratchpad memory: a design alternative for cache on-chip memory in embedded systems](https://ieeexplore.ieee.org/document/1003604)
- [SHAKTI Processors: An Open-Source Hardware Initiative](https://ieeexplore.ieee.org/document/7434907?arnumber=7434907&newsearch=true&queryText=risc-v)
- [SHAKTI-F: A Fault Tolerant Microprocessor Architecture](https://ieeexplore.ieee.org/document/7422253?arnumber=7422253&newsearch=true&queryText=risc-v)
- [Simty: a Synthesizable General-Purpose SIMTProcessor](https://hal.inria.fr/hal-01351689v2/document)
- [Simty: generalized SIMT execution on RISC-V](https://hal.inria.fr/hal-01622208/document)
- [SonicBOOM: The 3rd Generation Berkeley Out-of-OrderMachine](https://carrv.github.io/2020/papers/CARRV2020_paper_15_Zhao.pdf)
- [Specification for the FIRRTL Language](https://aspire.eecs.berkeley.edu/wp/wp-content/uploads/2017/11/Specification-for-the-FIRRTL-Language-Izraelevitz.pdf)
- [The Berkeley Out-of-Order Machine (BOOM): An Industry-Competitive, Synthesizable, Parameterized RISC-VProcessor](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-167.pdf)
- [The Case for RISC-V in Space](https://link.springer.com/chapter/10.1007/978-3-030-11973-7_37)
- [The RISC-V Instruction Set Manual, Volume I: BaseUser-Level ISA](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2011/EECS-2011-62.pdf)
- [The Rocket Chip Generator](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-17.pdf)
- [TIMBER-V: Tag-Isolated Memory BringingFine-grained Enclaves to RISC-V](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_10-3_Weiser_paper.pdf)
- [Towards a High-Performance RISC-V Emulator](https://www.researchgate.net/publication/328314631_Towards_a_High-Performance_RISC-V_Emulator)
- [Towards Deep Learning using TensorFlow Lite on RISC-V](https://www.researchgate.net/publication/339298701_Towards_Deep_Learning_using_TensorFlow_Lite_on_RISC-V)
- [Towards General-Purpose Neural Network Computing](https://ieeexplore.ieee.org/document/7429298?arnumber=7429298&filter=AND(p_Publication_Number:7425426) - ).
- [Tuning Algorithms and Generators for Efficient Edge Inference](https://arxiv.org/abs/1908.02239)
- [Using FireSim to Enable Agile End-to-End RISC-V ComputerArchitecture Research](https://people.eecs.berkeley.edu/~alonamid/papers/carrv2019-firesim_agile.pdf)
- [Variable Precision Floating-Point RISC-V Coprocessor Evaluation using Lightweight Software and Compiler Support](https://www.researchgate.net/publication/336778311_Variable_Precision_Floating-Point_RISC-V_Coprocessor_Evaluation_using_Lightweight_Software_and_Compiler_Support)

### Uncategorized

- [Advanced Examples of Using Chisel](https://github.com/librecores/riscv-sodor/wiki/Advanced-Examples-of-Using-Chisel)
- [Chipyard](https://chipyard.readthedocs.io/en/latest/)
- [CHISEL Bootcamp](https://github.com/freechipsproject/chisel-bootcamp)
- [CHISEL Cheatsheet](https://github.com/freechipsproject/chisel-cheatsheet)
- [Chisel/FIRRTL Hardware Compiler Framework](https://www.chisel-lang.org/)
- [Cookbook](https://github.com/freechipsproject/chisel3/wiki/Cookbook)
- [Embedded Linux on RISC-V](https://elinux.org/images/a/ad/Elce_2018_khem_raj_Embedded_Linux-Riscv.pdf)
- [FTPVL](https://github.com/TypingKoala/FPGA-Tool-Performance-Visualization-Library) - FPGA Tool Performance Visualization Library.
- [How I built a RISC-V CPU Core in a span of 5 days](https://github.com/iamrk-vlsi/RISC-V-MYTH-Workshop)
- [Intensivate's Learning Journey for Chisel](https://github.com/Intensivate/learning-journey/wiki)
- [Notes for Rocket-Chip](https://github.com/cnrv/rocket-chip-read)
- [Open SoC Fabric](http://www.opensocfabric.org/home.php)
- [Ripes Wiki](https://github.com/mortbopet/Ripes/wiki/Ripes-Introduction)
- [RISC-V](https://wiki.debian.org/RISC-V)
- [RISC-V BOOM](https://github.com/ccelio/riscv-boom-doc)
- [RISC-V Notes](https://github.com/cnrv/riscv-notes)
- [UVM](https://github.com/SymbiFlow/uvm)

### Videos

- [Looking into Hello World on RISC-V by Dennis Clarke](https://www.twitch.tv/tsoding/video/498698691)
- [R32V2020 32-Bit RISC CPU Design](https://www.youtube.com/playlist?list=PLn__0BqzWEWPIsUE0TUdsspej2vHV-osY)
- [RISC-V ASM Tutorial Collection](https://www.youtube.com/watch?v=KLybwrpfQ3I&list=PL6noQ0vZDAdh_aGvqKvxd0brXImHXMuLY&ab_channel=WesternDigitalCorporation) - By Western Digital Corporation.
- [RISC-V Workshop Zurich](https://www.youtube.com/playlist?list=PL85jopFZCnbMcS3bdzdd7AdLop5DtEOWB)

## Social Media

These social media profiles will update about recent RISC-V related news.

### Forums

- [OSDForum](https://www.osdforum.org/)
- [RISC-V official forum](https://riscv.org/technical/technical-forums/)

### Google Groups

- [Chisel Users](https://groups.google.com/g/chisel-users)
- [RISC-V HW Dev](https://groups.google.com/a/groups.riscv.org/g/hw-dev?pli=1)
- [RISC-V ISA Dev](https://groups.google.com/a/groups.riscv.org/g/isa-dev)
- [RISC-V Teach](https://groups.google.com/a/groups.riscv.org/g/riscv-teach)

### Reddit

- [RISC-V](https://www.reddit.com/r/RISCV/)

### Telegram

- [RISC-V](https://t.me/riscv)

## Contribute

This list grows with the community. Whether you've found a new open-source core, a great course, or a tool that made your RISC-V workflow significantly better — your contribution is welcome here.

Please read the **[Contribution Guidelines](Contributing.md)** before opening a pull request. We follow the [sindresorhus/awesome](https://github.com/sindresorhus/awesome) standard: every entry must have a description, a live `https://` link, and be actively maintained.

> Found a dead link or an outdated resource? Open an [issue](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/issues) — that's a contribution too! ✨

## Support This Project

<div align="center">

This list is free, open, and maintained entirely in spare time. If it has saved you hours of research, helped you pick the right core, or made RISC-V more accessible for you or your students, consider supporting its continued curation.

[![Sponsor on GitHub](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86&style=for-the-badge)](https://github.com/sponsors/suryakantamangaraj)

*Every sponsor helps keep this list accurate, up-to-date, and free for everyone.*

</div>

## Credits

<div align="center">

Created and maintained by [Surya Raj](https://suryaraj.com).

Special thanks to every [contributor](https://github.com/suryakantamangaraj/AwesomeRISC-VResources/graphs/contributors) who has submitted a resource, reported a dead link, or improved the list — this project is yours as much as it is mine.

List structure inspired by [sindresorhus/awesome](https://github.com/sindresorhus/awesome).
RISC-V® is a registered trademark of [RISC-V International](https://riscv.org).

</div>

## License

<div align="center">

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Surya Raj](https://suryaraj.com) has waived all copyright and related or neighboring rights to this work.

*You are free to copy, modify, and distribute this list — no permission required.*

</div>