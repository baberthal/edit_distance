# frozen_string_literal: true

require 'rake/extensiontask'
require_relative 'constants'

task build: :compile

Rake::ExtensionTask.new('edit_distance') do |ext|
  ext.lib_dir = 'lib/edit_distance'
end
