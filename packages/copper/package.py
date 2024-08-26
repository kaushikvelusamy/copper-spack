import os

from spack.package import *

class Copper(CMakePackage):
    """Copper: Cooperative Caching Layer for Scalable Data Loading in Exascale Supercomputers"""

    # Replace this with the actual URL to download your source code
    homepage = "https://github.com/argonne-lcf/copper"
    url      = "https://github.com/argonne-lcf/copper.git"
    git      = "https://github.com/argonne-lcf/copper.git"
    
    maintainers("kaushikvelusamy", "kevin-harms")

    # Add versions of your software here
    version("main", branch="main")

    # Add the dependencies your software requires
    depends_on('pkgconfig')
    depends_on('fuse@3')
    depends_on('mercury@2.3:')
    depends_on('cereal@1.3:')
    depends_on('mochi-margo@0.15:')
    depends_on('mochi-thallium@0.11:')
    depends_on('mpi')
    variant("block_redundant_rpcs", default=True, description="On off block_redundant_rpcs ")

    def cmake_args(self):
        args = []

        # hardcoded flags
        args.extend([
            self.define('CMAKE_VERBOSE_MAKEFILE', True),
            self.define('CMAKE_EXPORT_COMPILE_COMMANDS', True),
        ])

        # from variants
        args.extend([
            self.define_from_variant("BLOCK_REDUNDANT_RPCS", "block_redundant_rpcs"),
        ])

        return args
