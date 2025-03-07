from nomad.config.models.plugins import SchemaPackageEntryPoint


class BeamlinePackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_hzb_beamlines.schema_packages.beamline_package import m_package

        return m_package


beamline_package_entry_point = BeamlinePackageEntryPoint(
    name='Beamline package',
    description='Package for HZB beamlines.',
)
