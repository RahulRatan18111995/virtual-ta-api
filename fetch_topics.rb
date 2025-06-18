require 'net/http'
require 'json'

url = URI("https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json")

response = Net::HTTP.get(url)
puts "Raw response:\n#{response}"  # Add this line for debugging

data = JSON.parse(response)

puts "\nParsed keys: #{data.keys}"  # See what keys are present

# Only proceed if "topic_list" is present
if data["topic_list"]
  data["topic_list"]["topics"].each do |topic|
    puts "#{topic['title']} => https://discourse.onlinedegree.iitm.ac.in/t/#{topic['slug']}/#{topic['id']}"
  end
else
  puts "No topic_list found in response!"
end
