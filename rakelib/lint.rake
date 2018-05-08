# frozen_string_literal: true

require 'rubocop/rake_task'

RuboCop::RakeTask.new(:rubocop) do |task|
  task.patterns = %w[lib/**/*.rb spec/**/*.rb]
  task.formatters = ['files']
  task.fail_on_error = true
end

desc 'Run linters and static analysis tools'
task lint: [:rubocop]
