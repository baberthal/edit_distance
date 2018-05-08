# frozen_string_literal: true

source 'https://rubygems.org'

git_source(:github) { |repo_name| "https://github.com/#{repo_name}" }

# Specify your gem's dependencies in edit_distance.gemspec
gemspec

group :development, :test do
  gem 'rubocop', '>= 0.52', require: false
  gem 'rubocop-rspec', '>= 1.21',  require: false

  gem 'colorize', require: false # for pry prompt support

  gem 'pry', require: false
  gem 'pry-theme', require: false
end
