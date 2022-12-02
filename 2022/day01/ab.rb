numbers = STDIN.read.split("\n\n").map{ |x| x.split("\n").map{|x| x.to_i}.sum }.sort

puts "a: #{numbers.last}"
puts "b: #{numbers.last(3).sum}"