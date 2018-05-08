# frozen_string_literal: true

lib = File.expand_path('lib', __dir__)
$:.unshift(lib) unless $:.include?(lib)
require 'edit_distance/version'

Gem::Specification.new do |spec|
  spec.name          = 'edit_distance'
  spec.version       = EditDistance::VERSION
  spec.authors       = ['J. Morgan Lieberthal']
  spec.email         = ['j.morgan.lieberthal@gmail.com']

  spec.summary       = 'Calculate edit distance (levenshtein distance)'
  spec.homepage      = 'https://github.com/baberthal/ruby-edit_distance'
  spec.license       = 'MIT'

  spec.files = %x(git ls-files -z).split("\x0").reject do |f|
    f.match(%r{^(test|spec|features)/})
  end
  spec.bindir        = 'exe'
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ['lib']
  spec.extensions    = ['ext/edit_distance/extconf.rb']

  spec.add_development_dependency 'bundler', '~> 1.16'
  spec.add_development_dependency 'rake', '~> 10.0'
  spec.add_development_dependency 'rake-compiler'
  spec.add_development_dependency 'rspec', '~> 3.0'
end
