# frozen_string_literal: true

require 'edit_distance/version'
require 'edit_distance/edit_distance'

module EditDistance
module_function

  def compute_edit_distance(str1, str2, **options)
    allow_replacements = options.fetch(:allow_replacements, true)
    max_edit_distance  = options.fetch(:max_edit_distance, 0)
    _compute_edit_distance(str1, str2, allow_replacements, max_edit_distance)
  end
end
