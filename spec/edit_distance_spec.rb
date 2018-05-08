# frozen_string_literal: true

# rubocop:disable Metrics/BlockLength

RSpec.describe EditDistance do
  it 'has a version number' do
    expect(EditDistance::VERSION).not_to be nil
  end

  describe '#compute_edit_distance' do
    before do
      allow(described_class).to receive(:_compute_edit_distance)
        .and_call_original
    end

    let(:options) { {} }

    shared_examples 'properly computes edit distance' do
      [
        ['hello', 'heloo', 1],
        ['blah', 'blorg', 3]
      ].each do |arr|
        str1, str2, expected_distance = arr
        it "computes edit distance from '#{str1}' to '#{str2}'" do
          distance = described_class.compute_edit_distance(str1, str2, **options)
          expect(distance).to eq expected_distance
        end
      end
    end

    it_behaves_like 'properly computes edit distance'

    context 'when called without options' do
      let(:options) { {} }

      it 'calls the native method with the correct arguments' do
        described_class.compute_edit_distance('hello', 'heloo', **options)
        expect(described_class).to have_received(:_compute_edit_distance).with(
          'hello', 'heloo', true, 0
        )
      end

      it_behaves_like 'properly computes edit distance'
    end

    context 'when called with options[:allow_replacements]' do
      let(:options) { { allow_replacements: false } }

      it 'calls the native method with the correct arguments' do
        described_class.compute_edit_distance('hello', 'heloo', **options)
        expect(described_class).to have_received(:_compute_edit_distance).with(
          'hello', 'heloo', false, 0
        )
      end

      it 'properly computes the edit distance, without allowing replacements' do
        [['hello', 'heloo', 2], ['blah', 'blorg', 5]].each do |arr|
          str1, str2, expected_distance = arr
          distance = described_class.compute_edit_distance(str1, str2, **options)
          expect(distance).to eq expected_distance
        end
      end
    end

    context 'when called with options[:max_edit_distance]' do
      let(:str1) { 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr' }
      let(:str2) { 'this is a very long string that is not good' }
      let(:options) { { max_edit_distance: 12 } }

      it 'calls the native method with the correct arguments' do
        described_class.compute_edit_distance('hello', 'heloo', **options)
        expect(described_class).to have_received(:_compute_edit_distance).with(
          'hello', 'heloo', true, 12
        )
      end

      it_behaves_like 'properly computes edit distance'

      it 'returns max_edit_distance + 1 when result is greater' do
        opts = options
        opts[:allow_replacements] = false
        distance = described_class.compute_edit_distance(str1, str2, **opts)
        expect(distance).to eq 13
      end
    end
  end
end

# rubocop:enable Metrics/BlockLength
