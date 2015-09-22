from os.path import dirname
from django.conf import settings

from pipeline.compilers import SubProcessCompiler


class SasscCompiler(SubProcessCompiler):
    output_extension = 'css'
    command_debug_args = '-m -l -t nested'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        self._compile_file_sassc(infile, outfile)

    def _compile_file_sassc(self, infile, outfile):
        command = "{sassc} {options} {input} {output}".format(
            sassc=getattr(settings, 'PIPELINE_SASSC_BINARY', 'sassc'),
            options=self.get_command_args(),
            input=infile,
            output=outfile,
        )
        return self.execute_command(command, cwd=dirname(infile))

    def get_command_args(self):
        options = []
        if settings.DEBUG:
            options.append(self.command_debug_args)
        options.append(
            getattr(settings, 'PIPELINE_SASSC_ARGUMENTS', '').strip())
        return ' '.join(options)
