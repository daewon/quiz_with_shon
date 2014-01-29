is_palendrome = -> word { word.reverse == word }
delete_index = -> word, i { next_word = word.dup; next_word[i] = ""; next_word }

word = catch :found do
  k_palendrome = -> word, cnt do
    return word if is_palendrome.call word
    return false if cnt == -1

    (0..word.length).each { |i|
      next_word = delete_index.call word, i
      t = k_palendrome.call next_word, cnt - 1
      throw :found, next_word if t and cnt == 1
    }

    return false
  end
  k_palendrome.call "abaxbabax", 2
end

p word
