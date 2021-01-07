card_public = 10212254
door_public = 12577395
subject = 7

val = 1
loop_count = 0
while val != card_public:
    val = (val*subject) % 20201227
    loop_count += 1

print("card loop", loop_count)

val = 1
loop_count = 0
while val != door_public:
    val = (val*subject) % 20201227
    loop_count += 1

print("door loop", loop_count)

val = 1
for _ in range(loop_count):
    val = (val*card_public) % 20201227

print("key", val)