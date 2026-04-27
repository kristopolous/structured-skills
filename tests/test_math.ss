# Math test script
$total = 0
$numbers = []
for each $file in %list_files tests/data_math:
    $val = %read $file
    %append $numbers $val
end

$sum = %sum $numbers
$message = infer the total sum of $numbers is $sum
%write tests/math_result.txt $message
