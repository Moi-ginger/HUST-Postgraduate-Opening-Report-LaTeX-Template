# frozen_string_literal: true

# Convert the two review-ready Markdown manuscripts into the LaTeX chapter files
# used by main.tex. Reference-list links are mapped to the shared BibLaTeX keys.

URL_TO_BIB = {
  'https://arxiv.org/abs/2210.03629' => 'yao2023react',
  'https://doi.org/10.1207/s15327051hci0304_2' => 'ref15',
  'https://doi.org/10.1109/TSE.2006.116' => 'ref14',
  'https://doi.org/10.1080/00140137408931355' => 'ref09',
  'https://doi.org/10.1109/TSE.2010.47' => 'ref33',
  'https://doi.org/10.1145/985692.985712' => 'ref06',
  'https://doi.org/10.1145/1368088.1368130' => 'ref05',
  'https://doi.org/10.1145/3487065' => 'ref04',
  'https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework' => 'ref30',
  'https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/' => 'ref32',
  'https://doi.org/10.1145/2815400.2815415' => 'ref31',
  'https://doi.org/10.1109/TVCG.2015.2467551' => 'ref36',
  'https://doi.org/10.1109/VAST.2009.5333020' => 'ref38',
  'https://doi.org/10.1109/MCG.2015.50' => 'ref37',
  'https://doi.org/10.1109/TVCG.2015.2467591' => 'ref39',
  'https://doi.org/10.1109/TVCG.2019.2934287' => 'ref40',
  'https://doi.org/10.1145/3706598.3713581' => 'ref02',
  'https://doi.org/10.1145/3772318.3791069' => 'ref01',
  'https://doi.org/10.1145/2362364.2362371' => 'hook2012strong',
  'https://doi.org/10.1109/TSE.2010.111' => 'ref08',
  'https://doi.org/10.1016/j.ijhcs.2007.07.005' => 'ref34',
  'https://doi.org/10.1145/2001420.2001445' => 'ref35',
  'https://doi.org/10.1109/TVCG.2024.3394053' => 'ref22',
  'https://doi.org/10.18653/v1/2024.emnlp-demo.8' => 'ref25',
  'https://arxiv.org/abs/2602.06593' => 'ref18',
  'https://proceedings.mlr.press/v267/zhang25cq.html' => 'ref03',
  'https://arxiv.org/abs/2606.06324v2' => 'ref20',
  'https://doi.org/10.1016/j.artint.2018.07.007' => 'ref47',
  'https://doi.org/10.1145/3313831.3376590' => 'ref49',
  'https://doi.org/10.1145/3290605.3300233' => 'ref48',
  'https://doi.org/10.1145/3290605.3300831' => 'ref53',
  'https://doi.org/10.1145/3173574.3174156' => 'ref52',
  'https://doi.org/10.1145/3313831.3376219' => 'ref50',
  'https://doi.org/10.1145/3449287' => 'ref55',
  'https://doi.org/10.18653/v1/2024.emnlp-main.1084' => 'ref56',
  'https://doi.org/10.1145/3411764.3445188' => 'ref51',
  'https://doi.org/10.1109/MIS.2006.100' => 'ref11',
  'https://doi.org/10.1109/MIS.2006.88' => 'ref10',
  'https://doi.org/10.1017/CBO9780511612062.006' => 'ref12',
  'https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf' => 'ref17',
  'https://doi.org/10.1145/1240624.1240704' => 'zimmerman2007rtd',
  'https://doi.org/10.1109/TVCG.2012.213' => 'sedlmair2012design',
  'https://doi.org/10.1109/TVCG.2019.2934539' => 'meyer2020rigor',
  'https://doi.org/10.1177/1049732315617444' => 'malterud2016information',
  'https://doi.org/10.1186/1471-2288-13-117' => 'gale2013framework',
  'https://doi.org/10.1145/1518701.1518942' => 'ref07',
  'https://doi.org/10.1145/3613904.3642016' => 'arawjo2024chainforge',
  'https://arxiv.org/abs/2503.13657' => 'cemri2025mast',
  'https://doi.org/10.1145/3637396' => 'ref54'
}.freeze

