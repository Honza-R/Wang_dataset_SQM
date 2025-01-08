Wang 2015 dataset - pool of poses, SQM scoring
==============================================

Additional poses and SQM scoring results for the Wang 2015 dataset of protein-ligand complexes

General information
-------------------

There are two complete set of modeled structures of the P-L complexes of the Wang 2015 dataset [1], published by Zariquiey et al [2] and Ross et al [3]. 
The data set consists of 8 target proteins, each with a series of ligands. Each target contains a single protein structure and multiple ligands poses. 
The poses of the Zariquiey set are expanded by adding pool of poses obtainned by manual modifications and tamplate-based docking. 

| Target   | Ligands | Protein                                    |
|----------|---------|--------------------------------------------|
| BACE     | 36      | 4DJX (for Zariquiey) & 4DJW (for Ross set) |
| CDK2     | 16      | 1H1Q                                       |
| JNK1     | 21      | 2GMX                                       |
| MLC1     | 42      | 4HW3                                       |
| p38      | 34      | 3FLY                                       |
| PTP1B    | 23      | 2QBS                                       |
| thrombin | 11      | 2ZFF                                       |
| Tyk2     | 16      | 4GIH                                       |


Repository structure
--------------------

Two top-level directories contain data for derived from the original set of structures published by Zariquiey and Ross. 
Each directory contains 8 subdirectories named by the protein target. Individual P-L complexes identified by ligand names.

The experimental binding free energies are available in the `experimental_dG.txt` files.
All the SQM2.20' scores are  available in the `SQM2.20_all_poses.txt` files.
The selected SQM2.20' score of the best pose, i.e. pose with ithe lowest SQM energy, are summarized in `SQM2.20_selected_poses.txt` files.
The SQM energies of the optimized complexes are available in the `SQM_energies.txt` files.

The structure of the whole protein target prepared for docking is available as `proteined_anealed.pdb` in the subdirectory `protein`.

The structures of the optimized P-L complexes are stored in the subdirectory `structures` of each protein target. Each ligand pose has its own subdirectory containing: 
- `ligand.sdf` - The geometry of the ligand in the optimized complex. 
- `receptor.pdb` - Model of the active site used in the complex.
The `ligand.sdf` and `receptor.pdb` represent the geometry on which the SQM2.20 score was calculated. Additionally, the optimized active site has been ported back into the structure of the whole protein and is provided as `protein.pdb`.

The ligand poses of the expanded set of Zariquiey structures are named accordingly:
- The original pose derived from Zariquiey et al [2] are denoted as `[ligand name]_pose_orig`.
- The manually modified poses are denoted as `[ligand name]_pose_manual`.
- The first docking pose is named just as `[ligand name]` and the other docking poses are named `[ligand name]_pose_[number]`.

Scores obtained with standard scoring functions are available in the `scores` subdirectory.

References
----------
1) Wang, L.; Wu, Y.; Deng, Y.; Kim, B.; Pierce, L.; Krilov, G.; Lupyan, D.; Robinson, S.; Dahlgren, M. K.; Greenwood, J.; Romero, D. L.; Masse, C.; Knight, J. L.; Steinbrecher, T.; Beuming, T.; Damm, W.; Harder, E.; Sherman, W.; Brewer, M.; Wester, R.; Murcko, M.; Frye, L.; Farid, R.; Lin, T.; Mobley, D. L.; Jorgensen, W. L.; Berne, B. J.; Friesner, R. A.; Abel, R. Accurate and Reliable Prediction of Relative Binding Potency in Prospective Drug Discovery by Way of a Modern Free-Energy Calculation Protocol and Force Field. J. Am. Chem Soc. 2015, 137, 2695–2703.(https://pubs.acs.org/doi/10.1021/ja512751q)

2) Zariquiey, F. S.; Perez, A.; Majewski, M.; Gallicchio, E.; De Fabritiis, G. Validation of the Alchemical Transfer Method for the Estimation of Relative Binding Affinities of Molecular Series. J. Chem. Inf. Model. 2023, 63, 2438–2444.(https://pubs.acs.org/doi/10.1021/acs.jcim.3c00178)

3) Ross, G. A.; Lu, C.; Scarabelli, G.; Albanese, S. K.; Houang, E.; Abel, R.; Harder, E. D.; Wang, L. The maximal and current accuracy of rigorous protein-ligand binding free energy calculations. Commun. Chem. 2023, 6, 222.
