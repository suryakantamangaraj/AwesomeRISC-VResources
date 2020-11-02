<h1 align="center">Awesome RISC-V Resources</h1>
<div align="center">
<img src="https://awesome.re/badge.svg" alt="Awesome Badge"/>
<img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
<a href="https://github.com/suryakantamangaraj/AwesomeRISC-VResources/blob/master/LICENSE"><img src="https://img.shields.io/github/license/suryakantamangaraj/AwesomeRISC-VResources?color=brightgreen" alt="License Badge"/></a>
</a><br>

<i>A curated list of awesome RISC-V resources</i>

<i>Hopefully this repo can serve as a source of inspiration for your RISC-V related projects!</i>

<a href="https://github.com/suryakantamangaraj/AwesomeRISC-VResources/stargazers"><img src="https://img.shields.io/github/stars/suryakantamangaraj/AwesomeRISC-VResources" alt="Stars Badge"/></a>
<a href="https://github.com/suryakantamangaraj/AwesomeRISC-VResources/pulls"><img src="https://img.shields.io/github/issues-pr/suryakantamangaraj/AwesomeRISC-VResources" alt="Pull Requests Badge"/></a>
<a href="https://github.com/suryakantamangaraj/AwesomeRISC-VResources/issues"><img src="https://img.shields.io/github/issues/suryakantamangaraj/AwesomeRISC-VResources" alt="Issues Badge"/></a>
<a href="https://github.com/suryakantamangaraj/AwesomeRISC-VResources/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/suryakantamangaraj/AwesomeRISC-VResources?color=2b9348"></a>

<i>Loved the project? Please support it to improve!</i>

</div>

#

### Contents

