a = """hello-$
there-$
world$
"""

b = """a-$
-$
-$
b$"""

c = """i am ver-$
y sleepy arent-$
 you$"""

d = """jong-man rules$"""

e = """-"""

[a, b, c, d, e].each { |txt|
  head, *tail = txt.split(/\n|\$$/).reject &:empty?
  t = tail.inject([head]) { |acc, word|
    if acc.last[-1] == '-' and (acc.last[-2] || '').match(/^[[:alpha:]]$/) and word[0].match(/^[[:alpha:]]$/)
      acc[-1] = acc.last[0...acc.last.length-1] + word
    else
      acc << word
    end
    acc
  }
  t = t.map {|w| w.strip}.flatten
  t = txt.split(/\n/).join.gsub(/([a-z])[-]\$([a-z])/, '\1\2').gsub('-', '_-').split(/[-$]/).reject &:empty?
  p t.map{ |w| w.gsub('_', '-') }
  puts sprintf("%.3f", t.join.length.to_f / t.length)
}
