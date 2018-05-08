# frozen_string_literal: true

TMP_COMPILE_COMMANDS = 'tmp/compile_commands.json'
TMP_COMPDB = File.expand_path("../#{TMP_COMPILE_COMMANDS}", __dir__).freeze

ENV['MAKE'] = "bear -o #{TMP_COMPDB} make"
