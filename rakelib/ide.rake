# frozen_string_literal: true

require 'pathname'
require_relative 'constants'

module IDE
  def self.db_path
    TMP_COMPILE_COMMANDS
  end

  def self.compile_commands
    @compile_commands ||= begin
      require 'json'
      JSON.parse(File.read(db_path))
    end
  end

  class CompilationDatabase
    def initialize(data)
      @data = data
    end
  end

  class CompileCommand
    attr_reader :file, :directory, :arguments

    def initialize(data)
      @file = Pathname.new(data['file'])
      @directory = Pathname.new(data['directory'])
      @arguments = data['arguments']
    end

    def absolute_file_path
      @absolute_file_path ||= file.expand_path(directory)
    end

    def include_flags; end

    def warning_flags
      @warning_flags ||= arguments.grep(/^-W/)
    end

  private

    def include_flag?(flag)
      flag.start_with? '-I', '-isystem'
    end

    def warning_flag?(flag)
      flag.start_with? '-W'
    end

    def feature_flag?(flag)
      flag.start_with? '-f'
    end

    def def_flag?(flag)
      flag.start_with? '-D', '-U'
    end
  end
end

namespace :ide do
  directory 'tmp'

  file TMP_COMPILE_COMMANDS => :compile
end