- [Open Source Implementations](#open-source-implementations)
  - [Cores](#cores)
  - [SoCs](#socs)
  - [Deprecated](#deprecated)
- [Open Source Toolchains](#open-source-toolchains)
  - [HDLs](#hdls)
  - [Simulators/Emulators](#simulatorsemulators)
  - [Design Environment](#design-environment)
  - [Verification and Testing Environment](#verification-and-testing-environment)
  - [Uncategorized](#uncategorized)
- [Technical Resources](#technical-resources)
  - [Books](#books)
  - [Videos](#videos)
  - [Courses](#courses)
  - [Articles](#articles)
  - [Uncategorized](#uncategorized-1)
- [Social Media](#social-media)
  - [Forums](#forums)
  - [Google Groups](#google-groups)
  - [Reddit](#reddit)
  - [Telegram](#telegram)
- [Contribute](#contribute)
- [License](#license)

## Open Source Implementations

A curated list of awesome RISC-V open source implementations which will inspire you to make yours.

### Cores

- [riscv-boom](https://github.com/riscv-boom/riscv-boom) - The Berkeley Out-of-Order RISC-V Processor
- [Shakti C-Class](https://gitlab.com/shaktiproject/cores/c-class) - Shakti C-Class Core
- [Shakti E-Class](https://gitlab.com/shaktiproject/cores/e-class) - Shakti E-Class Core
- [CVA6](https://github.com/openhwgroup/cva6) - CVA6 RISC-V CPU
- [CV32E40P](https://github.com/openhwgroup/cv32e40p) - OpenHW Group CORE-V CV32E40P RISC-V IP
- [FWRISC](https://github.com/mballance/fwrisc) - a Featherweight RISC-V implementation
- [FWRISC-S](https://github.com/mballance/fwrisc-s)
- [Ibex](https://github.com/lowRISC/ibex) - Ibex RISC-V Core
- [Minerva](https://github.com/lambdaconcept/minerva) - a 32-bit RISC-V soft processor
- [PicoRV32](https://github.com/cliffordwolf/picorv32) - a Size-Optimized RISC-V CPU
- [riscv-mini](https://github.com/ucb-bar/riscv-mini)
- [Rocket](https://github.com/chipsalliance/rocket-chip) - Rocket Chip Generator 🚀
- [SERV](https://github.com/olofk/serv) - SERV is an award-winning bit-serial RISC-V core
- [SweRV](https://github.com/chipsalliance/Cores-SweRV) - EH1 SweRV RISC-V CoreTM 1.8 from Western Digital
- [VexRiscv](https://github.com/SpinalHDL/VexRiscv)
- [SSRV](https://github.com/risclite/SuperScalar-RISCV-CPU) - SuperScalar-RISCV-CPU
- [Leros](https://github.com/leros-dev/leros) - a Tiny Processor Core
- [patmos](https://github.com/t-crest/patmos) - a time-predictable VLIW processor
- [lipsi](https://github.com/schoeberl/lipsi) - Lipsi: Probably the Smallest Processor in the World
- [DANA](https://github.com/bu-icsg/dana) - Dynamically Allocated Neural Network (DANA) Accelerator
- [Sodor](https://github.com/ucb-bar/riscv-sodor)
- [Taiga](https://gitlab.com/sfu-rcl/Taiga) - Taiga is a 32-bit RISC-V processor 
- [Reindeer](https://github.com/PulseRain/Reindeer) - PulseRain Reindeer - RISCV RV32I[M] Soft CPU
- [Rattlesnake](https://github.com/PulseRain/Rattlesnake) - RISC-V RV32IMC Soft CPU, with a Security-Hardened Processor Core
- [RISCV-FS](https://github.com/mrLSD/riscv-fs) - RISC-V formal ISA Specification
- [RISCV-CLaSH](https://github.com/adamwalker/clash-riscv) - A RiscV processor implementing the RV32I instruction set written in clash
- [Sail RISC-V](https://github.com/rems-project/sail-riscv) - RISCV Sail Model
- [FlexPRET](https://github.com/pretis/flexpret) - a 5-stage, fine-grained multithreaded RISC-V* processor

### SoCs

- [Shakti SoC](https://gitlab.com/shaktiproject/cores/shakti-soc)


### Deprecated

- [zscale](https://github.com/ucb-bar/zscale)
- [Ariane](https://github.com/pulp-platform/ariane)
- [SweRV from WD](https://github.com/westerndigitalcorporation/swerv_eh1_fpga) - FPGA Reference Design for the SweRV RISC-V CoreTM from Western Digital

## Open Source Toolchains

### HDLs

- [CHISEL](https://github.com/freechipsproject/chisel3)

### Simulators/Emulators

- [Spike](https://github.com/riscv/riscv-isa-sim/) - RISC-V ISA Simulator
- [Verilator](https://github.com/verilator/verilator) - The fastest Verilog/SystemVerilog simulator.
- [Dromajo](https://github.com/chipsalliance/dromajo) - Esperanto Technology's RISC-V Reference Model
- [TLBSim](https://github.com/nbdd0121/TLBSim) - Fast TLB simulator for RISC-V systems
- [Ripes](https://github.com/mortbopet/Ripes) - a visual computer architecture simulator and assembly code editor
- [FireSim](https://github.com/firesim/firesim) - Easy-to-use, Scalable, FPGA-accelerated Cycle-accurate Hardware Simulation
- [FireSim-NVDLA](https://github.com/CSL-KU/firesim-nvdla) - full-system simulator integrated with NVIDIA Deep Learning Accelerator (NVDLA)
- [SweRV ISS](https://github.com/westerndigitalcorporation/swerv-ISS)
- [GAP8 SDK](https://github.com/GreenWaves-Technologies/gap_sdk)
- [Shakti SDK](https://gitlab.com/shaktiproject/software/shakti-sdk)
- [FuseSoC](https://github.com/olofk/fusesoc) - FuseSoC is an award-winning package manager and a set of build tools for HDL 
- [riscv-VM](https://github.com/openhwgroup/riscv_vm) - OpenHW Group's RISC-V Virtual Machine
- [TinyEMU](https://bellard.org/tinyemu/) - a system emulator for the RISC-V and x86 architectures
- [RARS](https://github.com/TheThirdOne/rars) - RISC-V Assembler and Runtime Simulator

### Design Environment

- [RISC-V LINUX](https://github.com/westerndigitalcorporation/RISC-V-Linux/) - Build Fedora Gnome Desktop on RISC-V!!
- [Treadle](https://github.com/freechipsproject/treadle) - A Chisel/Firrtl Execution Engine
- [Chipyard](https://github.com/ucb-bar/chipyard) - framework for agile development of Chisel-based systems-on-chip
- [Firrtl](https://github.com/freechipsproject/firrtl) - Flexible Internal Representation for RTL
- [RISC-V GNU Toolchain](https://github.com/riscv/riscv-gnu-toolchain) - RISC-V GNU Compiler Toolchain

### Verification and Testing Environment

- [RISC-V Tests](https://github.com/riscv/riscv-tests) - unit tests for RISC-V processors
- [CHISEL Tester](https://github.com/freechipsproject/chisel-testers)
- [RISC-V Torture](https://github.com/ucb-bar/riscv-torture) - RISC-V Torture Test Generator
- [RISC-V Formal](https://github.com/SymbioticEDA/riscv-formal) - RISC-V Formal Verification Framework
- [BOOM Attacks](https://github.com/riscv-boom/boom-attacks) - BOOM Speculative Attacks
- [Axe](https://github.com/CTSRD-CHERI/axe) - automatic black box testing

### Uncategorized

- [WebRISC-V](https://github.com/Mariotti94/WebRISC-V) - a web-based graphical pipelined datapath simulation environment built for the RISC-V
- [BRSIC-V](https://ascslab.org/research/briscv/explorer/explorer.html)

## Technical Resources

### Books

- [Digital Design with Chisel](https://github.com/schoeberl/chisel-book) or, [PDF](https://raw.githubusercontent.com/wiki/schoeberl/chisel-book/chisel-book.pdf)

### Videos

- [RISC-V ASM Tutorial Collection](https://www.youtube.com/watch?v=KLybwrpfQ3I&list=PL6noQ0vZDAdh_aGvqKvxd0brXImHXMuLY&ab_channel=WesternDigitalCorporation) - by Western Digital Corporation
- [R32V2020 32-Bit RISC CPU Design](https://www.youtube.com/playlist?list=PLn__0BqzWEWPIsUE0TUdsspej2vHV-osY)
- [Looking into Hello World on RISC-V by Dennis Clarke](https://www.twitch.tv/tsoding/video/498698691)
- [RISC-V Workshop Zurich](https://www.youtube.com/playlist?list=PL85jopFZCnbMcS3bdzdd7AdLop5DtEOWB)

### Courses

- [VLSI Systems Design](https://www-inst.eecs.berkeley.edu//~cs250/sp17/) - by UC Berkely
- [Computer Organization - Fall 2019](https://ascslab.org/courses/ec413/lectures.html) - by Boston University
- [Computer Architecture, Summer 2017](https://passlab.github.io/CSE564/) - by Oakland University
- [Organization of Digital Computers Laboratory](https://canvas.eee.uci.edu/courses/7673/assignments/syllabus) - by UC Irvine
- [Complex Digital Systems](http://csg.csail.mit.edu/6.375/6_375_2016_www/handouts.html) - by MIT
- [Computer Architecture - Spring 2018](https://ascslab.org/courses/ec513/index.html) - by Boston University
- [Debugging & Verifying Programs](https://www.cs.utexas.edu/users/hunt/class/2019-spring/cs340d/cs340d.html) - by University of Texas
- [Computer Organization II](https://www.cs.fsu.edu/~zwang/cda3101.html) - by Florida State University
- [RISC-V ISA using Chisel](http://pages.cs.wisc.edu/~karu/courses/cs752/fall2016/wiki/index.php?n=Main.Project) - by University of Wisconsin–Madison

### Articles

- [Making a real processor step by step using RISC-V ISA](https://dl.acm.org/doi/10.1145/3210713.3210741)
- [Sail](https://www.cl.cam.ac.uk/~pes20/sail/)
- [RISC-V RV32I assembly with Ripes simulator](https://dantalion.nl/en/risc-v-rv32i-assembly-with-ripes-simulator/)
- [2019 : A year of RISC-V and Open source silicon](https://www.linkedin.com/pulse/2019-year-risc-v-open-source-silicon-olof-kindgren/)
- [Research](https://www.ocf.berkeley.edu/~qmn/research.html)
- [RISC-V Bases and Extensions Explained](https://www.cnx-software.com/2019/08/27/risc-v-bases-and-extensions-explained/)

### Uncategorized

- [Linux on RISC-V](https://riscv.ics.forth.gr/doku.php/developers/getting_started)
- [RISC-V](https://wiki.debian.org/RISC-V)
- [Intensivate's Learning Journey for Chisel](https://github.com/Intensivate/learning-journey/wiki)
- [CHISEL Bootcamp](https://github.com/freechipsproject/chisel-bootcamp)
- [Notes for Rocket-Chip](https://github.com/cnrv/rocket-chip-read)
- [Chipyard](https://chipyard.readthedocs.io/en/latest/)
- [CHISEL Cheatsheet](https://github.com/freechipsproject/chisel-cheatsheet)
- [FTPVL](https://github.com/TypingKoala/FPGA-Tool-Performance-Visualization-Library) - FPGA Tool Performance Visualization Library
- [RISC-V Notes](https://github.com/cnrv/riscv-notes)
- [Tutorial on RISC-V Design and Verification](http://events.dvcon.org/Europe/2018/proceedings/slides/07T.pdf)
- [Advanced Examples of Using Chisel](https://github.com/librecores/riscv-sodor/wiki/Advanced-Examples-of-Using-Chisel)
- [Chisel – Accelerating Hardware Design](https://riscv.org/wp-content/uploads/2015/01/riscv-chisel-tutorial-bootcamp-jan2015.pdf)
- [Cookbook](https://github.com/freechipsproject/chisel3/wiki/Cookbook)
- [Introduction to Chisel for Biginners](https://github.com/IAMAl/How2Start_Chisel3)
- [RISC-V BOOM](https://github.com/ccelio/riscv-boom-doc)
- [Ripes Wiki](https://github.com/mortbopet/Ripes/wiki/Ripes-Introduction)
- [Open SoC Fabric](http://www.opensocfabric.org/home.php)
- [UVM](https://github.com/SymbiFlow/uvm)

## Social Media

### Forums

- [RISC-V official forum](https://riscv.org/technical/technical-forums/)
- [OSDForum](https://www.osdforum.org/)

### Google Groups

- [RISC-V HW Dev](https://groups.google.com/a/groups.riscv.org/g/hw-dev?pli=1)
- [RISC-V Teach](https://groups.google.com/a/groups.riscv.org/g/riscv-teach)
- [RISC-V ISA Dev](https://groups.google.com/a/groups.riscv.org/g/isa-dev)
- [Chisel Users](https://groups.google.com/g/chisel-users)

### Reddit

- [RISC-V](https://www.reddit.com/r/RISCV/)

### Telegram

- [RISC-V](https://t.me/riscv)

## Contribute

Contributions are welcome!
Please read the [contribution guidelines](Contributing.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Surya Raj](https://suryaraj.me) has waived all copyright and related or neighboring rights to this work.



