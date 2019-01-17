#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=40
#SBATCH --time=02:00:00     
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=slurmnotifs@gmail.com
#SBATCH --account=rrg-maassenj
#SBATCH --job-name=Bi2Se3_bulk_scf


module load CCEnv
module load StdEnv
module load nixpkgs/16.09
module load intel/2016.4
module load openmpi/2.1.1
module load quantumespresso/6.0 

srun pw.x < scf.in > scf.out

