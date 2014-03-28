map = {
  '%20' => " ",
  '%21' => "!",
  '%24' => "$",
  '%25' => "%",
  '%28' => "(",
  '%29' => ")",
  '%2a' => "*"
}

t = gets.to_i
for i in (0...t)
  str = gets.to_s.strip
  i = 0
  acc = []
  while i < str.length
    if str[i] == '%' && str[i+1] && str[i+2]
      acc << map["#{str[i]}#{str[i+1]}#{str[i+2]}"]
      i += 3
    else
      acc << str[i]
      i += 1
    end
  end
  print("#{acc.join}\n")
end