def escape_text(text)
  citations = []
  text = text.gsub(/\[(\d+)\]\((https?:\/\/[^)]+)\)/) do
    url = Regexp.last_match(2)
    key = URL_TO_BIB.fetch(url) { raise "No BibLaTeX key for #{url}" }
    token = "@@CITE#{citations.length}@@"
    citations << [token, "\\cite{#{key}}"]
    token
  end

  text = text.gsub('\\', '\\\\')
  text = text.gsub(/([%&#_])/, '\\\\\1')
  text = text.gsub(/\*\*(.+?)\*\*/, '\\textbf{\1}')
  citations.each { |token, citation| text = text.gsub(token, citation) }
  text
end

def table_to_tex(lines)
  rows = lines.map { |line| line.strip.sub(/^\|/, '').sub(/\|$/, '').split('|').map(&:strip) }
  rows.delete_at(1) if rows[1]&.all? { |cell| cell.match?(/^:?-{3,}:?$/) }
  columns = rows.first.length
  spec = case columns
         when 2 then 'p{0.24\\textwidth} Y'
         when 3 then 'p{0.18\\textwidth} p{0.37\\textwidth} Y'
         when 4 then 'p{0.15\\textwidth} p{0.25\\textwidth} p{0.25\\textwidth} Y'
         else Array.new(columns, 'Y').join(' ')
         end
  rendered = [
    '\\begin{table}[H]',
    '  \\centering',
    '  \\small',
    "  \\begin{tabularx}{\\textwidth}{#{spec}}",
    '    \\toprule',
    "    #{rows.first.map { |cell| escape_text(cell) }.join(' & ')} \\\\",
    '    \\midrule'
  ]
  rows.drop(1).each do |row|
    rendered << "    #{row.map { |cell| escape_text(cell) }.join(' & ')} \\\\"
  end
  rendered.concat(['    \\bottomrule', '  \\end{tabularx}', '\\end{table}'])
  rendered
end

def heading_text(text)
  text.sub(/^[一二三四五六七八九十]+、/, '').sub(/^\d+\.\d+\s*/, '')
end

def convert(source, target, chapter_title, chapter_label, literature: false)
  lines = File.readlines(source, chomp: true)
  reference_index = lines.index { |line| line == '## 参考文献' }
  lines = lines[0...reference_index] if reference_index

  output = ["\\chapter{#{chapter_title}}\\label{#{chapter_label}}", '']
  list_open = false
  i = 0
  while i < lines.length
    line = lines[i]
    i += 1

    next if line.start_with?('# ')
    next if literature && line.start_with?('## ')

    if line.start_with?('|') && i < lines.length && lines[i].strip.match?(/^\|?\s*:?-{3,}/)
      table_lines = [line]
      while i < lines.length && lines[i].start_with?('|')
        table_lines << lines[i]
        i += 1
      end
      output.concat(table_to_tex(table_lines))
      output << ''
      next
    end

    if (match = line.match(/^(\d+)\.\s+(.+)$/))
      unless list_open
        output << '\\begin{enumerate}'
        list_open = true
      end
      output << "  \\item #{escape_text(match[2])}"
      next
    elsif list_open
      output << '\\end{enumerate}'
      output << ''
      list_open = false
    end

    case line
    when /^##\s+(.+)$/
      output << "\\section{#{escape_text(heading_text(Regexp.last_match(1)))}}"
      output << ''
    when /^###\s+(.+)$/
      command = literature ? 'section' : 'subsection'
      output << "\\#{command}{#{escape_text(heading_text(Regexp.last_match(1)))}}"
      output << ''
    when /^####\s+(.+)$/
      command = literature ? 'subsection' : 'subsubsection'
      output << "\\#{command}{#{escape_text(heading_text(Regexp.last_match(1)))}}"
      output << ''
    when ''
      output << '' unless output.last == ''
    else
      output << escape_text(line)
      output << ''
    end
  end
  output << '\\end{enumerate}' if list_open

  File.write(target, output.join("\n").gsub(/\n{3,}/, "\n\n") + "\n")
end

convert('literature-review.md', 'body/literature-review.tex', '文献综述', 'chap:literature-review', literature: true)
convert('selection-report.md', 'body/selection-report.tex', '选题报告', 'chap:selection-report')
