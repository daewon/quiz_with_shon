def solv weight, list_of_items

end

gets.to_i.times do
  count, weight = gets.split.map &:to_i
  list_of_items = []
  count.times do
    name, *others = gets.split
    w, j = others.map &:to_i
    list_of_items << []
    p [name, w, j]
  end
  solv weight, list_of_items
  exit
end
