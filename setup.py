#****************************************************************************************/
#*  Copyright (c) Letshavealook. All rights are reserved.                            */
#*  Reproduction in whole or in part is prohibited without the prior                    */
#*  written consent of the copyright owner.                                             */
#*                                                                                      */
#*  This software and any compilation or derivative thereof is and                      */
#*  shall remain the proprietary information of Letshavealook and is                    */
#*  not highly confidential in nature.                                                      */
#****************************************************************************************/
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="ecarton_code_challenge",
    version="0.0.1",
    author="Evert Carton",
    author_email="evert@letshavealook.info",
    description="Engie Code Challenge",
    url="https://https://github.com/evert2410/engie",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['ecarton_code_challenge=ecarton_code_challenge.scripts.main:main',
                           ]
    }
)

