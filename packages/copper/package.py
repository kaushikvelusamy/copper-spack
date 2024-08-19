from spack.package import *

class Copper(CMakePackage):
    """Copper: Cooperative Caching Layer for Scalable Data Loading in Exascale Supercomputers"""

    # Replace this with the actual URL to download your source code
    homepage = "https://github.com/argonne-lcf/copper"
    url      = "https://github.com/argonne-lcf/copper.git"
    
    maintainers("kaushikvelusamy", "kevin-harms")

    # Add versions of your software here
    version("main", branch="main")

    # Add the dependencies your software requires
    depends_on('pkgconfig')
    depends_on('fuse@3')
    depends_on('mercury')
    depends_on('cereal')
    depends_on('mochi-margo')
    depends_on('mochi-thallium')

    variant("block_redundant_rpcs", default=ON, description="On off block_redundant_rpcs ")

    def cmake_args(self):
        from_variant = self.define_from_variant
        args = []
        args.append('-DCMAKE_BUILD_TYPE = Release')
        args.append(from_variant("BLOCK_REDUNDANT_RPCS", "block_redundant_rpcs"))
        args.append('-DCMAKE_VERBOSE_MAKEFILE = ON')
        args.append('-DCMAKE_EXPORT_COMPILE_COMMANDS = ON')
        args.append('-DFUSE3_LIB = self.spec['fuse'].prefix.lib')
        args.append('-DFUSE3_INCLUDE = self.spec['fuse'].prefix.include')
        return args
